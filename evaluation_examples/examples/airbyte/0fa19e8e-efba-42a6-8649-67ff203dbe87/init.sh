#!/bin/bash

####################################################################################################
# Please ensure that Chromium or Chrome, VSCode, docker and anaconda3 is installed on your system before running this script.
# The installed anaconda3 should be in the directory /home/user/anaconda3/.
# Some images should be pre-downloaded in VM snapshots to accelerate the process.
# Please ensure the snowflake settings.json and connection.json is copied to the home directory.
# BTW, a database named COVID19 should be created in Snowflake.
# This script is tested on Ubuntu 22.04 LTS.
####################################################################################################

# ignore all output and error
exec 1>/dev/null
exec 2>/dev/null

# source /home/user/anaconda3/etc/profile.d/conda.sh
# conda create -n airbyte python=3.11 -y
# conda activate airbyte
# echo "source /home/user/anaconda3/etc/profile.d/conda.sh" >> ~/.bashrc
# echo "conda activate airbyte" >> ~/.bashrc
mkdir -p /home/user/projects

# start airbyte local server
function start_airbyte_server() {
    git clone --depth=1 https://github.com/airbytehq/airbyte.git
    cd airbyte
    VERSION=0.55.2
    # declare -a image_list=(
    #     "alpine/socat"
    #     "airbyte/init:${VERSION}"
    #     "airbyte/bootloader:${VERSION}"
    #     "airbyte/db:${VERSION}"
    #     "airbyte/worker:${VERSION}"
    #     "airbyte/server:${VERSION}"
    #     "airbyte/webapp:${VERSION}"
    #     "airbyte/temporal:${VERSION}"
    #     "airbyte/cron:${VERSION}"
    #     "airbyte/airbyte-api-server:${VERSION}"
    #     "airbyte/connector-builder-server:${VERSION}"
    #     "airbyte/proxy:${VERSION}"
    # )
    # images=$(docker images | awk 'NR > 1 {if ($2 == "latest") print $1; else print $1 ":" $2}')
    # for img in ${image_list[@]}; do
    #     echo ${images} | grep -Fiq -- "$img"
    #     if [ $? -ne 0 ]; then
    #         docker pull ${img}
    #     fi
    # done
    sed -i.bak "s/^VERSION=.*$/VERSION=${VERSION}/" run-ab-platform.sh
    bash run-ab-platform.sh -d # only download file
    # remove airbyte basic auth, set username and password to empty ""
    sed -i '/^BASIC_AUTH_USERNAME=/c\
BASIC_AUTH_USERNAME=""
' .env
    sed -i '/^BASIC_AUTH_PASSWORD=/c\
BASIC_AUTH_PASSWORD=""
' .env
    bash run-ab-platform.sh > start_server.log &
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

cd /home/user/projects
start_airbyte_server


# configure Postgres
# pull image
docker pull postgres:16.0
docker run --rm --name airbyte-source -e POSTGRES_PASSWORD=password -p 5432:5432 -d postgres:16.0
sleep 10

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
curl -X POST http://localhost:8000/api/v1/sources/list -H "Content-Type: application/json" -d "{\"workspaceId\": \"${workspace}\"}" | jq -rM ".sources | .[] | select(.sourceName == \"${source_name}\") | .sourceId" > /home/user/srcid.txt
read -r source_id < /home/user/srcid.txt
# 5. get destination definition id
destination_name="Snowflake"
destination_defid=$(curl -X POST http://localhost:8000/api/v1/destination_definitions/list -H "Content-Type: application/json" | jq -rM ".destinationDefinitions | .[] | select(.name == \"${destination_name}\") | .destinationDefinitionId")
# 6. create destination, the connectionConfiguration field is destination-specific
SNOWFLAKE_ACCOUNT=$(cat /home/user/settings.json | jq -rM ".account")
SNOWFLAKE_USER=$(cat /home/user/settings.json | jq -rM ".user")
SNOWFLAKE_PASSWORD=$(cat /home/user/settings.json | jq -rM ".password")
curl -X POST http://localhost:8000/api/v1/destinations/create -H "Content-Type: application/json" -d "
{
    \"workspaceId\": \"${workspace}\",
    \"connectionConfiguration\": {
        \"host\": \"${SNOWFLAKE_ACCOUNT}\",
        \"role\": \"ACCOUNTADMIN\",
        \"schema\": \"customers\",
        \"database\": \"development\",
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
curl -X POST http://localhost:8000/api/v1/destinations/list -H "Content-Type: application/json" -d "{\"workspaceId\": \"${workspace}\"}" | jq -rM ".destinations | .[] | select(.destinationName == \"${destination_name}\") | .destinationId" > /home/user/destid.txt
read -r destination_id < /home/user/destid.txt
# 8. create connection
connection=$(cat /home/user/connection.json | sed "s/\${source_id}/${source_id}/" | sed "s/\${destination_id}/${destination_id}/")
curl -X POST http://localhost:8000/api/v1/connections/create -H "Content-Type: application/json" -d "${connection}"
# 9. get connection id
curl -X POST http://localhost:8000/api/v1/connections/list -H "Content-Type: application/json" -d "{\"workspaceId\": \"${workspace}\"}" | jq -rM ".connections | .[] | .connectionId" > /home/user/connid.txt
rm /home/user/connection.json

#configure data-diff
pip install data-diff
pip install "pydantic>=1.10.12,<2.0.0"
pip install psycopg2-binary
pip install 'data-diff[postgresql]'
pip install 'data-diff[snowflake]'


gnome-terminal --maximize --working-directory=home/user/projects/

# waiting for the first sync
sleep 120

#add data into source database
# docker exec -i airbyte-source psql -U postgres -d development -c "INSERT INTO customers.users(col1) VALUES('record4');"
# docker exec -i airbyte-source psql -U postgres -d development -c "INSERT INTO customers.users(col1) VALUES('record5');"

# "snowflake://XLANG:Spider2.0@zd89187.us-central1.gcp/development/CUSTOMERS?warehouse=COMPUTE_WH&role=ACCOUNTADMIN" USER
# "postgresql://postgres:password@localhost:5432/development" customers.user
# data-diff "snowflake://XLANG:Spider2.0@zd89187.us-central1.gcp/development/CUSTOMERS?warehouse=COMPUTE_WH&role=ACCOUNTADMIN" USERS "postgresql://postgres:password@localhost:5432/development" customers.users >> diff_test.csv