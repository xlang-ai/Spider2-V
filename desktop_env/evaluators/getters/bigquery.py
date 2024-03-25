#coding=utf8
import json, os, logging, platform
from google.cloud import bigquery
from google.oauth2 import service_account
from google.cloud.bigquery.dataset import DatasetListItem
from google.cloud.bigquery.table import TableListItem


logger = logging.getLogger("desktopenv.getters.bigquery")


def get_bigquery_table_to_csv(env, config):
    """ Given the project name or index, dataset id and table id, return the table content if found, otherwise return None.
    @args:
        env(dict): the environment dictionary
        config(dict): the configuration dictionary
            - config_file(str): the path to the GCP config file
            - project_name(str): the project name
            - project_index(int): the project index, either project_name or project_index must be specified
            - dataset_id(str): the dataset id
            - table_id(str): the table id
            - dest(str): the path to the output file, combined with env.cache_dir
    @return:
        filepath: the filepath containing target db content if found, otherwise None
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

    dataset_id, table_id = config['dataset_id'], config['table_id']
    try:
        dataset_ref = f'{project_id}.{dataset_id}'
        list(client.list_tables(dataset_ref))
    except:
        logger.error(f'[ERROR]: Failed to get the dataset {dataset_ref} from bigquery!')
        client.close()
        return

    try:
        table_ref = f'{project_id}.{dataset_id}.{table_id}'
        client.get_table(table_ref)
    except:
        logger.error(f'[ERROR]: Failed to get the table {table_ref} from bigquery!')
        client.close()
        return

    schema = ', '.join(config['schema'])
    query = f"SELECT {schema} FROM {project_id}.{dataset_id}.{table_id}"
    try:
        job = client.query(query)
        df = job.to_dataframe()
        output_file = os.path.join(env.cache_dir, config['dest']) # adding prefix cache_dir
        df.to_csv(output_file, index=False, header=False)
    except Exception as e:
        logger.error(f'[ERROR]: Failed to get the table content from bigquery, query is {query}. Error: {e}')
        return
    finally:
        client.close()
    return output_file