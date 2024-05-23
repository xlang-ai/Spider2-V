#coding=utf8
import json, re, logging, csv, os, platform, time
from typing import List, Dict, Any
from snowflake import connector
from snowflake.connector import SnowflakeConnection
from desktop_env.configs.general import get_browser, find_page_by_url
from playwright.sync_api import expect, sync_playwright

logger = logging.getLogger("desktopenv.getters.snowflake")


def write_data_into_csv(rows, csv_file, headers=[]):
    with open(csv_file, 'w', newline='', encoding='utf-8', errors='ignore') as of:
        writer = csv.writer(of)
        if headers != []:
            writer.writerow(headers)
        for row in rows:
            writer.writerow(row)
    return csv_file


def get_snowflake_execution_result(env, config: Dict[str, Any]) -> str:
    """ Get the execution results of a specific SQL command/SQL script, return the output to a file or string.
    @config:
        settings_file(str): the path to the settings file, default is 'evaluation_examples/settings/snowflake/settings.json'
        sql_command(str): the SQL command to be executed
        sql_script(str): file path to the SQL script to be executed, either this field or `sql_command` should be provided.
            Attention, the sql_script contains only one SQL command (multiple SQL commands not supported)
        include_header(bool): whether return the header execution output, default to true
        return_string(bool): concatenate output results into string (usually for quick evaluation), default to True.
            note that, this field is only used when `dest` is not provided
        dest(str): the path to the output file, optional, if not provided, directly return the execution results
    @returns:
        result(Union[str, Any]): the path to the output result or raw output object
    """
    settings_file = config.get('settings_file', 'evaluation_examples/settings/snowflake/settings.json')
    if platform.system() == 'Windows':
        settings_file = settings_file.replace('/', '\\')
    settings = json.load(open(settings_file, 'r'))
    account = settings['account']
    matched = re.search(r'https://(.*?)\.snowflakecomputing\.com', account)
    if matched: settings['account'] = matched.group(1)
    client, cursor, headers = None, None, []
    result_file = config.get('dest', None)
    include_header = config.get('include_header', True)

    try:
        client: SnowflakeConnection = connector.connect(**settings)
        cursor = client.cursor()
        if config.get('sql_script', False):
            with open(config['sql_script'], 'r') as f:
                sql_command = f.read()
        else: sql_command = config['sql_command']
        cursor.execute(sql_command)

        if result_file is not None:
            if include_header:
                headers = [col.name for col in cursor.description]
            rows = cursor.fetchall()
            write_data_into_csv(rows, result_file, headers)
            return result_file
        else:
            result = cursor.fetchall()
            if include_header:
                headers = [col.name for col in cursor.description]
                result = [headers] + result
            if config.get('return_string', True):
                # by default, use '\n' as row separator, ',' as column separator
                result = '\n'.join([','.join([str(c) for c in row]) for row in result])
            return str(result)
    except:
        logger.error(f'[ERROR]: failed to execute the SQL command/script on Snowflake!')
        return
    finally:
        if cursor is not None: cursor.close()
        if client is not None: client.close()


def get_snowflake_database_schema_to_csv(env, config: Dict[str, Any]) -> str:
    """ Get the database schema from snowflake and write into a json file. Arguments for config dict:
    @args:
        settings_file(str): the path to the settings file, default is 'evaluation_examples/settings/snowflake/settings.json'
        database(Union[str, List[str]]): the database (or list) to be checked, required
        schema(Union[str, List[str]]): schema name to be checked, default to 'PUBLIC' with the same length of database
        include_type(bool): whether include data type for columns, default to False
        dest(str): the path to the json file, required
    @returns:
        json_file(str): the path to the json file, which contains the database schema, if found, else None
    """
    settings_file = config.get('settings_file', 'evaluation_examples/settings/snowflake/settings.json')
    if platform.system() == 'Windows':
        settings_file = settings_file.replace('/', '\\')
    settings = json.load(open(settings_file, 'r'))
    account = settings['account']
    matched = re.search(r'https://(.*?)\.snowflakecomputing\.com', account)
    if matched: settings['account'] = matched.group(1)

    client, cursor = None, None
    csv_file = os.path.join(env.cache_dir, config['dest'])
    database = config['database']
    schema = config.get('schema', 'PUBLIC')
    headers = ['database', 'schema', 'table', 'column', 'type'] if config.get('include_type', False) else ['database', 'schema', 'table', 'column']
    data_type = ', DATA_TYPE' if config.get('include_type', False) else ''
    query_template = f'SELECT TABLE_CATALOG, TABLE_SCHEMA, TABLE_NAME, COLUMN_NAME{data_type} FROM {{database}}.INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = \'{{schema}}\' ORDER BY TABLE_CATALOG, TABLE_SCHEMA, TABLE_NAME, COLUMN_NAME;'
    try:
        client: SnowflakeConnection = connector.connect(**settings)
        cursor = client.cursor()
        if type(database) == str:
            cursor.execute(f'USE DATABASE {database};')
            rows = cursor.execute(query_template.format(database=database, schema=schema)).fetchall()
            write_data_into_csv(rows, csv_file, headers)
        else:
            rows = []
            for idx, db in enumerate(database):
                cur_schema = schema[idx] if type(schema) == list else schema
                cursor.execute(f'USE DATABASE {db};')
                rows += cursor.execute(query_template.format(database=db, schema=cur_schema)).fetchall()
            write_data_into_csv(rows, csv_file, headers)
    except Exception as e:
        logger.error(f'[ERROR]: unexpected error occurred when fetching database schema on Snowflake. {e}')
    finally:
        if cursor is not None: cursor.close()
        if client is not None: client.close()
    return csv_file


def get_snowflake_table_to_csv(env, config: Dict[str, Any]) -> str:
    """ Get the table schema and data from snowflake. Arguments for config dict:
    @args:
        settings_file(str): the path to the settings file, default is 'evaluation_examples/settings/snowflake/settings.json'
        database(str): the database name of the target table, required
        table(str): the table name to get the information, required
        dest(str): csv file name, default is '{table_name}.csv'
        include_header(bool): add column names in the first line, default to True
    @returns:
        csv_file(str): the path to the csv file, which contains the table schema and data, if found, else None
    """
    settings_file = config.get('settings_file', 'evaluation_examples/settings/snowflake/settings.json')
    if platform.system() == 'Windows':
        settings_file = settings_file.replace('/', '\\')
    settings = json.load(open(settings_file, 'r'))
    account = settings['account']
    matched = re.search(r'https://(.*?)\.snowflakecomputing\.com', account)
    if matched: settings['account'] = matched.group(1)
    settings['database'], settings['schema'] = config['database'], config.get('schema', 'PUBLIC')

    client, cursor, headers = None, None, []
    table, include_header = config['table'], config.get('include_header', True)
    csv_file = os.path.join(env.cache_dir, config.get('dest', f'{config["table"]}.csv'))
    try:
        client: SnowflakeConnection = connector.connect(**settings)
        cursor = client.cursor()
        if '-' in table:
            cursor.execute(f'SELECT * FROM "{table}";')
        else:
            cursor.execute(f'SELECT * FROM {table};')
        if include_header:
            headers = [col.name for col in cursor.description]
        rows = cursor.fetchall()
        write_data_into_csv(rows, csv_file, headers)
    except Exception as e:
        logger.error(f'[ERROR]: failed to write data in table {table} into csv file {csv_file}. {e}')
        return
    finally:
        if client is not None: client.close()
        if cursor is not None: cursor.close()
    return csv_file


def get_snowflake_user_info(env, config: Dict[str, Any]) -> Dict[str, Any]:
    """ Get the user information from snowflake. Arguments for config dict:
    @args:
        settings_file(str): the path to the settings file, default is 'evaluation_examples/settings/snowflake/settings.json'
        username(str): the username to get the information, required
    @returns:
        result_dict(Dict[str, Any]): the dict of user information, each key(uppercased)-value pair is like, e.g.,
            {'NAME': 'snowflake_name'}
            special care to some fields like 'PASSWORD', 'ROLE'
    """
    settings_file = config.get('settings_file', 'evaluation_examples/settings/snowflake/settings.json')
    settings = json.load(open(settings_file, 'r'))
    account = settings['account']
    matched = re.search(r'https://(.*?)\.snowflakecomputing\.com', account)
    if matched: settings['account'] = matched.group(1)

    client, cursor = None, None
    result_dict = {'ROLE': ["PUBLIC"]}
    try:
        client: SnowflakeConnection = connector.connect(**settings)
        username = config['username']
        cursor = client.cursor()
        results = cursor.execute(f'DESC USER {username}').fetchall()
        for row in results:
            if row[0].upper() == 'PASSWORD': # ignore password
                continue
            result_dict[row[0].upper()] = str(row[1])

        # get granted roles
        results = cursor.execute(f'SHOW GRANTS TO USER {username}').fetchall()
        for row in results:
            result_dict['ROLE'].append(str(row[1]))

        return result_dict
    except Exception as e:
        logger.error(f'[ERROR]: failed to get full user information from Snowflake! {e}')
        return result_dict
    finally:
        if cursor is not None: cursor.close()
        if client is not None: client.close()


def get_snowflake_function_result(env, config: Dict[str, Any]) -> Any:
    """ Get the result of a snowflake function. Arguments for config dict:
    @args:
        settings_file(str): the path to the settings file, default is 'evaluation_examples/settings/snowflake/settings.json'
        database(str): the database name of the target table, required
        table(str): the table name to get the information, required
        function(str): the name of the function to be called, required
    @returns:
        result(Any): the result of the function call, can be any type
    """
    settings_file = config.get('settings_file', 'evaluation_examples/settings/snowflake/settings.json')
    settings = json.load(open(settings_file, 'r'))
    account = settings['account']
    matched = re.search(r'https://(.*?)\.snowflakecomputing\.com', account)
    if matched: settings['account'] = matched.group(1)
    settings['database'], settings['schema'] = config['database'], config.get('schema', 'PUBLIC')

    client, cursor = None, None
    try:
        client: SnowflakeConnection = connector.connect(**settings)
        cursor = client.cursor()
        cursor.execute(f"ALTER ACCOUNT SET EVENT_TABLE = {config['database']}.public.{config['table']}")
        cursor.execute('ALTER SESSION SET LOG_LEVEL = INFO')
        cursor.execute(f"SELECT {config['function']}()")
        result = cursor.fetchone()[0]
        return result
    except Exception as e:
        logger.error(f'[ERROR]: failed to get the function result from Snowflake! {e}')
        return None
    finally:
        if cursor is not None: cursor.close()
        if client is not None: client.close()


def get_snowflake_log_message(env, config: Dict[str, Any]) -> str:
    """ Get the log message from snowflake. Arguments for config dict:
    @args:
        settings_file(str): the path to the settings file, default is 'evaluation_examples/settings/snowflake/settings.json'
        database(str): the database name of the target table, required
        table(str): the table name to get the information, required
        logger(str): the name of the logger to get the information, required
    @returns:
        result_dict(Dict[str, Any]): the dict of log message, each key(uppercased)-value pair is like, e.g.,
            {'severity': 'INFO', 'message': 'Logging from Python function.'}
    """
    settings_file = config.get('settings_file', 'evaluation_examples/settings/snowflake/settings.json')
    settings = json.load(open(settings_file, 'r'))
    account = settings['account']
    matched = re.search(r'https://(.*?)\.snowflakecomputing\.com', account)
    if matched: settings['account'] = matched.group(1)
    settings['database'], settings['schema'] = config['database'], config.get('schema', 'PUBLIC')

    client, cursor = None, None
    try:
        client: SnowflakeConnection = connector.connect(**settings)
        cursor = client.cursor()
        for _ in range(3):
            cursor.execute(f"SELECT RECORD['severity_text'], VALUE FROM {config['database']}.public.{config['table']} WHERE RECORD_TYPE = 'LOG' AND SCOPE['name'] = '{config['logger']}'")
            result = cursor.fetchone()
            if result is not None:
                break
            time.sleep(60)
        return {'severity': result[0].strip('"'), 'message': result[1].strip('"')}
    except Exception as e:
        logger.error(f'[ERROR]: failed to get log message from Snowflake! {e}')
        return None
    finally:
        if cursor is not None: cursor.close()
        if client is not None: client.close()


def get_snowflake_worksheet_sql(env, config: Dict[str, Any]) -> str:
    """ Get the SQL command in the opened snowflake worksheet. Arguments for config dict:
    @args:
        listening_port(int): the port number that the opened google-chrome is listening on, default is 9222
    @returns:
        sql(str): the SQL command in the opened snowflake worksheet, if found, else None
    """
    listening_port = config.get('listening_port', 9222)
    remote_debugging_url = f"http://{env.vm_ip}:{listening_port}"
    with sync_playwright() as p:
        browser = get_browser(p, remote_debugging_url)
        if browser is None:
            logger.error('[ERROR]: failed to connect to Google Chrome browser in the running VM!')
            return None
        context = browser.contexts[0]
        page = find_page_by_url(context, 'https://app.snowflake.com', matching_func=lambda x, y: x.startswith(y))
        if page is None:
            logger.error('[ERROR]: failed to find the worksheet in the running VM!')
            return None
        worksheet_content = page.locator('div[aria-label="worksheet"]')
        return worksheet_content.inner_text().strip()


def get_snowflake_worksheet_sql_result(env, config: Dict[str, Any]) -> str:
    """ Get the result of a snowflake worksheet SQL command. Arguments for config dict:
    @args:
        settings_file(str): the path to the settings file, default is 'evaluation_examples/settings/snowflake/settings.json'
        worksheet(str): the name of the worksheet to execute the SQL command, required
        database(str): the database name of the target table, required
        schema(str): the schema name of the target table, required
        dest(str): csv file name, required
    @returns:
        csv_file(str): the path to the csv file, which contains the execution result, if found, else None
    """
    listening_port = config.get('listening_port', 9222)
    remote_debugging_url = f"http://{env.vm_ip}:{listening_port}"
    with sync_playwright() as p:
        browser = get_browser(p, remote_debugging_url)
        if browser is None:
            logger.error('[ERROR]: failed to connect to Google Chrome browser in the running VM!')
            return None
        context = browser.contexts[0]
        for page in context.pages:
            try:
                worksheet_tab = page.locator(f'div[data-action-name="worksheet-tab"][aria-label="{config["worksheet"]}"]')
                if worksheet_tab.count() > 0:
                    break
            except:
                continue
        else:
            logger.error(f'[ERROR]: failed to find the worksheet "{config["worksheet"]}" in the running VM!')
            return None
        db_and_schema_selector = page.locator('div[role="button"][data-testid="databaseAndSchemaSelector"]')
        if db_and_schema_selector.inner_text() != f'{config["database"]}.{config["schema"]}':
            logger.error(f'[ERROR]: the selected database and schema is not the same as the target "{config["database"]}.{config["schema"]}"!')
            return None
        worksheet_content = page.locator('div[aria-label="worksheet"]')
        sql = worksheet_content.inner_text().replace('\n', ' ').split(';')[-1]

    settings_file = config.get('settings_file', 'evaluation_examples/settings/snowflake/settings.json')
    settings = json.load(open(settings_file, 'r'))
    account = settings['account']
    matched = re.search(r'https://(.*?)\.snowflakecomputing\.com', account)
    if matched: settings['account'] = matched.group(1)
    settings['database'], settings['schema'] = config['database'], config['schema']

    client, cursor, headers = None, None, []
    csv_file = os.path.join(env.cache_dir, config['dest'])
    try:
        client: SnowflakeConnection = connector.connect(**settings)
        cursor = client.cursor()
        cursor.execute(sql)
        headers = [col.name for col in cursor.description]
        rows = cursor.fetchall()
        write_data_into_csv(rows, csv_file, headers)
    except Exception as e:
        logger.error(f'[ERROR]: failed to execute SQL command "{sql}" in worksheet "{config["worksheet"]}" on Snowflake! {e}')
        return
    finally:
        if client is not None: client.close()
        if cursor is not None: cursor.close()
    return csv_file


def get_snowflake_worksheet_names_in_folder(env, config: Dict[str, Any]) -> List[str]:
    """ Get the worksheet names in a snowflake folder. Arguments for config dict:
    @args:
        listening_port(int): the port number that the opened google-chrome is listening on, default is 9222
        folder_name(str): the name of the snowflake folder to get the worksheet names, required
    @returns:
        worksheet_names(List[str]): the list of worksheet names in the snowflake folder, if found, else None
    """
    listening_port = config.get('listening_port', 9222)
    remote_debugging_url = f"http://{env.vm_ip}:{listening_port}"
    with sync_playwright() as p:
        browser = get_browser(p, remote_debugging_url)
        if browser is None:
            logger.error('[ERROR]: failed to connect to Google Chrome browser in the running VM!')
            return None
        context = browser.contexts[0]
        page = context.new_page()
        page.goto('https://app.snowflake.com', wait_until='load')
        try:
            worksheet_or_folder_list = page.locator('div[role="rowgroup"]')
            expect(worksheet_or_folder_list).to_be_enabled(timeout=60000)
            time.sleep(3)
            for i in range(page.locator('div[role="rowgroup"] > div').count() - 1):
                worksheet_or_folder = page.locator(f'div[role="rowgroup"] > div:nth-child({i + 2}) > div:nth-child(1) > a')
                if worksheet_or_folder.get_attribute('aria-label') == config['folder_name']:
                    break
            else:
                logger.error(f'[ERROR]: failed to find the snowflake folder "{config["folder_name"]}" in the running VM!')
                return None
            expect(worksheet_or_folder).to_be_enabled(timeout=60000)
            worksheet_or_folder.click()
            worksheet_list = page.locator('div[role="rowgroup"]')
            expect(worksheet_list).to_be_enabled(timeout=60000)
            time.sleep(3)
            worksheet_names = []
            for i in range(page.locator('div[role="rowgroup"] > div').count() - 1):
                worksheet = page.locator(f'div[role="rowgroup"] > div:nth-child({i + 2}) > div:nth-child(1) > a')
                worksheet_names.append(worksheet.get_attribute('aria-label'))
        except Exception as e:
            logger.error(f'[ERROR]: failed to get worksheet names in snowflake folder "{config["folder_name"]}"! {e}')
            return None
    return worksheet_names
