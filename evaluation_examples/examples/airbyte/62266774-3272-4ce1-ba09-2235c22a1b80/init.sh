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
mkdir -p /home/user/projects
cd /home/user/projects
mv /home/user/ecommerce_analytics.zip .
unzip -q ecommerce_analytics.zip
rm -rf ecommerce_analytics.zip

function create_airbyte_env() {
    source /home/user/anaconda3/etc/profile.d/conda.sh
    conda create -n airbyte python=3.11 -y
    conda activate airbyte
    echo "source /home/user/anaconda3/etc/profile.d/conda.sh" >> ~/.bashrc
    echo "conda activate airbyte" >> ~/.bashrc
    pip install -e ".[dev]"
}
cd ecommerce_analytics/
create_airbyte_env

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

code /home/user/projects/ecommerce_analytics
gnome-terminal --maximize --working-directory=/home/user/projects/ecommerce_analytics
sleep 30 # waiting for server start
code /home/user/projects/ecommerce_analytics/README.md