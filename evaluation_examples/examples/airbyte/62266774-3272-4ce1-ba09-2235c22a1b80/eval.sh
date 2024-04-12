#!/bin/bash

exec 2>/dev/null

source /home/user/anaconda3/etc/profile.d/conda.sh
conda activate airbyte

# 1. check the connection from Faker to Snowflake
# API docs: see https://airbyte-public-api-docs.s3.us-east-2.amazonaws.com/rapidoc-api-docs.html#overview
workspaces=$(curl -X POST http://localhost:8000/api/v1/workspaces/list -H "Content-Type: application/json" -d {} | jq -rM ".workspaces | .[] | .workspaceId")
airbyte_connection=false
for workspaceid in ${workspaces}; do
    connections=$(curl -X POST http://localhost:8000/api/v1/connections/list -H "Content-Type: application/json" -d "{\"workspaceId\": \"${workspaceid}\"}")
    # extract source/destination ids in the current workspace
    declare -a source_ids=($(echo ${connections} | jq -rM ".connections | .[] | .sourceId"))
    declare -a destination_ids=($(echo ${connections} | jq -rM ".connections | .[] | .destinationId"))
    length=${#source_ids[@]}
    for (( i=0; i<$length; i++ )); do
        source_id=${source_ids[$i]}
        source_name=$(curl -X POST http://localhost:8000/api/v1/sources/get -H "Content-Type: application/json" -d "{\"sourceId\": \"${source_id}\"}" | jq -rM ".sourceName")
        destination_id=${destination_ids[$i]}
        destination_name=$(curl -X POST http://localhost:8000/api/v1/destinations/get -H "Content-Type: application/json" -d "{\"destinationId\": \"${destination_id}\"}" | jq -rM ".destinationName")
        if [ "${source_name}" = "Sample Data (Faker)" ] && [ "${destination_name}" = "Snowflake" ] ; then
            echo "Airbyte Connection from Sample Data (Faker) to Snowflake, succeed"
            airbyte_connection=true
            break
        fi
    done
    if [ ${airbyte_connection} = true ] ; then
        break
    fi
done
if [ ${airbyte_connection} = false ] ; then
    echo "Airbyte Connection from Sample Data (Faker) to Snowflake, failed"
    exit 0
fi

# 2. check dbt transformation result
cd /home/user/projects/ecommerce_analytics/dbt_project
# this step is critical to ensure ENV functions
source <(grep '^export SNOWFLAKE_' /home/user/.bashrc)
connection_output=$(dbt debug | grep -i "OK connection ok")
transformed_output=$(dbt run | grep -i "Completed successfully")
if [ -n "${connection_output}" ] && [ -n "${transformed_output}" ] ; then
    echo "dbt transformation succeed"
else
    echo "dbt transformation failed"
fi