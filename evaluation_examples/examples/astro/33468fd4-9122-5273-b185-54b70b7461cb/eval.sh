#!/bin/bash

# check docker installed and add user into group docker
output=$(sg docker -c "docker run hello-world" | grep "Hello from Docker!")
if [ -n "$output" ] ; then
    echo "Docker without sudo succeed"
else
    echo "Docker without sudo failed"
    exit 0
fi

# check auto-start of docker
output=$(systemctl list-unit-files | grep enabled | grep docker)
if [ -n "$output" ] ; then
    echo "Docker auto-start succeed"
else
    echo "Docker auto-start failed"
fi
