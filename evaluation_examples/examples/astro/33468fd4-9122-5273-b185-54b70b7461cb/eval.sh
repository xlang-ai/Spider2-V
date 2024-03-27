#!/bin/bash

PASSWORD=password

# check whether the user is added into group docker
output=$(cat /etc/group | grep docker | grep $USER)
# cannot use groups or id command because the information is not updated immediately
if [ -n "$output" ]; then
    echo "Docker without sudo succeed"
else
    echo "Docker without sudo failed"
    exit 0
fi  

# check whether docker is successfully installed
output=$(sg docker -c "docker run hello-world" | grep "Hello from Docker!")
if [ -n "$output" ] ; then
    echo "Docker installation succeed"
else
    echo "Docker installation failed"
    exit 0
fi

# check auto-start of docker
output=$(echo $PASSWORD | sudo -S systemctl list-unit-files | grep enabled | grep docker)
if [ -n "$output" ] ; then
    echo "Docker auto-start succeed"
else
    echo "Docker auto-start failed"
    exit 0
fi

# check astro-cli
output=$(astro version | grep "Astro CLI Version:")
if [ -n "$output" ] ; then
    echo "Astro-CLI installation succeed"
else
    echo "Astro-CLI installation failed"
    exit 0
fi

# check whether postgresql is installed successfully and set auto-start
cd /home/
flag=$(echo $PASSWORD | sudo -S -u postgres psql -c "select version();" | grep "PostgreSQL")
if [ -n "$flag" ]; then
    echo "Postgresql installation succeed"
else
    echo "Postgresql installation failed"
    exit 0
fi
output=$(echo $PASSWORD | sudo -S systemctl status postgresql)
declare -a prompt_list=(
    "Loaded: loaded"
    "Active: active"
    "postgresql.service; enabled"
    "status=0/SUCCESS"
)
for prompt in "${prompt_list[@]}"; do
    if [[ ! ${output} == *"$prompt"* ]]; then
        echo "postgresql auto-start failed"
        exit 0
    fi
done
echo "postgresql auto-start succeed"