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
# # Start a source Postgres container running at port 2000 on localhost
docker run --rm --name airbyte-source -e POSTGRES_PASSWORD=password -p 2000:5432 -d postgres:${POSTGRES_VERSION}
# Start a destination Postgres container running at port 3000 on localhost
docker run --rm --name airbyte-destination -e POSTGRES_PASSWORD=password -p 3000:5432 -d postgres:${POSTGRES_VERSION}


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

docker exec -i airbyte-source psql -U postgres -d postgres -c "CREATE TABLE basic_file(id integer PRIMARY KEY, name VARCHAR(200));"
docker exec -i airbyte-source psql -U postgres -d postgres -c "INSERT INTO basic_file(id, name) VALUES(1, 'Mary X');"
docker exec -i airbyte-source psql -U postgres -d postgres -c "INSERT INTO basic_file(id, name) VALUES(2, 'John D');"


echo password | sudo -S apt-get install -y expect
expect -c '
set timeout -1
spawn bash -c "curl -s -o- https://raw.githubusercontent.com/observablehq/airbyte/master/octavia-cli/install.sh | bash"
expect {
    "❓ - Allow Airbyte to collect telemetry to improve the CLI? (Y/n)" {
        send "Y\r"
        exp_continue
    }
    eof {
        puts "Installation complete."
    }
}
'
sleep 10

source /home/user/.bashrc
echo "OCTAVIA_ENABLE_TELEMETRY=True" >> ~/.octavia
echo "AIRBYTE_USERNAME=airbyte" >> ~/.octavia
echo "AIRBYTE_PASSWORD=password" >> ~/.octavia
mkdir airbyte-configuration && cd airbyte-configuration


gnome-terminal --maximize --working-directory=/home/user/projects/airbyte/airbyte-configuration/

# octavia init

## octavia list connectors sources | grep postgres
# octavia generate source decd338e-5647-4c0b-adf4-da0e75f5a750 postgres
# nano sources/postgres/configuration.yaml
# octavia apply

## octavia list connectors destinations | grep postgres
# octavia generate destination 25c5221d-dce2-4163-ade9-739ef790f503 postgres
# nano postgres destinations/bigquery/configuration.yaml

#  octavia generate connection --source sources/postgres/configuration.yaml --destination destinations/postgres/configuration.yaml postgres-to-postgres
# nano connections/postgres_to_postgres/configuration.yaml
# octavia apply -f connections/postgres_to_postgres/configuration.yaml




