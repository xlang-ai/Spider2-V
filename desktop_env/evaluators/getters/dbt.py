#coding=utf8
import json
import os, subprocess
from typing import Dict
from .general import get_vm_command_line
from .file import get_vm_file


def get_dbt_profiles(env, config: Dict[str, str]) -> str:
    """ Download dbt profiles.yml file from VM, search all possible paths and return the first one found.
    Paths include:
        config (Dict[str, Any]):
            dirs (List[str]): a list of possible dirs to search profiles.yml, if the path starts with a '$', it will be treated as an environment variable
            dest (str): local file name of the downloaded file
        working, default and environment variable DBT_PROFILES_DIR
    """
    for fp in config["dirs"]:
        if fp.startswith('$'):
            # fetching ENV vars does not work, because the command below is executed in a new shell in non-login, non-interactive mode
            # thus, the environment variable is not available
            fp = get_vm_command_line(env, {"command": ["/bin/bash", "-c", f"echo \"{fp}\""]})
            if type(fp) == str and fp.strip() != "":
                file = get_vm_file(env, {"path": fp.strip() + '/profiles.yml', "dest": config["dest"]})
                if file is not None:
                    return file
        else:
            file = get_vm_file(env, {"path": fp + '/profiles.yml', "dest": config["dest"]})
            if file is not None:
                return file

    return None

def get_dbt_project_info_output(env, config: Dict[str, str]):
    """ Print the information on Dbt cloud projects.
    @args:
        env(desktop_env.envs.DesktopEnv): the environment object
        config (dict):
            setting_files: the path to the settings file, default is 'evaluation_examples/settings/dbt_cloud/settings.json'
            field: the specific field we want to extract for evaluation. Could be:
            - name
            - connection_type
            - ... (to be added)

    """
    settings_file = config.get('settings_file', 'evaluation_examples/settings/dbt_cloud/settings.json')
    settings = json.load(open(settings_file, 'r'))

    os.environ["DBT_CLOUD_ACCOUNT_ID"] = settings["account_id"]
    os.environ["DBT_CLOUD_API_TOKEN"] = settings["token"]

    state = subprocess.run('dbt-cloud project list', shell=True, capture_output=True, text=True)
    project_list = json.loads(state.stdout)['data']

    field = config.get("field", "name")

    if len(project_list) == 0:
        return "None"
    elif field == "connection_type":
        if project_list[0]["connection"] is None:
            return "None"
        return project_list[0]["connection"]["type"]
    else:
        return project_list[0][field]

