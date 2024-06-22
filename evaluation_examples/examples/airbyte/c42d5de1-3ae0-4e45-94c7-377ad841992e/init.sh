#!/bin/bash

####################################################################################################
# Please ensure that Chromium or Chrome, VSCode, docker and anaconda3 is installed on your system before running this script.
# The installed anaconda3 should be in the directory /home/user/anaconda3/.
# Some images should be pre-downloaded in VM snapshots to accelerate the process.
# Please ensure the snowflake settings.json and connection.json is copied to the home directory.
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
echo $PASSWORD | sudo -S systemctl stop mysql
# configure the MySQL Database and load init data
MYSQL_HOST=127.0.0.1
MYSQL_PORT=3306
MYSQL_USER=root
MYSQL_PASSWORD=password
MYSQL_VERSION=8
docker run -p ${MYSQL_HOST}:${MYSQL_PORT}:${MYSQL_PORT} --name airbyte-mysql -e MYSQL_ROOT_PASSWORD=${MYSQL_PASSWORD} -d mysql:${MYSQL_VERSION}

function start_airbyte_server() {
    cd /home/user/projects/airbyte
    bash run-ab-platform.sh > start_server.log 2> start_server.log &
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

CONTAINER_ID=$(docker ps | grep "mysql:${MYSQL_VERSION}" | awk '{print $1}')
MYSQL_FILE=/home/user/mysql_init.sql
MYSQL_CONTAINER_FILE=/home/mysql_init.sql
docker cp ${MYSQL_FILE} ${CONTAINER_ID}:${MYSQL_CONTAINER_FILE}
docker exec ${CONTAINER_ID} bash -c "mysql -u${MYSQL_USER} -p${MYSQL_PASSWORD} <${MYSQL_CONTAINER_FILE}"
rm -rf ${MYSQL_FILE}