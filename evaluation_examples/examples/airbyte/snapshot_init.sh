#!/bin/bash

exec 2>/dev/null

PASSWORD=password

source /home/user/anaconda3/etc/profile.d/conda.sh
conda create -n airbyte python=3.11 -y
conda activate airbyte
pip install dbt-snowflake==1.7.3 pytest==8.1.1 # for case 95ddd295-bb86-4f10-8d6b-6eb89ebb65cc
pip install data-diff==0.2.0 # for case 0fa19e8e-efba-42a6-8649-67ff203dbe87
pip install "pydantic>=1.10.15"
echo $PASSWORD | sudo -S apt-get install -y libpq-dev=9.0.0
pip install 'data-diff[postgresql]'
pip install 'data-diff[snowflake]'


VERSION=0.55.2 # $(awk -F'=' '/^VERSION=/ {print $2; exit}' run-ab-platform.sh)
POSTGRES_VERSION=12.6
ASTRO_RUNTIME_VERSION=10.5.0
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
    "quay.io/astronomer/astro-runtime:${ASTRO_RUNTIME_VERSION}"
    "airbyte/source-postgres:3.3.18"
    "airbyte/source-faker:6.0.3"
    "airbyte/source-bigquery:0.4.2"
    "airbyte/source-slack:0.4.0"
    "airbyte/source-github:1.7.0"
    "airbyte/source-mysql:3.3.13"
    "airbyte/source-file:0.5.0"
    "airbyte/source-snowflake:0.3.1"
    "airbyte/destination-csv:1.0.0"
    "airbyte/destination-sqlite:0.1.0"
    "airbyte/destination-local-json:0.2.11"
    "airbyte/destination-postgres:2.0.4"
    "airbyte/destination-snowflake:3.6.4"
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

# airflow related tool astro-cli install
ASTRO_CLI_VERSION=1.25.0
astro version | grep "1\.25\.0"
if [ $? -ne 0 ]; then
    echo $PASSWORD | sudo -S bash -c "curl -sSL install.astronomer.io | bash -s -- v${ASTRO_CLI_VERSION} >/dev/null 2>&1"
fi

# for 52f71f15-b156-4ad7-b342-97a8a5926e25
source /home/user/anaconda3/etc/profile.d/conda.sh
conda create -n superset python=3.11 -y
conda activate superset

function install_superset() {
    mkdir -p /home/user/projects && cd /home/user/projects
    git clone https://github.com/apache/superset.git
    cd superset
    # disable CSRF protection, secure cookie, and Talisman, to support easier evaluation
    touch docker/pythonpath_dev/superset_config_docker.py
    cat >> docker/pythonpath_dev/superset_config_docker.py <<EOF
SESSION_COOKIE_SAMESITE = None
SESSION_COOKIE_SECURE = False
SESSION_COOKIE_HTTPONLY = False
WTF_CSRF_ENABLED = False
TALISMAN_ENABLED = False
EOF
    # fix the version of the pre-downloaded docker images
    TAG=3.1.1
    REDIS_VERSION=7
    POSTGRES_VERSION=16-alpine
    echo "TAG=3.1.1" >> .env
    sed -i "s/image: redis:.*$/image: redis:${REDIS_VERSION}/" docker-compose-image-tag.yml
    sed -i "s/image: postgres:.*$/image: postgres:${POSTGRES_VERSION}/" docker-compose-image-tag.yml
    declare -a image_list=(
        "redis:${REDIS_VERSION}"
        "postgres:${POSTGRES_VERSION}"
        "apachesuperset.docker.scarf.sh/apache/superset:${TAG}"
    )
    images=$(docker images | awk 'NR > 1 {if ($2 == "latest") print $1; else print $1 ":" $2}')
    for img in ${image_list[@]}; do
        echo ${images} | grep -Fiq -- "$img"
        if [ $? -ne 0 ]; then
            docker pull ${img}
        fi
    done
}
install_superset

# for 85a356d4-448c-4894-8151-856428886e65
# 1. install JAVA, set JAVA_HOME
echo $PASSWORD | sudo -S apt-get update
echo $PASSWORD | sudo -S apt-get install -y default-jre default-jdk
JAVA_RUNTIME=$(readlink -f $(which java))
JAVA_HOME=$(dirname $(dirname $JAVA_RUNTIME))
export JAVA_HOME=$JAVA_HOME
echo "export JAVA_HOME=$JAVA_HOME" >> ~/.bashrc
echo $PASSWORD | sudo -S bash -c "echo 'export JAVA_HOME=$JAVA_HOME' >> /etc/environment" # may need to restart the system

# 2. set up metabase
mkdir -p /home/user/projects/metabase
cd /home/user/projects/metabase
wget -c https://downloads.metabase.com/v0.49.6/metabase.jar

# 336663dd-6fa8-44b9-8e12-6877bb5a120e
cd /home/user/projects
git clone https://github.com/OwenKephart/airbyte_demo.git
cd airbyte_demo
# change python file EventMetaData 
sed -i 's/EventMetadata/MetadataValue/g' /home/user/projects/airbyte/airbyte_demo/airbyte_demo/slack_github_analytics.py
pip install -e .