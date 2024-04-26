#!/bin/bash

function to_ready_state(){
    cd /home/user/projects
    mv /home/user/weather.zip .
    chmod a+x weather.zip  
    unzip -q weather.zip  
    rm -rf weather.zip 
    cd /home/user/projects/weather
    echo -e "y\n" | astro dev init
    sed -i "s/astro-runtime:.*$/astro-runtime:${ASTRO_RUNTIME_VERSION}/" Dockerfile
    astro dev start >/dev/null 2>&1
    wait
}
to_ready_state