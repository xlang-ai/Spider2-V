from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.providers.airbyte.operators.airbyte import AirbyteTriggerSyncOperator
from airflow.providers.airbyte.sensors.airbyte import AirbyteJobSensor
from airflow.sensors.filesystem import FileSensor
import pendulum

AIRBYTE_CONNECTION_ID = '' # Task 1: REPLACE THIS WITH YOUR CONNECTION ID
RAW_PRODUCTS_FILE = '/tmp/airbyte_local/json_from_faker/_airbyte_raw_products.jsonl'
COPY_OF_RAW_PRODUCTS = '/tmp/airbyte_local/json_from_faker/moved_raw_products.jsonl'

with DAG(dag_id='airbyte_example_airflow_dag',
        default_args={'owner': 'airflow'},
        schedule='@daily',
        start_date=pendulum.today('UTC').add(days=-1)
   ) as dag:

   trigger_airbyte_sync = AirbyteTriggerSyncOperator(
       task_id='airbyte_trigger_sync',
       airbyte_conn_id='airflow-call-to-airbyte-example',
       connection_id=AIRBYTE_CONNECTION_ID,
       asynchronous=True
   )

   wait_for_sync_completion = AirbyteJobSensor(
       task_id='airbyte_check_sync',
       airbyte_conn_id='airflow-call-to-airbyte-example',
       airbyte_job_id=trigger_airbyte_sync.output
   )

   raw_products_file_sensor = FileSensor(
       task_id='check_if_file_exists_task',
       timeout=5,
       filepath=RAW_PRODUCTS_FILE,
       fs_conn_id='airflow-file-connector'
   )

   move_raw_products_file = BashOperator(
       task_id='move_raw_products_file',
       bash_command=f'mv {RAW_PRODUCTS_FILE} {COPY_OF_RAW_PRODUCTS}'
   )

   trigger_airbyte_sync >> wait_for_sync_completion >>  raw_products_file_sensor >> move_raw_products_file