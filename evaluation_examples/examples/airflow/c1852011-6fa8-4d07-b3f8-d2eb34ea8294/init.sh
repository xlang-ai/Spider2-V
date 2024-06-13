#!/bin/bash

exec 1>/dev/null
exec 2>/dev/null

ASTRO_RUNTIME_VERSION=10.5.0

function to_ready_state(){
    echo "source /home/user/anaconda3/etc/profile.d/conda.sh" >> ~/.bashrc
    echo "conda activate airflow" >> ~/.bashrc
    cd /home/user/projects
    mv /home/user/task_today.zip .
    chmod a+x task_today.zip  
    unzip -q task_today.zip  
    rm -rf task_today.zip 
    cd /home/user/projects/task_today
    echo -e "y\n" | astro dev init
    rm -rf /home/user/projects/task_today/dags/exampledag.py
    sed -i "s/astro-runtime:.*$/astro-runtime:${ASTRO_RUNTIME_VERSION}/" Dockerfile
    code /home/user/projects/task_today
    astro dev start --no-browser
    wait
}
to_ready_state

code /home/user/projects/task_today/dags/task_today.py
code /home/user/projects/task_today/README.md