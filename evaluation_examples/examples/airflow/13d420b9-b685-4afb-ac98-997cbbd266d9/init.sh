#!/bin/bash

function to_ready_state(){
    cd /home/user/projects
    yes | astro dev init 2>&1 
    astro dev start >/dev/null 2>&1 
    wait
}
to_ready_state


