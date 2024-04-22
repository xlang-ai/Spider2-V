#!/bin/bash

# ensure that no error information is output
exec 2>/dev/null

cd /home/user/projects/task_today
# astro dev restart >/dev/null 2>&1
export DAG_ID=task_today
export CONTAINER_ID=$(docker ps | grep "webserver" | awk '{print $1}')
export DAG_RUN_ID=$(docker exec -i ${CONTAINER_ID} airflow dags list-runs -o plain --dag-id ${DAG_ID} | grep -m 1 "manual" | awk '{print $2}')
export TASK_ID=tell_me_what_to_do

RUN_ID=$(echo $DAG_RUN_ID | sed 's/:/%3A/g' | sed 's/+/%2B/g' | sed 's/manual__//')
echo "http://localhost:8080/task?dag_id=${DAG_ID}&task_id=${TASK_ID}&execution_date=${RUN_ID}&map_index=-1"