#!/bin/bash

source ~/anaconda3/etc/profile.d/conda.sh
conda activate dbt
cd ~/projects/materialize_test

output=$(dbt run)
flag1=$(echo $output | grep "Completed successfully")
flag2=$(echo $output | grep -E "of 2 OK created sql table model .*\.my_first_dbt_model")
flag3=$(echo $output | grep -E "of 2 OK created sql table model .*\.my_second_dbt_model")
flag4=$(echo $output | grep "PASS=2")
flag5=$(echo $output | grep "TOTAL=2")

if [ -n "$flag1" ] && [ -n "$flag2" ] && [ -n "$flag3" ] && [ -n "$flag4" ] && [ -n "$flag5" ]; then
    echo "dbt run succeed"
else
    echo "dbt run failed"
fi