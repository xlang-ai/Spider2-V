#coding=utf8
import json, os
import gymnasium as gym
import logging
import numpy as np
import playwright.sync_api
from playwright.sync_api import expect
from abc import ABC
from typing import Optional, Union
from browsergym.core.chat import Chat
from browsergym.core.task import AbstractBrowserTask
from browsergym.core.constants import BROWSERGYM_ID_ATTRIBUTE
from browsergym.core import _get_global_playwright, _set_global_playwright
from desktop_env.configs.general import get_browser
from browsergym.workarena import ALL_WORKARENA_TASKS


logger = logging.getLogger("desktopenv.setup")


def get_workarena_task_from_name(task_name):
    for task in ALL_WORKARENA_TASKS:
        if task.__name__ == task_name:
            return task
    raise ValueError(f"[ERROR]: Task {task_name} not found in workarena task set!")


class ServiceNowEnv(gym.Env, ABC):
    """ Simplified wrapper class adapted from the original BrowserEnv class.
    """
    # gym metadata
    metadata = {"render_modes": None}

    def __init__(
        self,
        task_entrypoint: Union[type[AbstractBrowserTask], str],
        cdp_url: str = 'http://172.16.12.130:9222',
        **task_kwargs,
    ):
        super().__init__()

        self.task_entrypoint = task_entrypoint if isinstance(task_entrypoint, type) else get_workarena_task_from_name(task_entrypoint)
        self.task_kwargs = task_kwargs
        self.cdp_url = cdp_url
        self.task = None
        self.browser: playwright.sync_api.Browser = None
        self.context: playwright.sync_api.BrowserContext = None
        self.page: playwright.sync_api.Page = None
        self.page_history: dict = {}
        self.chat: Chat = None


    def close(self):
        # The completely teardown is performed in DesktopEnv class, donot worry about it here.
        if self.task is not None:
            try:
                self.task.teardown()
            except: pass
            self.task = None
        if self.chat is not None:
            try:
                self.chat.close()
            except: pass
            self.chat = None
        if self.context is not None:
            try:
                self.context.close()
            except: pass
        if self.browser is not None:
            try:
                self.browser.close()
            except: pass
        pw: playwright.sync_api.Playwright = _get_global_playwright()
        if pw is not None:
            pw.stop()
            _set_global_playwright(None)
        return


    def reset(self, seed: int = 999):
        # we need the following line to seed self.np_random
        super().reset(seed=seed)

        pw: playwright.sync_api.Playwright = _get_global_playwright()
        # important: change playwright's test id attribute from "data-testid" to "bid"
        pw.selectors.set_test_id_attribute(BROWSERGYM_ID_ATTRIBUTE)
        self.browser = get_browser(pw, self.cdp_url)

        # create a new browser context for pages
        self.context = self.browser.contexts[0]
        # create the chat at the same time to make sure videos are synced
        self.chat = Chat(
            headless=True, # do not visualize the chat window
            chat_size=(500, 800)
        )

        self.context.expose_binding(
            "browsergym_page_activated", lambda source: self._activate_page_from_js(source["page"])
        )
        self.context.add_init_script(
            r"""
window.browsergym_page_activated();
window.addEventListener("focus", () => {window.browsergym_page_activated();}, {capture: true});
window.addEventListener("focusin", () => {window.browsergym_page_activated();}, {capture: true});
window.addEventListener("load", () => {window.browsergym_page_activated();}, {capture: true});
window.addEventListener("pageshow", () => {window.browsergym_page_activated();}, {capture: true});
window.addEventListener("mousemove", () => {window.browsergym_page_activated();}, {capture: true});
window.addEventListener("mouseup", () => {window.browsergym_page_activated();}, {capture: true});
window.addEventListener("mousedown", () => {window.browsergym_page_activated();}, {capture: true});
window.addEventListener("wheel", () => {window.browsergym_page_activated();}, {capture: true});
window.addEventListener("keyup", () => {window.browsergym_page_activated();}, {capture: true});
window.addEventListener("keydown", () => {window.browsergym_page_activated();}, {capture: true});
window.addEventListener("input", () => {window.browsergym_page_activated();}, {capture: true});
window.addEventListener("touchstart", () => {window.browsergym_page_activated();}, {capture: true});
window.addEventListener("touchend", () => {window.browsergym_page_activated();}, {capture: true});
document.addEventListener("visibilitychange", () => {
    if (document.visibilityState === "visible") {
        window.browsergym_page_activated();
    }
}, {capture: true});
"""
        )

        # create a new page
        self.page = self.context.new_page()
        default_page = self.context.pages[0]
        default_page.close()

        # create and setup a new task
        task_seed = self.np_random.integers(np.iinfo(np.int32).max + 1)
        self.task = self.task_entrypoint(seed=task_seed, **self.task_kwargs)
        goal, info = self.task.setup(page=self.page)

        # initialize the chat
        self.chat.add_message(
            role="assistant",
            msg="Hi! I am your UI assistant, I can perform web tasks for you. What can I help you with?",
        )
        # if any, add the task's goal to the chat
        if goal:
            self.chat.add_message(role="user", msg=goal)

        self._wait_dom_loaded()

        # after the task's setup, the active page might have changed
        # perform a safety check
        self._active_page_check()
        return


    def _wait_dom_loaded(self):
        for page in self.context.pages:
            try:
                page.wait_for_load_state("domcontentloaded", timeout=3000)
            except playwright.sync_api.TimeoutError:
                pass
            for frame in page.frames:
                try:
                    frame.wait_for_load_state("domcontentloaded", timeout=3000)
                except playwright.sync_api.TimeoutError:
                    pass

    def _activate_page_from_js(self, page: playwright.sync_api.Page):
        if not page.context == self.context:
            raise RuntimeError(
                f"Unexpected: activating a page that belongs to a different browser context ({page})."
            )

        # add the activated page to the page history (or move it to last which is the most recent)
        if page in self.page_history:
            self.page_history[page] = self.page_history.pop(
                page
            )  # move page to the end of dictionnary
        else:
            self.page_history[page] = None  # add page to the end of dictionnary

        self.page = page

    def _active_page_check(self):
        # make sure there is always a page open
        # if all pages have been closed, create a new page
        if len(self.context.pages) == 0:
            logging.warning(f"All pages are closed, opening a new page.")
            self.page = self.context.new_page()

        # if the active page got closed, get the last active page from the history
        while self.page_history and (self.page.is_closed() or self.page not in self.context.pages):
            self.page_history.pop(self.page)  # remove active page from history
            self.page = list(self.page_history.keys())[
                -1
            ]  # set last active page as the active page (most recent)

        # active page should share the same browser context with the environment
        if self.page not in self.context.pages:
            raise RuntimeError(
                f"Unexpected: active page is not part of the browser context's open pages ({self.page})."
            )

        # active page should not be closed
        if self.page.is_closed():
            raise RuntimeError(f"Unexpected: active page has been closed ({self.page}).")


WORKARENA_ENV: Optional[ServiceNowEnv] = None


def get_global_workarena():
    global WORKARENA_ENV
    return WORKARENA_ENV


def workarena_task_init_setup(controller, **config):
    """ Initialize the WorkArena task environment.
    @config:
        listening_port(int): the port number that the opened google-chrome is listening on, default is 9222
        settings_file(str): the path to the settings file, which contains `SNOW_INSTANCE_URL`, `SNOW_INSTANCE_UNAME`, `SNOW_INSTANCE_PWD`, default is 'evaluation_examples/settings/servicenow/settings.json'
        task_name(str): the name of the task to initialize
        task_kwargs(dict): the keyword arguments to pass to the task
    """
    listening_port = config.get('listening_port', 9222)
    remote_debugging_url = f"http://{controller.vm_ip}:{listening_port}"
    settings_file = json.load(open(config.get('settings_file', 'evaluation_examples/settings/servicenow/settings.json'), 'r'))
    for key in settings_file:
        if key.startswith('SNOW_'):
            os.environ[key] = settings_file[key]

    global WORKARENA_ENV
    if WORKARENA_ENV is not None:
        try:
            WORKARENA_ENV.close()
        except: pass
    instance = ServiceNowEnv(config['task_name'], cdp_url=remote_debugging_url, **config.get('task_kwargs', {}))
    instance.reset(seed=999) # random seed is fixed for selecting examples, donot modify this line
    WORKARENA_ENV = instance

    # remove the "Enable Analytics" dialog if it appears
    try:
        page = instance.page
        button = page.locator('div[role="document"][class="now-modal-dialog"] div[class="now-modal-footer"] button').filter(has_text="No")
        expect(button).to_be_enabled()
        button.click()
    except Exception as e:
        pass
    return


def workarena_unique_fields_setup(controller, **config):
    """ For Form tasks in workarena, CreateHardwareAssetTask and CreateUserTask both have unique fields that are randomly generated each time (serial_number and user_name, respectively). We write these fields into a file (with the format `field: value`), such that we only need to mention it without concrete values in the instruction.
    @config:
        field_mappings(Dict[str, str]): the field name(s) and value(s) to retrieve from task.template_record, and write the value into file
        path(str): output path in VM to save the config
    """
    field_mappings = config.get('field_mappings', {})
    if field_mappings == []: return
    instance = get_global_workarena()
    command = []
    path = config.get('path', '/home/user/Desktop/unique_fields.txt')
    for field in field_mappings:
        value = instance.task.template_record[field]
        mapping_field = field_mappings[field]
        command.append(f'echo "{mapping_field}: {value}" >> {path}')
    command = ' ; '.join(command)
    controller._execute_setup(command=["/bin/bash", "-c", command])
    return