#coding=utf8
import os, logging, time, requests, json, random, uuid, platform
from typing import List, Union, Tuple
from playwright.sync_api import expect, sync_playwright, BrowserContext, Page
from .general import get_browser

logger = logging.getLogger("desktopenv.setup")


def waiting_for_airbyte_server(context: BrowserContext, url: str = "http://localhost:8000", max_trials=10):
    page = context.new_page()
    for _ in range(max_trials):
        try:
            page.goto(url, wait_until='load')
            return page
        except:
            time.sleep(3)
            continue
    # using `start_server` function in init.sh
    # for _ in range(max_trials):
    #     try:
    #         page.goto(url + '/setup', wait_until='load')
    #         input_box = page.locator('input[name="email"]')
    #         expect(input_box).to_be_editable()
    #     except:
    #         time.sleep(3)
    #         continue
    #     return page
    return


def airbyte_webui_login(page: Page, email: str = "anonym@gmail.com", company: str = "ANONYM"):
    try: # maybe already used, not need to fill in the forms
        homepage = page.locator('a[aria-label="Homepage"]')
        expect(homepage).to_be_visible()
    except: pass
    try:
        email_input = page.locator('input[name="email"]')
        expect(email_input).to_be_editable()
        email_input.fill(email)
        company_input = page.locator('input[name="organizationName"]')
        expect(company_input).to_be_editable()
        company_input.fill(company)
        time.sleep(3) # wait for the button to be enabled
        button = page.locator('button[type="submit"]')
        expect(button).to_be_visible()
        pos = button.bounding_box()
        page.mouse.click(pos['x'], pos['y'])
        expect(button).to_be_enabled()
        button.click()
        homepage = page.locator('a[aria-label="Homepage"]')
        expect(homepage).to_be_visible()
    except:
        logger.warning("[WARNING]: Failed to fill in email and company name on airbyte localhost login page!")
    return


AIRBYTE_WEBUI_FUNCTIONS = {
    "login": airbyte_webui_login
}


def airbyte_webui_init_setup(controller, **config):
    """ Log into the airbyte localhost webui and perform environment setup. Arguments for config dict:
    @args:
        listening_port(int): the port number that the opened google-chrome is listening on, default is 9222
        url(str): the url of the airbyte webui, default is localhost 'http://localhost:8000'
        actions(list): the list of actions to perform, each action is one dict with `type` field chosen from ['empty']:
    """
    listening_port = config.get('listening_port', 9222)
    remote_debugging_url = f"http://{controller.vm_ip}:{listening_port}"

    with sync_playwright() as p:
        browser = get_browser(p, remote_debugging_url)
        if browser is None:
            logger.error('[ERROR]: failed to connect to Google Chrome browser in the running VM!')
            return

        context = browser.contexts[0]
        url = config.get('url', 'http://localhost:8000')
        # special care for airbyte to log in, it requires HTTP basic auth and server startup time
        page = waiting_for_airbyte_server(context, url)
        if page is None:
            logger.error('[ERROR]: failed to connect to Airbyte Web UI!')
            return

        for action in config.get('actions', []):
            action_type = action.pop('type', None)
            init_func = AIRBYTE_WEBUI_FUNCTIONS[action_type]
            init_func(page, **action)
    return