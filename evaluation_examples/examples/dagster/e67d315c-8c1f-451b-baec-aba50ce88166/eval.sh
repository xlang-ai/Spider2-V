#!/bin/bash

exec 2>/dev/null

PROJECT_NAME=airbyte-mysql-to-json

cd /home/user/$PROJECT_NAME
source /home/user/anaconda3/etc/profile.d/conda.sh
conda activate dagster

export DAGSTER_HOME=~/.dagster

# Extract the last run ID
run_id=$(dagster run list | grep -oP 'Run: \K.*' | head -n 1)

log_check=$(python -c "import pickle; import json; f = open('/home/user/.dagster/storage/$run_id/mysql_to_json/result', 'rb'); x = pickle.load(f); x = json.dumps(x); print('\"status\": \"succeeded\"' in x and '{\"streamName\": \"pageview_counts\", \"stats\": {\"recordsEmitted\": 5, \"bytesEmitted\": 271, \"recordsCommitted\": 5}}' in x)")

if [ "$log_check" == "True" ]; then
    echo "Check dagster log succeeded"
else
    echo "Check dagster log failed"
    exit 0
fi

