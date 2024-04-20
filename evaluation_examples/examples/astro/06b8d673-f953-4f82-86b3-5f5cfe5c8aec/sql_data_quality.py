from airflow.decorators import dag
from airflow.providers.common.sql.operators.sql import (
    SQLColumnCheckOperator,
    SQLTableCheckOperator,
    SQLCheckOperator,
)
from airflow.providers.sqlite.operators.sqlite import SqliteOperator
from pendulum import datetime

_CONN_ID = "sqlite_conn"
_TABLE_NAME = "birds"


@dag(
    start_date=datetime(2024, 4, 1),
    schedule=None,
    catchup=False,
    template_searchpath=["/usr/local/airflow/include/"],
)
def sql_data_quality():
    create_table = SqliteOperator(
        task_id="create_table",
        sqlite_conn_id=_CONN_ID,
        sql=f"""
        CREATE TABLE IF NOT EXISTS {_TABLE_NAME} (
            bird_name VARCHAR,
            observation_year INT,
            bird_happiness INT
        );
        """,
    )

    populate_data = SqliteOperator(
        task_id="populate_data",
        sqlite_conn_id=_CONN_ID,
        sql=f"""
            INSERT INTO {_TABLE_NAME} (bird_name, observation_year, bird_happiness) VALUES
                ('Bald Eagle (Haliaeetus leucocephalus)', 2022, 8),
                ('African Grey Parrot (Psittacus erithacus)', 2021, 7),
                ('Blue Jay (Cyanocitta cristata)', 2020, 8),
                ('Emperor Penguin (Aptenodytes forsteri)', 2019, 9),
                ('Snowy Owl (Bubo scandiacus)', 2018, 10);
        """,
    )

    check_column = SQLColumnCheckOperator(
        
    )

    check_table = SQLTableCheckOperator(
        
    )

    create_table >> populate_data >> [check_column, check_table]


sql_data_quality()
