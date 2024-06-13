#!/bin/bash

source ~/anaconda3/etc/profile.d/conda.sh
conda activate dbt
cd ~/projects/analytics

output=$(dbt snapshot)
flag1=$(echo $output | grep "Completed successfully")
flag2=$(echo $output | grep -E "1 of 1 OK snapshotted snapshots.orders_snapshot")
flag3=$(echo $output | grep "PASS=1")
flag4=$(echo $output | grep "TOTAL=1")
if [ -n "$flag1" ] && [ -n "$flag2" ] && [ -n "$flag3" ] && [ -n "$flag4" ] ; then
    echo "dbt snapshot succeed"
else
    echo "dbt snapshot failed"
fi
