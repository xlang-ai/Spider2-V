#!/bin/bash
exec 2>/dev/null

source /home/user/anaconda3/etc/profile.d/conda.sh
conda activate dagster

curl -s -o slack_github_analytics.html http://localhost:3000/locations/__repository__slack_github_analytics@slack_github_analytics.py/jobs/slack_github_analytics
if [ -s slack_github_analytics.html ] ; then
    echo "Create dagster job succeeded"
else
    echo "Create dagster job failed"
    exit 0
fi