#!/bin/bash

####################################################################################################
# Please ensure that Chromium or Chrome, VSCode, docker anaconda and astro cli are installed on your system before running this script.
# The installed anaconda3 should be in the directory /home/user/anaconda3/.
# Docker engine is installed following official docs: https://docs.docker.com/engine/install/ubuntu/
# The current user should be added into group docker.
# This script is tested on Ubuntu 22.04.4 LTS.
####################################################################################################

# Create a directory for the project
mkdir -p ~/projects/astro_Project

# Set the password for sudo commands
PASSWORD=password

ASTRO_RUNTIME_VERSION=10.5.0
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


function create_astro_env() {
    source /home/user/anaconda3/etc/profile.d/conda.sh
    conda create -n astro python=3.11 -y >/dev/null 2>&1
    conda activate astro
    # ASTRO_CLI_VERSION=1.25.0
    # astro version | grep "$ASTRO_CLI_VERSION"
    # if [ $? -ne 0 ]; then
    #     echo $PASSWORD | sudo -S bash -c "curl -sSL install.astronomer.io | bash -s -- v$ASTRO_CLI_VERSION" >/dev/null 2>&1
    # fi
    echo "source /home/user/anaconda3/etc/profile.d/conda.sh" >> ~/.bashrc
    echo "conda activate astro" >> ~/.bashrc
}
create_astro_env


function to_ready_state(){
    cd /home/user/projects/astro_Project # Change the current directory to the project directory
    echo "FROM quay.io/astronomer/astro-runtime:${ASTRO_RUNTIME_VERSION}" > Dockerfile
    gnome-terminal --maximize --working-directory=/home/user/projects/astro_Project # Open a new terminal window with the project directory as the working directory      
}
to_ready_state
