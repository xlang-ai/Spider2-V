#coding=utf8
import os, re, logging, time, requests, json, random, uuid, platform
from typing import List, Union, Tuple, Dict, Any
from playwright.sync_api import expect, sync_playwright, BrowserContext, Page
from .general import get_browser, copyfile_from_host_to_guest_setup, find_page_by_url

logger = logging.getLogger("desktopenv.setup")


def superset_webui_login(page: Page, url: str = 'http://localhost:8088', username: str = "admin", password: str = "admin", retry: int = 10):
    for _ in range(retry):
        try:
            page.goto(url)
            break
        except:
            time.sleep(3)
    else:
        logger.error(f'[ERROR]: failed to goto page {url}')
        return

    try:
        page.wait_for_load_state('load')
        input_box = page.locator('input#username')
        expect(input_box).to_be_editable()
        input_box.fill(username)
        input_box = page.locator('input#password')
        expect(input_box).to_be_editable()
        input_box.fill(password)
        button = page.locator('input[type="submit"][value="Sign In"i]')
        expect(button).to_be_enabled()
        button.click()
        welcome = page.locator('a[href="/superset/welcome/"]')
        expect(welcome).to_be_visible(timeout=30000)
    except:
        logger.error(f'[ERROR]: failed to login to superset webui {url}')
        return
    return page


SUPERSET_WEBUI_FUNCTIONS = {

}


def superset_webui_init_setup(controller, **config):
    """ Log into the superset localhost webui and perform environment setup. Arguments for config dict:
    @args:
        listening_port(int): the port number that the opened google-chrome is listening on, default is 9222
        url(str): the url of the superset webui, default is localhost 'http://localhost:8088'
    """
    listening_port = config.get('listening_port', 9222)
    remote_debugging_url = f"http://{controller.vm_ip}:{listening_port}"

    with sync_playwright() as p:
        browser = get_browser(p, remote_debugging_url)
        if browser is None:
            logger.error('[ERROR]: failed to connect to Google Chrome browser in the running VM!')
            return

        context = browser.contexts[0]
        url = config.get('url', 'http://localhost:8088')
        page = find_page_by_url(context, url, matching_func=lambda x, y: x.startswith(y))

        if page is None:
            # logger.error(f'[ERROR]: failed to find the Superset localhost webui page {url}. Nothing done.')
            page = context.new_page()
            page = superset_webui_login(page, url)
        
        for action in config.get('actions', []):
            action_type = action.pop('type', None)
            init_func = SUPERSET_WEBUI_FUNCTIONS[action_type]
            init_func(page, **action)
    return