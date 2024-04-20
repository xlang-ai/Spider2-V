#!/bin/bash

source ~/anaconda3/etc/profile.d/conda.sh
conda activate dbt
cd ~/projects/analytics

_=$(dbt run)
_=$(echo "password" | sudo -S timedatectl set-ntp false)
_=$(echo "password" | sudo -S date -s "+6 hours")

output=$(dbt source freshness)
flag=$(echo $output | grep "1 of 1 ERROR STALE freshness of analytics.orders")

if [ -n "$flag" ] ; then
    echo "dbt source freshness succeed"
else
    echo "dbt source freshness failed"
fi

echo "password" | sudo -S timedatectl set-ntp true
