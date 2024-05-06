#!/bin/bash

exec 2>/dev/null

PROJECT_NAME=apod-proj

cd /home/user/$PROJECT_NAME
source /home/user/anaconda3/etc/profile.d/conda.sh
conda activate dagster

export DAGSTER_HOME=~/.dagster

unzip gold_data.zip

all_files_identical=true

for date in "2024-04-10" "2024-04-11" "2024-04-12" "2024-04-13"
do
    if ! diff -b "data/apod_url_$date.txt" "gold_data/apod_url_$date.txt" > /dev/null; then
        all_files_identical=false
        break
    fi
done

if $all_files_identical; then
    echo "Check data succeeded"
else
    echo "Check data failed"
    exit 0
fi

# Extract run IDs
run_ids=$(dagster run list | grep -oP 'Run: \K.*')

declare -A partitions
partitions=(["2024-04-10"]=false ["2024-04-11"]=false ["2024-04-12"]=false ["2024-04-13"]=false)

for run_id in $run_ids
do
    dagster debug export $run_id run_log.gz

    gunzip -qf run_log.gz

    for partition in "${!partitions[@]}"
    do
        if grep -q "\"partition\": \"$partition\"" run_log; then
            partitions[$partition]=true
        fi
    done
done

# Check if all partitions are found
all_partitions_found=true
for partition_found in "${partitions[@]}"
do
    if ! $partition_found; then
        all_partitions_found=false
        break
    fi
done

if $all_partitions_found; then
    echo "Check partition succeeded"
else
    echo "Check partition failed"
fi