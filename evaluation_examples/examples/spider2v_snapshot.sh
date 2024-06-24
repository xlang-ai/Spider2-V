#!/bin/bash

# This is the Shell script creating the snapshot from raw Ubuntu 22.04 LST image for Spider2-V dataset.
# Before running the following setup, please ensure that:
# 1. Chromium/Google Chrome is installed and can be started via chromium-browser or google-chrome command in the terminal.
# 2. Docker is installed and the current user is in the docker group. It is also configured to start on boot.
# 3. Anaconda3 is installed in the directory /home/user/anaconda3/ and has file path /home/user/anaconda3/etc/profile.d/conda.sh.
# 4. Visual Studio Code is installed and can be launched via `code` command in the terminal. Disable auto-update, auto-indent, auto-bracket and accept-suggestion functions.
# 5. Chromium/Chrome, gnome-terminal, Visual Studio Code and Libreoffice Calc have been added to the application menu bar.

exec 2>/dev/null

PASSWORD=password

# Docker images
AIRBYTE_VERSION=0.55.2
POSTGRES_VERSION=16-alpine
ASTRO_POSTGRES_VERSION=12.6
ASTRO_RUNTIME_VERSION=10.5.0
MYSQL_VERSION=8
REDIS_VERSION=7
SUPERSET_TAG=3.1.1
declare -a image_list=(
    "redis:${REDIS_VERSION}"
    "apachesuperset.docker.scarf.sh/apache/superset:${SUPERSET_TAG}"
    "quay.io/astronomer/astro-runtime:${ASTRO_RUNTIME_VERSION}"
    "postgres:${ASTRO_POSTGRES_VERSION}"
    "postgres:${POSTGRES_VERSION}"
    "mysql:${MYSQL_VERSION}"
    "alpine/socat:1.8.0.0"
    "airbyte/init:${AIRBYTE_VERSION}"
    "airbyte/bootloader:${AIRBYTE_VERSION}"
    "airbyte/db:${AIRBYTE_VERSION}"
    "airbyte/worker:${AIRBYTE_VERSION}"
    "airbyte/server:${AIRBYTE_VERSION}"
    "airbyte/webapp:${AIRBYTE_VERSION}"
    "airbyte/temporal:${AIRBYTE_VERSION}"
    "airbyte/cron:${AIRBYTE_VERSION}"
    "airbyte/airbyte-api-server:${AIRBYTE_VERSION}"
    "airbyte/connector-builder-server:${AIRBYTE_VERSION}"
    "airbyte/proxy:${AIRBYTE_VERSION}"
    "airbyte/source-postgres:3.3.18"
    "airbyte/source-faker:6.0.3"
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

# JAVA
function install_java() {
    echo $PASSWORD | sudo -S apt-get update
    echo $PASSWORD | sudo -S apt-get install -y default-jre default-jdk
    JAVA_RUNTIME=$(readlink -f $(which java))
    JAVA_HOME=$(dirname $(dirname $JAVA_RUNTIME))
    export JAVA_HOME=$JAVA_HOME
    echo "export JAVA_HOME=$JAVA_HOME" >> ~/.bashrc
    echo $PASSWORD | sudo -S bash -c "echo 'export JAVA_HOME=$JAVA_HOME' >> /etc/environment"
}
install_java

# Postgresql and MySQL
function install_postgresql() {
    echo $PASSWORD | sudo -S apt-get install postgresql postgresql-contrib -y >/dev/null 2>&1
    cd /home
    # allow connection from any IP (including docker container)
    config_file=$(echo $PASSWORD | sudo -S -u postgres psql -tc "SHOW config_file" | awk 'NR==1 {print $1}')
    echo $PASSWORD | sudo -S bash -c "echo \"listen_addresses = '*'\" >> ${config_file}"
    # change the default authentication method to scram-sha-256
    hba_file=$(echo $PASSWORD | sudo -S -u postgres psql -tc "SHOW hba_file" | awk 'NR==1 {print $1}')
    echo $PASSWORD | sudo -S cp ${hba_file} ${hba_file}.bak
    echo $PASSWORD | sudo -S bash -c "sudo sed -i 's/local[[:space:]]\+all[[:space:]]\+all[[:space:]]\+peer/local   all             all                                     scram-sha-256/' ${hba_file}"
    echo $PASSWORD | sudo -S bash -c "sudo sed -i 's/local[[:space:]]\+replication[[:space:]]\+all[[:space:]]\+peer/local   replication     all                                     scram-sha-256/' ${hba_file}"
    echo $PASSWORD | sudo -S bash -c "echo \"host    all             all             172.0.0.0/8             scram-sha-256\" >> ${hba_file}"
    sudo systemctl restart postgresql
    sudo systemctl enable postgresql
}
install_postgresql
function install_mysql() {
    echo $PASSWORD | sudo -S apt-get install -y pkg-config build-essential libmysqlclient-dev
    echo $PASSWORD | sudo -S apt-get install -y mysql-server=8.0.36-0ubuntu0.22.04.1
    sudo systemctl start mysql
    sudo systemctl enable mysql
}
install_mysql

# Conda Environments
source /home/user/anaconda3/etc/profile.d/conda.sh
mkdir -p /home/user/projects && cd /home/user/projects

# 1. Airbyte
function setup_airbyte() {
    conda create -n airbyte python=3.11 -y
    conda activate airbyte
    pip install dbt-snowflake==1.7.3 pytest==8.1.1 # for case 95ddd295-bb86-4f10-8d6b-6eb89ebb65cc
    pip install data-diff==0.2.0 # for case 0fa19e8e-efba-42a6-8649-67ff203dbe87
    pip install "pydantic>=1.10.15"
    echo $PASSWORD | sudo -S apt-get install -y libpq-dev
    pip install 'data-diff[postgresql]'
    pip install 'data-diff[snowflake]'
    # download airbyte repository
    git clone --depth=1 https://github.com/airbytehq/airbyte.git
    cd airbyte
    sed -i.bak "s/^VERSION=.*$/VERSION=${AIRBYTE_VERSION}/" run-ab-platform.sh
    bash run-ab-platform.sh -d # only download dependency files
    # remove airbyte basic auth, set username and password to empty ""
    sed -i '/^BASIC_AUTH_USERNAME=/c\
BASIC_AUTH_USERNAME=""
' .env
    sed -i '/^BASIC_AUTH_PASSWORD=/c\
BASIC_AUTH_PASSWORD=""
' .env
    conda deactivate
    # install octavia-cli
    cd /home/user/
    echo $PASSWORD | sudo -S apt-get install -y expect
    curl -o install.sh https://raw.githubusercontent.com/observablehq/airbyte/master/octavia-cli/install.sh
    expect -c '
set timeout -1
spawn bash install.sh
expect {
    "❓ - Allow Airbyte to collect telemetry to improve the CLI? (Y/n)" {
        send "Y\r"
        exp_continue
    }
    eof {
        puts "Installation complete."
    }
}
'
    rm -rf install.sh
}
setup_airbyte

# 2. Airflow
function setup_airflow() {
    ASTRO_CLI_VERSION=1.25.0
    astro version | grep "1\.25\.0"
    if [ $? -ne 0 ]; then
        echo $PASSWORD | sudo -S bash -c "curl -sSL install.astronomer.io | bash -s -- v${ASTRO_CLI_VERSION} >/dev/null 2>&1"
    fi
    conda create -n airflow python=3.11 -y >/dev/null 2>&1  
    conda activate airflow
    pip install apache-airflow==2.9.1 apache-airflow-providers-airbyte==3.8.0
    conda deactivate
    cd /home/user/projects
    mkdir -p airflow_temp && cd airflow_temp
    cat >> Dockerfile <<EOF
FROM quay.io/astronomer/astro-runtime:10.5.0
RUN python -m venv dbt_venv && source dbt_venv/bin/activate && \
pip install --no-cache-dir dbt-postgres==1.7.10 && deactivate
EOF
    touch packages.txt
    cat >> requirements.txt <<EOF
astronomer-cosmos==1.0.4
apache-airflow-providers-postgres==5.6.0
EOF
    docker build -t my-astro:1.0 .
    cd /home/user/projects
    rm -rf airflow_temp/
}
setup_airflow

# 3. BigQuery
function setup_bigquery() {
    conda create -n bigquery python=3.11 -y >/dev/null 2>&1  
    conda activate bigquery
    pip install google-cloud-bigquery==3.21.0 pandas==2.2.2 db-dtypes==1.2.0
    conda deactivate
}
setup_bigquery

# 4. Dagster
function setup_dagster() {
    conda create -n dagster python=3.11 -y >/dev/null 2>&1  
    conda activate dagster
    pip install dagster==1.7.2 dagster-cloud==1.7.2 dagster-cloud-cli==1.7.2 dagster-graphql==1.7.2 dagster-pipes==1.7.2 dagster-webserver==1.7.2 dagster-airflow==1.7.2 dagster-airbyte==0.23.2 dagster-dbt==0.23.2 dagster-duckdb==0.23.2 dagster-duckdb-pandas==0.23.2 duckdb==0.10.2 dbt-duckdb==1.7.4 pandas==2.0.3 pytest==8.2.0 pyarrow==16.0.0 apache-airflow==2.9.0 apache-airflow-providers-mysql==5.5.4 mysqlclient==2.2.4 scikit-learn==1.4.2 notebook==7.1.2 matplotlib==3.8.4 seaborn==0.13.2 scipy==1.13.0 dagstermill==0.23.2 'papermill-origami>=0.0.8'
    pip uninstall jwt
    pip install --force-reinstall PyJWT==2.8.0
    mkdir -p /home/user/.dagster
    touch /home/user/.dagster/dagster.yaml
    echo "export DAGSTER_HOME=/home/user/.dagster" >> /home/user/.bashrc
    conda deactivate
}
setup_dagster

# 5. dbt
function setup_dbt() {
    conda create -n dbt python=3.11 -y
    conda activate dbt
    pip install dbt-core==1.7.13 dbt-duckdb==1.7.4
    conda deactivate
}
setup_dbt

# 6. Jupyter
function setup_jupyter() {
    conda create -n jupyter python=3.11 -y
    conda activate jupyter
    pip install jupyter==1.0.0 jupyterlab==4.1.6 ipykernel==6.29.4 numpy==1.26.4 pandas==2.2.2 matplotlib==3.8.4 seaborn==0.13.2 scipy==1.13.0 scikit-learn==1.5.0
    jupyter notebook --generate-config
    jupyter lab --generate-config
    browser=$(which chromium-browser) # $(which google-chrome)
    echo "c.ServerApp.browser = '$browser'" >> /home/user/.jupyter/jupyter_notebook_config.py
    echo "c.ServerApp.browser = '$browser'" >> /home/user/.jupyter/jupyter_lab_config.py
    conda deactivate
}
setup_jupyter

# 7. Metabase
function setup_metabase() {
    mkdir -p /home/user/projects/metabase
    cd /home/user/projects/metabase
    wget -c https://downloads.metabase.com/v0.49.6/metabase.jar
    conda create -n metabase python=3.11 -y
    conda activate metabase
    conda deactivate
}
setup_metabase

# 8. Snowflake
function setup_snowflake() {
    conda create -n snowflake python=3.11 -y
    conda activate snowflake
    conda deactivate 
}
setup_snowflake

# 9. Superset
function setup_superset() {
    mkdir -p /home/user/projects && cd /home/user/projects
    # download the github repo to local folder
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
    echo "TAG=${SUPERSET_TAG}" >> .env
    sed -i "s/image: redis:.*$/image: redis:${REDIS_VERSION}/" docker-compose-image-tag.yml
    sed -i "s/image: postgres:.*$/image: postgres:${POSTGRES_VERSION}/" docker-compose-image-tag.yml
    # conda environment
    conda create -n superset python=3.11 -y
    conda activate superset
    conda deactivate 
}
setup_superset
