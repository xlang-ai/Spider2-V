#!/bin/bash

function to_ready_state(){
    cd /home/user/projects
    mv /home/user/workFlow.zip .
    chmod a+x workFlow.zip  
    unzip -q workFlow.zip  
    rm -rf workFlow.zip 
    cd /home/user/projects/workFlow
    echo -e "y\n" | astro dev init
    sed -i "s/astro-runtime:.*$/astro-runtime:${ASTRO_RUNTIME_VERSION}/" Dockerfile
    astro dev start --no-browser >/dev/null 2>&1
    wait
}
to_ready_state
