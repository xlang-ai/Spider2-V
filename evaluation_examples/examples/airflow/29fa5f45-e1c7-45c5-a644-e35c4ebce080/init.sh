#!/bin/bash

exec 1>/dev/null
exec 2>/dev/null

ASTRO_RUNTIME_VERSION=10.5.0

function to_ready_state(){
    echo "source /home/user/anaconda3/etc/profile.d/conda.sh" >> ~/.bashrc
    echo "conda activate airflow" >> ~/.bashrc
    mkdir -p /home/user/projects/astro_Project
    cd /home/user/projects/astro_Project # Change the current directory to the project directory
    echo "FROM quay.io/astronomer/astro-runtime:${ASTRO_RUNTIME_VERSION}" > Dockerfile
    gnome-terminal --maximize --working-directory=/home/user/projects/astro_Project # Open a new terminal window with the project directory as the working directory
}
to_ready_state
