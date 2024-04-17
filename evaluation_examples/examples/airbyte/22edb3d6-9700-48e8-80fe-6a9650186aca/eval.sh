#!/bin/bash

exec 2>/dev/null

# source /home/user/anaconda3/etc/profile.d/conda.sh
# conda activate airbyte

# API docs: see https://airbyte-public-api-docs.s3.us-east-2.amazonaws.com/rapidoc-api-docs.html#overview
workspaces=$(curl -X POST http://localhost:8000/api/v1/workspaces/list -H "Content-Type: application/json" -d {} | jq -rM ".workspaces | .[] | .workspaceId")

for workspaceid in ${workspaces}; do
    response=$(curl -X POST http://localhost:8000/api/v1/destinations/list -H "Content-Type: application/json" -d "{\"workspaceId\": \"${workspaceid}\"}")
    flag1=$(echo ${response} | jq -rM ".destinations | .[] | .destinationName" | grep "Local JSON")
    flag2=$(echo ${response} | jq -rM ".destinations | .[] | .connectionConfiguration | .destination_path" | grep "/local/json_destination")
    if [ -n "${flag1}" ] && [ -n "${flag2}" ]; then
        echo "Found Local JSON destination, succeed"
        exit 0
    fi
done
echo "Found Local JSON destination, failed"