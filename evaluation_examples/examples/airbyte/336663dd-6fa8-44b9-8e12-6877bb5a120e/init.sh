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
# conda activate airbyte
# echo "source /home/user/anaconda3/etc/profile.d/conda.sh" >> ~/.bashrc
# echo "conda activate airbyte" >> ~/.bashrc

POSTGRES_VERSION=16-alpine
# Start a source Postgres container running at port 5432 on localhost
docker run --rm --name airbyte-source -e POSTGRES_PASSWORD=password123 -p 5432:5432 -d postgres:${POSTGRES_VERSION}


# start airbyte local server
function start_airbyte_server() {
    cd /home/user/projects/airbyte
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
start_airbyte_server

# set up connection 
# create source and destination
# 1. get workspace id
workspace=$(curl -X POST http://localhost:8000/api/v1/workspaces/list -H "Content-Type: application/json" -d {} | jq -rM ".workspaces | .[] | .workspaceId")
# 2. get source definition id
source_name1="Slack"
source_defid1=$(curl -X POST http://localhost:8000/api/v1/source_definitions/list -H "Content-Type: application/json" | jq -rM ".sourceDefinitions | .[] | select(.name == \"${source_name1}\") | .sourceDefinitionId")
# 3. create source, the connectionConfiguration field is source-specific
curl -X POST http://localhost:8000/api/v1/sources/create -H "Content-Type: application/json" -d "
{
    \"workspaceId\": \"${workspace}\",
    \"connectionConfiguration\": {
        \"start_date\": \"2020-01-01T00:00:00Z\",
        \"credentials\": {
            \"api_token\": \"xoxb-7126660183568-7126671285552-2vC6WXKDc7gw2yffKMA385D3\",
            \"option_title\": \"API Token Credentials\"
        },
        \"join_channels\": true,
        \"channel_filter\": [],
        \"lookback_window\": 0
    },
    \"sourceDefinitionId\": \"${source_defid1}\",
    \"name\": \"${source_name1}\", 
    \"sourceName\": \"${source_name1}\"
}
"
# 4. get source id and write into file
curl -X POST http://localhost:8000/api/v1/sources/list -H "Content-Type: application/json" -d "{\"workspaceId\": \"${workspace}\"}" | jq -rM ".sources | .[] | select(.sourceName == \"${source_name1}\") | .sourceId" > /home/user/srcid1.txt
read -r source_id1 < /home/user/srcid1.txt

source_name2="GitHub"
source_defid2=$(curl -X POST http://localhost:8000/api/v1/source_definitions/list -H "Content-Type: application/json" | jq -rM ".sourceDefinitions | .[] | select(.name == \"${source_name2}\") | .sourceDefinitionId")
# 3. create source, the connectionConfiguration field is source-specific
curl -X POST http://localhost:8000/api/v1/sources/create -H "Content-Type: application/json" -d "
{
    \"workspaceId\": \"${workspace}\",
    \"connectionConfiguration\": {
        \"api_url\": \"https://api.github.com/\",
        \"credentials\":{
            \"access_token\": \"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\",
            \"option_title\": \"OAuth Credentials\"
        },
        \"repositories\":[
            \"airbytehq/airbyte\"
        ]
    },
    \"sourceDefinitionId\": \"${source_defid2}\",
    \"name\": \"${source_name2}\", 
    \"sourceName\": \"${source_name2}\"
}
"
# 4. get source id and write into file
curl -X POST http://localhost:8000/api/v1/sources/list -H "Content-Type: application/json" -d "{\"workspaceId\": \"${workspace}\"}" | jq -rM ".sources | .[] | select(.sourceName == \"${source_name2}\") | .sourceId" > /home/user/srcid2.txt
read -r source_id2 < /home/user/srcid2.txt

# 5. get destination definition id
destination_name="Postgres"
destination_defid=$(curl -X POST http://localhost:8000/api/v1/destination_definitions/list -H "Content-Type: application/json" | jq -rM ".destinationDefinitions | .[] | select(.name == \"${destination_name}\") | .destinationDefinitionId")
# 6. create destination, the connectionConfiguration field is destination-specific
curl -X POST http://localhost:8000/api/v1/destinations/create -H "Content-Type: application/json" -d "
{
    \"workspaceId\": \"${workspace}\",
    \"connectionConfiguration\": {
       \"ssl\": false,
       \"host\": \"localhost\",
       \"port\": 5432,
       \"schema\": \"public\",
       \"database\": \"postgres\",
       \"password\": \"password123\",
       \"ssl_mode\":{
            \"mode\": \"disable\"
        },
        \"username\": \"postgres\",
        \"tunnel_method\":{
            \"tunnel_method\": \"NO_TUNNEL\"
        },
        \"disable_type_dedupe\": false
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
connection1=$(cat /home/user/connection_slack.json | sed "s/\${source_id1}/${source_id1}/" | sed "s/\${destination_id}/${destination_id}/")
curl -X POST http://localhost:8000/api/v1/connections/create -H "Content-Type: application/json" -d "${connection1}"

sed "s/\${source_id2}/${source_id2}/; s/\${destination_id}/${destination_id}/" /home/user/connection_github.json > /home/user/connection_github_new.json
curl -X POST http://localhost:8000/api/v1/connections/create -H "Content-Type: application/json" -d @/home/user/connection_github_new.json
# 9. get connection id
# 9. get connection id
curl -X POST http://localhost:8000/api/v1/connections/list -H "Content-Type: application/json" -d "{\"workspaceId\": \"${workspace}\"}" | jq -rM ".connections | .[] | .connectionId" > /home/user/connid.txt
rm /home/user/connection_slack.json
rm /home/user/connection_github.json
rm /home/user/connection_github_new.json

# set up dagster
git clone https://github.com/OwenKephart/airbyte_demo.git
cd airbyte_demo
# change python file EventMetaData 
sed -i 's/EventMetadata/MetadataValue/g' /home/user/projects/airbyte/airbyte_demo/airbyte_demo/slack_github_analytics.py
pip install -e .

gnome-terminal --maximize --working-directory=/home/user/projects/airbyte/airbyte_demo

