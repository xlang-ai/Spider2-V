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

function create_airbyte_env() {
    source /home/user/anaconda3/etc/profile.d/conda.sh
    conda create -n airbyte python=3.11 -y
    conda activate airbyte
    echo "source /home/user/anaconda3/etc/profile.d/conda.sh" >> ~/.bashrc
    echo "conda activate airbyte" >> ~/.bashrc
    pip install -e ".[dev]"
}
create_airbyte_env
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
    bash run-ab-platform.sh & # by default, use port 8000
}

cd /home/user/projects
start_airbyte_server

# configure Postgres
# pull image
docker pull postgres:16.2
# Start a source Postgres container
docker run --rm --name airbyte-source -e POSTGRES_PASSWORD=password -p 2000:5432 -d postgres
# Start a destination Postgres container running at port 3000 on localhost
docker run --rm --name airbyte-destination -e POSTGRES_PASSWORD=password -p 3000:5432 -d postgres
docker exec -i airbyte-source bash -c "sed -i '/^#*wal_level/c\wal_level = logical' /var/lib/postgresql/data/postgresql.conf"
docker restart airbyte-source
docker exec -i airbyte-source psql -U postgres -c "CREATE TABLE cdc_file (id integer PRIMARY KEY, name VARCHAR(200));"
docker exec -i airbyte-source psql -U postgres -c "INSERT INTO cdc_file(id, name) VALUES(1, 'A1 CDCSyn');"
docker exec -i airbyte-source psql -U postgres -c "INSERT INTO cdc_file(id, name) VALUES(2, 'A2 CDCSyn');"
# Configure the Postgres source for CDC replication
docker exec -i airbyte-source psql -U postgres -c "SELECT pg_create_logical_replication_slot('airbyte_slot', 'pgoutput');"
docker exec -i airbyte-source psql -U postgres -c "CREATE PUBLICATION cdc_pub FOR TABLE cdc_file;"

sleep 60
#docker exec -it airbyte-destination psql --username=postgres


