#!/bin/bash

####################################################################################################
# Please ensure that Chromium or Chrome, VSCode, docker and anaconda3 is installed on your system before running this script.
# The installed anaconda3 should be in the directory /home/user/anaconda3/.
# Some images should be pre-downloaded in VM snapshots to accelerate the process.
# Please ensure the snowflake settings.json and connection.json is copied to the home directory.
# BTW, a database named COVID19 should be created in Snowflake.
# This script is tested on Ubuntu 20.04 LTS.
####################################################################################################

# ignore all output and error
exec 1>/dev/null
exec 2>/dev/null

source /home/user/anaconda3/etc/profile.d/conda.sh
conda create -n airbyte python=3.11 -y
conda activate airbyte
echo "source /home/user/anaconda3/etc/profile.d/conda.sh" >> ~/.bashrc
echo "conda activate airbyte" >> ~/.bashrc
mkdir -p /home/user/projects

# start airbyte local server
# download images are very slow, better pre-download them in VM snapshots
VERSION=0.55.2 # $(awk -F'=' '/^VERSION=/ {print $2; exit}' run-ab-platform.sh)
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
function start_airbyte_server() {
    git clone --depth=1 https://github.com/airbytehq/airbyte.git
    cd airbyte
    sed -i.bak "s/^VERSION=.*$/VERSION=${VERSION}/" run-ab-platform.sh
    bash run-ab-platform.sh -d # only download file
    # remove airbyte basic auth, set username and password to empty ""
    sed -i '/^BASIC_AUTH_USERNAME=/c\
BASIC_AUTH_USERNAME=""
' .env
    sed -i '/^BASIC_AUTH_PASSWORD=/c\
BASIC_AUTH_PASSWORD=""
' .env
    bash run-ab-platform.sh &
}

cd /home/user/projects
start_airbyte_server
sleep 60

# create source and destination
# 1. get workspace id
workspace=$(curl -X POST http://localhost:8000/api/v1/workspaces/list -H "Content-Type: application/json" -d {} | jq -rM ".workspaces | .[] | .workspaceId")
# 2. get source definition id
source_name="File (CSV, JSON, Excel, Feather, Parquet)"
source_defid=$(curl -X POST http://localhost:8000/api/v1/source_definitions/list -H "Content-Type: application/json" | jq -rM ".sourceDefinitions | .[] | select(.name == \"${source_name}\") | .sourceDefinitionId")
# 3. create source, the connectionConfiguration field is source-specific
curl -X POST http://localhost:8000/api/v1/sources/create -H "Content-Type: application/json" -d "
{
    \"workspaceId\": \"${workspace}\",
    \"connectionConfiguration\": {
        \"url\": \"https://storage.googleapis.com/covid19-open-data/v2/latest/epidemiology.csv\",
        \"format\": \"csv\",
        \"provider\": {
            \"storage\": \"HTTPS\",
            \"user_agent\": false
        },
        \"dataset_name\": \"epidemiology\"
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
        \"schema\": \"PUBLIC\",
        \"database\": \"COVID19\",
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