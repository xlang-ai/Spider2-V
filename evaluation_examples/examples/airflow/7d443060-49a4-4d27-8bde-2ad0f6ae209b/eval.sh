#!/bin/bash

cd /home/user/projects/today_task

source /home/user/anaconda3/etc/profile.d/conda.sh
conda activate airflow 

pip install pytest > /dev/null 2>&1

airflow db migrate > /dev/null 2>&1

cd ~/projects/today_task/tests/dags

pytest test_dag.py > log.txt

if cat log.txt | grep -q "AssertionError: DAG schedule interval is not set to daily." && cat log.txt | grep -q "AssertionError: Tasks are not in the expected order:"; then
    echo "Test creation succeed."
else
    echo "Test creation failed."
fi