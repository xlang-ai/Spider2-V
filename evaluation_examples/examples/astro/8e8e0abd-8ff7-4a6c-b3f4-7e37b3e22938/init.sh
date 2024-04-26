#!/bin/bash

mkdir -p ~/minio/data

docker run \
   -p 9000:9000 \
   -p 9001:9001 \
   --name minio \
   -v ~/minio/data:/data \
   -e "MINIO_ROOT_USER=ROOTNAME" \
   -e "MINIO_ROOT_PASSWORD=CHANGEME123" \
   quay.io/minio/minio server /data --console-address ":9001"


function to_ready_state(){
    cd /home/user/projects
    yes | astro dev init 2>&1 
    astro dev start >/dev/null 2>&1 
    wait
}
to_ready_state


