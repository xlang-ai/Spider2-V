#!/bin/bash

PROJECT_NAME=orders

cd ~/$PROJECT_NAME
source /home/user/anaconda3/etc/profile.d/conda.sh
conda activate dagster

export DAGSTER_HOME=~/.dagster

run_ids=$(dagster run list | grep -oP 'Run: \K.*')

check_report_materialization_succeeded=false
check_asset_check_succeeded=false

for run_id in $run_ids
do
    dagster debug export $run_id run_log.gz

    gunzip -f run_log.gz

    if grep -q "\"__class__\": \"IntMetadataEntryData\", \"value\": 15" run_log; then
        check_report_materialization_succeeded=true
    fi

    if grep -q "\"check_name\": \"no_null_check\", \"description\": null, \"metadata\": {}, \"severity\": {\"__enum__\": \"AssetCheckSeverity.ERROR\"}, \"success\": true" run_log; then
        check_asset_check_succeeded=true
    fi
done

if $check_report_materialization_succeeded; then
    echo "Check report materialization succeeded"
else
    echo "Check report materialization failed"
fi

if $check_asset_check_succeeded; then
    echo "Check asset check for orders without null succeeded"
else
    echo "Check asset check for orders without null failed"
fi

echo DELETE | dagster run wipe

mv orders_data_with_null.csv orders_data.csv

dagster asset materialize --select subprocess_asset -m orders > /dev/null 2>&1

run_ids=$(dagster run list | grep -oP 'Run: \K.*')

check_asset_check_succeeded=false

for run_id in $run_ids
do
    dagster debug export $run_id run_log.gz

    gunzip -f run_log.gz

    if grep -q "\"check_name\": \"no_null_check\", \"description\": null, \"metadata\": {}, \"severity\": {\"__enum__\": \"AssetCheckSeverity.ERROR\"}, \"success\": false" run_log; then
        check_asset_check_succeeded=true
    fi
done

if $check_asset_check_succeeded; then
    echo "Check asset check for orders with null succeeded"
else
    echo "Check asset check for orders with null failed"
fi