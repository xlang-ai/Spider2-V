#!/bin/bash

exec 1>/dev/null
exec 2>/dev/null

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
    code /home/user/projects/SQL_Check
    astro dev start --no-browser
    wait
}
to_ready_state

gnome-terminal --working-directory=/home/user/Downloads
gnome-terminal --working-directory=/home/user/projects/SQL_Check
code /home/user/projects/SQL_Check/dags/SQL_Check.py
code /home/user/projects/SQL_Check/include/custom_check.sql
code /home/user/projects/SQL_Check/README.md