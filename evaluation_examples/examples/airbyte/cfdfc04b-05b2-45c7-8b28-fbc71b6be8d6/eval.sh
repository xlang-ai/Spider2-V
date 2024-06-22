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
        source_host=$(echo $source_config | jq -rM ".connectionConfiguration.host")
        source_port=$(echo $source_config | jq -rM ".connectionConfiguration.port")
        source_database=$(echo $source_config | jq -rM ".connectionConfiguration.database")
        source_username=$(echo $source_config | jq -rM ".connectionConfiguration.username")
        replication_method=$(echo $source_config | jq -rM ".connectionConfiguration.replication_method.method")
        if [ "${source_name}" = "Postgres" ] && [ "${source_host}" = "localhost" ] && [ "${source_port}" = "2000" ] && [ "${source_database}" = "postgres" ] && [ "${source_username}" = "postgres" ] && [ "${replication_method}" = "Standard" ]; then
            echo "Airbyte Connection from source Postgres, succeed"
        else
            continue
        fi
        
        # check the destination
        destination_id=${destination_ids[$i]}
        destination_config=$(curl -X POST http://localhost:8000/api/v1/destinations/get -H "Content-Type: application/json" -d "{\"destinationId\": \"${destination_id}\"}")
        destination_name=$(echo $destination_config | jq -rM ".destinationName")
        destination_path=$(echo $destination_config | jq -rM ".connectionConfiguration.destination_path")
        if [ "${destination_name}" = "Local SQLite" ] && [ "${destination_path}" = "/local/obesity.sqlite" ] ; then
            echo "Airbyte Connection to destination Local SQLite, succeed"
        else
            continue
        fi

        # check the connection config
        connection_config=$(echo $connections | jq -rM ".connections | .[${i}] | .")
        incremental=$(echo $connection_config | grep "\"syncMode\": \"incremental\"")
        append=$(echo $connection_config | grep "\"destinationSyncMode\": \"append\"")
        cursor=$(echo $connection_config | jq -r '.syncCatalog.streams[].config.cursorField[]')
        if [ -n "$incremental" ] && [ -n "$append" ] && [ "${cursor}" = "id" ]; then
            echo "Airbyte Connection config, succeed."
            airbyte_connection=true
            break
        fi
    done
done
if [ ${airbyte_connection} = false ] ; then
    echo "Airbyte Connection from source Postgres to destination Local SQLite, failed"
    exit 0
fi
