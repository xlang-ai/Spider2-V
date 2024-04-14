#coding=utf8
import json, re, logging
from typing import List, Tuple, Dict, Any
from copy import deepcopy
from snowflake import connector
from snowflake.connector import SnowflakeConnection

logger = logging.getLogger("desktopenv.metrics.snowflake")


def is_snowflake_user_created(result_dict: Dict[str, Any], expected: Dict[str, str], **options) -> float:
    """ Check if the user is created in snowflake. Note: the password is checked through creating a connection.
    Arguments for config dict:
    @args:
        settings_file(str): the path to the settings file, default is 'evaluation_examples/settings/snowflake/settings.json'
        result_dict(Dict[Tuple[str]]): the dict of user information, each key(uppercased)-value pair is like, e.g.,
            {'NAME': 'snowflake_name'}
        expected(Dict[str, str]): the expected user information, e.g., 
            {'NAME': 'username', 'FIRST_NAME': 'Name'}
        special care to some fields like 'PASSWORD', 'ROLE':
            - 'PASSWORD': use it to build a connection to snowflake, thus check if the password is correct
            - 'ROLE': the role of the user granted, may be a list, PUBLIC is always granted to all new users
    @returns:
        bool: True if the user with desired information is created, False otherwise
    """
    excluded = ['PASSWORD', 'ROLE']

    expected_dict = {
        key.upper(): str(value)
        for key, value in expected.items() if key.upper() not in excluded
    }
    
    result_dict_copy = deepcopy(result_dict)
    result_dict_copy.update(**expected_dict)

    if result_dict_copy == result_dict:
        # check some other fields
        if 'PASSWORD' in expected: # try to use this password to login
            # attention that, please ensure that must_change_password is false
            settings_file = options.get('settings_file', 'evaluation_examples/settings/snowflake/settings.json')
            settings = json.load(open(settings_file, 'r'))
            account = settings['account']
            matched = re.search(r'https://(.*?)\.snowflakecomputing\.com', account)
            conn = {"account": account, "user": result_dict['LOGIN_NAME'], "password": expected['PASSWORD']}
            if matched: conn['account'] = matched.group(1)
            try:
                client = None
                client: SnowflakeConnection = connector.connect(**conn)
            except Exception as e: # unable to connect, password is not correct
                logger.error(f'[UNABLE TO CONNECT]: {e}')
                return 0.
            finally:
                if client is not None: client.close()

        # check the Role
        if 'ROLE' in expected:
            roles = expected['ROLE']
            if type(roles) == str:
                if roles not in result_dict['ROLE']:
                    return 0
            else:
                for role in roles:
                    if role not in result_dict['ROLE']:
                        return 0

        return 1.0
    
    return 0.


def check_snowflake_log_message(result_dict: Dict[str, Any], expected: Dict[str, str], **options) -> float:
    """ Check if the log message contains the expected information.
    Arguments for config dict:
    @args:
        result_dict(Dict[str, str]): the dict of log message, each key(uppercased)-value pair is like, e.g.,
            {'severity': 'INFO', 'message': 'Logging from Python function.'}
        expected(Dict[str, str]): the expected log message, e.g., 
            {'severity': 'INFO', 'message': 'Logging from Python function.'}
    @returns:
        bool: True if the log message contains the expected information, False otherwise
    """
    if result_dict is None:
        return 0.
    if result_dict.get('severity', None) != expected['severity']:
        return 0.
    if result_dict.get('message', None) != expected['message']:
        return 0.
    return 1.0
