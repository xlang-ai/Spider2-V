#!/bin/bash

exec 2>/dev/null

# source /home/user/anaconda3/etc/profile.d/conda.sh
# conda activate airbyte

# API docs: see https://airbyte-public-api-docs.s3.us-east-2.amazonaws.com/rapidoc-api-docs.html#overview
workspaces=$(curl -X POST http://localhost:8000/api/v1/workspaces/list -H "Content-Type: application/json" -d {} | jq -rM ".workspaces | .[] | .workspaceId")
read -r connid < /home/user/connid.txt

for workspaceid in ${workspaces}; do
    connections=$(curl -X POST http://localhost:8000/api/v1/connections/list -H "Content-Type: application/json" -d "{\"workspaceId\": \"${workspaceid}\"}")
    flag=$(echo ${connections} | jq -rM ".connections | .[] | select(.connectionId == \"${connid}\")")
    if [ -n "${flag}" ]; then
        echo "Delete connection from File to Snowflake, failed"
        exit 0
    fi
done

read -r srcid < /home/user/srcid.txt
for workspaceid in ${workspaces}; do
    sources=$(curl -X POST http://localhost:8000/api/v1/sources/list -H "Content-Type: application/json" -d "{\"workspaceId\": \"${workspaceid}\"}")
    flag=$(echo ${sources} | jq -rM ".sources | .[] | select(.sourceId == \"${srcid}\")")
    if [ -n "${flag}" ]; then
        echo "Delete source File, failed"
        exit 0
    fi
done

read -r destid < /home/user/destid.txt
for workspaceid in ${workspaces}; do
    destinations=$(curl -X POST http://localhost:8000/api/v1/destinations/list -H "Content-Type: application/json" -d "{\"workspaceId\": \"${workspaceid}\"}")
    flag=$(echo ${destinations} | jq -rM ".destinations | .[] | select(.destinationId == \"${destid}\")")
    if [ -n "${flag}" ]; then
        echo "Delete destination Snowflake, failed"
        exit 0
    fi
done

echo "Delete connection from File to Snowflake, succeed"