#!/bin/bash

exec 2>/dev/null

cd /home/user/projects/astro-project
export CONTAINER=$(astro dev ps | grep "webserver" | awk '{print $1}')
export CONN_ID=postgres_conn

conn_info=$(docker exec -i $CONTAINER airflow connections get ${CONN_ID} -o plain)
flag=$(echo $conn_info | grep "postgres://user:password@172.17.0.1:5432/jaffle_shop")
if [ -n "$flag" ]; then
    echo "Check airflow connection info succeed"
else
    echo "Check airflow connection info failed"
fi