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

function create_airbyte_env() {
    source /home/user/anaconda3/etc/profile.d/conda.sh
    conda create -n airbyte python=3.11 -y
    conda activate airbyte
    echo "source /home/user/anaconda3/etc/profile.d/conda.sh" >> ~/.bashrc
    echo "conda activate airbyte" >> ~/.bashrc
}
# create_airbyte_env # can be skipped since no pip install is needed
mkdir -p /home/user/projects

# configure Postgres
POSTGRES_VERSION=15
# docker pull postgres:${POSTGRES_VERSION}
# Start a source Postgres container running at port 3000 on localhost
docker run --rm --name airbyte-source -e POSTGRES_PASSWORD=password -p 2000:5432 -d postgres:${POSTGRES_VERSION}
# Start a destination Postgres container running at port 3000 on localhost
docker run --rm --name airbyte-destination -e POSTGRES_PASSWORD=password -p 3000:5432 -d postgres:${POSTGRES_VERSION}

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

cd /home/user/projects
start_airbyte_server

# Configure the Postgres source for CDC replication
docker exec -i airbyte-source bash -c "sed -i '/^#*wal_level/c\
wal_level = logical
' /var/lib/postgresql/data/postgresql.conf"
docker restart airbyte-source
docker exec -i airbyte-source psql -U postgres -c "CREATE TABLE cdc_file (id integer PRIMARY KEY, name VARCHAR(200));"
docker exec -i airbyte-source psql -U postgres -c "INSERT INTO cdc_file(id, name) VALUES(1, 'A1 CDCSyn');"
docker exec -i airbyte-source psql -U postgres -c "INSERT INTO cdc_file(id, name) VALUES(2, 'A2 CDCSyn');"
docker exec -i airbyte-source psql -U postgres -c "SELECT pg_create_logical_replication_slot('airbyte_slot', 'pgoutput');"
docker exec -i airbyte-source psql -U postgres -c "CREATE PUBLICATION cdc_pub FOR TABLE cdc_file;"
