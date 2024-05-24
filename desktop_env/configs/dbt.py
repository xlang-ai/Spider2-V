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
    subprocess.run(['dbt-cloud', 'project', 'create', '--name', f'{name}'],
                   shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=60, text=True, encoding="utf-8")

    return


def dbt_cloud_delete_project(**config: Dict[str, Any]):
    """ Delete a project on the supplied account. Argument for the config dict:
    @args:
        project_id (str): the id of project to be deleted. if not supplied, this will delete the first
        project on the account.
    """
    # suppose trial account - one project per account
    if config.get("project_id", False):
        subprocess.run(['dbt-cloud', 'project', 'delete', '--project-id', f'{config["project_id"]}'],
                       shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=60, text=True,
                       encoding="utf-8")
    else:
        state = subprocess.run(['dbt-cloud', 'project', 'list'],
                               shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=60, text=True,
                               encoding="utf-8")
        project_list = json.loads(state.stdout)['data']
        if len(project_list) == 0:
            logger.info('[INFO]: there are no projects to be deleted!')
        else:
            subprocess.run(['dbt-cloud', 'project', 'delete', '--project-id', f'{project_list[0]["id"]}'],
                           shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=60, text=True,
                           encoding="utf-8")

    return


def dbt_cloud_create_env(**config: Dict[str, Any]):
    """ Create a new environment. Before running this function, a project should be created in the given account.
    @args:
        env_name (str): the name of the project. default "New Environment" (as in dbt Cloud default)
    """
    name = config.get("env_name", "New Environment")
    state = subprocess.run(['dbt-cloud', 'project', 'list'],
                           shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=60, text=True,
                           encoding="utf-8")
    project_list = json.loads(state.stdout)['data']
    if len(project_list) == 0:
        logger.info('[INFO]: there are no projects to create environments on!')
    else:
        os.environ["DBT_CLOUD_PROJECT_ID"] = str(project_list[0]['id'])
        subprocess.run(['dbt-cloud', 'environment', 'create', '--name', f'{name}', '--dbt-version', '1.5.0-latest'],
                       shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=60, text=True,
                       encoding="utf-8")
    return


def dbt_cloud_create_job(**config: Dict[str, Any]):
    """ Create a new job. Before running this function, a project and an environment should be initiated.
    @args:
        job_name (str): the name of the job. default "New Job" (as in dbt Cloud default)
        env_name (str): since multiple envs could be created in a project, environment name is required4
        execute_steps (list): the execution steps of the job
    """

    job_name = config.get("job_name", "New Job")
    env_name = config.get("env_name", "New Environment")
    execute_steps = config.get("execute_steps", ["dbt build"])

    state = subprocess.run(['dbt-cloud', 'project', 'list'],
                           shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=60, text=True,
                           encoding="utf-8")
    project_list = json.loads(state.stdout)['data']
    if len(project_list) == 0:
        logger.info('[INFO]: there are no projects to create jobs on!')
    else:
        os.environ["DBT_CLOUD_PROJECT_ID"] = str(project_list[0]['id'])
        state = subprocess.run(['dbt-cloud', 'environment', 'list'],
                               shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=60, text=True,
                               encoding="utf-8")
        env_list = json.loads(state.stdout)['data']

        if len(env_list) == 0:
            logger.info('[INFO]: there are no environments to create jobs on!')
        else:
            found = False
            env_id = ""
            for env in env_list:
                if env['name'] == env_name:
                    found = True
                    env_id = env['id']
                    break
            if found is not True:
                logger.info('[INFO]: there are no environments with the specified name!')
                return
            subprocess.run(['dbt-cloud', 'job', 'create', '--environment-id', f'{env_id}', '--name', f'{job_name}', '--execute-steps', f'{execute_steps}'],
                           shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=60, text=True, encoding="utf-8")

    return


DBT_CLOUD_FUNCTIONS = {
    "create_project": dbt_cloud_create_project,
    "delete_project": dbt_cloud_delete_project,
    "create_environment": dbt_cloud_create_env,
    "create_job": dbt_cloud_create_job
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
    os.environ["DBT_CLOUD_HOST"] = settings["cloud_host"]

    for action in config.get('actions', []):
        action_type = action.pop('type', None)
        init_func = DBT_CLOUD_FUNCTIONS[action_type]
        init_func(**action)

    return


def dbt_cloud_webui_login_setup(controller, **config):
    """ Log into dbt Cloud website. Argument for the config dict:
    @args:
        listening_port(int): the port number that the opened google-chrome is listening on, default is 9222
        settings_file(str): the path to the settings file, default is 'evaluation_examples/settings/dbt_cloud/settings.json'
        goto_page(str): the page you want to go to after logged in, default is 'project_setup'
                        available values: account_setup, cli_setup
    """

    listening_port = config.get('listening_port', 9222)
    remote_debugging_url = f"http://{controller.vm_ip}:{listening_port}"
    settings_file = config.get('settings_file', 'evaluation_examples/settings/dbt_cloud/settings.json')
    settings = json.load(open(settings_file, 'r'))
    url = "http://cloud.getdbt.com"
    if "cloud_host" in settings:
        url = f"http://{settings['cloud_host']}"

    with sync_playwright() as p:
        browser = get_browser(p, remote_debugging_url)
        if browser is None:
            logger.error('[ERROR]: failed to connect to Google Chrome browser in the running VM!')
            return

        context = browser.contexts[0]
        page = context.new_page()
        page.goto(url, wait_until='load')

        try:
            email = page.locator('input[id="username"]')
            expect(email).to_be_editable(timeout=60000)
            email.fill(settings['email'])
            password = page.locator('input[id="password"]')
            expect(password).to_be_editable()
            password.fill(settings['password'])
            # remember = page.locator('input[type="checkbox"]')
            # expect(remember).not_to_be_checked()
            # remember.check()
            signin = page.locator('button[name="action"]')
            expect(signin).to_be_enabled()
            signin.click()
            page.wait_for_load_state('load')
            button = page.locator('button[data-testid="settings-menu"]')
            expect(button).to_be_visible(timeout=60000)

            # navigate to the specific account page
            os.environ["DBT_CLOUD_ACCOUNT_ID"] = settings["account_id"]
            os.environ["DBT_CLOUD_API_TOKEN"] = settings["token"]
            os.environ["DBT_CLOUD_HOST"] = settings["cloud_host"]

            state = subprocess.run(['dbt-cloud', 'project', 'list'],
                                   shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=60, text=True,
                                   encoding="utf-8")
            project_list = json.loads(state.stdout)['data']

            goto_page = config.get('goto_page', 'project_setup')
            if goto_page == 'project_setup' and len(project_list) > 0:
                project_id = project_list[0]["id"]
                page.goto(f'{url}/{settings["account_id"]}/projects/{project_id}/setup',
                          wait_until='load')

                # skip the connection/repository configuration
                # 0 - no skip
                # 1 - skip connection configuration
                # 2 - skip connection + repository configuration
                skip_step = config.get("skip_step", 0)
                for i in range(skip_step):
                    page.wait_for_selector('button[type="button"]')
                    skip = page.locator('button[type="button"]').filter(has_text="Skip")
                    expect(skip).to_be_visible()
                    skip.click()

                    # fixme: hard wait!!
                    page.wait_for_timeout(1500)
                    page.wait_for_load_state('load')
            elif goto_page == 'account_setup':
                page.goto(f'{url}/settings/accounts/{settings["account_id"]}/pages/account')
            elif goto_page == 'cli_setup':
                page.goto(f'{url}/settings/profile/cloud-cli')

        except Exception as e:
            logger.error(f'[ERROR]: failed to login to the dbt Cloud website! {e}')
            return

        logger.info('[INFO]: successfully logged into the dbt Cloud website!')

    return
