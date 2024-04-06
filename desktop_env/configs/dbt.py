# coding=utf8
import json, logging, platform
import subprocess, os
from typing import List, Union, Tuple, Dict, Any
from playwright.sync_api import expect, sync_playwright, BrowserContext, Page
from .general import get_browser

logger = logging.getLogger("desktopenv.setup")


def dbt_cloud_create_project(**config: Dict[str, Any]):
    """ Create a new project on the supplied account. Argument for the config dict:
    @args:
        project_name (str): the name of the project. default "Analytics" (as in dbt Cloud default)
    """
    name = config.get("project_name", "Analytics")
    subprocess.run(f'dbt-cloud project create --name \"{name}\"')

    return


def dbt_cloud_delete_project(**config: Dict[str, Any]):
    """ Delete a project on the supplied account. Argument for the config dict:
    @args:
        project_id (str): the id of project to be deleted. if not supplied, this will delete the first
        project on the account.
    """
    # suppose trial account - one project per account
    if config.get("project_id", False):
        subprocess.run(f'dbt-cloud project delete --project-id {config["project_id"]}', shell=True)
    else:
        state = subprocess.run('dbt-cloud project list', shell=True, capture_output=True, text=True)
        project_list = json.loads(state.stdout)['data']
        if len(project_list) == 0:
            logger.info('[INFO]: there are no projects to be deleted!')
        else:
            subprocess.run(f'dbt-cloud project delete --project-id {project_list[0]["id"]}', shell=True)

    return


DBT_CLOUD_FUNCTIONS = {
    "create_project": dbt_cloud_create_project,
    "delete_project": dbt_cloud_delete_project
}


def dbt_cloud_init_setup(controller, **config):
    """ set up environment variables for dbt-cloud CLI on host machine. Argument for the config dict:
    @args:
        settings_file(str): the path to the settings file, default is 'evaluation_examples/settings/dbt_cloud/settings.json'
        actions(List[Dict[str, Any]]): the list of actions to perform, each action is one dict with `type` field chosen from:
            - create_project: create a new dbt cloud project on the supplied account
            - delete_project: delete a dbt cloud project on the supplied account
    """

    settings_file = config.get('settings_file', 'evaluation_examples/settings/dbt_cloud/settings.json')
    settings = json.load(open(settings_file, 'r'))

    os.environ["DBT_CLOUD_ACCOUNT_ID"] = settings["account_id"]
    os.environ["DBT_CLOUD_API_TOKEN"] = settings["token"]

    for action in config.get('actions', []):
        action_type = action.pop('type')
        init_func = DBT_CLOUD_FUNCTIONS[action_type]
        init_func(**action)

    return


def dbt_cloud_webui_login_setup(controller, **config):
    """ Log into dbt Cloud website. Argument for the config dict:
    @args:
        listening_port(int): the port number that the opened google-chrome is listening on, default is 9222
        url(str): the url of the dagster webui, default is 'https://cloud.getdbt.com/'
        settings_file(str): the path to the settings file, default is 'evaluation_examples/settings/dbt_cloud/settings.json'

    """

    listening_port = config.get('listening_port', 9222)
    remote_debugging_url = f"http://{controller.vm_ip}:{listening_port}"
    url = config.get('url', 'https://cloud.getdbt.com/')
    settings_file = config.get('settings_file', 'evaluation_examples/settings/dbt_cloud/settings.json')
    settings = json.load(open(settings_file, 'r'))

    with sync_playwright() as p:
        browser = get_browser(p, remote_debugging_url)
        if browser is None:
            logger.error('[ERROR]: failed to connect to Google Chrome browser in the running VM!')
            return

        context = browser.contexts[0]
        page = context.new_page()
        page.goto(url, wait_until='load')

        try:
            email = page.locator('input[id="email"]')
            expect(email).to_be_editable(timeout=20000)
            email.fill(settings['email'])
            password = page.locator('input[id="password"]')
            expect(password).to_be_editable()
            password.fill(settings['password'])
            remember = page.locator('input[type="checkbox"]')
            expect(remember).not_to_be_checked()
            remember.check()
            signin = page.locator('button[id="sign-in"]')
            expect(signin).to_be_enabled()
            signin.click()
            page.wait_for_load_state('load')

            # navigate to the specific account page
            os.environ["DBT_CLOUD_ACCOUNT_ID"] = settings["account_id"]
            os.environ["DBT_CLOUD_API_TOKEN"] = settings["token"]

            state = subprocess.run('dbt-cloud project list', shell=True, capture_output=True, text=True)
            project_list = json.loads(state.stdout)['data']
            if len(project_list) > 0:
                project_id = project_list[0]["id"]
                page.goto(f'https://cloud.getdbt.com/{settings["account_id"]}/projects/{project_id}/setup')

            # tick remember me

        except Exception as e:
            logger.error(f'[ERROR]: failed to login to the dbt Cloud website! {e}')
            return

        logger.info('[INFO]: successfully logged into the dbt Cloud website!')

    return
