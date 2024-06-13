#!/bin/bash

####################################################################################################
# Please ensure that Chromium or Chrome, VSCode, docker and anaconda3 is installed on your system before running this script.
# The installed anaconda3 should be in the directory /home/user/anaconda3/.
# Some images should be pre-downloaded in VM snapshots to accelerate the process.
# Please ensure the initial project is copied to the home directory.
# This script is tested on Ubuntu 22.04 LTS.
####################################################################################################

# ignore all output and error
exec 1>/dev/null
exec 2>/dev/null

#source /home/user/anaconda3/etc/profile.d/conda.sh
#conda activate airflow
#echo "source /home/user/anaconda3/etc/profile.d/conda.sh" >> ~/.bashrc
#echo "conda activate airflow" >> ~/.bashrc


# mount docker volume oss_local_root to /tmp/airbyte_local
docker volume ls | grep oss_local_root
if [ $? -eq 0 ]; then
    docker volume rm oss_local_root
fi
mkdir -p /tmp/airbyte_local
cd /home/user/projects/airbyte
# bind docker volume oss_local_root to /tmp/airbyte_local
sed -i.bak '/local_root:$/a\
    driver: local\
    driver_opts:\
      type: none\
      device: \/tmp\/airbyte_local\
      o: bind
' docker-compose.yaml

# start airbyte local server
function start_airbyte_server() {
    cd /home/user/projects/airbyte
    # may not need to wait, since airflow also needs to wait
    bash run-ab-platform.sh > start_server.log 2> start_server.log &
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
source_id=$(curl -X POST http://localhost:8000/api/v1/sources/list -H "Content-Type: application/json" -d "{\"workspaceId\": \"${workspace}\"}" | jq -rM ".sources | .[] | select(.sourceName == \"${source_name}\") | .sourceId")
# 5. get destination definition id
destination_name="Local JSON"
destination_defid=$(curl -X POST http://localhost:8000/api/v1/destination_definitions/list -H "Content-Type: application/json" | jq -rM ".destinationDefinitions | .[] | select(.name == \"${destination_name}\") | .destinationDefinitionId")
# 6. create destination, the connectionConfiguration field is destination-specific
curl -X POST http://localhost:8000/api/v1/destinations/create -H "Content-Type: application/json" -d "
{
    \"workspaceId\": \"${workspace}\",
    \"connectionConfiguration\": {
        \"destination_path\":\"/json_data\"
    },
    \"destinationDefinitionId\": \"${destination_defid}\",
    \"name\": \"${destination_name}\", 
    \"destinationName\": \"${destination_name}\"
}
"
# 7. get destination id and write into file
destination_id=$(curl -X POST http://localhost:8000/api/v1/destinations/list -H "Content-Type: application/json" -d "{\"workspaceId\": \"${workspace}\"}" | jq -rM ".destinations | .[] | select(.destinationName == \"${destination_name}\") | .destinationId")
# 8. create connection
connection=$(cat /home/user/connection.json | sed "s/\${source_id}/${source_id}/" | sed "s/\${destination_id}/${destination_id}/")
curl -X POST http://localhost:8000/api/v1/connections/create -H "Content-Type: application/json" -d "${connection}"
rm /home/user/connection.json

# please ensure that the project astro-airbyte-proj is copied to the home directory
function to_ready_state(){
    mv /home/user/astro-airbyte-proj.zip /home/user/projects
    cd /home/user/projects/
    unzip -q astro-airbyte-proj.zip
    rm -f astro-airbyte-proj.zip
    code /home/user/projects/astro-airbyte-proj
    cd astro-airbyte-proj
    astro dev start --no-browser >start_server.log 2>start_server.log
}
to_ready_state

# docker compose build
gnome-terminal --maximize --working-directory=/home/user/projects/astro-airbyte-proj
code /home/user/projects/astro-airbyte-proj/dags/faker_to_json_dag.py
code /home/user/projects/astro-airbyte-proj/README.md