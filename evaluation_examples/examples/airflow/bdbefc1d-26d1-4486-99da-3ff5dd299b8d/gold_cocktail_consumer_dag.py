#coding=utf8
from pendulum import datetime
from airflow.decorators import dag, task

from airflow.datasets import Dataset

INSTRUCTIONS = Dataset("file://localhost/airflow/include/cocktail_instructions.txt")
INFO = Dataset("file://localhost/airflow/include/cocktail_info.txt")

@dag(
    dag_id="cocktail_consumer_dag",
    start_date=datetime(2024, 1, 1),
    schedule=[INSTRUCTIONS, INFO],  # Scheduled on both Datasets
    catchup=False,
)
def cocktail_consumer_dag():
    @task
    def merge_cocktail_output():
        all_contents = ''
        for filename in ("info", "instructions"):
            with open(f"include/cocktail_{filename}.txt", "r") as f:
                contents = f.read()
                all_contents += contents
        with open(f"include/cocktail.txt", 'w') as of:
            of.write(all_contents)
        return all_contents

    merge_cocktail_output()

cocktail_consumer_dag()