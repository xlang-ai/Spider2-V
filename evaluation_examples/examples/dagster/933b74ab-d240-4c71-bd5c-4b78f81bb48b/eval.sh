#!/bin/bash

cd ~/projects/hacker_news
source /home/user/anaconda3/etc/profile.d/conda.sh
conda activate dagster

JOB_MODULE=hacker_news
JOB_NAME=hacker_news_pipeline
# ensure the job exists
declare -a asset_list=(
    "Op: top10_story_ids"
    "Op: top10_stories"
    "Op: top5_mfw"
)
all_assets=$(dagster job print --job ${JOB_NAME} | grep -v "dagster.code_server")
contains_all=true
for asset in "${asset_list[@]}"; do
    if [[ ! ${all_assets} == *"$asset"* ]]; then
        contains_all=false
        break
    fi
done
if ${contains_all}; then
    echo "dagster job ${JOB_NAME} succeed"
else
    echo "dagster job ${JOB_NAME} failed"
    exit 0
fi

# materialize the asset
dagster job execute -j ${JOB_NAME} -m ${JOB_MODULE} >output.log 2>&1
declare -a output_list=(
    "top10_story_ids - STEP_SUCCESS"
    "top10_stories - STEP_SUCCESS"
    "top5_mfw - STEP_SUCCESS"
    "RUN_SUCCESS"
)
for output in "${output_list[@]}"; do
    flag=$(cat output.log | grep -i "${output}")
    if [ -z "$flag" ] ; then
        echo "Run job ${JOB_NAME} failed"
        exit 0
    fi
done
echo "Run job ${JOB_NAME} succeed"

# check whether the schedule is configured correctly
rm -f output.log
export DAGSTER_HOME=/home/user/.dagster
dagster schedule list | grep -v "dagster.code_server" > output.log
declare -a schedule_list=(
    "${JOB_NAME}_schedule \[RUNNING\]"
    "Cron Schedule: 0 \* \* \* \*"
)
for schedule_info in "${schedule_list[@]}"; do
    flag=$(cat output.log | grep -i "${schedule_info}")
    if [ -z "$flag" ] ; then
        echo "Schedule ${JOB_NAME}_schedule failed"
        exit 0
    fi
done
echo "Schedule ${JOB_NAME}_schedule succeed"