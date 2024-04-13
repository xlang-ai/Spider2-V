#!/bin/bash

####################################################################################################
# Please ensure that Chromium or Chrome, VSCode and anaconda3 is installed on your system before running this script.
# The installed anaconda3 should be in the directory /home/user/anaconda3/.
# This script is tested on Ubuntu 20.04 LTS.
####################################################################################################

# ignore all output and error
exec 1>/dev/null
exec 2>/dev/null

# create conda environment and install dagster
cd /home/user
source /home/user/anaconda3/etc/profile.d/conda.sh
# conda create -n dagster python=3.11 -y
conda activate dagster
# pip install dagster
pip install dagster-webserver
# Please uncomment the above two lines if you want to install dagster in a new conda environment.

mkdir -p ~/.dagster
export DAGSTER_HOME=~/.dagster
# create the target dagster project
PROJECT_NAME=harry-potter-potions
dagster project scaffold --name $PROJECT_NAME
mkdir -p $PROJECT_NAME/data
cd $PROJECT_NAME
pip install -e ".[dev]"

# start dagster Web UI service
dagster dev -p 3000 &
sleep 5

code /home/user/$PROJECT_NAME
echo "source /home/user/anaconda3/etc/profile.d/conda.sh" >> ~/.bashrc
echo "conda activate dagster" >> ~/.bashrc
echo "export DAGSTER_HOME=~/.dagster" >> ~/.bashrc
code /home/user/$PROJECT_NAME/harry_potter_potions_tests/test_assets.py