#!/bin/bash

cd ~/projects/hacker_news
source /home/user/anaconda3/etc/profile.d/conda.sh
conda activate dagster

# ensure the asset exists
assets=$(dagster asset list -m hacker_news | grep "top10_story_ids")
if [ -n "$assets" ]; then
    echo "create top10_story_ids succeed"
else
    echo "create top10_story_ids failed"
    exit 0
fi

# materialize the asset
dagster asset materialize --select top10_story_ids -m hacker_news > output.log 2>&1
flag=$(cat output.log | grep -i "RUN_SUCCESS")
if [ -n "$flag" ] && [ -s data/story_ids.json ] ; then
    echo "materialize top10_story_ids succeed"
else
    echo "materialize top10_story_ids failed"
    exit 0
fi

# Before running the following commands:
# please ensure that golden project is copied to the home directory
unzip -q /home/user/hacker_news.zip -d /home/user 2>/dev/null
cd /home/user/hacker_news
dagster asset materialize --select top10_story_ids -m hacker_news >/dev/null 2>&1