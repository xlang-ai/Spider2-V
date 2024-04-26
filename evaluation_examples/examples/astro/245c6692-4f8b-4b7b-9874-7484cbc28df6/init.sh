#!/bin/bash

function to_ready_state(){
    cd /home/user/projects
    mv /home/user/task_today.zip .
    chmod a+x task_today.zip  
    unzip -q task_today.zip  
    rm -rf task_today.zip 
    cd /home/user/projects/task_today
    echo -e "y\n" | astro dev init
    rm -rf /home/user/projects/task_today/dags/exampledag.py
    sed -i "s/astro-runtime:.*$/astro-runtime:${ASTRO_RUNTIME_VERSION}/" Dockerfile
    code --user-data-dir=/home/user/projects/task_today
    astro dev start >/dev/null 2>&1
    wait
}
to_ready_state

code /home/user/projects/task_today/dags/task_today.py
code /home/user/projects/task_today/README.md