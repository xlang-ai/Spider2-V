#coding=utf8
import json, re, logging
from typing import Dict, Any
from snowflake import connector
from snowflake.connector import SnowflakeConnection

logger = logging.getLogger("desktopenv.getters.snowflake")


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