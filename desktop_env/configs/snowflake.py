#coding=utf8
import os, re, logging, time, requests, json, random, uuid, platform
from typing import List, Union, Tuple, Dict, Any
from playwright.sync_api import expect, sync_playwright, BrowserContext, Page
from .general import get_browser, copyfile_from_host_to_guest_setup, find_page_by_url
from snowflake import connector
from snowflake.connector import SnowflakeConnection

logger = logging.getLogger("desktopenv.setup")


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
                db_name = db[1]
                if db_name not in preserved: # 0 -> created datetime, 1 -> name
                    cursor.execute(f'DROP DATABASE IF EXISTS {db_name} CASCADE;')
    except Exception as e:
        logger.error(f'[ERROR]: unexpected error occurred when trying to delete database {e}')
    finally:
        if cursor is not None: cursor.close()
    return


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
            command = f'begin; USE DATABASE {config["database"]}; CREATE SCHEMA IF NOT EXISTS {config["schema"]}; commit;'
            cursor.execute(command)
    except:
        logger.error(f"[ERROR]: failed to create database {config['database']} in snowflake!")
    finally:
        if cursor is not None: cursor.close()
    return


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
    "delete_user": snowflake_delete_user,
    "delete_database": snowflake_delete_database,
    "create_database": snowflake_create_database,
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
            action_type = action.pop('type')
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
        url(str): the url of the dagster webui, default is 'https://app.snowflake.com'
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