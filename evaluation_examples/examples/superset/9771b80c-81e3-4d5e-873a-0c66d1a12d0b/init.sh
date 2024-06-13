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
# cd /home/user
# wget https://raw.githubusercontent.com/apache-superset/examples-data/master/tutorial_flights.csv



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

function create_database() {
    token=$(curl -X POST "http://localhost:8088/api/v1/security/login" \
        -H "Content-Type: application/json" \
        -d '{
            "username": "admin",
            "password": "admin",
            "provider": "db"
        }' | jq -rM ".access_token")

    echo $(curl -X POST "http://localhost:8088/api/v1/database/" \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer ${token}" \
        -d '{
                "database_name":"PublicData",
                "sqlalchemy_uri": "postgresql://superset:superset@db:5432/superset"
        }'
    )
}

create_database
