#!/bin/bash

source ~/anaconda3/etc/profile.d/conda.sh
conda activate dbt
cd ~/projects/jaffle_shop

output=$(dbt run)
flag1=$(echo $output | grep "Completed successfully")
flag2=$(echo $output | grep -E "of 3 OK created sql view model .*\.stg_customers")
flag3=$(echo $output | grep -E "of 3 OK created sql view model .*\.stg_orders")
flag4=$(echo $output | grep -E "of 3 OK created sql table model .*\.customers")
flag5=$(echo $output | grep "PASS=3")
flag6=$(echo $output | grep "TOTAL=3")
if [ -n "$flag1" ] && [ -n "$flag2" ] && [ -n "$flag3" ] && [ -n "$flag4" ] && [ -n "$flag5" ] && [ -n "$flag6" ]; then
    echo "dbt run succeed"
else
    echo "dbt run failed"
fi
