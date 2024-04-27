#!/bin/bash

ASTRO_RUNTIME_VERSION=10.5.0

function to_ready_state(){
    echo "source /home/user/anaconda3/etc/profile.d/conda.sh" >> ~/.bashrc
    echo "conda activate airflow" >> ~/.bashrc
    cd /home/user/projects
    mv /home/user/SQL_Check.zip .
    chmod a+x SQL_Check.zip  
    unzip -q SQL_Check.zip  
    rm -rf SQL_Check.zip 
    cd /home/user/projects/SQL_Check
    echo -e "y\n" | astro dev init
    rm -rf /home/user/projects/SQL_Check/dags/exampledag.py
    sed -i "s/astro-runtime:.*$/astro-runtime:${ASTRO_RUNTIME_VERSION}/" Dockerfile
    astro dev start >/dev/null 2>&1
    wait
}
to_ready_state

gnome-terminal --working-directory=/home/user/projects/SQL_Check
