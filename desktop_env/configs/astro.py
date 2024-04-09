import logging, time, platform
from typing import List, Union, Tuple
from playwright.sync_api import expect, sync_playwright, BrowserContext, Page
from .general import get_browser

#coding=utf8

logger = logging.getLogger("desktopenv.setup")

def waiting_for_astro_server(context: BrowserContext, url: str = "http://localhost:8080", max_trials=10):
    page = context.new_page()
    for _ in range(max_trials):
        try:
            page.goto(url, wait_until='load')
            break
        except:
            time.sleep(3)
            continue
    for _ in range(max_trials):
        try:
            page.goto(url + '/setup', wait_until='load')
            input_box = page.locator('input#username')
            expect(input_box).to_be_editable()
        except:
            time.sleep(3)
            continue
        return page
    return

def astro_webui_login (page: Page, username: str = "admin", password: str = "admin"):
    try:

        username_input = page.locator('input#username')
        expect(username_input).to_be_editable()
        username_input.fill(username)

        password_input = page.locator('input#password')
        expect(password_input).to_be_editable()
        password_input.fill(password)

        button = page.locator('input[type="submit"].btn.btn-primary.btn-block')
        expect(button).to_be_enabled()
        button.click()

        homepage = page.locator('a[aria-label="Homepage"]')
        expect(homepage).to_be_visible()
    except Exception as e:
        print(f"[WARNING]: Failed to fill in username and password on astro localhost login page! {e}")
    return

ASTRO_WEBUI_FUNCTIONS = {
    "login": astro_webui_login
}

def astro_webui_init_setup(controller, **config):
    """ Log into the airflow localhost webui and perform environment setup. Arguments for config dict:
    @args:
        listening_port(int): the port number that the opened google-chrome is listening on, default is 9222
        url(str): the url of the airflow webui, default is localhost 'http://localhost:8080'
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
        url = config.get('url', 'http://localhost:8080')
        #page = waiting_for_astro_server(context, url)
        page = context.new_page()
        page.goto(url, wait_until='load')
        if page is None:
            logger.error('[ERROR]: failed to connect to Airflow Web UI!')
            return
        
        for action in config.get('actions', []):
            action_type = action.pop('type')
            init_func = ASTRO_WEBUI_FUNCTIONS[action_type]
            init_func(page, **action)

        # Close extra windows
        for i in range(2):
            context.pages[0].close()
    return
