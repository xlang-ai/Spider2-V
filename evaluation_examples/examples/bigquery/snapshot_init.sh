#!/bin/bash

exec 2>/dev/null

echo "password" | sudo -S apt install chromium-browser

mkdir -p ~/projects/bigquery

source /home/user/anaconda3/etc/profile.d/conda.sh  
conda create -n bigquery python=3.11 -y >/dev/null 2>&1  
conda activate bigquery
pip install google-cloud-bigquery pandas db-dtypes