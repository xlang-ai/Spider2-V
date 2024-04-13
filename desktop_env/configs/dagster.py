#coding=utf8
import os, logging, time, requests, json, random, uuid, platform
from typing import List, Union, Tuple
from playwright.sync_api import expect, sync_playwright, Page
from .general import get_browser, find_page_by_url, init_page_with_js

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


DAGSTER_WEBUI_FUNCTIONS = {
    "execute_js": init_page_with_js,
    "close_popups": dagster_webui_close_popups,
    "materialize_assets": dagster_webgui_materialize_assets
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
            action_type = action.pop('type')
            init_func = DAGSTER_WEBUI_FUNCTIONS[action_type]
            init_func(page, **action)
    return