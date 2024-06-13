#!/bin/bash

exec 2>/dev/null

# source /home/user/anaconda3/etc/profile.d/conda.sh
# conda activate airbyte

# API docs: see https://airbyte-public-api-docs.s3.us-east-2.amazonaws.com/rapidoc-api-docs.html#overview
workspaces=$(curl -X POST http://localhost:8000/api/v1/workspaces/list -H "Content-Type: application/json" -d {} | jq -rM ".workspaces | .[] | .workspaceId")
read -r connid < /home/user/connid.txt

for workspaceid in ${workspaces}; do
    connections=$(curl -X POST http://localhost:8000/api/v1/connections/list -H "Content-Type: application/json" -d "{\"workspaceId\": \"${workspaceid}\"}")
    flag=$(echo ${connections} | jq -rM ".connections | .[] | select(.connectionId == \"${connid}\" and (.scheduleData.cron.cronExpression | tostring | split(\" \")[0:3] == [\"0\", \"0\", \"18\"]))")
    if [ -n "${flag}" ]; then
        echo "Connection from Sample Data (Faker) to Local CSV, succeed"
        exit 0
    fi
done
echo "Connection from Sample Data (Faker) to Local CSV, failed"