#!/bin/bash

exec 1>/dev/null
exec 2>/dev/null

ASTRO_RUNTIME_VERSION=10.5.0

function to_ready_state(){
    echo "source /home/user/anaconda3/etc/profile.d/conda.sh" >> ~/.bashrc
    echo "conda activate airflow" >> ~/.bashrc
    cd /home/user/projects
    mv /home/user/Dag_Explorer.zip .
    chmod a+x Dag_Explorer.zip  
    unzip -q Dag_Explorer.zip  
    rm -rf Dag_Explorer.zip 
    cd /home/user/projects/Dag_Explorer
    echo -e "y\n" | astro dev init
    rm -rf /home/user/projects/Dag_Explorer/dags/exampledag.py
    sed -i "s/astro-runtime:.*$/astro-runtime:${ASTRO_RUNTIME_VERSION}/" Dockerfile
    astro dev start --no-browser >/dev/null 2>&1
    wait
}
to_ready_state