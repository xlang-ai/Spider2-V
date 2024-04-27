#!/bin/bash

function to_ready_state(){
    cd /home/user/projects/astro_Project # Change the current directory to the project directory
    echo "FROM quay.io/astronomer/astro-runtime:${ASTRO_RUNTIME_VERSION}" > Dockerfile
    gnome-terminal --maximize --working-directory=/home/user/projects/astro_Project # Open a new terminal window with the project directory as the working directory      
}
to_ready_state
