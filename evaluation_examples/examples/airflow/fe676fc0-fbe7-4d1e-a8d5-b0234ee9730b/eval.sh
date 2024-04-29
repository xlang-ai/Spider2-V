#!/bin/bash

source /home/user/anaconda3/etc/profile.d/conda.sh

cd /home/user/projects

export DAG_ID=sql_data_quality
export DAG_RUN_ID=$(docker exec -i $(docker ps | grep "webserver" | awk '{print $1}') airflow dags list-runs -o plain --dag-id ${DAG_ID} | grep "manual" | awk '{print $2}')
export TASK_ID=column_checks
export TABS=logs

echo "${DAG_ID}, ${DAG_RUN_ID}, ${TASK_ID}, ${TABS}"