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
    return


DAGSTER_WEBUI_FUNCTIONS = {
    "execute_js": init_page_with_js,
    "close_popups": dagster_webui_close_popups
}


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
            page.goto(url, wait_until='load')
        
        for action in config.get('actions', []):
            action_type = action.pop('type')
            init_func = DAGSTER_WEBUI_FUNCTIONS[action_type]
            init_func(page, **action)
    return