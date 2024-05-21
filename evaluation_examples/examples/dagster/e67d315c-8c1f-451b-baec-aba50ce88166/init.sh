#!/bin/bash

####################################################################################################
# Please ensure that Chromium or Chrome, VSCode and anaconda3 is installed on your system before running this script.
# The installed anaconda3 should be in the directory /home/user/anaconda3/.
# This script is tested on Ubuntu 22.04 LTS.
####################################################################################################

# ignore all output and error
exec 1>/dev/null
exec 2>/dev/null

PASSWORD=password

# install mysql for some examples
echo $PASSWORD | sudo -S apt install pkg-config build-essential libmysqlclient-dev -y
echo $PASSWORD | sudo -S apt install mysql-server=8.0.36-0ubuntu0.22.04.1 -y # Version may differ on other machines. Not tested.
echo $PASSWORD | sudo -S systemctl enable mysql

# The commands above should be executed only in a snapshot where MySQL is not installed (like airbyte).

# some ENV for dagster
mkdir -p /home/user/.dagster
touch /home/user/.dagster/dagster.yaml
echo "export DAGSTER_HOME=/home/user/.dagster" >> /home/user/.bashrc

# The commands above should be executed only in a snapshot where dagster environment is not installed (like airbyte).

# create conda environment and install dagster
source /home/user/anaconda3/etc/profile.d/conda.sh
conda create -n dagster python=3.11 -y # Comment this line if you have dagster conda environment configured.
conda activate dagster
pip install dagster==1.7.2 dagster-webserver==1.7.2 dagster-airbyte==0.23.2


cd /home/user
# create the target dagster project
PROJECT_NAME=airbyte-mysql-to-json
mkdir -p $PROJECT_NAME
code /home/user/$PROJECT_NAME

echo $PASSWORD | sudo -S ls > /dev/null
sudo -S mysql < database_init.sql
rm -f database_init.sql

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
source_name="MySQL"
source_defid=$(curl -X POST http://localhost:8000/api/v1/source_definitions/list -H "Content-Type: application/json" | jq -rM ".sourceDefinitions | .[] | select(.name == \"${source_name}\") | .sourceDefinitionId")
# 3. create source, the connectionConfiguration field is source-specific
curl -X POST http://localhost:8000/api/v1/sources/create -H "Content-Type: application/json" -d "
{
    \"workspaceId\": \"${workspace}\",
    \"connectionConfiguration\": {
        \"sourceType\": \"mysql\",
        \"port\": 3306,
        \"ssl_mode\": {
            \"mode\": \"preferred\"
        },
        \"replication_method\": {
            \"method\": \"CDC\"
        },
        \"tunnel_method\": {
            \"tunnel_method\": \"NO_TUNNEL\"
        },
        \"host\": \"localhost\",
        \"database\": \"master\",
        \"username\": \"user\",
        \"password\": \"password\"
    },
    \"sourceDefinitionId\": \"${source_defid}\",
    \"name\": \"${source_name}\", 
    \"sourceName\": \"${source_name}\"
}
"

# 4. get source id and write into file
curl -X POST http://localhost:8000/api/v1/sources/list -H "Content-Type: application/json" -d "{\"workspaceId\": \"${workspace}\"}" | jq -rM ".sources | .[] | select(.sourceName == \"${source_name}\") | .sourceId" > /home/user/srcid.txt
read -r source_id < /home/user/srcid.txt
rm /home/user/srcid.txt
# 5. get destination definition id
destination_name="Local JSON"
destination_defid=$(curl -X POST http://localhost:8000/api/v1/destination_definitions/list -H "Content-Type: application/json" | jq -rM ".destinationDefinitions | .[] | select(.name == \"${destination_name}\") | .destinationDefinitionId")
# 6. create destination, the connectionConfiguration field is destination-specific
curl -X POST http://localhost:8000/api/v1/destinations/create -H "Content-Type: application/json" -d "
{
    \"workspaceId\": \"${workspace}\",
    \"connectionConfiguration\": {
        \"destination_path\":\"/pageviews_data\"
    },
    \"destinationDefinitionId\": \"${destination_defid}\",
    \"name\": \"${destination_name}\", 
    \"destinationName\": \"${destination_name}\"
}
"
# 7. get destination id and write into file
curl -X POST http://localhost:8000/api/v1/destinations/list -H "Content-Type: application/json" -d "{\"workspaceId\": \"${workspace}\"}" | jq -rM ".destinations | .[] | select(.destinationName == \"${destination_name}\") | .destinationId" > /home/user/destid.txt
read -r destination_id < /home/user/destid.txt
rm /home/user/destid.txt
# 8. create connection
connection=$(cat /home/user/connection_mysql.json | sed "s/\${source_id}/${source_id}/" | sed "s/\${destination_id}/${destination_id}/")
curl -X POST http://localhost:8000/api/v1/connections/create -H "Content-Type: application/json" -d "${connection}"
rm /home/user/connection_mysql.json

# 9. get connection id
# curl -X POST http://localhost:8000/api/v1/connections/list -H "Content-Type: application/json" -d "{\"workspaceId\": \"${workspace}\"}" | jq -rM ".connections | .[] | .connectionId" > /home/user/connid.txt

touch /home/user/$PROJECT_NAME/dagster_migration.py
code /home/user/$PROJECT_NAME/dagster_migration.py
echo "source /home/user/anaconda3/etc/profile.d/conda.sh" >> ~/.bashrc
echo "conda activate dagster" >> ~/.bashrc