#!/bin/bash

function to_ready_state(){
    cd /home/user/projects
    mv /home/user/workFlow.zip .
    chmod a+x workFlow.zip  
    unzip -q workFlow.zip  
    rm -rf workFlow.zip 
    cd /home/user/projects/workFlow
    yes | astro dev init 2>&1 
    astro dev start >/dev/null 2>&1 
    wait
}
to_ready_state


