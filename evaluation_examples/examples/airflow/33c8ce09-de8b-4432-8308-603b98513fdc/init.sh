#!/bin/bash

ASTRO_RUNTIME_VERSION=10.5.0

function to_ready_state(){
    echo "source /home/user/anaconda3/etc/profile.d/conda.sh" >> ~/.bashrc
    echo "conda activate airflow" >> ~/.bashrc
    cd /home/user/projects
    yes | astro dev init 2>&1 
    sed -i "s/astro-runtime:.*$/astro-runtime:${ASTRO_RUNTIME_VERSION}/" Dockerfile
    astro dev start >/dev/null 2>&1 
    wait
}
to_ready_state


