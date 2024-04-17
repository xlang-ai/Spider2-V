#!/bin/bash

exec 2>/dev/null

# source /home/user/anaconda3/etc/profile.d/conda.sh
# conda activate airbyte

# API docs: see https://airbyte-public-api-docs.s3.us-east-2.amazonaws.com/rapidoc-api-docs.html#overview
workspaces=$(curl -X POST http://localhost:8000/api/v1/workspaces/list -H "Content-Type: application/json" -d {} | jq -rM ".workspaces | .[] | .workspaceId")
read -r srcid < /home/user/srcid.txt
read -r destid < /home/user/destid.txt

for workspaceid in ${workspaces}; do
    connections=$(curl -X POST http://localhost:8000/api/v1/connections/list -H "Content-Type: application/json" -d "{\"workspaceId\": \"${workspaceid}\"}")
    flag=$(echo ${connections} | jq -rM ".connections | .[] | select(.sourceId == \"${srcid}\" and .destinationId == \"${destid}\" and .status == \"active\")")
    if [ -n "${flag}" ]; then
        echo "Connection from Sample Data (Faker) to Local SQLite, succeed"
        exit 0
    fi
done
echo "Connection from Sample Data (Faker) to Local SQLite, failed"