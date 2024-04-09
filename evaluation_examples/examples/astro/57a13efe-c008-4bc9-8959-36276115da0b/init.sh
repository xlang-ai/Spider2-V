#!/bin/bash

####################################################################################################
# Please ensure that Chromium or Chrome, VSCode, docker and anaconda3 is installed on your system before running this script.
# The installed anaconda3 should be in the directory /home/user/anaconda3/.
# Docker engine is installed following official docs: https://docs.docker.com/engine/install/ubuntu/
# The current user should be added into group docker.
# This script is tested on Ubuntu 22.04.4 LTS.
####################################################################################################

# Create a directory for the project
mkdir -p ~/projects/Project

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
    cd /home/user/projects/Project # Change the current directory to the project directory     
    # Initialize and activate the Astro environment for the Airflow project
    astro dev init
    astro dev start >/dev/null 2>&1
    # TODO: Use Playwright to automatically fill in the username and password
}
to_ready_state

