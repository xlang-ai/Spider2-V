#!/bin/bash

# ensure that no error information is output
exec 2>/dev/null

cd /home/user/projects/weather
# astro dev restart >/dev/null 2>&1
export DAG_ID=weather_data_dag
export CONTAINER_ID=$(docker ps | grep "webserver" | awk '{print $1}')
export DAG_RUN_ID=$(docker exec -i ${CONTAINER_ID} airflow dags list-runs -o plain --dag-id ${DAG_ID} | grep -m 1 "manual" | awk '{print $2}')
export TASK_ID=get_hong_kong_weather

RUN_ID=$(echo $DAG_RUN_ID | sed 's/:/%3A/g' | sed 's/+/%2B/g')
echo "http://localhost:8080/dags/${DAG_ID}/grid?dag_run_id=${RUN_ID}&task_id=${TASK_ID}"