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

source /home/user/anaconda3/etc/profile.d/conda.sh
conda create -n superset python=3.11 -y
conda activate superset
echo "source /home/user/anaconda3/etc/profile.d/conda.sh" >> ~/.bashrc
echo "conda activate superset" >> ~/.bashrc

# start superset local server using docker with fixed version
function start_superset_server() {
    git clone https://github.com/apache/superset.git
    cd superset
    export TAG=3.1.1
    echo "export TAG=3.1.1 >> /home/user/.bashrc"
    declare -a image_list=(
        "redis:7"
        "postgres:15"
        "apachesuperset.docker.scarf.sh/apache/superset:${TAG}"
    )
    images=$(docker images | awk 'NR > 1 {if ($2 == "latest") print $1; else print $1 ":" $2}')
    for img in ${image_list[@]}; do
        echo ${images} | grep -Fiq -- "$img"
        if [ $? -ne 0 ]; then
            docker pull ${img}
        fi
    done
    # docker compose -f docker-compose-image-tag.yml up > start_server.log &
    # while true; do
    #     sleep 3
    #     cat start_server.log | grep "Init Step 4/4"
    #     if [ $? -eq 0 ]; then
    #         # the server has been started
    #         break
    #     fi
    # done
}

mkdir -p /home/user/projects && cd /home/user/projects
start_superset_server # only pre-install docker images to save time
gnome-terminal --maximize --working-directory=/home/user/projects