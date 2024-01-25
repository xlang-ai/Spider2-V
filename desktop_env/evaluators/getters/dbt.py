#coding=utf8
import os
from typing import Dict
from .general import get_vm_command_line
from .file import get_vm_file


def get_dbt_profiles(env, config: Dict[str, str]) -> str:
    """ Download dbt profiles.yml file from VM, search all possible paths and return the first one found.
    Paths include:
        config (Dict[str, Any]):
            paths (List[str]): a list of possible paths to search, if the path starts with a '$', it will be treated as an environment variable
            dest (str): local file name of the downloaded file
        working, default and environment variable DBT_PROFILES_DIR
    """
    for fp in config["paths"]:
        if fp.startswith('$'):
            fp = get_vm_command_line(env, {"command": ["/bin/bash", "-c", f"echo \"{fp}\""]})
            if type(fp) == str and fp.strip() != "":
                file = get_vm_file(env, {"path": fp.strip(), "dest": config["dest"]})
                if file is not None:
                    return file
        else:
            file = get_vm_file(env, {"path": fp, "dest": config["dest"]})
            if file is not None:
                return file

    return None


def get_dbt_test_result(env, config: Dict[str, str]) -> str:
    """ Download cloud test cases to VM and run test command for each test case through VM to get test results.
    @args:
        config(Dict[str, Any]): contain keys
            path (Union[str, List[str]]): path to the cloud test cases, usually path list for multiple test cases
            dest (str): download path on VM, usually the same destination for all test cases
            pre-processing (str): optional. command to run before downloading test cases
            post-processing (str): optional. command to run after downloading test cases
    """
    if 'pre-processing' in config: # prepare the environment, usually backup the original databases or data
        _ = get_vm_command_line(env, {"command": config['pre-processing']})
    
    # download test cases to VM
    download_paths = [config['path']] if type(config['path']) == str else config['path']
    results = []
    for fp in download_paths:
        env.setup_controller._download_setup([{"url": fp, "path": config["dest"]}])
        # run test command
        result = get_vm_command_line(env, {"command": config['command']})
        results.append(result)

    if 'post-processing' in config: # restore the environment, usually restore the original databases or data
        _ = get_vm_command_line(env, {"command": config['post-processing']})

    if type(config['path']) == str:
        return results[0]
    return results