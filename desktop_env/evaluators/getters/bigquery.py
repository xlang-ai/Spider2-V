#coding=utf8
import json, os, logging, platform
from google.cloud import bigquery
from google.oauth2 import service_account
from google.cloud.bigquery.dataset import DatasetListItem
from google.cloud.bigquery.table import TableListItem
from google.cloud import bigquery_connection_v1


logger = logging.getLogger("desktopenv.getters.bigquery")


def get_bigquery_database_to_zip(env, config):
    pass


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
    config_file = config.get('config_file', 'evaluation_examples/settings/google/gcp_config.json')
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
    credentials = service_account.Credentials.from_service_account_file(filename=keyfile_path, scopes=['https://www.googleapis.com/auth/cloud-platform',"https://www.googleapis.com/auth/drive","https://www.googleapis.com/auth/bigquery"])
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


def get_bigquery_datasets(env, config):
    """ Given the project name or index, dataset id and table id, return the table content if found, otherwise return None.
    @args:
        env(dict): the environment dictionary
        config(dict): the configuration dictionary
            - config_file(str): the path to the GCP config file
            - project_name(str): the project name
            - project_index(int): the project index, either project_name or project_index must be specified
    @return:
        datasets(list): the list of datasets
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

    try:
        datasets = client.list_datasets(project=project_id)
        dataset_names = []
        for dataset in datasets:
            dataset_names.append(dataset.dataset_id)
    except:
        logger.error(f'[ERROR]: Failed to get the {project_id} project from bigquery!')
        client.close()
        return
    return dataset_names




def get_bigquery_connections(env, config):
    """Given the BigQuery project, return the connections, otherwise return None.
    @args:
        env(dict): the environment dictionary
        config(dict): the configuration dictionary
            - config_file(str): the path to the GCP config file
    @return:
        connections(list): the list of connectionss
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
    
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = keyfile_path

    parent = f"projects/{project_id}/locations/us"
    client = bigquery_connection_v1.ConnectionServiceClient()
    request = bigquery_connection_v1.ListConnectionsRequest(parent=parent,page_size=10 )
    response = client.list_connections(request=request)
    connection_names = []
    for connection in response:
        connection_name = connection.name
        connection_names.append(connection_name.split("/")[-1])
        
    return connection_names







def get_bigquery_sql_result_to_csv(env, config):
    """ Given the project name or index, sql, return the execution results.
    @args:
        env(dict): the environment dictionary
        config(dict): the configuration dictionary
            - config_file(str): the path to the GCP config file
            - project_name(str): the project name
            - project_index(int): the project index, either project_name or project_index must be specified
            - sql(str): the path of sql file 
            - dest(str): the path to the output file, combined with env.cache_dir
    @return:
        filepath: the filepath containing target db content if found, otherwise None
    """
    config_file = config.get('config_file', 'evaluation_examples/settings/google/gcp_config.json')
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
    credentials = service_account.Credentials.from_service_account_file(filename=keyfile_path, scopes=['https://www.googleapis.com/auth/cloud-platform',"https://www.googleapis.com/auth/drive","https://www.googleapis.com/auth/bigquery"])
    client = bigquery.Client(project=project_id, credentials=credentials)

    sql = open(config['sql'], 'r').read().format(project_id)
    try:
        job = client.query(sql)
        df = job.to_dataframe()
        output_file = os.path.join(env.cache_dir, config['dest']) # adding prefix cache_dir
        df.to_csv(output_file, index=False, header=False)
    except Exception as e:
        logger.error(f'[ERROR]: Failed to get the result from bigquery, query is {sql}. Error: {e}')
        return
    finally:
        client.close()
    return output_file