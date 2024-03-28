#!/bin/bash

####################################################################################################
# Please ensure that Chromium or Chrome, VSCode, docker and anaconda3 is installed on your system before running this script.
# The installed anaconda3 should be in the directory /home/user/anaconda3/.
# Please ensure the initial project is copied to the home directory.
# This script is tested on Ubuntu 20.04 LTS.
####################################################################################################

# ignore all output and error
exec 1>/dev/null
exec 2>/dev/null

mkdir -p /home/user/projects
source /home/user/anaconda3/etc/profile.d/conda.sh
conda create -n airbyte python=3.11 -y
conda activate airbyte
echo "source /home/user/anaconda3/etc/profile.d/conda.sh" >> ~/.bashrc
echo "conda activate airbyte" >> ~/.bashrc

# download images are very slow, better pre-download them in VM snapshots
# VERSION=0.55.2
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

gnome-terminal --working-directory=/home/user/projects