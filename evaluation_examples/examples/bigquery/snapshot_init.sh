#!/bin/bash

exec 2>/dev/null

echo "password" | sudo -S apt install chromium-browser

source /home/user/anaconda3/etc/profile.d/conda.sh  
conda create -n bigquery python=3.11 -y >/dev/null 2>&1  
conda activate bigquery

pip install google-cloud-bigquery==3.21.0 pandas==2.2.2 db-dtypes==1.2.0
