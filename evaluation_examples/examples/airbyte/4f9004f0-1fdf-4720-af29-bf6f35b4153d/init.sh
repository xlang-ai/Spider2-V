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
conda activate airbyte
echo "source /home/user/anaconda3/etc/profile.d/conda.sh" >> ~/.bashrc
echo "conda activate airbyte" >> ~/.bashrc

cd /home/user/projects
mv /home/user/ecommerce_analytics.zip .
unzip -q ecommerce_analytics.zip
rm -rf ecommerce_analytics.zip
cd ecommerce_analytics/
# pip install -e ".[dev]" # should be installed in the snapshot
code /home/user/projects/ecommerce_analytics

function start_airbyte_server() {
    cd /home/user/projects/airbyte
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
start_airbyte_server

# write environment variables
keyfile_path=/home/user/keyfile.json
SNOWFLAKE_HOST=$(cat ${keyfile_path} | jq -rM ".account")
SNOWFLAKE_ACCOUNT=$(echo $SNOWFLAKE_HOST | grep -oP 'https://\K[^/]+(?=\.snowflakecomputing)')
SNOWFLAKE_USER=$(cat ${keyfile_path} | jq -rM ".user")
SNOWFLAKE_PASSWORD=$(cat ${keyfile_path} | jq -rM ".password")
echo "export SNOWFLAKE_HOST=${SNOWFLAKE_HOST}" >> /home/user/.bashrc
echo "export SNOWFLAKE_ACCOUNT=${SNOWFLAKE_ACCOUNT}" >> /home/user/.bashrc
echo "export SNOWFLAKE_USER=${SNOWFLAKE_USER}" >> /home/user/.bashrc
echo "export SNOWFLAKE_PASSWORD=${SNOWFLAKE_PASSWORD}" >> /home/user/.bashrc
rm -rf ${keyfile_path}

gnome-terminal --maximize --working-directory=/home/user/projects/ecommerce_analytics
code /home/user/projects/ecommerce_analytics/README.md