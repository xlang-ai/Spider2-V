#!/bin/bash

function to_ready_state(){
    cd /home/user/projects
    mv /home/user/weather.zip .
    chmod a+x weather.zip  
    unzip -q weather.zip  
    rm -rf weather.zip 
    cd /home/user/projects/weather
    echo -e "y\n" | astro dev init
    rm -rf /home/user/projects/weather/dags/exampledag.py
    sed -i "s/astro-runtime:.*$/astro-runtime:${ASTRO_RUNTIME_VERSION}/" Dockerfile
    code --user-data-dir=/home/user/projects/weather
    astro dev start --no-browser >/dev/null 2>&1
    wait
}
to_ready_state

gnome-terminal --working-directory=/home/user/projects/weather
code /home/user/projects/weather/plugins/my_extra_link_plugin.py
code /home/user/projects/weather/README.md