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

VERSION=10.5.0
img=quay.io/astronomer/astro-runtime:${VERSION}
images=$(docker images | awk 'NR > 1 {if ($2 == "latest") print $1; else print $1 ":" $2}')
echo ${images} | grep -Fiq -- "$img"
if [ $? -ne 0 ]; then
    docker pull ${img} >/dev/null 2>&1
fi

VERSION=1.25.0
astro version | grep "$VERSION"
if [ $? -ne 0 ]; then
    echo $PASSWORD | sudo -S bash -c "curl -sSL install.astronomer.io | bash -s -- -v $VERSION" >/dev/null 2>&1
fi

function create_astro_env() {
    source /home/user/anaconda3/etc/profile.d/conda.sh
    conda create -n astro python=3.11 -y >/dev/null 2>&1
    conda activate astro
    echo "source /home/user/anaconda3/etc/profile.d/conda.sh" >> ~/.bashrc
    echo "conda activate astro" >> ~/.bashrc
}
create_astro_env

# Function to stop and remove Docker containers running on port 8002
# function stop_and_remove_containers() {
#     docker stop $(docker ps -q --filter "expose=8002")  # Stop containers running on port 8002
#     docker rm $(docker ps -q --filter "expose=8002")  # Remove containers running on port 8002
# }
# stop_and_remove_containers

function to_ready_state(){
    cd /home/user/projects/astro_Project # Change the current directory to the project directory
    gnome-terminal --maximize --working-directory=/home/user/projects/astro_Project # Open a new terminal window with the project directory as the working directory      
}
to_ready_state


