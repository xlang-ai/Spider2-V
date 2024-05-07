#!/bin/bash

####################################################################################################
# Please ensure that Chromium or Chrome, VSCode, docker anaconda and astro cli are installed on your system before running this script.
# The installed anaconda3 should be in the directory /home/user/anaconda3/.
# Docker engine is installed following official docs: https://docs.docker.com/engine/install/ubuntu/
# Docker version 26.0.0
# The current user should be added into group docker.
# This script is tested on Ubuntu 22.04.4 LTS.
####################################################################################################

mkdir -p ~/projects
PASSWORD=password

source /home/user/anaconda3/etc/profile.d/conda.sh  
conda create -n airflow python=3.11 -y >/dev/null 2>&1  
conda activate airflow

pip install apache-airflow==2.9.0

ASTRO_CLI_VERSION=1.25.0
echo $PASSWORD | sudo -S bash -c "curl -sSL install.astronomer.io | bash -s -- v${ASTRO_CLI_VERSION} >/dev/null 2>&1"

ASTRO_RUNTIME_VERSION=10.5.0
# it seems astro is stubbornly using this old postgres image version
POSTGRES_VERSION=12.6

declare -a image_list=(
    "quay.io/astronomer/astro-runtime:${ASTRO_RUNTIME_VERSION}"
    "postgres:${POSTGRES_VERSION}"
)
images=$(docker images | awk 'NR > 1 {if ($2 == "latest") print $1; else print $1 ":" $2}')
for img in ${image_list[@]}; do
    echo ${images} | grep -Fiq -- "$img"
    if [ $? -ne 0 ]; then
        docker pull ${img} >/dev/null 2>&1
    fi
done

function install_postgres() {
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
    echo $PASSWORD | sudo -S bash -c "echo \"host    all             all             172.16.0.0/14           scram-sha-256\" >> ${hba_file}"
    sudo systemctl restart postgresql
    sudo systemctl enable postgresql
}
install_postgres