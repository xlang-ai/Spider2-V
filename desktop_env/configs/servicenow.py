#coding=utf8
import copy, json, os
import gymnasium as gym
import logging
import numpy as np
import playwright.sync_api
from playwright.sync_api import expect
from abc import ABC
from pathlib import Path
from typing import Optional, Literal, Union
import browsergym.core
from browsergym.core.chat import Chat
from browsergym.core.task import AbstractBrowserTask
from browsergym.core.spaces import Unicode, AnyDict
from browsergym.core.constants import TEXT_MAX_LENGTH, BROWSERGYM_ID_ATTRIBUTE, EXTRACT_OBS_MAX_TRIES
from browsergym.core.observation import (
    _pre_extract,
    _post_extract,
    extract_screenshot,
    extract_dom_snapshot,
    extract_merged_axtree,
    extract_focused_element_bid,
)
from browsergym.core.action.base import execute_python_code
from browsergym.core.action.highlevel import HighLevelActionSet
from browsergym.core.action.base import execute_python_code
from browsergym.core import _get_global_playwright
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
        # headless: bool = True,
        # viewport: dict = {"width": 1280, "height": 720},
        # slow_mo: int = 1000,  # in milliseconds
        # timeout: int = 5000,
        # wait_for_user_message: bool = False,
        # demo_mode: Literal["off", "default", "only_visible_elements"] = "off",
        # record_video_dir: str = None,
        # playwright_kwargs: dict = {},
        # action_mapping: Optional[callable] = HighLevelActionSet().to_python_code,
        **task_kwargs,
    ):
        super().__init__()

        self.task_entrypoint = task_entrypoint if isinstance(task_entrypoint, type) else get_workarena_task_from_name(task_entrypoint)
        self.task_kwargs = task_kwargs
        self.cdp_url = cdp_url
        # self.headless = headless
        # self.slow_mo = slow_mo
        # self.timeout = timeout
        # self.wait_for_user_message = wait_for_user_message
        # self.demo_mode = demo_mode
        # self.action_mapping = action_mapping
        # self.record_video_dir = record_video_dir

        # task
        self.task = None

        # playwright
        # self.playwright_kwargs = playwright_kwargs
        # self.playwright_kwargs.setdefault("headless", self.headless)
        # self.playwright_kwargs.setdefault("slow_mo", self.slow_mo)
        # self.playwright_kwargs.setdefault(
        #     "args", [f"--window-size={self.viewport['width']},{self.viewport['height']}"]
        # )
        self.browser: playwright.sync_api.Browser = None
        self.context: playwright.sync_api.BrowserContext = None
        self.page: playwright.sync_api.Page = None
        self.page_history: dict = {}

        # chat
        self.chat: Chat = None

        # observation space
        # self.observation_space = gym.spaces.Dict(
        #     {
        #         "chat_messages": gym.spaces.Sequence(
        #             gym.spaces.Dict(
        #                 {
        #                     "role": Unicode(min_length=0, max_length=TEXT_MAX_LENGTH),
        #                     "message": Unicode(min_length=0, max_length=TEXT_MAX_LENGTH),
        #                 }
        #             )
        #         ),
        #         # TODO: this is redundant with chat messages, to be removed
        #         "goal": Unicode(min_length=0, max_length=TEXT_MAX_LENGTH),
        #         "open_pages_urls": gym.spaces.Sequence(
        #             Unicode(min_length=0, max_length=TEXT_MAX_LENGTH)
        #         ),
        #         "active_page_index": gym.spaces.Box(low=0, high=255, dtype=int),
        #         "url": Unicode(min_length=0, max_length=TEXT_MAX_LENGTH),
        #         "screenshot": gym.spaces.Box(
        #             0,
        #             255,
        #             shape=(viewport["height"], viewport["width"], 3),
        #             dtype=np.uint8,
        #         ),  # swapped axes (height first)
        #         "dom_object": AnyDict(),
        #         "axtree_object": AnyDict(),
        #         "focused_element_bid": Unicode(min_length=0, max_length=TEXT_MAX_LENGTH),
        #         "last_action": Unicode(min_length=0, max_length=TEXT_MAX_LENGTH),
        #         "last_action_error": Unicode(min_length=0, max_length=TEXT_MAX_LENGTH),
        #         "elapsed_time": gym.spaces.Box(low=0, high=np.inf, dtype=float),
        #     }
        # )

        # action space
        # self.action_space = Unicode(min_length=0, max_length=TEXT_MAX_LENGTH)

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


    def reset(self, seed=None, *args, **kwargs):
        # we need the following line to seed self.np_random
        super().reset(seed=seed, *args, **kwargs)

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

        # set default timeout
        # self.context.set_default_timeout(self.timeout)

        # hack: keep track of the active page with a javascript callback
        # there is no concept of active page in playwright
        # https://github.com/microsoft/playwright/issues/2603
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
        self.task = self.task_entrypoint(**self.task_kwargs)
        goal, info = self.task.setup(seed=task_seed, page=self.page)

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

        # init start time
        # self.start_time = time.time()

        # no action yet
        # self.last_action = ""
        # self.last_action_error = ""

        # if asked, wait for user message
        # self._wait_for_user_message()

        # extract obs and info from environment
        # obs = self._get_obs()

        # if self.record_video_dir:
            # info["recording_start_time"] = recording_start_time
        
        # return info
        return

    # def step(self, action: str) -> tuple:
    #     self.last_action = action

    #     # try to execute the action
    #     try:
    #         if self.action_mapping:
    #             code = self.action_mapping(action)
    #         else:
    #             code = action
    #         execute_python_code(
    #             code,
    #             self.page,
    #             send_message_to_user=lambda text: self.chat.add_message(role="assistant", msg=text),
    #         )
    #         self.last_action_error = ""
    #     except Exception as e:
    #         self.last_action_error = f"{type(e).__name__}: {e}"

    #     # wait a bit (for the JavaScript callback to set the active page)
    #     time.sleep(0.5)  # wait for JS events to be fired (half a second)
    #     self.context.cookies()  # trigger all waiting Playwright callbacks on the stack (hack, see https://playwright.dev/java/docs/multithreading)

    #     # wait for the network to idle before extracting the observation, reward etc.
    #     self._wait_dom_loaded()

    #     # after the action is executed, the active page might have changed
    #     # perform a safety check
    #     self._active_page_check()

    #     # if asked, wait for user message
    #     self._wait_for_user_message()

    #     # extract reward, done, user_message, info (task-specific)
    #     reward, done, user_message, info = self._task_validate()

    #     # add any user message sent by the task to the chat
    #     if user_message:
    #         self.chat.add_message(role="user", msg=user_message)

    #     # extract observation (generic)
    #     obs = self._get_obs()

    #     # new step API wants a 5-tuple (gymnasium)
    #     terminated = done
    #     truncated = False

    #     return obs, reward, terminated, truncated, info

    # def _task_validate(self):
    #     # back-up these in case validate() navigates pages and messes the history
    #     prev_active_page = self.page
    #     prev_page_history = self.page_history.copy()

    #     # call validate
    #     reward, done, user_message, info = self.task.validate(self.page, self.chat.messages)

    #     # safety fix, in case validate() did mess up the active page and/or page history
    #     if prev_active_page != self.page or prev_page_history != self.page_history:
    #         logging.warning(
    #             "The active page and / or page history has changed during task.validate(). A recovery fix will be applied."
    #         )
    #         self.page = prev_active_page
    #         self.page_history = prev_page_history

    #     return reward, done, user_message, info

    # def _wait_for_user_message(self):
    #     # if last message is from the assistant, wait for a user message to continue
    #     # TODO: be smarter about when to wait for a user message (different action from the assistant?)
    #     logger.info("Waiting for user message...")
    #     if self.chat.messages[-1]["role"] == "assistant" and self.wait_for_user_message:
    #         self.chat.wait_for_user_message()

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

    # def _get_obs(self):

    #     for retries_left in reversed(range(EXTRACT_OBS_MAX_TRIES)):
    #         try:
    #             # pre-extraction, mark dom elements (set bid, set dynamic attributes like value and checked)
    #             _pre_extract(self.page)

    #             dom = extract_dom_snapshot(self.page)
    #             axtree = extract_merged_axtree(self.page)
    #             focused_element_bid = extract_focused_element_bid(self.page)
    #         except playwright.sync_api.Error as e:
    #             err_msg = str(e)
    #             # try to add robustness to async events (detached / deleted frames)
    #             if retries_left > 0 and (
    #                 "Frame was detached" in err_msg
    #                 or "Frame with the given frameId is not found" in err_msg
    #                 or "Execution context was destroyed" in err_msg
    #             ):
    #                 logging.warning(
    #                     f"An error occured while extracting the dom and axtree. Retrying ({retries_left}/{EXTRACT_OBS_MAX_TRIES} tries left).\n{repr(e)}"
    #                 )
    #                 # post-extract cleanup (aria-roledescription attribute)
    #                 _post_extract(self.page)
    #                 time.sleep(0.5)
    #                 continue
    #             else:
    #                 raise e
    #         break

    #     # post-extraction cleanup of temporary info in dom
    #     _post_extract(self.page)

    #     # use first user message as goal, if any
    #     if len(self.chat.messages) > 1:
    #         assert self.chat.messages[1]["role"] == "user"
    #         goal = self.chat.messages[1]["message"]
    #     else:
    #         goal = "Do whatever."

    #     # obs is generic to all tasks
    #     obs = {
    #         "chat_messages": copy.deepcopy(self.chat.messages),
    #         "goal": goal,  # TODO: redundant with chat messages, to be removed?
    #         "open_pages_urls": [page.url for page in self.context.pages],
    #         "active_page_index": np.asarray([self.context.pages.index(self.page)]),
    #         "url": self.page.url,
    #         "screenshot": extract_screenshot(self.page),
    #         "dom_object": dom,
    #         "axtree_object": axtree,
    #         "focused_element_bid": focused_element_bid,
    #         "last_action": self.last_action,
    #         "last_action_error": self.last_action_error,
    #         "elapsed_time": np.asarray([time.time() - self.start_time]),
    #     }

    #     return obs


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