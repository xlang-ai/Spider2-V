#!/bin/bash

####################################################################################################
# Please ensure that Chromium or Chrome, VSCode, docker and anaconda3 is installed on your system before running this script.
# The installed anaconda3 should be in the directory /home/user/anaconda3/.
# Some images should be pre-downloaded in VM snapshots to accelerate the process.
# Please ensure the snowflake settings.json and connection.json is copied to the home directory.
# BTW, a database named COVID19 should be created in Snowflake.
# This script is tested on Ubuntu 20.04 LTS.
####################################################################################################

# ignore all output and error
exec 1>/dev/null
exec 2>/dev/null

# source /home/user/anaconda3/etc/profile.d/conda.sh
# conda create -n airbyte python=3.11 -y
# conda activate airbyte
# echo "source /home/user/anaconda3/etc/profile.d/conda.sh" >> ~/.bashrc
# echo "conda activate airbyte" >> ~/.bashrc
mkdir -p /home/user/projects

# start airbyte local server
# download images are very slow, better pre-download them in VM snapshots
VERSION=0.55.2 # $(awk -F'=' '/^VERSION=/ {print $2; exit}' run-ab-platform.sh)
MYSQL_VERSION=8
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
#     "airbyte/proxy:${VERSION}",
#     "mysql:${MYSQL_VERSION}"
# )
# images=$(docker images | awk 'NR > 1 {if ($2 == "latest") print $1; else print $1 ":" $2}')
# for img in ${image_list[@]}; do
#     echo ${images} | grep -Fiq -- "$img"
#     if [ $? -ne 0 ]; then
#         docker pull ${img}
#     fi
# done

# configure the MySQL Database and load init data
MYSQL_HOST=127.0.0.1
MYSQL_PORT=3306
MYSQL_USER=root
MYSQL_PASSWORD=password
docker run -p ${MYSQL_HOST}:${MYSQL_PORT}:${MYSQL_PORT} --name airbyte-mysql -e MYSQL_ROOT_PASSWORD=${MYSQL_PASSWORD} -d mysql:${MYSQL_VERSION}

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
    bash run-ab-platform.sh &
}

cd /home/user/projects
start_airbyte_server

sleep 60

CONTAINER_ID=$(docker ps | grep "mysql:${MYSQL_VERSION}" | awk '{print $1}')
MYSQL_FILE=/home/user/mysql_init.sql
MYSQL_CONTAINER_FILE=/home/mysql_init.sql
docker cp ${MYSQL_FILE} ${CONTAINER_ID}:${MYSQL_CONTAINER_FILE}
docker exec ${CONTAINER_ID} bash -c "mysql -u${MYSQL_USER} -p${MYSQL_PASSWORD} <${MYSQL_CONTAINER_FILE}"
rm -rf ${MYSQL_FILE}