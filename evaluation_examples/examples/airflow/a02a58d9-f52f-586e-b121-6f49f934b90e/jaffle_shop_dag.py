"""
### Run a dbt Core project as a task group with Cosmos
"""
import os

CONNECTION_ID = "postgres_conn"
DB_NAME = "jaffle_shop"
SCHEMA_NAME = "public"
TARGET_NAME = "dev"

# The path to the dbt project
DBT_PROJECT_PATH = f"{os.environ['AIRFLOW_HOME']}/dags/dbt/jaffle_shop"
# The path where Cosmos will find the dbt executable
# in the virtual environment created in the Dockerfile
DBT_EXECUTABLE_PATH = f"{os.environ['AIRFLOW_HOME']}/dbt_venv/bin/dbt"

from airflow.decorators import dag
from cosmos import DbtTaskGroup, ProjectConfig, ProfileConfig, ExecutionConfig
from cosmos.profiles import PostgresUserPasswordProfileMapping
from pendulum import datetime

profile_config = ProfileConfig(
    profile_name="default",
    target_name=TARGET_NAME,
    profile_mapping=PostgresUserPasswordProfileMapping(
        conn_id=CONNECTION_ID,
        profile_args={"schema": SCHEMA_NAME},
    ),
)

execution_config = ExecutionConfig(
    dbt_executable_path=DBT_EXECUTABLE_PATH,
)

@dag(
    start_date=datetime(2024, 1, 1),
    schedule='0 10 * * *',
    catchup=False
)
def jaffle_shop_dag():
    transform_data = DbtTaskGroup(
        group_id="transform_data",
        project_config=ProjectConfig(DBT_PROJECT_PATH),
        profile_config=profile_config,
        execution_config=execution_config,
        default_args={"retries": 2},
    )

    transform_data

jaffle_shop_dag()