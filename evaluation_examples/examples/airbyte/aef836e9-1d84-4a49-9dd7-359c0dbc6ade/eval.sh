#!/bin/bash

exec 2>/dev/null

# source /home/user/anaconda3/etc/profile.d/conda.sh
# conda activate airbyte

# 1. check the connection from source Postgres to source Postgres
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
        # check the source
        source_id=${source_ids[$i]}
        source_config=$(curl -X POST http://localhost:8000/api/v1/sources/get -H "Content-Type: application/json" -d "{\"sourceId\": \"${source_id}\"}")
        source_name=$(echo $source_config | jq -rM ".sourceName")
        source_database=$(echo $source_config | jq -rM ".connectionConfiguration.database")
        source_port=$(echo $source_config | jq -rM ".connectionConfiguration.port")
        replication_slot=$(echo $source_config | jq -rM ".connectionConfiguration.replication_method.replication_slot")
        publication=$(echo $source_config | jq -rM ".connectionConfiguration.replication_method.publication")
        #username=$(echo $source_config | jq -rM ".connectionConfiguration.username")
        if [ "${source_name}" = "Sample Data (Faker)" ]; then
            echo "Airbyte Connection from source Faker, succeed"
        else
            continue
        fi
        
        # check the destination
        destination_id=${destination_ids[$i]}
        destination_config=$(curl -X POST http://localhost:8000/api/v1/destinations/get -H "Content-Type: application/json" -d "{\"destinationId\": \"${destination_id}\"}")
        destination_name=$(echo $destination_config | jq -rM ".destinationName")
        destination_path=$(echo $destination_config | jq -rM ".connectionConfiguration.destination_path")
        if [ "${destination_name}" = "Snowflake" ]; then
            echo "Airbyte Connection to Snowflake, succeed"
        else
            continue
        fi

        # check streams
        connection_config=$(echo $connections | jq -rM ".connections | .[${i}] | .")
        sync_catalog=$(echo "${connection_config}" | jq -r '.syncCatalog')
        

        # Check if streams only contain products and users
        streams=$(echo ${sync_catalog} | jq -r ".streams | .[].stream.name")
        expected_streams="products"

        if echo "$streams" | grep -qw "products" && echo "$streams" | grep -qw "purchases" && [ $(echo "$streams" | wc -w) -eq 2 ]; then
            echo "Streams only contain products and purchases."
            airbyte_connection=true
            break
        fi
    done
done
if [ ${airbyte_connection} = false ] ; then
    echo "Streams modification of airbyte Connection from Faker to destination Snowflake, failed"
    exit 0
fi