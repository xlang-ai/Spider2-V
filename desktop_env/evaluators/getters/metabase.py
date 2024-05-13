#coding=utf8
import logging, time
from typing import Dict, Any
from desktop_env.configs.general import get_browser, find_page_by_url
from playwright.sync_api import expect, sync_playwright

logger = logging.getLogger("desktopenv.getters.metabase")


def get_metabase_question_sql(env, config: Dict[str, Any]) -> str:
    """ Get the SQL query of the metabase question. Arguments for config dict:
    @args:
        listening_port(int): the port number that the opened google-chrome is listening on, default is 9222
    @returns:
        sql(str): the SQL query of the metabase question, if found, else None
    """
    listening_port = config.get('listening_port', 9222)
    remote_debugging_url = f"http://{env.vm_ip}:{listening_port}"
    with sync_playwright() as p:
        browser = get_browser(p, remote_debugging_url)
        if browser is None:
            logger.error('[ERROR]: failed to connect to Google Chrome browser in the running VM!')
            return None
        context = browser.contexts[0]
        page = find_page_by_url(context, 'http://localhost:3000', matching_func=lambda x, y: x.startswith(y))
        if page is None:
            logger.error('[ERROR]: failed to find Metabase page in the running VM!')
            return None
        try:
            button = page.locator('button[aria-label="View the SQL"]')
            expect(button).to_be_enabled(timeout=60000)
            button.click()
            panel = page.locator('div[role="dialog"] > div:nth-child(1) > div:nth-child(2)')
            for _ in range(3):
                sql = ' '.join(panel.inner_text().lower().replace('\n', ' ').split())
                if len(sql) > 0:
                    break
                time.sleep(3)
        except Exception as e:
            logger.error(f'[ERROR]: failed to get SQL query of the metabase question! {e}')
            return None
    return sql
