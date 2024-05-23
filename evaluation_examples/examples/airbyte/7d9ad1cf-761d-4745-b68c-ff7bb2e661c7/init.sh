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
# conda activate airbyte
# echo "source /home/user/anaconda3/etc/profile.d/conda.sh" >> ~/.bashrc
# echo "conda activate airbyte" >> ~/.bashrc
PASSWORD=password
echo $PASSWORD | sudo -S systemctl stop postgresql
# configure Postgres
POSTGRES_VERSION=16-alpine
# Start a source Postgres container running at port 2000 on localhost
docker run --rm --name airbyte-source -e POSTGRES_PASSWORD=password -p 2000:5432 -d postgres:${POSTGRES_VERSION}
echo "export POSTGRES_PASSWORD=password" >> ~/.bashrc


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

# Configure the Postgres source
docker exec -i airbyte-source psql -U postgres -c "CREATE TABLE connection_file (id integer PRIMARY KEY, name VARCHAR(200));"
docker exec -i airbyte-source psql -U postgres -c "INSERT INTO connection_file(id, name) VALUES(1, 'A1 CDCSyn');"
docker exec -i airbyte-source psql -U postgres -c "INSERT INTO connection_file(id, name) VALUES(2, 'A2 CDCSyn');"
