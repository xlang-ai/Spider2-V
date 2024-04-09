#!/bin/bash

source /home/user/anaconda3/etc/profile.d/conda.sh
conda activate astro
cd /home/user/projects/Project

astro dev start >/dev/null 2>/dev/null
export DAG_ID = example_astronauts
export CONTAINER = $(astro dev ps | grep "webserver" | awk '{print $1}')

# check whether the DAG is not paused
active_flag=$(docker exec -i $CONTAINER airflow dags details -o plain ${DAG_ID} | grep "is_paused" | grep -i "false")
if [ -n "$active_flag" ]; then
    echo "dag active succeed"
else
    echo "dag active failed"
    exit 0
fi

# check whether the DAG run successfully
astro run ${DAG_ID} >/dev/null 2>/dev/null # manually run it
flag_start=$(docker exec -i $CONTAINER airflow dags list-runs -o plain --dag-id ${DAG_ID} --no-backfill | grep "${DAG_id}" | grep -m 1 "manual" | awk '{print $3}')
if [ "$flag_start" = "success" ]; then
    echo "astro run dag succeed"
else
    echo "astro run dag failed"
    exit 0
fi

