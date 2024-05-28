#!/bin/bash
cd /home/user/projects/mlflow
pip install mlflow >/dev/null 2>&1

export DAG_ID="feature_eng"
export CONTAINER=$(astro dev ps | grep "webserver" | awk '{print $1}')

active_flag=$(docker exec -i $CONTAINER airflow dags details -o plain ${DAG_ID} | grep "is_paused" | grep -i "false")
if [ -n "$active_flag" ]; then
    echo "DAG activation success."
else
    echo "DAG activation failed."
    exit 0
fi

flag_start=$(docker exec -i $CONTAINER airflow dags list-runs -o plain --dag-id ${DAG_ID} --no-backfill | grep "${DAG_id}" | grep -m 1 "manual" | awk '{print $3}')
if [ "$flag_start" = "success" ]; then
    echo "DAG run success."
else
    echo "DAG run failed."
    exit 0
fi

LATEST_RUN_ID=$(docker exec -i $CONTAINER airflow dags list-runs --dag-id ${DAG_ID} --no-backfill --output plain | grep -m 1 "${DAG_ID}" | awk '{print $2}')

declare -a TASK_NAMES=("start" "extract_data" "save_data_to_s3" "build_features" "end") 

ALL_SUCCESS=true
for TASK_ID in "${TASK_NAMES[@]}"; do
    TASK_STATE=$(docker exec -i $CONTAINER airflow tasks state $DAG_ID $TASK_ID $LATEST_RUN_ID | sed -n '$p')
    echo "Task $TASK_ID State: $TASK_STATE"  
    if [ "$TASK_STATE" != "success" ]; then
        echo "Failed - Task ${TASK_ID} failed."
        ALL_SUCCESS=false
        break
    fi
done

chmod a+x validation.py
python3 validation.py
