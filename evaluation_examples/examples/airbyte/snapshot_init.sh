#!/bin/bash

exec 2>/dev/null

source /home/user/anaconda3/etc/profile.d/conda.sh
conda create -n airbyte python=3.11 -y
conda activate airbyte
pip install dbt-snowflake==1.7.3 pytest==8.1.1 # for case 95ddd295-bb86-4f10-8d6b-6eb89ebb65cc
pip install ...???... # for case 0fa19e8e-efba-42a6-8649-67ff203dbe87

VERSION=0.55.2 # $(awk -F'=' '/^VERSION=/ {print $2; exit}' run-ab-platform.sh)
POSTGRES_VERSION=16
MYSQL_VERSION=8
declare -a image_list=(
    "alpine/socat:1.8.0.0"
    "airbyte/init:${VERSION}"
    "airbyte/bootloader:${VERSION}"
    "airbyte/db:${VERSION}"
    "airbyte/worker:${VERSION}"
    "airbyte/server:${VERSION}"
    "airbyte/webapp:${VERSION}"
    "airbyte/temporal:${VERSION}"
    "airbyte/cron:${VERSION}"
    "airbyte/airbyte-api-server:${VERSION}"
    "airbyte/connector-builder-server:${VERSION}"
    "airbyte/proxy:${VERSION}"
    "postgres:${POSTGRES_VERSION}"
    "mysql:${MYSQL_VERSION}"
)
images=$(docker images | awk 'NR > 1 {if ($2 == "latest") print $1; else print $1 ":" $2}')
for img in ${image_list[@]}; do
    echo ${images} | grep -Fiq -- "$img"
    if [ $? -ne 0 ]; then
        docker pull ${img}
    fi
done

# download airbyte repository
mkdir -p /home/user/projects && cd /home/user/projects
git clone --depth=1 https://github.com/airbytehq/airbyte.git
cd airbyte
sed -i.bak "s/^VERSION=.*$/VERSION=${VERSION}/" run-ab-platform.sh
bash run-ab-platform.sh -d # only download dependency files
# remove airbyte basic auth, set username and password to empty ""
sed -i '/^BASIC_AUTH_USERNAME=/c\
BASIC_AUTH_USERNAME=""
' .env
sed -i '/^BASIC_AUTH_PASSWORD=/c\
BASIC_AUTH_PASSWORD=""
' .env