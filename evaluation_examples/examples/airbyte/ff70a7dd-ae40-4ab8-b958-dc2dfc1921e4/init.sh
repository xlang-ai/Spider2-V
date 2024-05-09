#!/bin/bash

####################################################################################################
# Please ensure that Chromium or Chrome, VSCode, docker and anaconda3 is installed on your system before running this script.
# The installed anaconda3 should be in the directory /home/user/anaconda3/.
# Some images should be pre-downloaded in VM snapshots to accelerate the process.
# Please ensure the initial project is copied to the home directory.
# This script is tested on Ubuntu 20.04 LTS.
####################################################################################################

# ignore all output and error
exec 1>/dev/null
exec 2>/dev/null

# source /home/user/anaconda3/etc/profile.d/conda.sh
# conda activate airbyte
# echo "source /home/user/anaconda3/etc/profile.d/conda.sh" >> ~/.bashrc
# echo "conda activate airbyte" >> ~/.bashrc
mkdir -p /home/user/projects

# start airbyte local server
function start_airbyte_server() {
    cd /home/user/projects/airbyte
    bash run-ab-platform.sh > start_server.log &
    total_time=0
    while true; do
        sleep 3
        total_time=$(expr ${total_time} + 3)
        msg=$(cat start_server.log | grep -i "Startup completed" | grep "airbyte-worker")
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

# create source and destination
# 1. get workspace id
workspace=$(curl -X POST http://localhost:8000/api/v1/workspaces/list -H "Content-Type: application/json" -d {} | jq -rM ".workspaces | .[] | .workspaceId")
# 2. get source definition id
source_name="Sample Data (Faker)"
source_defid=$(curl -X POST http://localhost:8000/api/v1/source_definitions/list -H "Content-Type: application/json" | jq -rM ".sourceDefinitions | .[] | select(.name == \"${source_name}\") | .sourceDefinitionId")
# 3. create source, the connectionConfiguration field is source-specific
curl -X POST http://localhost:8000/api/v1/sources/create -H "Content-Type: application/json" -d "
{
    \"workspaceId\": \"${workspace}\",
    \"connectionConfiguration\": {
        \"seed\": -1,
        \"count\": 1000,
        \"parallelism\": 4,
        \"always_updated\": true, 
        \"records_per_slice\": 1000
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
destination_name="Local JSON"
destination_defid=$(curl -X POST http://localhost:8000/api/v1/destination_definitions/list -H "Content-Type: application/json" | jq -rM ".destinationDefinitions | .[] | select(.name == \"${destination_name}\") | .destinationDefinitionId")
# 6. create destination, the connectionConfiguration field is destination-specific
curl -X POST http://localhost:8000/api/v1/destinations/create -H "Content-Type: application/json" -d "
{
    \"workspaceId\": \"${workspace}\",
    \"connectionConfiguration\": {
        \"destination_path\":\"/json_from_faker\"
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


# source /home/user/anaconda3/etc/profile.d/conda.sh  
# conda create -n airflow python=3.11 -y >/dev/null 2>&1  
# conda activate airflow

# pip install apache-airflow==2.9.0
# function to_ready_state(){
#     echo "source /home/user/anaconda3/etc/profile.d/conda.sh" >> ~/.bashrc
#     echo "conda activate airflow" >> ~/.bashrc
#     cd /home/user/projects
#     yes | astro dev init 2>&1 
#     astro dev start >/dev/null 2>&1 
#     wait
# }
# to_ready_state


pip install apache-airflow==2.9.0
pip install apache-airflow-providers-airbyte
pip install 
mkdir airflow 
cd airflow
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.5.1/docker-compose.yaml'
mkdir -p ./dags ./logs ./plugins
echo -e "AIRFLOW_UID=$(id -u)" > .env
# create Dockerfile
echo "FROM \${AIRFLOW_IMAGE_NAME:-apache/airflow:2.5.1}" > Dockerfile
echo "USER airflow" >> Dockerfile
echo "RUN pip install apache-airflow-providers-airbyte[http] \\" >> Dockerfile
echo "&& pip install apache-airflow-providers-airbyte" >> Dockerfile
#edit ymal
sed -i '/x-airflow-common/,/airflow-common-env/{s/# *build:/build:/}' /home/user/projects/airbyte/airflow/docker-compose.yaml
LINE_NUMBER=$(awk "/x-airflow-common/,/volumes:/"'{if ($0 ~ /volumes:/) print NR}' /home/user/projects/airbyte/airflow/docker-compose.yaml)
NEW_VOLUME='\ \ \ \ - /tmp/airbyte_local:/tmp/airbyte_local'
sed -i "${LINE_NUMBER}a $NEW_VOLUME" /home/user/projects/airbyte/airflow/docker-compose.yaml
# docker compose build
gnome-terminal --maximize --working-directory=/home/user/projects/airbyte/airflow/

# docker compose build > build.log 2>&1
# docker compose up -d airflow-init
# docker compose logs -f airflow-init | tee airflow-init.log
# docker compose up -d

