#!/bin/bash

cd /home/user/projects/today_task

pip install pytest > /dev/null 2>&1
pip install apache-airflow > /dev/null 2>&1

airflow db init > /dev/null 2>&1

cd ~/projects/today_task/tests/dags

if pytest test_dag.py | "3 passed" ; then
    echo "Error correction succeed."
else
    echo "Error correction failed."
fi