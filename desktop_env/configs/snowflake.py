#coding=utf8
import os, re, logging, time, requests, json, random, uuid, platform
from typing import List, Union, Tuple, Dict, Any
from playwright.sync_api import expect, sync_playwright, BrowserContext, Page
from .general import get_browser, copyfile_from_host_to_guest_setup, find_page_by_url
from snowflake import connector
from snowflake.connector import SnowflakeConnection

logger = logging.getLogger("desktopenv.setup")

def remove_comments(sql_script):
    # remove single-line .sql comment
    sql_script = re.sub(r'--.*?$', '', sql_script, flags=re.MULTILINE)
    # remove multi-line .sql comments
    sql_script = re.sub(r'/\*.*?\*/', '', sql_script, flags=re.DOTALL)
    return sql_script


def snowflake_execute_script(client: SnowflakeConnection, **config: Dict[str, Any]) -> str:
    """ Execute a SQL script in Snowflake. General approach for initialization.
    @config:
        sql_command(Union[List[str], str]): the SQL command or command list to be executed
        sql_script(str): file path to the SQL script to be executed, either this field or `sql_command` should be provided
    """
    try:
        cursor = client.cursor()
        if config.get('sql_script', False):
            with open(config['sql_script'], 'r') as f:
                sql_command = f.read()
                sql_command = remove_comments(sql_command)
                sql_command = [s.strip() for s in sql_command.split(';') if s.strip()]
        else:
            sql_command = config['sql_command']
            if type(sql_command) == str: sql_command = [sql_command]
        query_ids = []
        for s in sql_command:
            cursor.execute(s)
            query_ids.append(cursor.sfqid)
        if config.get('query_ids_path', None):
            with open(os.path.join(config['controller'].cache_dir, config['query_ids_path']), 'w', encoding='utf-8') as file:
                for query_id in query_ids:
                    file.write(query_id + '\n')
        return
    except:
        logger.error(f'[ERROR]: failed to execute the SQL command/script on Snowflake!')
        return
    finally:
        if cursor is not None: cursor.close()
        if client is not None: client.close()


def snowflake_delete_user(client: SnowflakeConnection, **config: Dict[str, Any]):
    """ Delete the specified user in snowflake. Arguments for config dict:
    @args:
        username(str): the username to delete, optional, if not specified, delete all users except the current user and system preserved SNOWFLAKE
    """
    try:
        cursor = None
        cursor = client.cursor()
        username = config.get('username', None)
        if username is not None:
            if type(username) == str:
                cursor.execute(f'DROP USER IF EXISTS {username}')
            else:
                assert iter(username), "username field is neither string nor iterable"
                for name in username:
                    cursor.execute(f'DROP USER IF EXISTS {name}')
        else:
            current_user = cursor.execute('SELECT CURRENT_USER();').fetchone()[0]
            preserved = ['SNOWFLAKE', current_user]
            all_users = cursor.execute('SHOW USERS;').fetchall()
            for user in all_users:
                username = user[0]
                if username in preserved: continue
                cursor.execute(f'DROP USER IF EXISTS {username}')
    except:
        logger.error(f'[ERROR]: failed to delete the specified user `{username}` in snowflake!')
    finally:
        if cursor is not None: cursor.close()
    return


def snowflake_delete_database(client: SnowflakeConnection, **config: Dict[str, Any]):
    """ Delete the specified database in snowflake. Arguments for config dict:
    @args:
        database(str): database name to delete, optional, if not specified, delete all except preserved
    """
    database = config.get('database', None)
    preserved = ['SNOWFLAKE', 'SNOWFLAKE_SAMPLE_DATA']
    try:
        cursor = None
        cursor = client.cursor()
        if database is not None:
            if type(database) == str:
                cursor.execute(f'DROP DATABASE IF EXISTS {database} CASCADE;')
            else:
                assert iter(database), "database field is neither string nor iterable"
                for db in database:
                    cursor.execute(f'DROP DATABASE IF EXISTS {db} CASCADE;')
        else: # delete all DBs except preserved
            all_dbs = cursor.execute(f'SHOW DATABASES;').fetchall()
            for db in all_dbs:
                db_name = db[1] # 0 -> created datetime, 1 -> name
                if db_name not in preserved:
                    cursor.execute(f'DROP DATABASE IF EXISTS {db_name} CASCADE;')
    except Exception as e:
        logger.error(f'[ERROR]: unexpected error occurred when trying to delete database {e}')
    finally:
        if cursor is not None: cursor.close()
    return


def snowflake_delete_warehouse(client: SnowflakeConnection, **config: Dict[str, Any]):
    """ Delete the specified warehouse in snowflake. Arguments for config dict:
    @args:
        warehouse(str): the name of the warehouse to delete, optional, if not specified, delete all except preserved
    """
    warehouse = config.get('warehouse', None)
    preserved = ['COMPUTE_WH']
    try:
        cursor = None
        cursor = client.cursor()
        if warehouse is not None:
            if type(warehouse) == str:
                cursor.execute(f'DROP WAREHOUSE IF EXISTS {warehouse}')
            else:
                assert iter(warehouse), "warehouse field is neither string nor iterable"
                for wh in warehouse:
                    cursor.execute(f'DROP WAREHOUSE IF EXISTS {wh}')
        else: # delete all warehouses except preserved
            all_whs = cursor.execute(f'SHOW WAREHOUSES').fetchall()
            for wh in all_whs:
                wh_name = wh[0]
                if wh_name not in preserved:
                    cursor.execute(f'DROP WAREHOUSE IF EXISTS {wh_name}')
    except:
        logger.error(f'[ERROR]: failed to delete the specified warehouse `{warehouse}` in snowflake!')
    finally:
        if cursor is not None: cursor.close()


def snowflake_create_database(client: SnowflakeConnection, **config: Dict[str, Any]):
    """ Create the specified database in snowflake. Arguments for config dict:
    @args:
        database(str): the name of the database to create, required
        schema(str): the name of the schema to create, optional, default to None
        delete_first(bool): delete the database if already exists, default True
    """
    try:
        cursor = None
        cursor = client.cursor()
        delete_first = config.get('delete_first', True)
        if delete_first:
            snowflake_delete_database(client, database=config['database'])
        cursor.execute(f'CREATE DATABASE IF NOT EXISTS {config["database"]};')
        if config.get('schema', None):
            command = f'USE DATABASE {config["database"]};'
            cursor.execute(command)
            command = f'CREATE SCHEMA IF NOT EXISTS {config["schema"]};'
            cursor.execute(command)
    except:
        logger.error(f"[ERROR]: failed to create database {config['database']} in snowflake!")
    finally:
        if cursor is not None: cursor.close()
    return


def snowflake_create_table(client: SnowflakeConnection, **config: Dict[str, Any]):
    """ Create the specified table in snowflake. Arguments for config dict:
    @args:
        database(str): the name of the database to create the table in, required
        schema(str): the name of the schema to create the table in, default to PUBLIC
        table(str): the name of the table to create, required
        sql(str): the SQL command to create the table, required
    """
    try:
        cursor = None
        cursor = client.cursor()
        cursor.execute(f"USE DATABASE {config['database']}")
        cursor.execute(f"USE SCHEMA {config.get('schema', 'PUBLIC')}")
        cursor.execute(f"CREATE OR REPLACE TABLE {config['table']} AS {config['sql']}")
    except:
        logger.error(f"[ERROR]: failed to create table {config['table']} in snowflake!")
    finally:
        if cursor is not None: cursor.close()


def snowflake_copy_keyfile(client: SnowflakeConnection, **config: Dict[str, Any]):
    """ Copy the keyfile to the specified path. Arguments for config dict:
    @args:
        keyfile_path(str): the path to the keyfile, required
        dest(str): the path to the destination, default is '/home/user/keyfile.json'
    """
    dest = config.get('dest', '/home/user/keyfile.json')
    controller = config['controller']
    src = config['keyfile_path']
    copyfile_from_host_to_guest_setup(controller, src, dest)
    return


SNOWFLAKE_INIT_FUNCTIONS = {
    "execute_script": snowflake_execute_script,
    "delete_user": snowflake_delete_user,
    "delete_database": snowflake_delete_database,
    "delete_warehouse": snowflake_delete_warehouse,
    "create_database": snowflake_create_database,
    "create_table": snowflake_create_table,
    "copy_keyfile": snowflake_copy_keyfile,
}


def snowflake_init_setup(controller, **config):
    """ Initialize the snowflake environment. Arguments for config dict:
    @args:
        settings_file(str): the path to the settings file, default is 'evaluation_examples/settings/snowflake/settings.json'
        actions(List[Dict[str, Any]]): the list of actions to perform, each action is one dict with `type` field chosen from:
            - delete_user: delete the specified user, see `snowflake_delete_user` function
    """
    settings_file = config.get('settings_file', 'evaluation_examples/settings/snowflake/settings.json')
    settings = json.load(open(settings_file, 'r'))
    try:
        client = None
        # connection to the real account
        account = settings['account']
        matched = re.search(r'https://(.*?)\.snowflakecomputing\.com', account)
        if matched: settings['account'] = matched.group(1)
        client = connector.connect(**settings)

        # initialize the cloud workspace, e.g., users, databases, tables, etc.
        for action in config.get('actions', []):
            action_type = action.pop('type', None)
            action['keyfile_path'], action['controller'] = settings_file, controller
            init_func = SNOWFLAKE_INIT_FUNCTIONS[action_type]
            init_func(client, **action)
    except Exception as e:
        logger.error(f'[ERROR]: Unknown error occurred when connecting to snowflake during environment initialization!\n{e}')
    finally:
        if client is not None: client.close()
    return


def snowflake_skip_popups(page: Page):
    try:
        skip = page.locator('div[role="button"][aria-disabled="false"]').filter(has_text="Skip for now")
        expect(skip).to_be_enabled()
        skip.click()
    except: pass
    try:
        skip = page.locator('div[role="button"][data-testid="feedback-popover-close-button"]')
        expect(skip).to_be_enabled()
        skip.click()
    except: pass
    return


def snowflake_login_setup(controller, **config):
    """ Log into the snowflake website. Arguments for config dict:
    @args:
        listening_port(int): the port number that the opened google-chrome is listening on, default is 9222
        url(str): the url of the snowflake webui, default is 'https://app.snowflake.com'
        settings_file(str): the path to the settings file, default is 'evaluation_examples/settings/snowflake/settings.json'
    """
    listening_port = config.get('listening_port', 9222)
    remote_debugging_url = f"http://{controller.vm_ip}:{listening_port}"
    url = config.get('url', 'https://app.snowflake.com')
    settings_file = config.get('settings_file', 'evaluation_examples/settings/snowflake/settings.json')
    settings = json.load(open(settings_file, 'r'))

    with sync_playwright() as p:
        browser = get_browser(p, remote_debugging_url)
        if browser is None:
            logger.error('[ERROR]: failed to connect to Google Chrome browser in the running VM!')
            return
        
        context = browser.contexts[0]
        page = find_page_by_url(context, url, matching_func=lambda x, y: x.startswith(y))
        if page is None:
            page = context.new_page()
            page.goto(url, wait_until='load')

        try:
            account = page.locator('input[aria-label="Account identifier"]')
            expect(account).to_be_editable(timeout=60000)
            account.fill(settings['account'])
            signin = page.locator('div[role="button"][aria-disabled="false"]').filter(has_text="Sign in")
            expect(signin).to_be_visible()
            signin.click()
            username = page.locator('input[name="username"]')
            expect(username).to_be_editable(timeout=60000)
            username.fill(settings['user'])
            password = page.locator('input[name="password"]')
            expect(password).to_be_editable()
            password.fill(settings['password'])
            button = page.locator('div[role="button"][aria-disabled="false"]').filter(has_text="Sign in")
            expect(button).to_be_enabled()
            button.click()
            nav = page.locator('nav[role="navigation"]')
            expect(nav).to_be_visible(timeout=60000)
        except Exception as e:
            logger.error(f'[ERROR]: failed to login to the snowflake website! {e}')
            return
        
        snowflake_skip_popups(page)

        logger.info('[INFO]: successfully logged into the snowflake website!')
    return


def snowflake_write_sqls_in_new_worksheet_setup(controller, **config):
    """ Write the SQLs in the new worksheet. Arguments for config dict:
    @args:
        listening_port(int): the port number that the opened google-chrome is listening on, default is 9222
        sqls(List[str]): the list of SQLs to be written in the new worksheet, default is empty list
        close(bool): whether to close the worksheet after writing the SQLs, default is True
    """
    listening_port = config.get('listening_port', 9222)
    remote_debugging_url = f"http://{controller.vm_ip}:{listening_port}"
    sqls = config.get('sqls', [])
    close = config.get('close', True)

    def skip_worksheet_tips(page: Page):
        try:
            popup = page.locator('div[role="dialog"][aria-label="tutorial"] div[role="button"][aria-label="close"]')
            expect(popup).to_be_enabled()
            popup.click()
            gotit = page.locator('//div/span[text()="Got it!"][count(*)=0]/parent::div')
            expect(gotit).to_be_enabled()
            gotit.click()
        except:
            pass
        return

    def wait_for_sql_run(page: Page, timeout: int = 10000):
        try:
            query_results = page.locator('//span[text()="Query results"][count(*)=0]')
            expect(query_results).to_be_visible(timeout=timeout)
        except: # wait for the execution for at most {timeout} seconds
            pass
        return

    with sync_playwright() as p:
        browser = get_browser(p, remote_debugging_url)
        if browser is None:
            logger.error('[ERROR]: failed to connect to Google Chrome browser in the running VM!')
            return

        context = browser.contexts[0]
        page = find_page_by_url(context, 'https://app.snowflake.com', matching_func=lambda x, y: x.startswith(y))
        if page is None:
            logger.error('[ERROR]: failed to find the snowflake website page!')
            return

        try:
            new_worksheet_or_folder = page.locator('div[data-testid="new-button"]')
            expect(new_worksheet_or_folder).to_be_enabled(timeout=60000)
            new_worksheet_or_folder.click()
            sql_worksheet = page.locator('div[role="listbox"] > div:nth-child(1)')
            expect(sql_worksheet).to_be_enabled(timeout=60000)
            sql_worksheet.click()
            worksheet_content = page.locator('div[aria-label="worksheet"]')
            run = page.locator('div[role="button"][aria-label="Run"]')

            for sql in sqls:
                expect(worksheet_content).to_be_editable(timeout=60000)
                worksheet_content.fill(sql)
                expect(run).to_be_enabled(timeout=60000)
                run.click()
                wait_for_sql_run(page, 10000)
        except Exception as e:
            logger.error(f'[ERROR]: failed to write SQLs in the new worksheet! {e}')
            return

        skip_worksheet_tips(page) # move it here

        if close: # directly click the Projects button to return
            try:
                back = page.locator('a[role="link"][aria-label="Projects"]')
                expect(back).to_be_enabled()
                back.click()
            except:
                logger.error(f'[ERROR]: failed to click back to the main Homepage of Snowflake!')

        logger.info('[INFO]: successfully wrote SQLs in the new worksheet!')
        return


def snowflake_delete_folder_setup(controller, **config):
    """ Delete the specified folder in snowflake. Arguments for config dict:
    @args:
        listening_port(int): the port number that the opened google-chrome is listening on, default is 9222
        folder_name(str): the name of the folder to delete, required
    """
    listening_port = config.get('listening_port', 9222)
    remote_debugging_url = f"http://{controller.vm_ip}:{listening_port}"

    with sync_playwright() as p:
        browser = get_browser(p, remote_debugging_url)
        if browser is None:
            logger.error('[ERROR]: failed to connect to Google Chrome browser in the running VM!')
            return

        context = browser.contexts[0]
        page = find_page_by_url(context, 'https://app.snowflake.com', matching_func=lambda x, y: x.startswith(y))
        if page is None:
            logger.error('[ERROR]: failed to find the snowflake website page!')
            return

        try:
            worksheet_or_folder_list = page.locator('div[role="rowgroup"]')
            expect(worksheet_or_folder_list).to_be_enabled(timeout=60000)
            time.sleep(3)
            for i in range(page.locator('div[role="rowgroup"] > div').count() - 1):
                worksheet_or_folder = page.locator(f'div[role="rowgroup"] > div:nth-child({i + 2}) > div:nth-child(1) > a')
                if worksheet_or_folder.get_attribute('aria-label') == config['folder_name']:
                    break
            else:
                logger.info(f'[INFO]: folder {config["folder_name"]} not found in snowflake!')
                return
            expect(worksheet_or_folder).to_be_enabled(timeout=60000)
            worksheet_or_folder.click()
            manage = page.locator('h1[role="heading"]').first
            expect(manage).to_be_enabled(timeout=60000)
            manage.click()
            delete_folder = page.locator('div[data-action-name="Delete Folder"]')
            expect(delete_folder).to_be_enabled(timeout=60000)
            delete_folder.click()
            confirm = page.locator('div[class="c-modal-overlay js-modal-overlay"] > div:nth-child(1) > div:nth-child(3) > div:nth-child(3)')
            expect(confirm).to_be_enabled(timeout=60000)
            confirm.click()
        except Exception as e:
            logger.error(f'[ERROR]: failed to delete folder {config["folder_name"]} in snowflake! {e}')
            return

        logger.info(f'[INFO]: successfully deleted folder {config["folder_name"]} in snowflake!')


def hasura_login_setup(controller, **config):
    """ Log into the hasura website. Arguments for config dict:
    @args:
        listening_port(int): the port number that the opened google-chrome is listening on, default is 9222
        url(str): the url of the hasura webui, default is 'https://cloud.hasura.io/signup/email'
        settings_file(str): the path to the settings file, default is 'evaluation_examples/settings/hasura_cloud/settings.json'
    """
    listening_port = config.get('listening_port', 9222)
    remote_debugging_url = f"http://{controller.vm_ip}:{listening_port}"
    url = config.get('url', 'https://cloud.hasura.io/signup/email')
    settings_file = config.get('settings_file', 'evaluation_examples/settings/hasura_cloud/settings.json')
    settings = json.load(open(settings_file, 'r'))

    with sync_playwright() as p:
        browser = get_browser(p, remote_debugging_url)
        if browser is None:
            logger.error('[ERROR]: failed to connect to Google Chrome browser in the running VM!')
            return
        
        context = browser.contexts[0]
        page = find_page_by_url(context, url, matching_func=lambda x, y: x.startswith(y))
        if page is None:
            page = context.new_page()
            page.goto(url, wait_until='load', timeout=60000)

        try:
            email = page.locator('form >> [type = "email"]')
            expect(email).to_be_editable(timeout=60000)
            email.fill(settings['email'])
            password = page.locator('form >> [type = "password"]')
            expect(password).to_be_editable()
            password.fill(settings['password'])
            button = page.get_by_role("button", name="Continue")
            expect(button).to_be_enabled()
            button.click()
        except Exception as e:
            logger.error(f'[ERROR]: failed to login to the hasura website! {e}')
            return

        logger.info('[INFO]: successfully logged into the hasura website!')
    return


def snowflake_delete_filter_setup(controller, **config):
    """ Delete specific filter if exists. Arguments for config dict:
    @args:
        listening_port(int): the port number that the opened google-chrome is listening on, default is 9222
        filter_name(str): the SQL keyword of the filter which needs to be deleted, default is ':title_keyword'
    """
    listening_port = config.get('listening_port', 9222)
    filter_name = config.get('filter_name', ':title_keyword')
    remote_debugging_url = f"http://{controller.vm_ip}:{listening_port}"

    with sync_playwright() as p:
        browser = get_browser(p, remote_debugging_url)
        if browser is None:
            logger.error('[ERROR]: failed to connect to Google Chrome browser in the running VM!')
            return

        context = browser.contexts[0]
        page = find_page_by_url(context, 'https://app.snowflake.com', matching_func=lambda x, y: x.startswith(y))
        if page is None:
            logger.error('[ERROR]: failed to find the snowflake website page!')
            return

        try:
            create_button = page.locator('div[role="button"][data-testid="new-button"]')
            create_button.click()
            sql_worksheet = page.locator('div[role="option"]', has_text='SQL Worksheet')
            sql_worksheet.click()
            close_tips = page.locator('div[role="button"][aria-label="close"]')
            close_tips.click()
            got_it = page.locator('div[role="button"]', has_text='Got it!')
            got_it.click()
            filter_button = page.locator('div[role="button"][aria-label="show or hide filter"]')
            filter_button.click()
            manage_button = page.locator('div[role="button"]', has_text='Manage Filters')
            manage_button.click()
        except Exception as e:
            logger.error(f'[ERROR]: failed to delete filter {config["filter_name"]} in snowflake! {e}')
            return
        
        try:
            title_keyword = page.locator('div[role="cell"]', has_text=filter_name)
            title_keyword.hover()
        except Exception as e:
            try:
                done_button = page.locator('div[role="button"]', has_text='Done')
                done_button.click()
            except Exception as exception:
                logger.error(f'[ERROR]: failed to delete filter {config["filter_name"]} in snowflake! {exception}')
                return
            logger.info(f'[INFO]: successfully deleted filter {config["filter_name"]} in snowflake!')
            return

        try:
            edit_button =  page.locator('div[role="cell"]', has_text="Edit")
            edit_button.click()
            delete_button = page.locator('div[role="button"]', has_text='Delete')
            delete_button.click()
            confirm_button = page.locator('div[role="button"]', has_text='Delete')
            confirm_button.click()
            done_button = page.locator('div[role="button"]', has_text='Done')
            done_button.click()
        except Exception as e:
            logger.error(f'[ERROR]: failed to delete filter {config["filter_name"]} in snowflake! {e}')
            return

        logger.info(f'[INFO]: successfully deleted filter {config["filter_name"]} in snowflake!')