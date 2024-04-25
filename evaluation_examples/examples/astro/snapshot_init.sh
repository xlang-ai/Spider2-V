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
conda create -n astro python=3.11 -y >/dev/null 2>&1  
conda activate astro 

pip install apache-airflow

ASTRO_CLI_VERSION=1.25.0
echo $PASSWORD | sudo -S bash -c "curl -sSL install.astronomer.io | bash -s -- v${ASTRO_CLI_VERSION} >/dev/null 2>&1"
echo "source /home/user/anaconda3/etc/profile.d/conda.sh" >> ~/.bashrc  # Add the conda script to the .bashrc file for automatic activation
echo "conda activate astro" >> ~/.bashrc  # Add the activation command to the .bashrc file for automatic activation

ASTRO_RUNTIME_VERSION=10.5.0
POSTGRES_VERSION=16-alpine

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

