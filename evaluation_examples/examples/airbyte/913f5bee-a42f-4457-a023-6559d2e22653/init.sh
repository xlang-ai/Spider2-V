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
# conda create -n airbyte python=3.11 -y
# conda activate airbyte
# echo "source /home/user/anaconda3/etc/profile.d/conda.sh" >> ~/.bashrc
# echo "conda activate airbyte" >> ~/.bashrc
mkdir -p /home/user/projects

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

cd /home/user/projects
start_airbyte_server