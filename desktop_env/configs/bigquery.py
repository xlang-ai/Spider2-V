#coding=utf8
import json, logging, platform
from google.cloud import bigquery
from google.oauth2 import service_account
from google.cloud.bigquery.dataset import DatasetListItem
from .google_cloud import gcp_webgui_setup
from .general import download_file_to_local
from typing import List, Tuple, Union


logger = logging.getLogger("desktopenv.setup")


def bigquery_init_setup(controller, **config):
    """ Setup the BigQuery client and perform environment setup. Please ensure that BigQuery API is enabled for the specified project. Arguments for config dict:
    @args:
        config_file(str): the path to the GCP keyfile, default is 'evaluation_examples/google/gcp_config.json'
        project_name(str): the GCP name to search in the config file, if not provided, use project_index to get the project
        project_index(int): the index of the project in the config file, either this field or project_name must be provided
        actions(list): the list of actions to perform, each action is one dict with `type` field chosen from ['empty']:
        (No perfect documentation found, please refer to bigquery source codes for more details)
            - empty: empty the entire GCP, including datasets, jobs, routines, models, tables, etc.
    """
    config_file = config.get('config_file', 'evaluation_examples/google/gcp_config.json')
    if platform.system() == 'Windows':
        config_file = config_file.replace('/', '\\')
    gcp_config = json.load(open(config_file, 'r'))
    if 'project_name' in config:
        prj_name = config['project_name']
        for proj in gcp_config:
            if prj_name == proj['project_name']:
                gcp_config = proj
                break
        else:
            raise ValueError(f'[ERROR]: The specified project name {prj_name} is not found in the GCP config file!')
    else:
        assert 'project_index' in config, "Must specify either project_name or project_index in config!"
        gcp_config = gcp_config[config['project_index']]
    keyfile_path, project_id = gcp_config['keyfile_path'], gcp_config['project_id']
    credentials = service_account.Credentials.from_service_account_file(keyfile_path)
    client = bigquery.Client(project=project_id, credentials=credentials)

    actions = config.get('actions', [])
    if len(actions) == 0:
        logger.error('[ERROR]: No action is specified in the `actions` field!')
        return

    for action in actions:
        if action['type'] == 'empty':
            for job in client.list_jobs():
                client.cancel_job(job)
                client.delete_job_metadata(job)
            for dataset in client.list_datasets():
                # TODO: not sure whether routines and models should be included
                for routine in client.list_routines(dataset):
                    client.delete_routine(routine, not_found_ok=True)
                for model in client.list_models(dataset):
                    client.delete_model(model, not_found_ok=True)
                client.delete_dataset(dataset, delete_contents=True)
        elif action['type'] == 'create_table':
            dataset_id, table_id, schema = action['dataset_id'], action['table_id'], None
            dataset_ref = f'{project_id}.{dataset_id}'
            dataset = bigquery.Dataset(dataset_ref)
            client.create_dataset(dataset, exists_ok=True) # if dataset exists, it is ok
            table_ref = f'{project_id}.{dataset_id}.{table_id}'
            if 'schema_from_json' in action:
                schema = [bigquery.SchemaField(
                    s["name"], 
                    s.get('type', "STRING"),
                    mode=s.get('mode', "NULLABLE")) for s in action['schema_from_json']]
            # other methods to load schema can be added here
            try:
                client.create_table(bigquery.Table(table_ref, schema=schema), exists_ok=False)
            except:
                logger.error(f'[ERROR]: Error when creating table {table_id}, please check whether it already exists!')
                client.close()
                return
            if 'data_from_csv' in action:
                url_path = action['data_from_csv']
                local_path = download_file_to_local(controller, url_path, f'{table_ref}.csv')
                # either autodetect or schema must be provided
                config = {'skip_leading_rows': 1, 'autodetect': True} if schema is None else {'skip_leading_rows': 0, 'schema': schema}
                job_config = bigquery.LoadJobConfig(source_format=bigquery.SourceFormat.CSV, **config)
                with open(local_path, 'rb') as source_file:
                    job = client.load_table_from_file(source_file, table_ref, job_config=job_config)
                job.result()
            # other methods to load data, e.g., data_from_uri, etc., can be added here
        else:
            raise ValueError(f'[ERROR]: The action type {action["type"]} is not supported yet for bigquery!')
    client.close()
    return


def bigquery_login_setup(controller, **config):
    """ Login in to the specified GCP. Arguments for config dict:
    @args:
        settings_file(str): the path to the google account and password, default is 'evaluation_examples/google/settings.json'
        config_file(str): the path to the GCP keyfile, default is 'evaluation_examples/google/gcp_config.json'
        project_name(str): the GCP name to search in the config file, if not provided, use project_index to get the project
        project_index(int): the index of the project in the config file, either this field or project_name must be provided
    """
    config_file = config.get('config_file', 'evaluation_examples/google/gcp_config.json')
    if platform.system() == 'Windows':
        config_file = config_file.replace('/', '\\')
    gcp_config = json.load(open(config_file, 'r'))
    if 'project_name' in config:
        prj_name = config['project_name']
        for proj in gcp_config:
            if prj_name == proj['project_name']:
                gcp_config = proj
                break
        else:
            raise ValueError(f'[ERROR]: The specified project name {prj_name} is not found in the GCP config file!')
    else:
        assert 'project_index' in config, "Must specify either project_name or project_index in config!"
        gcp_config = gcp_config[config['project_index']]

    product, project_id = 'bigquery', gcp_config['project_id']
    url = f'https://console.cloud.google.com/{product}?project={project_id}'
    params = {"url": url, "actions": []}
    if 'settings_file' in config: params['settings_file'] = config['settings_file']

    return gcp_webgui_setup(controller, **params)