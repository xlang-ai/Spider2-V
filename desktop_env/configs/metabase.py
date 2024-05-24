#coding=utf8
import os, re, logging, time, requests, json, random, uuid, platform, time
from typing import List, Union, Tuple, Dict, Any
from playwright.sync_api import expect, sync_playwright, BrowserContext, Page
from .general import get_browser, copyfile_from_host_to_guest_setup, find_page_by_url

logger = logging.getLogger("desktopenv.setup")


def metabase_webui_login(page: Page, url: str = 'http://localhost:3000', config: Dict[str, str] = {}, retry: int = 100):
    """ Log into the metabase server started from metabase.jar. Allow server launch time and retry times.
    """
    for _ in range(retry):
        try:
            page.goto(url)
            page.wait_for_load_state('load')
            start_button = page.locator('button > div').filter(has_text="Let's get started")
            expect(start_button).to_be_visible(timeout=10000)
            return page
        except:
            time.sleep(3)
    else:
        logger.error(f'[ERROR]: failed to goto page {url}')
        return

def metabase_webui_setup(page: Page, config: Dict[str, Any] = {}):
    """ From the getting start page, configure the language, profile, usage reason, add data, disable data collection, and finish setup. Finally, redirect to the home page.
    """
    try:
        # 1. click button, get started
        button = page.locator('button').filter(has_text="Let's get started")
        expect(button).to_be_enabled()
        button.click()
        # 2. configure language
        language = config.get('language', 'en')
        language_selector = page.locator(f'input[type="radio"][value="{language}"]')
        expect(language_selector).to_be_enabled()
        if not language_selector.is_checked():
            language_selector.check()
            expect(language_selector).to_be_checked()
        button = page.locator('button').filter(has_text="Next")
        expect(button).to_be_enabled()
        button.click()
        # 3. configure profile
        profile = config.get('profile', {})
        first_name = profile.get('first_name', 'John')
        last_name = profile.get('last_name', 'Wilson')
        email = profile.get('email', 'johnwilson@gmail.com')
        company = profile.get('company', 'Metabase')
        password = profile.get('password', 'Spider2.0')
        input_dict = {
            "input[name='first_name']": first_name,
            "input[name='last_name']": last_name,
            "input[name='email']": email,
            "input[name='site_name']": company,
            "input[name='password']": password,
            "input[name='password_confirm']": password
        }
        for input_selector in input_dict:
            input_box = page.locator(input_selector)
            expect(input_box).to_be_editable()
            input_box.fill(input_dict[input_selector])
        button = page.locator('button').filter(has_text="Next")
        expect(button).to_be_enabled()
        button.click()
        # 4. choose usage reason
        check_box = page.locator('input[type="radio"][value="not-sure"][name="usage-reason"]')
        expect(check_box).to_be_visible()
        if not check_box.is_checked():
            check_box.check()
            expect(check_box).to_be_checked()
        button = page.locator('button').filter(has_text="Next")
        expect(button).to_be_enabled()
        button.click()
        # 5. skip adding data
        data = config.get('add_data', {})
        if not data:
            button = page.locator('button').filter(has_text="I'll add my data later")
            expect(button).to_be_enabled()
            button.click()
        elif data['type'] == 'PostgreSQL':
            button = page.locator('li[role="option"]').filter(has_text='PostgreSQL')
            expect(button).to_be_enabled()
            button.click()
            input_dict = {
                'input[name="name"]': data['display_name'],
                'input[name="details.host"]': data['host'],
                'input[name="details.port"]': data['port'],
                'input[name="details.dbname"]': data['db_name'],
                'input[name="details.user"]': data['db_user'],
                'input[name="details.password"]': data['db_password']
            }
            for input_selector in input_dict:
                input_box = page.locator(input_selector)
                expect(input_box).to_be_editable()
                input_box.fill(input_dict[input_selector])
            button = page.locator('button[title="Connect database"]')
            expect(button).to_be_enabled()
            button.click()
        # 6. disable data collection
        selector = page.locator('input[type="checkbox"][role="switch"][aria-labelledby="anonymous-usage-events-label"]')
        expect(selector).to_be_visible()
        if selector.is_checked():
            selector.uncheck()
            expect(selector).not_to_be_checked()
        # 7. finish setup
        button = page.locator('button').filter(has_text="Finish")
        expect(button).to_be_enabled()
        button.click()
        redirect = page.locator('a[href="/"]')
        expect(redirect).to_be_enabled()
        redirect.click()
        page.wait_for_load_state('load')
        toggle_bar = page.locator('button[data-testid="sidebar-toggle"][aria-label="Toggle sidebar"]')
        expect(toggle_bar).to_be_visible()
    except Exception as e:
        logger.error(f'[ERROR]: failed to setup Metabase getting started page. {e}')
        return
    return page

def metabase_webui_delete_database(page: Page, database_url: str = "http://localhost:3000/database/1", database_name: str = "Sample Database"):
    """ Delete the sample database that comes pre-loaded with Metabase.
    @config:
        database_url: the url of the Metabase database, default is 'http://localhost:3000/database/1'
        database_name: the database name to delete
    """
    try:
        page.goto(database_url)
        page.wait_for_load_state('load')

        button = page.locator('button').filter(has_text="Remove this database")
        expect(button).to_be_enabled()
        button.click()

        input_box = page.locator("input[placeholder='Are you completely sure?']")
        expect(input_box).to_be_editable()
        input_box.fill("Sample Database")

        button = page.locator('button').filter(has_text="Delete")
        expect(button).to_be_enabled()
        button.click()
        
        return_button = page.locator('a[data-testid="exit-admin"][href="/"]')
        expect(return_button).to_be_enabled()
        return_button.click()
        page.wait_for_load_state('load')
        
        logger.info(f'{database_name} in Metabase deleted successfully')
    except Exception as e:
        logger.error(f'[ERROR]: failed to delete sample database. {e}')
    return


METABASE_WEBUI_FUNCTIONS = {
    "login": metabase_webui_login,
    "setup": metabase_webui_setup,
    "delete_database": metabase_webui_delete_database
}


def metabase_webui_init_setup(controller, **config):
    """ Log into the Metabase localhost webui and perform environment setup. Arguments for config dict:
    @args:
        listening_port(int): the port number that the opened google-chrome is listening on, default is 9222
        url(str): the url of the superset webui, default is localhost 'http://localhost:3000'
    """
    listening_port = config.get('listening_port', 9222)
    remote_debugging_url = f"http://{controller.vm_ip}:{listening_port}"

    with sync_playwright() as p:
        browser = get_browser(p, remote_debugging_url)
        if browser is None:
            logger.error('[ERROR]: failed to connect to Google Chrome browser in the running VM!')
            return

        context = browser.contexts[0]
        url = config.get('url', 'http://localhost:3000')
        page = find_page_by_url(context, url, matching_func=lambda x, y: x.startswith(y))

        if page is None:
            # logger.error(f'[ERROR]: failed to find the Metabase localhost webui page {url}. Nothing done.')
            page = context.new_page()
            metabase_webui_login(page, url)
        
        for action in config.get('actions', []):
            action_type = action.pop('type', None)
            init_func = METABASE_WEBUI_FUNCTIONS[action_type]
            init_func(page, **action)
    return