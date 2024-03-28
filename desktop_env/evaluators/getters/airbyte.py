#coding=utf8
import logging
from playwright.sync_api import sync_playwright, expect

logger = logging.getLogger("desktopenv.getters.airbyte")

def get_airbyte_localhost_page(env, config):
    """ Check whether the airbyte home page is opened in the browser, by default the url is http://localhost:8000.
    @return: 
        "Find airbyte home page succeed" if the airbyte home page is opened,
            otherwise "Find airbyte home page failed"
    """
    host = env.vm_ip
    port = 9222  # fixme: this port is hard-coded, need to be changed from config file

    remote_debugging_url = f"http://{host}:{port}"
    with sync_playwright() as p:
        # connect to remote Chrome instance
        try:
            browser = p.chromium.connect_over_cdp(remote_debugging_url)
        except:
            logger.error(f"[ERROR]: Failed to connect to remote Chrome instance at {remote_debugging_url}")
            return "Find airbyte home page failed"

        target_url = config.get('url', 'http://localhost:8000').replace('127.0.0.1', 'localhost')
        target_title = config.get('title', 'Airbyte').lower()
        for context in browser.contexts:
            for page in context.pages:
                try:
                    page.wait_for_load_state('networkidle')
                    url = page.url.replace('127.0.0.1', 'localhost')
                    if url.startswith(target_url) and target_title in page.title().lower():
                        element = page.locator('a[aria-label="Homepage"]')
                        expect(element).to_be_visible()
                        return "Find airbyte home page succeed"
                except:
                    pass
        return "Find airbyte home page failed"
