# coding=utf8
import base64
import os, logging, time, requests, json, random, uuid, platform
import shutil
from typing import List, Union, Tuple, Any
from playwright.sync_api import expect, sync_playwright, BrowserContext, Page
from requests_toolbelt.multipart.encoder import MultipartEncoder

logger = logging.getLogger("desktopenv.setup")


def get_browser(p, url, trial=15):
    for attempt in range(trial):
        try:
            browser = p.chromium.connect_over_cdp(url)
            break
        except Exception as e:
            if attempt < trial - 1:
                # logger.error(f"Attempt {attempt + 1}: Failed to connect Google Chrome, retrying. Error: {e}")
                time.sleep(3)
            else:
                # TODO: add error handling for browser close and re-open
                logger.error(f"Failed to connect after multiple attempts: {e}")
                return
    return browser


def find_page_by_url(context: BrowserContext, url: str, matching_func: callable = lambda x, y: x == y):
    """ Find the page with the specified URL in the context.
    @args:
        context(playwright.sync_api.BrowserContext): the browser context object
        url(str): the URL of the page to find
        matching_func(callable): the function to match the URL, default is exact match
    @return:
        page: the page object with the specified URL, if found else None
    """
    for page in context.pages:
        if matching_func(page.url, url):
            return page
    return


def init_page_with_js(page: Page, script_path: str) -> Any:
    with open(script_path, 'r') as f:
        js_script = f.read().strip()
    page.evaluate(js_script)
    return page


def google_chrome_browser_setup(controller, **config):
    """ Setup the Google Chrome browser with remote debugging port and listening port, and open some url pages.
    config(Dict[str, Any]):
        debugging_port(int): the remote debugging port in VM (default: 1337)
        listening_port(int): the listening port in localhost (default: 9222)
        incognito(bool): whether to open the browser in incognito mode (default: False)
        full_screen(bool): whether to open the browser in maximize size (default: False)
        urls(List[str]): a list of urls to open in the browser (default: [])
    """
    debugging_port = config.get('debugging_port', 1337)
    listening_port = config.get('listening_port', 9222)
    options = ["--incognito"] if config.get('incognito', False) else []
    if config.get('full_screen', False):
        options.append("--start-maximized")
    controller._launch_setup(command=["google-chrome", f"--remote-debugging-port={debugging_port}"] + options)
    controller._launch_setup(command=["socat", f"tcp-listen:{listening_port},fork", f"tcp:localhost:{debugging_port}"])

    urls_to_open = config.get('urls', [])
    if urls_to_open:
        remote_debugging_url = f"http://{controller.vm_ip}:{listening_port}"
        with sync_playwright() as p:
            browser = get_browser(p, remote_debugging_url)
            if not browser:
                logger.error('[ERROR]: failed to connect to Google Chrome browser in the running VM!')
                return

            for i, url in enumerate(urls_to_open):
                if i == 0:  # get content
                    context = browser.contexts[0]

                page = context.new_page()  # Create a new page within the existing context
                try:
                    page.goto(url, timeout=60000)
                except Exception as e:
                    logger.warning(f"[WARNING]: opening URL {url} exceeds time limit.")

                if i == 0:  # clear the default tab
                    default_page = context.pages[0]
                    default_page.close()

            # Do not close the context or browser; they will remain open after script ends
            return browser, context
    return


def simulate_human_click(controller, x_y: Tuple[float, float]):
    """ Simulate the human click at the position (x, y) on the desktop.
    @args:
        controller(desktop_env.controllers.SetupController): the controller object
        x_y(Tuple[float, float]): the position to click
    """
    # move_mode = random.choice(
    #         ["pyautogui.easeInQuad", "pyautogui.easeOutQuad", "pyautogui.easeInOutQuad", "pyautogui.easeInBounce",
    #          "pyautogui.easeInElastic"])
    # duration = random.uniform(3, 5)
    # move_command = f"pyautogui.moveTo({x_y[0]}, {x_y[1]}, {duration}, {move_mode})"
    # click_command = f"pyautogui.mouseDown({x_y[0]}, {x_y[1]}); time.sleep(random.uniform(0.1, .2)); pyautogui.mouseUp({x_y[0]}, {x_y[1]})"
    click_command = f"pyautogui.click({x_y[0]}, {x_y[1]}, duration={random.uniform(0.1, .2)})"
    pkg_prefix = "import pyautogui; {command}"
    command_list = ["python3", "-c", pkg_prefix.format(command=click_command)]
    payload = json.dumps({"command": command_list, "shell": False})
    headers = {
        'Content-Type': 'application/json'
    }

    try:
        http_server = 'http://' + controller.vm_ip + ':5000'
        response = requests.post(http_server + "/execute", headers=headers, data=payload)
        if response.status_code == 200: return
    except:
        pass
    logger.error(f"[ERROR]: Failed to simulate human click at position {x_y}, status code: {response.status_code}")
    return


def expand_toggle_button(button, key, value, trials=3):
    """ Click the toggle button to obtain the desired `key=value` state.
    @return:
        True: the desired state is obtained via clicking the toggle button
        False: unable to achieve the desired state after maximum trials = 3
    """
    count = 0
    while count < trials:
        try:
            # click the toggle button and attribute check are not synchronous, delay exists
            # assert to_have_attribute has timeout (5s), while get_attribute may fetch out-of-date values
            expect(button).to_have_attribute(key, value)
            return True
        except:
            button.click()
            button.page.wait_for_load_state('load')
        count += 1
    logger.error(f'[ERROR]: Failed to achieve the desired {key}={value} state for toggle button after {trials} trials!')
    return False


def get_element_desktop_position(page, element):
    """ Get the position of one element relative to the desktop.
    @return:
        (x1, y1): the top-left corner of the element
        (x2, y2): the bottom-right corner of the element
    """
    window_info = page.evaluate('''() => {
        return {
            x: window.screenX,
            y: window.screenY,
            dy: window.outerHeight - window.innerHeight
        };
    }''')
    box = element.bounding_box()
    x1, y1 = box['x'] + window_info['x'], box['y'] + window_info['y'] + window_info['dy']
    x2, y2 = x1 + box['width'], y1 + box['height']
    return [(x1, y1), (x2, y2)]


def download_file_to_local(controller, url, path='output.bin', use_cache=True):
    if platform.system() == 'Windows':
        path = path.replace('/', '\\')
    cache_path: str = os.path.join(controller.cache_dir, "{:}_{:}".format(
        uuid.uuid5(uuid.NAMESPACE_URL, url),
        os.path.basename(path)))

    if use_cache and os.path.exists(cache_path): return cache_path

    max_retries = 3
    downloaded = False
    e = None
    for i in range(max_retries):
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()

            with open(cache_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            # logger.info("File downloaded successfully")
            downloaded = True
            break

        except requests.RequestException as e:
            pass
            # logger.error(f"Failed to download {url} caused by {e}. Retrying... ({max_retries - i - 1} attempts left)")
    if not downloaded:
        raise requests.RequestException(f"Failed to download {url} after {max_retries} trials. Error: {e}")
    return cache_path


def script_and_execute_setup(controller, src: str, dest: str = '/home/user/init.sh', options: List[str] = []):
    """ Upload a script from remote cloud or localhost to VM and execute it to setup the environment.
    @args:
        controller(desktop_env.controllers.SetupController): the controller object
        src(str): remote url or local path to the script
        dest(str): the path to save the script on VM (default: '~/init.sh')
        options(List[str]): optional arguments to execute the script (default: [])
    """
    if src.startswith('http'):  # url path
        controller._download_setup([{'url': src, 'path': dest}])
    else:
        if platform.system() == 'Windows':
            src = src.replace('/', '\\')
        copyfile_from_host_to_guest_setup(controller, src=src, dest=dest)

    # execute the script
    controller._execute_setup(command=["chmod", "a+x", dest])
    if platform.system() == 'Windows':
        # check and convert the line endings to Unix format
        controller._execute_setup(command=["dos2unix", dest] + options)
    controller._execute_setup(command=["/bin/bash", dest] + options)
    controller._execute_setup(command=["rm", "-f", dest])
    return

def copyfile_from_guest_to_host_setup(controller, src: str, dest: str):
    """ Transfer a file from VM to host.
    @args:
        controller(desktop_env.controllers.SetupController): the controller object
        src(str): VM file path
        dest(str): local file path
    """
    http_server = f"http://{controller.vm_ip}:5000"
    response = requests.post(http_server + "/file", data={"file_path": src})
    if response.status_code != 200:
        logger.error(f"[ERROR]: Failed to copy file from VM. Status code: {response.status_code}")
        return

    file = response.content
    if platform.system() == 'Windows':
        dest = dest.replace('/', '\\')
    parent_dir = os.path.dirname(dest)
    if not os.path.exists(parent_dir):
        os.makedirs(parent_dir, exist_ok=True)
    with open(dest, "wb") as of:
        of.write(file)
    return


def copyfile_from_host_to_guest_setup(controller, src: str, dest: str, json_encode=False):
    """ Transfer a file from host to VM.
    @args:
        controller(desktop_env.controllers.SetupController): the controller object
        src(str): local file path
        dest(str): VM file path
    """
    http_server = f"http://{controller.vm_ip}:5000"

    temp_src = "cache/encoded_key_file.json"
    if platform.system() == 'Windows':
        src = src.replace('/', '\\')
        temp_src = temp_src.replace('/', '\\')

    if json_encode:
        cached_file = os.path.join(controller.cache_dir, os.path.basename(src))
        shutil.copy(src, cached_file)
        with open(cached_file, "r") as f:
            data = json.load(f)
        for key, value in data.items():
            encoded_value = base64.b64encode(str(value).encode()).decode()
            data[key] = encoded_value
        with open(cached_file, "w") as f:
            json.dump(data, f, indent=4)
        src = cached_file

    form = MultipartEncoder({
        "file_path": dest,
        "file_data": (os.path.basename(dest), open(src, "rb"))
    })
    headers = {"Content-Type": form.content_type}

    try:
        response = requests.post(http_server + "/setup/upload", headers=headers, data=form)
        if response.status_code == 200:
            logger.info(f"Command executed successfully: {response.text}")
        else:
            logger.error(f"Failed to upload file {src} to {dest}. Status code: {response.text}")
    except requests.exceptions.RequestException as e:
        logger.error("An error occurred while trying to send the request: %s", e)

    return
