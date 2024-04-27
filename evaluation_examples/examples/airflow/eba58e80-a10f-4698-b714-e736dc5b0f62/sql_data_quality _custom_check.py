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

    column_checks = SQLColumnCheckOperator(
        task_id="column_checks",
        conn_id=_CONN_ID,
        table=_TABLE_NAME,
        partition_clause="bird_name IS NOT NULL",
        column_mapping={
            "bird_name": {
                "null_check": {"equal_to": 0},
                "distinct_check": {"geq_to": 5},
            },
            "observation_year": {"min":{"geq_to": 2018}, "max": {"less_than": 2024}},
            "bird_happiness": {"min": {"greater_than": 0}, "max": {"leq_to": 10}},
        },
    )

    table_checks = SQLTableCheckOperator(
        task_id="table_checks",
        conn_id=_CONN_ID,
        table=_TABLE_NAME,
        checks={
            "average_happiness_check": {
                "check_statement": "AVG(bird_happiness) >= 8",
                "partition_clause": "observation_year >= 2019",
            },
        },
    )
    
    custom_happy_check = SQLCheckOperator(
        task_id="custom_happiness_check",
        conn_id=_CONN_ID,
        sql="custom_check.sql",
        params={"table_name": _TABLE_NAME},
    )

    create_table >> populate_data >> [column_checks, table_checks, custom_happy_check]


sql_data_quality()
