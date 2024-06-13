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

# source /home/user/anaconda3/etc/profile.d/conda.sh
# conda activate superset
# echo "source /home/user/anaconda3/etc/profile.d/conda.sh" >> ~/.bashrc
# echo "conda activate superset" >> ~/.bashrc

function start_superset_server() {
    cd /home/user/projects/superset
    docker compose -f docker-compose-image-tag.yml up --detach
    count=0
    while true; do
        sleep 5
        count=$(expr $count + 1)
        stop_flag=$(docker compose logs | grep "Init Step 4/4") # "Init Step 4/4 \[Complete\]"
        if [ $? -eq 0 ]; then
            echo "The server has been started"
            break
        fi
        if [ $count -gt 10 ]; then
            echo "The server has not been started in 30 seconds"
            break
        fi
    done
}

start_superset_server

cd /home/user
docker cp all_databases.sql superset_db:/all_databases.sql
docker exec -t superset_db psql -U superset -f /all_databases.sql

function init_data() {
    token=$(curl -X POST "http://localhost:8088/api/v1/security/login" \
        -H "Content-Type: application/json" \
        -d '{
            "username": "admin",
            "password": "admin",
            "provider": "db"
        }' | jq -rM ".access_token")

    charts=$(curl -X GET "http://localhost:8088/api/v1/chart/" \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer ${token}")

    chart_ids=$(echo $charts | jq -r '.result[].id')

    for id in $chart_ids; do
        curl -X DELETE "http://localhost:8088/api/v1/chart/${id}" \
            -H "Content-Type: application/json" \
            -H "Authorization: Bearer ${token}"
    done


    dashboards=$(curl -X GET "http://localhost:8088/api/v1/dashboard/" \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer ${token}")


    dashboard_ids=$(echo $dashboards | jq -r '.result[].id')


    for id in $dashboard_ids; do
        curl -X DELETE "http://localhost:8088/api/v1/dashboard/${id}" \
            -H "Content-Type: application/json" \
            -H "Authorization: Bearer ${token}"
    done
}

init_data

function create_database() {
    cd /home/user/
    token=$(curl -X POST "http://localhost:8088/api/v1/security/login" \
        -H "Content-Type: application/json" \
        -d '{
            "username": "admin",
            "password": "admin",
            "provider": "db"
        }' | jq -rM ".access_token")

    curl -X POST "http://localhost:8088/api/v1/database/import/" \
    -H "Authorization: Bearer ${token}" \
    -H "Content-Type: multipart/form-data" \
    -F "formData=@/home/user/database_export_20240523T204001.zip" \
    -F "overwrite=true" -F "passwords={\"databases/LineData.yaml\": \"superset\"}"
}

create_database