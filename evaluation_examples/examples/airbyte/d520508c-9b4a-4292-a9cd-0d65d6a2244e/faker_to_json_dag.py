from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.providers.airbyte.operators.airbyte import AirbyteTriggerSyncOperator
from airflow.providers.airbyte.sensors.airbyte import AirbyteJobSensor
from airflow.sensors.filesystem import FileSensor
import pendulum, os

AIRBYTE_CONNECTION_ID = '${connection_id}' # replace this with your connection id
SOURCE_RAW_PRODUCTS_FILE = '/tmp/airbyte_local/json_data/_airbyte_raw_products.jsonl'
TARGET_RAW_PRODUCTS_FILE = f'{os.environ["AIRFLOW_HOME"]}/data/raw_products.jsonl'

with DAG(dag_id='faker_to_json_dag',
        start_date=pendulum.today('UTC').add(days=-1)
    ) as dag:

    trigger_airbyte_sync = AirbyteTriggerSyncOperator(
        task_id='airbyte_trigger_sync',
        airbyte_conn_id='airbyte_conn',
        connection_id=AIRBYTE_CONNECTION_ID,
        asynchronous=True
    )

    wait_for_sync_completion = AirbyteJobSensor(
        task_id='airbyte_check_sync',
        airbyte_conn_id='airbyte_conn',
        airbyte_job_id=trigger_airbyte_sync.output
    )

    raw_products_file_sensor = FileSensor(
        task_id='check_if_file_exists_task',
        timeout=5,
        filepath=SOURCE_RAW_PRODUCTS_FILE,
        fs_conn_id='file_conn'
    )

    raw_products_file_ops= BashOperator(
        task_id='copy_and_rename_raw_file',
        bash_command=f'cp {SOURCE_RAW_PRODUCTS_FILE} {TARGET_RAW_PRODUCTS_FILE}'
    )

    trigger_airbyte_sync >> wait_for_sync_completion >>  raw_products_file_sensor >> raw_products_file_ops