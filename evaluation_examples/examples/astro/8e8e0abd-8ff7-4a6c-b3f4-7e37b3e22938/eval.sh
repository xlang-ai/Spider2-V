#!/bin/bash

source /home/user/anaconda3/etc/profile.d/conda.sh
#conda activate astro
cd /home/user/projects


if grep -E "MINIO_ACCESS_KEY|MINIO_SECRET_KEY|MINIO_IP" .env; then
    echo "Create connection succeed"
else
    echo "Create a connection failed"
    exit 0
fi