#coding=utf8
import logging, os, json
from typing import Dict, Any
from desktop_env.configs.servicenow import WORKARENA_ENV
from .chrome import get_active_url_from_accessTree
from desktop_env.configs.general import get_browser
from desktop_env.evaluators.metrics.utils import compare_urls
from playwright.sync_api import sync_playwright


logger = logging.getLogger("desktopenv.getters.servicenow")


def get_workarena_task_result(env, config: Dict[str, Any]) -> str:
    """
    @config:
        settings_file (str): path to the settings file, default to evaluation_examples/settings/servicenow/settings.json
        listening_port (int): the listening port of the remote debugging server, default to 9222
    """
    global WORKARENA_ENV
    if WORKARENA_ENV is None:
        logger.error(f'[ERROR]: The WORKARENA_ENV is not set up yet or has been toren down!')
        return 'failed'

    settings_file = json.load(open(config.get('settings_file', 'evaluation_examples/settings/servicenow/settings.json'), 'r'))
    for key in settings_file:
        if key.startswith('SNOW_'):
            os.environ[key] = settings_file[key]
    listening_port = config.get('listening_port', 9222)

    remote_debugging_url = f"http://{env.vm_ip}:{listening_port}"
    try:
        task = WORKARENA_ENV.task # get tasks from the WORKARENA_ENV
        messages = WORKARENA_ENV.chat.messages # get messages from the WORKARENA_ENV
        # get active page
        active_url = get_active_url_from_accessTree(env, {"goto_prefix": "https://"})
        if active_url is None:
            raise ValueError(f'[ERROR]: failed to get the active url from the accessTree!')

        with sync_playwright() as p:
            browser = get_browser(p, remote_debugging_url)
            if browser is None:
                raise ValueError('[ERROR]: failed to connect to Google Chrome browser in the running VM!')
            
            context = browser.contexts[0]
            for page in context.pages:
                if compare_urls(page.url, active_url):
                    result, _, _, _ = task.validate(page, messages)
                    break
            else:
                raise ValueError('[ERROR]: failed to find the active page in the browser context!')
    except Exception as e:
        logger.error(f'[ERROR]: error occurred when validating the task {task}! {e}')
        result = False

    WORKARENA_ENV.close()
    WORKARENA_ENV = None # after evaluation, close the WORKARENA_ENV no matter succeed or failed
    return 'succeed' if result else "failed"