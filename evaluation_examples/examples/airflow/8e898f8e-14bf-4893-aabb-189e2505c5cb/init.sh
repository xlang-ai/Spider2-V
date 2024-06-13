#!/bin/bash

exec 1>/dev/null
exec 2>/dev/null

ASTRO_RUNTIME_VERSION=10.5.0

function to_ready_state(){
    echo "source /home/user/anaconda3/etc/profile.d/conda.sh" >> ~/.bashrc
    echo "conda activate airflow" >> ~/.bashrc
    cd /home/user/projects
    mv /home/user/weather.zip .
    chmod a+x weather.zip  
    unzip -q weather.zip  
    rm -rf weather.zip 
    cd /home/user/projects/weather
    echo -e "y\n" | astro dev init
    sed -i "s/astro-runtime:.*$/astro-runtime:${ASTRO_RUNTIME_VERSION}/" Dockerfile
    astro dev start --no-browser
    wait
}
to_ready_state