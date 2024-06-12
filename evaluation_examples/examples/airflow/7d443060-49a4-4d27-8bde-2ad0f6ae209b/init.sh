#!/bin/bash

exec 1>/dev/null
exec 2>/dev/null

ASTRO_RUNTIME_VERSION=10.5.0

function to_ready_state(){
    echo "source /home/user/anaconda3/etc/profile.d/conda.sh" >> ~/.bashrc
    echo "conda activate airflow" >> ~/.bashrc
    cd /home/user/projects
    mv /home/user/today_task.zip .
    chmod a+x today_task.zip  
    unzip -q today_task.zip  
    rm -rf today_task.zip 
    cd /home/user/projects/today_task
    echo -e "y\n" | astro dev init
    rm -rf /home/user/projects/today_task/dags/exampledag.py
    rm -rf /home/user/projects/today_task/tests/dags/test_dag_example.py
    sed -i "s/astro-runtime:.*$/astro-runtime:${ASTRO_RUNTIME_VERSION}/" Dockerfile
    code home/user/projects/today_task
    astro dev start --no-browser
    wait
}
to_ready_state

gnome-terminal --working-directory=/home/user/projects/today_task
code /home/user/projects/today_task/tests/dags/test_dag.py
code /home/user/projects/today_task/README.md
