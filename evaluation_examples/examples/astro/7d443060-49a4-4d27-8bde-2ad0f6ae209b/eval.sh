#!/bin/bash

cd /home/user/projects/today_task

pip install pytest > /dev/null 2>&1
pip install apache-airflow > /dev/null 2>&1

airflow db init > /dev/null 2>&1

cd ~/projects/today_task/tests/dags

if pytest test_dag.py | grep -q "AssertionError: DAG schedule interval is not set to daily." && pytest test_dag.py | grep -q "AssertionError: Tasks are not in the expected order:"; then
    echo "Test creation succeed."
else
    echo "Test creation failed."
fi