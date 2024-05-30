#!/bin/bash

ASTRO_RUNTIME_VERSION=10.5.0

function to_ready_state(){
    echo "source /home/user/anaconda3/etc/profile.d/conda.sh" >> ~/.bashrc
    echo "conda activate airflow" >> ~/.bashrc
    cd /home/user/projects
    mv /home/user/mlflow.zip .
    chmod a+x mlflow.zip  
    unzip -q mlflow.zip  
    rm -rf mlflow.zip 
    cd /home/user/projects/mlflow
    echo -e "y\n" | astro dev init
    rm -rf /home/user/projects/mlflow/dags/exampledag.py
    sed -i "s/astro-runtime:.*$/astro-runtime:${ASTRO_RUNTIME_VERSION}/" Dockerfile
    code /home/user/projects/mlflow
    astro dev start --no-browser >/dev/null 2>&1
    wait
}
to_ready_state

gnome-terminal --working-directory=/home/user/projects/mlflow
code /home/user/projects/mlflow/dags/train.py