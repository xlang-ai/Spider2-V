#!/bin/bash

DAG_ID="workFlow_Echo"

CONTAINER_ID=$(docker ps | grep 'scheduler' | awk '{print $1}')

echo "Unpausing DAG: $DAG_ID"
docker exec $CONTAINER_ID airflow dags unpause $DAG_ID > /dev/null 2>&1

echo "Triggering DAG: $DAG_ID"
docker exec $CONTAINER_ID airflow dags trigger $DAG_ID > /dev/null 2>&1
