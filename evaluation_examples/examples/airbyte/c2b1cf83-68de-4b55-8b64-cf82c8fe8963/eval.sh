#!/bin/bash

exec 2>/dev/null

source /home/user/anaconda3/etc/profile.d/conda.sh
conda activate airbyte

# 1. check the connection from souce Postgres to source Postgres
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
        if [ "${source_name}" = "Postgres" ] &&[ "${source_port}" = "2000" ] && [ "${source_database}" = "postgres" ]; then
            echo "Airbyte Connection from source Postgres, succeed"
        else
#            echo "Airbyte Connection from source Postgres, failed."
            continue
        fi

        # check the destination
        destination_id=${destination_ids[$i]}
        destination_config=$(curl -X POST http://localhost:8000/api/v1/destinations/get -H "Content-Type: application/json" -d "{\"destinationId\": \"${destination_id}\"}")
        destination_name=$(echo $destination_config | jq -rM ".destinationName")
        destination_database=$(echo $source_config | jq -rM ".connectionConfiguration.database")
        destination_port=$(echo $destination_config | jq -rM '.connectionConfiguration.port')
        if [ "${destination_name}" = "Postgres" ] && [ "${destination_port}" = "3000" ] && [ "${destination_database}" = "postgres" ]; then
            echo "Airbyte Connection to destination Postgres, succeed"
        else
#            echo "Airbyte Connection to destination Postgres, failed."
            continue
        fi
        # check the connection config
        connection_config=$(echo $connections | jq -rM ".connections | .[${i}] | .")
        stream_length=$(echo $connection_config | jq ".syncCatalog.streams | length")
        # check the configuration of all streams
        all_streams_valid=true
        for (( i=0; i<length; i++ )) do
            sync_mode=$(echo $connection_config | jq -r ".syncCatalog.streams[${i}].config.syncMode")
            destination_sync_mode=$(echo $connection_config | jq -r ".syncCatalog.streams[${i}].config.destinationSyncMode")
            if [ "${sync_mode}" != "full_refresh" ] || [ "${destination_sync_mode}" != "append" ]; then
                all_streams_valid=false
            fi
        done
        if [ "${all_streams_valid}" = true ]; then
            echo "Full-refresh-overwrite Connection config, succeed."
            airbyte_connection=true
            break
#        else
#            echo "Full-refresh-overwrite Connection config, failed."
        fi
    done
done
if [ ${airbyte_connection} = false ] ; then
    echo "Airbyte full-refresh-overwrite connection from source Postgres to destination Postgres, failed"
    exit 0
fi