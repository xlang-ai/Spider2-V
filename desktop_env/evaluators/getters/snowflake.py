#coding=utf8
import json, re, logging, csv, os, platform, time
from typing import Dict, Any
from snowflake import connector
from snowflake.connector import SnowflakeConnection

logger = logging.getLogger("desktopenv.getters.snowflake")


def write_data_into_csv(rows, csv_file, headers=[]):
    with open(csv_file, 'w', newline='') as of:
        writer = csv.writer(of)
        if headers != []:
            writer.writerow(headers)
        for row in rows:
            writer.writerow(row)
    return csv_file


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

    client, cursor = None, None
    table, include_header = config['table'], config.get('include_header', True)
    csv_file = os.path.join(env.cache_dir, config.get('dest', f'{config["table"]}.csv'))
    try:
        client: SnowflakeConnection = connector.connect(**settings)
        cursor = client.cursor()
        cursor.execute(f'SELECT * FROM {table};')
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
