#!/bin/bash

####################################################################################################
# Please ensure that Chromium or Chrome, VSCode, docker and anaconda3 is installed on your system before running this script.
# The installed anaconda3 should be in the directory /home/user/anaconda3/.
# Some images should be pre-downloaded in VM snapshots to accelerate the process.
# Please ensure the snowflake settings.json and connection.json is copied to the home directory.
# This script is tested on Ubuntu 22.04 LTS.
####################################################################################################

# ignore all output and error
exec 1>/dev/null
exec 2>/dev/null

# source /home/user/anaconda3/etc/profile.d/conda.sh
# conda activate airbyte
# echo "source /home/user/anaconda3/etc/profile.d/conda.sh" >> ~/.bashrc
# echo "conda activate airbyte" >> ~/.bashrc
PASSWORD=password
echo $PASSWORD | sudo -S systemctl stop postgresql

POSTGRES_VERSION=16-alpine
# Start a source Postgres container running at port 5432 on localhost
docker run --rm --name airbyte-source -e POSTGRES_PASSWORD=password -p 5432:5432 -d postgres:${POSTGRES_VERSION}
echo "export POSTGRES_PASSWORD=password" >> ~/.bashrc

# start airbyte local server
function start_airbyte_server() {
    cd /home/user/projects/airbyte
    bash run-ab-platform.sh > start_server.log 2>start_server.log &
    total_time=0
    while true; do
        sleep 3
        total_time=$(expr ${total_time} + 3)
        cat start_server.log | grep -i "Startup completed" | grep "airbyte-worker"
        if [ $? -eq 0 ]; then # the server has been launched
            break
        fi
        if [ ${total_time} -gt 60 ]; then # exceeding maximum waiting time
            echo "Exceeding maximum waiting time 60s for airbyte server to launch!"
            break
        fi
    done
}
start_airbyte_server

# create database, schemas and tables
docker exec -i airbyte-source psql -U postgres -c "CREATE DATABASE development;"
docker exec -i airbyte-source psql -U postgres -d development -c "CREATE SCHEMA customers";
docker exec -i airbyte-source psql -U postgres -d development -c "CREATE TABLE customers.users(id SERIAL PRIMARY KEY, col1 VARCHAR(200));"
docker exec -i airbyte-source psql -U postgres -d development -c "INSERT INTO customers.users(col1) VALUES('record1');"
docker exec -i airbyte-source psql -U postgres -d development -c "INSERT INTO customers.users(col1) VALUES('record2');"
docker exec -i airbyte-source psql -U postgres -d development -c "INSERT INTO customers.users(col1) VALUES('record3');"

# create source and destination
# 1. get workspace id
workspace=$(curl -X POST http://localhost:8000/api/v1/workspaces/list -H "Content-Type: application/json" -d {} | jq -rM ".workspaces | .[] | .workspaceId")
# 2. get source definition id
source_name="Postgres"
source_defid=$(curl -X POST http://localhost:8000/api/v1/source_definitions/list -H "Content-Type: application/json" | jq -rM ".sourceDefinitions | .[] | select(.name == \"${source_name}\") | .sourceDefinitionId")
# 3. create source, the connectionConfiguration field is source-specific
curl -X POST http://localhost:8000/api/v1/sources/create -H "Content-Type: application/json" -d "
{
    \"workspaceId\": \"${workspace}\",
    \"connectionConfiguration\": {
        \"host\": \"localhost\",
        \"port\": 5432,
        \"schemas\": [\"customers\"],
        \"database\": \"development\",
        \"password\": \"password\",
        \"ssl_mode\": {\"mode\": \"disable\"},
        \"username\": \"postgres\",
        \"tunnel_method\": {\"tunnel_method\": \"NO_TUNNEL\"},
        \"replication_method\": {\"method\": \"Standard\"}
    },
    \"sourceDefinitionId\": \"${source_defid}\",
    \"name\": \"${source_name}\", 
    \"sourceName\": \"${source_name}\"
}
"
# 4. get source id and write into file
source_id=$(curl -X POST http://localhost:8000/api/v1/sources/list -H "Content-Type: application/json" -d "{\"workspaceId\": \"${workspace}\"}" | jq -rM ".sources | .[] | select(.sourceName == \"${source_name}\") | .sourceId")
# 5. get destination definition id
destination_name="Snowflake"
destination_defid=$(curl -X POST http://localhost:8000/api/v1/destination_definitions/list -H "Content-Type: application/json" | jq -rM ".destinationDefinitions | .[] | select(.name == \"${destination_name}\") | .destinationDefinitionId")
# 6. create destination, the connectionConfiguration field is destination-specific
SNOWFLAKE_ACCOUNT=$(cat /home/user/settings.json | jq -rM ".account")
SNOWFLAKE_USER=$(cat /home/user/settings.json | jq -rM ".user")
SNOWFLAKE_PASSWORD=$(cat /home/user/settings.json | jq -rM ".password")
# write account info into bashrc (environment variables)
echo "export SNOWFLAKE_ACCOUNT=${SNOWFLAKE_ACCOUNT}" >> ~/.bashrc
echo "export SNOWFLAKE_USER=${SNOWFLAKE_USER}" >> ~/.bashrc
echo "export SNOWFLAKE_PASSWORD=${SNOWFLAKE_PASSWORD}" >> ~/.bashrc
curl -X POST http://localhost:8000/api/v1/destinations/create -H "Content-Type: application/json" -d "
{
    \"workspaceId\": \"${workspace}\",
    \"connectionConfiguration\": {
        \"host\": \"${SNOWFLAKE_ACCOUNT}\",
        \"role\": \"ACCOUNTADMIN\",
        \"schema\": \"CUSTOMERS\",
        \"database\": \"DEVELOPMENT\",
        \"username\": \"${SNOWFLAKE_USER}\",
        \"warehouse\": \"COMPUTE_WH\",
        \"credentials\": {
            \"password\": \"${SNOWFLAKE_PASSWORD}\",
            \"auth_type\": \"Username and Password\"
        }
    },
    \"destinationDefinitionId\": \"${destination_defid}\",
    \"name\": \"${destination_name}\", 
    \"destinationName\": \"${destination_name}\"
}
"
rm /home/user/settings.json
# 7. get destination id and write into file
destination_id=$(curl -X POST http://localhost:8000/api/v1/destinations/list -H "Content-Type: application/json" -d "{\"workspaceId\": \"${workspace}\"}" | jq -rM ".destinations | .[] | select(.destinationName == \"${destination_name}\") | .destinationId")
# 8. create connection
connection=$(cat /home/user/connection.json | sed "s/\${source_id}/${source_id}/" | sed "s/\${destination_id}/${destination_id}/")
connid=$(curl -X POST http://localhost:8000/api/v1/connections/create -H "Content-Type: application/json" -d "${connection}" | jq -rM ".connectionId")
rm /home/user/connection.json
# 9. sync connection
curl -X POST http://localhost:8000/api/v1/connections/sync -H "Content-Type: application/json" -d "{\"connectionId\": \"${connid}\"}"
total_time=0
while true; do
    sleep 5
    total_time=$(expr $total_time + 5)
    # get the last sync job and wait for succeed status
    status=$(curl -X POST http://localhost:8000/api/v1/jobs/get_last_replication_job -H "Content-Type: application/json" -d "{\"connectionId\": \"${connid}\"}" | jq -rM ".job.status")
    if [ "${status}" = "succeeded" ]; then
        break
    fi
    if [ ${total_time} -gt 120 ]; then
        echo "Exceeding maximum waiting time 120s for sync connection!"
        break
    fi
done

gnome-terminal --maximize --working-directory=/home/user/Desktop/