#!/bin/bash

cd ~/projects/hacker_news
source /home/user/anaconda3/etc/profile.d/conda.sh
conda activate dagster

# ensure the asset exists
declare -a asset_list=(
    "top10_story_ids"
    "top10_stories"
    "top5_mfw"
)
all_assets=$(dagster asset list -m hacker_news)
contains_all=true
for asset in "${asset_list[@]}"; do
    if [[ ! ${all_assets} == *"$asset"* ]]; then
        contains_all=false
        break
    fi
done
if ${contains_all}; then
    echo "dagster assets succeed"
else
    echo "dagster assets failed"
    exit 0
fi

# materialize the asset
declare -a output_list=(
    "story_ids.json"
    "stories.json"
    "mfw.json"
)
for index in "${!asset_list[@]}"; do
    dagster asset materialize --select ${asset_list[$index]} -m hacker_news > output.log 2>&1
    flag=$(cat output.log | grep -i "RUN_SUCCESS")
    if [ -n "$flag" ] && [ -s data/${output_list[$index]} ] ; then
        echo "materialize ${asset_list[$index]} succeed"
    else
        echo "materialize ${asset_list[$index]} failed"
        exit 0
    fi
    rm output.log
done

# Before running the following commands:
# please ensure that golden project is copied to the home directory
unzip -q /home/user/hacker_news.zip -d /home/user 2>/dev/null
cd /home/user/hacker_news
for asset in "${asset_list[@]}"; do
    dagster asset materialize --select ${asset} -m hacker_news >/dev/null 2>&1
done