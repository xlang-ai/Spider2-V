#!/bin/bash

exec 2>/dev/null

# create conda env for dagster
source /home/user/anaconda3/etc/profile.d/conda.sh
conda create -n dagster python=3.11 -y
conda activate dagster
pip install dagster==1.7.2 dagster-cloud==1.7.2 dagster-cloud-cli==1.7.2 dagster-graphql==1.7.2 dagster-pipes==1.7.2 dagster-webserver==1.7.2 pytest

# some ENV for dagster
mkdir -p /home/user/.dagster
touch /home/user/.dagster/dagster.yaml
echo "export DAGSTER_HOME=/home/user/.dagster" >> /home/user/.bashrc