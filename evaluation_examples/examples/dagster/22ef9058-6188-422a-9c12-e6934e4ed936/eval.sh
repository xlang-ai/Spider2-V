#!/bin/bash

cd ~/hacker_news
source /home/user/anaconda3/etc/profile.d/conda.sh
conda activate dagster

if [ -s data/story_ids.json ] && [ ! -s data/askstory_ids.json ] && [ ! -s data/showstory_ids.json ] && [ ! -s data/jobstory_ids.json ]; then
    echo "Check materialization result succeeded"
else
    echo "Check materialization result failed"
    exit 0
fi

# materialize the asset (not needed)
# dagster asset materialize --select top10_story_ids -m hacker_news > output.log 2>&1
# flag=$(cat output.log | grep -i "RUN_SUCCESS")
# if [ -n "$flag" ]; then
#     echo "Materialize top10_story_ids succeeded"
# else
#     echo "Materialize top10_story_ids failed"
#     exit 0
# fi

# Before running the following commands:
# please ensure that golden project is copied to the home directory
unzip -q /home/user/golden_hacker_news.zip -d /home/user 2>/dev/null
cd /home/user/golden_hacker_news
dagster asset materialize --select top10_story_ids -m hacker_news >/dev/null 2>&1