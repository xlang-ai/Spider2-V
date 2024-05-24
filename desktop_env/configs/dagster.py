#coding=utf8
import os, logging, time, requests, json, random, uuid, platform
from typing import List, Union, Tuple
from playwright.sync_api import expect, sync_playwright, Page
from .general import get_browser, find_page_by_url, init_page_with_js
from .google_cloud import google_account_login_in
from .google_cloud import google_account_login_in_alert

logger = logging.getLogger("desktopenv.setup")


def dagster_webui_close_popups(page: Page):
    try:
        skip_button = page.locator('button').filter(has_text="Skip")
        expect(skip_button).to_be_enabled()
        skip_button.click()
    except: pass
    try:
        dismiss_button = page.locator('button').filter(has_text="Dismiss")
        expect(dismiss_button).to_be_enabled()
        dismiss_button.click()
    except: pass
    try:
        close_button = page.locator('button').filter(has_text="Close")
        expect(close_button).to_be_enabled()
        close_button.click()
    except: pass
    return


def dagster_webgui_materialize_assets(page: Page, timeout: int = 60000):
    """ Goto the Assets page and materialize selected assets, by default materializing all assets.
    @args:
        timeout(int): waiting time for materializing all assets, default is 60000ms
    """
    asset_menu = page.locator('a[href="/assets"]').filter(has_text="Assets")
    expect(asset_menu).to_be_enabled()
    asset_menu.click()
    reload_button = page.locator('button').filter(has_text="Reload definitions")
    expect(reload_button).to_be_enabled()
    reload_button.click()
    expect(reload_button).to_be_enabled(timeout=timeout) # waiting for reload to finish
    # select the first checkbox, by default materialize all assets
    checkbox = page.locator('label[for="checkbox-1"]').first
    expect(checkbox).to_be_enabled()
    if not checkbox.is_checked():
        checkbox.click()
        expect(checkbox).to_be_checked()
    materialize_button = page.locator('button').filter(has_text="Materialize selected")
    expect(materialize_button).to_be_enabled()
    materialize_button.click()

    total_count = page.locator('input[type="checkbox"]').count() - 1
    materialized_span = page.locator('xpath=//span[text() and not(child::*)]').filter(has_text="Materialized")
    expect(materialized_span).to_have_count(total_count, timeout=timeout) # ensure all assets are materialized

    if checkbox.is_checked():
        checkbox.click()
        expect(checkbox).not_to_be_checked()
    return

def dagster_webui_delete_environment_variables(page: Page, timeout: int = 60000):
    """
    Delete the environment variables file on the Dagster+ UI.
    @args:
        timeout(int): waiting time for deleting all environment variables, default is 60000ms
    """
    env_menu = page.locator('a[href="/prod/environment"]').filter(has_text="Environment variables")
    expect(env_menu).to_be_enabled()
    env_menu.click()
    while True:
        delete_button = page.locator("[aria-label='Delete']").first
        try:
            expect(delete_button).to_be_enabled(timeout=2000)
        except:
            location_menu = page.locator('a[href="/prod/locations"]').filter(has_text="Code locations")
            expect(location_menu).to_be_enabled()
            location_menu.click()
            return
        delete_button.click()
        confirm_button = page.get_by_text("Yes, delete")
        expect(confirm_button).to_be_enabled(timeout=timeout)
        confirm_button.click()
        time.sleep(2)

DAGSTER_WEBUI_FUNCTIONS = {
    "execute_js": init_page_with_js,
    "close_popups": dagster_webui_close_popups,
    "materialize_assets": dagster_webgui_materialize_assets,
    "delete_environment_variables": dagster_webui_delete_environment_variables
}


def dagster_webui_login(page, url='http://localhost:3000', trial=10):
    for _ in range(trial):
        try:
            page.goto(url, wait_until='load')
            return page
        except:
            logger.warning(f'[WARNING]: failed to open the Dagster localhost webui page {url}. Retry...')
            time.sleep(3)
    return


def dagster_webui_init_setup(controller, **config):
    """ Log into the dagster localhost webui and perform environment setup. Arguments for config dict:
    @args:
        listening_port(int): the port number that the opened google-chrome is listening on, default is 9222
        url(str): the url of the dagster webui, default is localhost 'http://localhost:3000'
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
            # logger.error(f'[ERROR]: failed to find the Dagster localhost webui page {url}. Nothing done.')
            page = context.new_page()
            page = dagster_webui_login(page, url)
        
        for action in config.get('actions', []):
            action_type = action.pop('type', None)
            if action_type is None: continue
            init_func = DAGSTER_WEBUI_FUNCTIONS[action_type]
            init_func(page, **action)
    return

def dagster_cloud_webui_login_setup(controller, **config):
    """ Log into Dagster+ (previously known as Dagster Cloud) website. Argument for the config dict:
    @args:
        listening_port(int): the port number that the opened google-chrome is listening on, default is 9222
        url(str): the url of the dagster webui, default is 'https://dagster.cloud'
        settings_file(str): the path to the settings file, default is 'evaluation_examples/settings/dagster_cloud/settings.json'

    """

    listening_port = config.get('listening_port', 9222)
    remote_debugging_url = f"http://{controller.vm_ip}:{listening_port}"
    url = config.get('url', 'https://dagster.cloud')
    settings_file = config.get('settings_file', 'evaluation_examples/settings/dagster_cloud/settings.json')
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
            # Currently using Google account to log into Dagster+
            page.get_by_role("button", name="Continue with Google").click()
            time.sleep(1)
            google_account_login_in(page, settings['email'], settings['password'])
            google_account_login_in_alert(page)
            # email = page.locator('input[id="email"]')
            # expect(email).to_be_editable(timeout=60000)
            # email.fill(settings['email'])
            # next_button = page.get_by_text("Continue with Email", exact=True)
            # expect(next_button).to_be_enabled()
            # next_button.click()
            # password = page.locator('input[id="password"]')
            # expect(password).to_be_editable()
            # password.fill(settings['password'])
            # remember = page.locator('input[type="checkbox"]')
            # expect(remember).not_to_be_checked()
            # remember.check()
            # signin = page.locator('button[id="sign-in"]')
            # expect(signin).to_be_enabled()
            # signin.click()
            # page.wait_for_load_state('load')
            # button = page.locator('button[data-testid="settings-menu"]')
            # expect(button).to_be_visible(timeout=60000)

            for action in config.get('actions', []):
                action_type = action.pop('type', None)
                init_func = DAGSTER_WEBUI_FUNCTIONS[action_type]
                init_func(page, **action)

        except Exception as e:
            logger.error(f'[ERROR]: failed to login to the Dagster+ website! {e}')
            return

        logger.info('[INFO]: successfully logged into the Dagster+ website!')

    return

def dagster_environment_variables_setup(controller, **config):
    """ Get environment variables from Dagster+. Argument for the config dict:
    @args:
        listening_port(int): the port number that the opened google-chrome is listening on, default is 9222
        dest(str): the path to save the downloaded file
        settings_file(str): the path to the settings file, default is 'evaluation_examples/settings/dagster_cloud/settings.json'
    """

    controller._execute_setup(command=["rm", "-f", "/home/user/Downloads/env.txt"])

    listening_port = config.get('listening_port', 9222)
    remote_debugging_url = f"http://{controller.vm_ip}:{listening_port}"
    
    settings_file = config.get('settings_file', 'evaluation_examples/settings/dagster_cloud/settings.json')
    settings = json.load(open(settings_file, 'r'))
    organization = settings['organization']
    url = config.get('url', f'https://{organization}.dagster.cloud/prod/environment')

    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp(remote_debugging_url)
        if browser is None:
            logger.error('[ERROR]: failed to connect to Google Chrome browser in the running VM!')
            return

        context = browser.contexts[0]
        page = context.new_page()
        page.goto(url, wait_until='load')

        try:
            # page.get_by_role("button", name="Continue with Google").click()
            # time.sleep(1)
            # google_account_login_in(page, settings['email'], settings['password'])
            # google_account_login_in_alert(page)
            # time.sleep(2)
            # try:
            #     dismiss_button = page.locator('button').filter(has_text="Dismiss")
            #     expect(dismiss_button).to_be_enabled()
            #     dismiss_button.click()
            # except: pass
            time.sleep(5)
            page.locator("[aria-label='Download']").click()
            time.sleep(1)
            page.get_by_text("Download local environment variables").click()
            time.sleep(1)
        except Exception as e:
            logger.error(f'[ERROR]: failed to download the environment variables! {e}')
            return None

        logger.info('[INFO]: successfully downloaded the environment variables!')

    return