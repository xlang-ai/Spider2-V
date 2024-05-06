#!/bin/bash

exec 2>/dev/null

PROJECT_NAME=wikipediaPageViews
PASSWORD=password

cd ~/$PROJECT_NAME
source /home/user/anaconda3/etc/profile.d/conda.sh
export DAGSTER_HOME=~/.dagster
conda activate dagster

mysql -p$PASSWORD < database_export.sql

echo $PASSWORD | sudo -S diff gold_pageviews.csv /var/lib/mysql-files/pageviews.csv > /dev/null 2>&1
if [ $? -eq 0 ] ; then
    echo "Check pageviews table succeeded"
else
    echo "Check pageviews table failed"
fi

if dagster schedule list -f dagster_migration.py | grep -q RUNNING; then
    echo "Check schedule running succeeded"
else
    echo "Check schedule running failed"
fi