#coding=utf8
import logging
from playwright.sync_api import sync_playwright, expect

from typing import Dict
import requests
import platform
from .general import get_vm_script_output
from bs4 import BeautifulSoup
from typing import Dict, Any, List
logger = logging.getLogger("desktopenv.getters.general")

import lxml.etree
from lxml.cssselect import CSSSelector

_accessibility_ns_map = {
    "st": "uri:deskat:state.at-spi.gnome.org",
    "attr": "uri:deskat:attributes.at-spi.gnome.org",
    "cp": "uri:deskat:component.at-spi.gnome.org",
    "doc": "uri:deskat:document.at-spi.gnome.org",
    "docattr": "uri:deskat:attributes.document.at-spi.gnome.org",
    "txt": "uri:deskat:text.at-spi.gnome.org",
    "val": "uri:deskat:value.at-spi.gnome.org",
    "act": "uri:deskat:action.at-spi.gnome.org"
}

logger = logging.getLogger("desktopenv.getters.superset")

def get_superset_localhost_page(env, config):
    """ Check whether the superset home page is opened in the browser, by default the url is http://localhost:8088.
    @return: 
        "Find superset home page succeed" if the superset home page is opened,
            otherwise "Find superset home page failed"
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
            return "Find superset home page failed"

        target_url = config.get('url', 'http://localhost:8088/superset/welcome').replace('127.0.0.1', 'localhost')
        target_title = config.get('title', 'superset').lower()
        for context in browser.contexts:
            for page in context.pages:
                try:
                    page.wait_for_load_state('networkidle')
                    url = page.url.replace('127.0.0.1', 'localhost')
                    if url.startswith(target_url) and target_title in page.title().lower():
                        element = page.locator('a[href="/superset/welcome/"]')
                        expect(element).to_be_visible()
                        return "Find superset home page succeed"
                except:
                    pass
        return "Find superset home page failed"



def get_validate_correct_url(env, config: Dict[str, str]):
    """
    @args:
        env(desktop_env.envs.DesktopEnv): the environment object
        config(Dict[str, Any]): contain keys
            src (str): remote url or local path to download the testing script
            dest (str): the path to save the script on VM
            shell (bool): optional. if the script is a shell script, defaults to False
            'goto_prefix':
                    the prefix you want to add to the beginning of the url to be opened, default is "https://",
                    (the url we get from accTree does not have prefix)
    @return: the result of the script execution
            
    """
    vm_ip = env.vm_ip
    port = 5000
    # download the testing script from remote url to VM
    src, dest = config["src"], config["dest"]
    if src.startswith('http'):
        env.setup_controller._download_setup([{"url": src, "path": dest}])
    else:
        env.setup_controller.setup([{"type": "copyfile_from_host_to_guest", "parameters": {"src": src, "dest": dest}}])
    env.setup_controller._execute_setup(command=["chmod", "a+x", dest])


    # execute the script to obtain the output
    script = ["/bin/bash", dest]
    shell = config.get("shell", False)
    response = requests.post(f"http://{vm_ip}:{port}/execute", json={"command": script, "shell": shell})

    if response.status_code == 200:
        result_json = response.json()
        respond = result_json.get("output", "")
    else:
        logger.error("Failed to get vm script output. Status code: %d", response.status_code)
        return None
    
    if hasattr(env, 'controller') and callable(getattr(env.controller, 'get_accessibility_tree', None)):
        accessibility_tree = env.controller.get_accessibility_tree()
        if accessibility_tree is None:
            print("Failed to get the accessibility tree.")
            return None
    else:
        print("Controller or method 'get_accessibility_tree' not found.")
        return None

    logger.debug("AT@eval: %s", accessibility_tree)

    at = None
    try:
        at = lxml.etree.fromstring(accessibility_tree)
    except ValueError as e:
        logger.error(f"Error parsing accessibility tree: {e}")
        return None

    # Determine the correct selector based on system architecture
    selector = None
    arch = platform.machine()
    print(f"Your architecture is: {arch}")

    if "arm" in arch:
        selector_string = "application[name=Chromium] entry[name=Address\\ and\\ search\\ bar]"
    else:
        selector_string = "application[name=Google\\ Chrome] entry[name=Address\\ and\\ search\\ bar]"

    try:
        selector = CSSSelector(selector_string, namespaces=_accessibility_ns_map)
    except Exception as e:
        logger.error(f"Failed to parse the selector for active tab URL: {e}")
        return None

    elements = selector(at) if selector else []
    if not elements:
        print("No elements found.")
        return None
    elif not elements[-1].text:
        print("No text found in the latest element.")
        return None

    # Use a default prefix if 'goto_prefix' is not specified in the config
    goto_prefix = config.get("goto_prefix", "https://")

    active_tab_url = f"{goto_prefix}{elements[0].text}"
    print(f"Active tab url now: {active_tab_url}")

    elements = respond.split(',')
    result = ""

    # Some change required for dag_run_id to be succesfully checked
    for element in elements:
        formatted_element = element.strip().replace(":", "%3A").replace("+", "%2B")
        
        if formatted_element in active_tab_url:
            print(f"{element} check succeed")
            result += f"{element} check succeed；"
        else:
            print(f"{element} check failed")
            result += f"{element} check failed；"

    return result

