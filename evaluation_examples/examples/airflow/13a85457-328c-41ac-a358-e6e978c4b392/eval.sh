#!/bin/bash

source /home/user/anaconda3/etc/profile.d/conda.sh
conda activate astro
cd /home/user/projects/workFlow

export DAG_ID=wweather_producer_dag
export DAG_RUN_ID=$(docker exec -i $(docker ps | grep "webserver" | awk '{print $1}') airflow dags list-runs -o plain --dag-id ${DAG_ID} | grep "manual" | awk '{print $2}')
export TASK_ID=get_hong_kong_weather

docker exec -i $(docker ps | grep "scheduler" | awk '{print $1}') airflow task_log ${DAG_ID} ${TASK_ID} ${DAG_RUN_ID}
