import logging
from typing import Dict
import requests

logger = logging.getLogger("desktopenv.getters.general")


def get_vm_script_output(env, config: Dict[str, str]):
    """ Download the testing script from remote url to VM and execute it to obtain the output.
    @args:
        env(desktop_env.envs.DesktopEnv): the environment object
        config(Dict[str, Any]): contain keys
            url (str): remote url to download the testing script
            dest (str): the path to save the script on VM
            shell (bool): optional. if the script is a shell script, defaults to False
    """
    vm_ip = env.vm_ip
    port = 5000
    # download the testing script from remote url to VM
    url, dest = config["url"], config["dest"]
    env.setup_controller._download_setup([{"url": url, "path": dest}])
    env.setup_controller._execute_setup(command=["chmod", "a+x", dest])

    # execute the script to obtain the output
    script = ["/bin/bash", dest]
    shell = config.get("shell", False)
    response = requests.post(f"http://{vm_ip}:{port}/execute", json={"command": script, "shell": shell})

    print(response.json())

    if response.status_code == 200:
        return response.json()["output"]
    else:
        logger.error("Failed to get vm script output. Status code: %d", response.status_code)
        return None


def get_vm_command_line(env, config: Dict[str, str]):
    vm_ip = env.vm_ip
    port = 5000
    command = config["command"]
    shell = config.get("shell", False)

    response = requests.post(f"http://{vm_ip}:{port}/execute", json={"command": command, "shell": shell})

    print(response.json())

    if response.status_code == 200:
        return response.json()["output"]
    else:
        logger.error("Failed to get vm command line. Status code: %d", response.status_code)
        return None

def get_vm_command_error(env, config: Dict[str, str]):
    vm_ip = env.vm_ip
    port = 5000
    command = config["command"]
    shell = config.get("shell", False)

    response = requests.post(f"http://{vm_ip}:{port}/execute", json={"command": command, "shell": shell})

    print(response.json())

    if response.status_code == 200:
        return response.json()["error"]
    else:
        logger.error("Failed to get vm command line error. Status code: %d", response.status_code)
        return None


def get_vm_terminal_output(env, config: Dict[str, str]):
    return env.controller.get_terminal_output()
