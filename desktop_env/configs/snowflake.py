#coding=utf8
import os, re, logging, time, requests, json, random, uuid, platform
from typing import List, Union, Tuple, Dict, Any
from playwright.sync_api import expect, sync_playwright, BrowserContext, Page
from .general import get_browser
from snowflake import connector
from snowflake.connector import SnowflakeConnection

logger = logging.getLogger("desktopenv.setup")


def snowflake_delete_user(client: SnowflakeConnection, **config: Dict[str, Any]):
    """ Delete the specified user in snowflake. Arguments for config dict:
    @args:
        username(str): the username to delete
    """
    try:
        cursor = None
        username = config['username']
        cursor = client.cursor()
        cursor.execute(f'DROP USER IF EXISTS {username}')
    except:
        logger.error(f'[ERROR]: failed to delete the specified user `{username}` in snowflake!')
    finally:
        if cursor is not None: cursor.close()
    return


SNOWFLAKE_INIT_FUNCTIONS = {
    "delete_user": snowflake_delete_user,
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
            init_func = SNOWFLAKE_INIT_FUNCTIONS[action_type]
            init_func(client, **action)
    except Exception as e:
        logger.error(f'[ERROR]: Unknown error occurred when connecting to snowflake during environment initialization!\n{e}')
    finally:
        if client is not None: client.close()
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
        page = context.new_page()
        page.goto(url, wait_until='load')

        try:
            account = page.locator('input[aria-label="Account identifier"]')
            expect(account).to_be_editable()
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
        except Exception as e:
            logger.error(f'[ERROR]: failed to login to the snowflake website! {e}')
            return
        
        try:
            skip = page.locator('div[role="button"][aria-disabled="false"]').filter(has_text="Skip for now")
            expect(skip).to_be_enabled()
            skip.click()
        except: pass

        logger.info('[INFO]: successfully logged into the snowflake website!')
    return