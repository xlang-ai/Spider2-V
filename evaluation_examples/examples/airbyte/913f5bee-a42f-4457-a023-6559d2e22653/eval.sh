#!/bin/bash

exec 2>/dev/null

# source /home/user/anaconda3/etc/profile.d/conda.sh
# conda activate airbyte

# API docs: see https://airbyte-public-api-docs.s3.us-east-2.amazonaws.com/rapidoc-api-docs.html#overview
workspaces=$(curl -X POST http://localhost:8000/api/v1/workspaces/list -H "Content-Type: application/json" -d {} | jq -rM ".workspaces | .[] | .workspaceId")

for workspaceid in ${workspaces}; do
    response=$(curl -X POST http://localhost:8000/api/v1/sources/list -H "Content-Type: application/json" -d "{\"workspaceId\": \"${workspaceid}\"}")
    flag=$(echo ${response} | jq -rM ".sources | .[] | .sourceName" | grep "Sample Data (Faker)")
    if [ -n "${flag}" ]; then
        echo "Found Sample Data Faker source, succeed"
        exit 0
    fi
done
echo "Found Sample Data Faker source, failed"