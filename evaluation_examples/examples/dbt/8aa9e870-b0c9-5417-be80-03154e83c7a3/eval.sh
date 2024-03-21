#!/bin/bash

source ~/anaconda3/etc/profile.d/conda.sh
conda activate dbt
cd ~/projects/jaffle_shop

output=$(dbt debug)
flag1=$(echo $output | grep "OK connection ok")
flag2=$(echo $output | grep "All checks passed")
if [ -n "$flag1" ] && [ -n "$flag2" ] ; then
    echo "dbt debug succeed"
else
    echo "dbt debug failed"
fi

output=$(dbt seed)
flag1=$(echo $output | grep "Completed successfully")
flag2=$(echo $output | grep "PASS=3")
flag3=$(echo $output | grep "TOTAL=3")
flag4=$(echo $output | grep "Nothing to do")
if [ -n "$flag1" ] && [ -n "$flag2" ] && [ -n "$flag3" ] && [ -z "$flag4" ] ; then
    echo "dbt seed succeed"
else
    echo "dbt seed failed"
fi
