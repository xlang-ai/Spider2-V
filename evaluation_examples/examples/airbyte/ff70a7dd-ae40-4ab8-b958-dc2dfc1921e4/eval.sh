#!/bin/bash

exec 2>/dev/null

PASSWORD=password
DAG_ID=faker_to_json_dag
cd /home/user/projects/astro-airbyte-proj

# remove all existing files
echo $PASSWORD | sudo -S rm -rf /tmp/airbyte_local/json_data
echo $PASSWORD | sudo -S rm -f ./data/*

# trigger the DAG manually
current_time=$(date -u +"%Y-%m-%dT%H:%M:%S.%N%:z")
astro run ${DAG_ID} >/dev/null 2>/dev/null # manually run it
wait=0
maximum_wait=120
declare -a source_files=(
    "json_data/_airbyte_raw_users.jsonl"
    "json_data/_airbyte_raw_products.jsonl"
    "json_data/_airbyte_raw_purchases.jsonl"
)
while [ $wait -le $maximum_wait ]; do
    status=$(astro dev run dags list-runs -o plain --dag-id ${DAG_ID} --no-backfill --start-date ${current_time} | grep "${DAG_id}" | grep -m 1 "manual" | awk '{print $3}')
    if [ "$status" = "success" ]; then
        # check more detailed states
        for file in ${source_files[@]}; do
            file="/tmp/airbyte_local/${file}"
            if [ ! -f $file ] || [ ! -s $file ] ; then
                echo "DAG ${DAG_ID} run failed, missing file $file"
                exit 1
            fi
        done
        if [ ! -f "./data/raw_products.jsonl" ] || [ ! -s "./data/raw_products.jsonl" ]; then
            echo "DAG ${DAG_ID} run failed, missing file ./data/raw_products.jsonl"
            exit 1
        fi
        comparison=$(diff ./data/raw_products.jsonl /tmp/airbyte_local/json_data/_airbyte_raw_products.jsonl)
        if [ -n "${comparison}" ]; then
            echo "DAG ${DAG_ID} run failed, ./data/raw_products.jsonl is different from /tmp/airbyte_local/json_data/_airbyte_raw_products.jsonl"
            exit 1
        fi
        echo "DAG ${DAG_ID} run succeed"
        exit 0
    fi
    if [ "$status" = "failed" ] || [ "$status" = "cancelled" ] || [ "$status" = "up_for_retry" ] || [ -z "$status" ]; then
        echo "DAG ${DAG_ID} run failed"
        exit 1
    fi
    # probably still running
    wait=$(expr $wait + 3)
    sleep 3
done
echo "Exceeding maximum waiting time ${maximum_wait}s, DAG ${DAG_ID} run failed"