#coding=utf8
import os, logging, time, requests, json, random
from typing import List, Union, Tuple
from playwright.sync_api import expect

logger = logging.getLogger("desktopenv.setup")


def get_browser(p, url, trial=15):
    for attempt in range(trial):
        try:
            browser = p.chromium.connect_over_cdp(url)
            break
        except Exception as e:
            if attempt < trial - 1:
                logger.error(f"Attempt {attempt + 1}: Failed to connect Google Chrome, retrying. Error: {e}")
                time.sleep(1)
            else:
                logger.error(f"Failed to connect after multiple attempts: {e}")
                return None
    return browser


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
    except: pass
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


def download_and_execute_setup(controller, url: str, path: str = '/home/user/init.sh', options: List[str] = []):
    """ Download a script from a remote url and execute it to setup the environment.
    @args:
        controller(desktop_env.controllers.SetupController): the controller object
        url(str): remote url to download the script
        path(str): the path to save the script on VM (default: '~/init.sh')
        options(List[str]): optional arguments to execute the script (default: [])
    """
    # download the script
    controller._download_setup([{'url': url, 'path': path}])
    # execute the script
    controller._execute_setup(command=["chmod", "a+x", path])
    controller._execute_setup(command=["/bin/bash", path] + options)
    controller._execute_setup(command=["rm", "-f", path])
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
        logger.error(f"[ERROR]: Failed to copy VM file. Status code: {response.status_code}")
        return

    file = response.content
    parent_dir = os.path.dirname(dest)
    if not os.path.exists(parent_dir):
        os.makedirs(parent_dir, exist_ok=True)
    with open(dest, "wb") as of:
        of.write(file)
    return