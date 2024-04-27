#!/bin/bash

function to_ready_state(){
    cd /home/user/projects/Project # Change the current directory to the project directory     
    # Initialize and activate the Astro environment for the Airflow project
    astro dev init
    astro dev start >/dev/null 2>&1
}
to_ready_state