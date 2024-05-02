#!/bin/bash

source /home/user/anaconda3/etc/profile.d/conda.sh

cd /home/user/projects/SQL_Check

export DAG_ID=sql_data_quality
export DAG_RUN_ID=$(docker exec -i $(docker ps | grep "webserver" | awk '{print $1}') airflow dags list-runs -o plain --dag-id ${DAG_ID} | grep "manual" | awk '{print $2}')
export TASK_ID=column_checks
export TABS=logs
export CONTAINER=$(astro dev ps | grep "webserver" | awk '{print $1}')

connection_stat=$(docker exec -i $CONTAINER airflow connections list | grep "/tmp/sqlite.db")
if [[ -n $connection_stat ]]; then
    echo ""
else
    echo "Connection failed"
    exit 0
fi

echo "${DAG_ID}, ${DAG_RUN_ID}, ${TASK_ID}, ${TABS}"