#!/bin/bash

PROJECT_NAME=dbt-dagster-proj

cd /home/user/$PROJECT_NAME
source /home/user/anaconda3/etc/profile.d/conda.sh
conda activate dagster

export DAGSTER_HOME=~/.dagster

python export_customers.py

if diff -i customers.csv gold_customers.csv > /dev/null; then
    echo "Check customers succeeded"
else
    echo "Check customers failed"
fi