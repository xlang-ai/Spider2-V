#!/bin/bash

####################################################################################################
# Please ensure that Chromium or Chrome, VSCode, docker anaconda and astro cli are installed on your system before running this script.
# The installed anaconda3 should be in the directory /home/user/anaconda3/.
# Docker engine is installed following official docs: https://docs.docker.com/engine/install/ubuntu/
# Docker version 26.0.0
# The current user should be added into group docker.
# This script is tested on Ubuntu 22.04.4 LTS.
####################################################################################################

# Create a directory for the project
mkdir -p ~/projects

# Set the password for sudo commands
PASSWORD=password

# Function to create an Astro environment using Conda
function create_astro_env() {
    source /home/user/anaconda3/etc/profile.d/conda.sh  # Load the conda script
    conda create -n astro python=3.11 -y >/dev/null 2>&1  # Create a new conda environment named "astro" with Python 3.11
    conda activate astro  # Activate the "astro" environment
    echo "source /home/user/anaconda3/etc/profile.d/conda.sh" >> ~/.bashrc  # Add the conda script to the .bashrc file for automatic activation
    echo "conda activate astro" >> ~/.bashrc  # Add the activation command to the .bashrc file for automatic activation
}
create_astro_env

function to_ready_state(){
    cd /home/user/projects
    mv /home/user/workFlow.zip .
    chmod a+x workFlow.zip  
    unzip -q workFlow.zip  
    rm -rf workFlow.zip 
    cd /home/user/projects/workFlow
    yes | astro dev init 2>&1 
    astro dev start >/dev/null 2>&1 
    wait
}
to_ready_state


