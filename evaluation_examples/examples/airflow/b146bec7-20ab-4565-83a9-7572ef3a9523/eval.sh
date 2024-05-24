#!/bin/bash


source /home/user/anaconda3/etc/profile.d/conda.sh
conda activate airflow

cd /home/user/projects/today_task
pip install pytest > /dev/null 2>&1
airflow db init > /dev/null 2>&1

cd /home/user/projects/today_task/tests/dags

if pytest test_dag.py | grep "3 passed" ; then
    echo "Error correction succeed."
else
    echo "Error correction failed."
fi