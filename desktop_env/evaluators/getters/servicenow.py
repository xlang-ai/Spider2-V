#coding=utf8
import logging, os, json
from typing import Dict, Any
from .chrome import get_active_url_from_accessTree
from desktop_env.configs.servicenow import get_global_workarena
from desktop_env.evaluators.metrics.utils import compare_urls
from desktop_env.evaluators.getters.file import get_vm_file


logger = logging.getLogger("desktopenv.getters.servicenow")


def get_workarena_task_result(env, config: Dict[str, Any]) -> str:
    """
    @config:
        settings_file (str): path to the settings file, default to evaluation_examples/settings/servicenow/settings.json
        path (str): path to the result file in the VM
        dest (str): filename of the result file to save in localhost
        close (bool): whether to close the workarena instance after the task is done, default to True
    """
    # must put it here, instead of the top of the file
    workarena_instance = get_global_workarena()
    if workarena_instance is None:
        logger.error(f'[ERROR]: The WORKARENA_ENV is not set up yet or has been toren down!')
        return 'failed'

    settings_file = json.load(open(config.get('settings_file', 'evaluation_examples/settings/servicenow/settings.json'), 'r'))
    for key in settings_file:
        if key.startswith('SNOW_'):
            os.environ[key] = settings_file[key]

    try:
        task = workarena_instance.task # get tasks from the WORKARENA_ENV
        messages = workarena_instance.chat.messages # get messages from the WORKARENA_ENV
        # for examples writing answers into files, e.g., KnowledgeBaseSearchTask
        if type(task).__name__ in ['KnowledgeBaseSearchTask']:
            filepath = get_vm_file(env, {'path': config['path'], 'dest': config['dest']})
            if filepath is None:
                raise ValueError(f'[ERROR]: failed to obtain the target file with path {config["path"]} in VM.')
            with open(filepath, 'r') as inf:
                answer = inf.read()
            messages.append({"role": "assistant", "message": answer})

        # get active page
        active_url = get_active_url_from_accessTree(env, {"goto_prefix": "https://"})
        if active_url is None:
            raise ValueError(f'[ERROR]: failed to get the active url from the accessTree!')
        
        context = workarena_instance.context
        for page in context.pages:
            page.reload() # the page.url is still the old url, need to refresh
            if compare_urls(page.url, active_url):
                result, _, _, info = task.validate(page, messages)
                logger.info(f'[INFO]: the task {type(task).__name__} is validated with result {result} and info {info}')
                break
        else:
            raise ValueError(f'[ERROR]: failed to find the active page {active_url} in the browser context!')
    except ValueError as e:
        logger.error(f'[ERROR]: value error with respect to active page urls for service now! {e}')
        result = False
    except Exception as e:
        logger.error(f'[ERROR]: error occurred when validating the task {task}! {e}')
        result = False
    if config.get('close', True) and workarena_instance is not None:
        try:
            workarena_instance.close()
        except:
            logger.warning('[WARNING]: failed to close the workarena instance!')
    return 'succeed' if result else "failed"