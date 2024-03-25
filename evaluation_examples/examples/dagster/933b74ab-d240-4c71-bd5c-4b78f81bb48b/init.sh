#!/bin/bash

####################################################################################################
# Please ensure that Chromium or Chrome, VSCode and anaconda3 is installed on your system before running this script.
# The installed anaconda3 should be in the directory /home/user/anaconda3/.
# Please ensure the initial project is copied to the home directory.
# This script is tested on Ubuntu 20.04 LTS.
####################################################################################################

# ignore all output and error
exec 1>/dev/null
exec 2>/dev/null

# create conda environment and install dagster
mkdir -p /home/user/.dagster
touch /home/user/.dagster/dagster.yaml
export DAGSTER_HOME=/home/user/.dagster
echo "export DAGSTER_HOME=/home/user/.dagster" >> /home/user/.bashrc
mkdir -p ~/projects/ && cd ~/projects
source /home/user/anaconda3/etc/profile.d/conda.sh
conda create -n dagster python=3.11 -y
conda activate dagster
pip install dagster

# unzip the initial dagster project
PROJECT_NAME=hacker_news
cp /home/user/${PROJECT_NAME}.zip .
unzip -q ${PROJECT_NAME}.zip
rm -f ${PROJECT_NAME}.zip
cd ${PROJECT_NAME}
pip install -e ".[dev]"

# start dagster Web UI service
dagster dev -p 3000 &
sleep 5

code /home/user/projects/$PROJECT_NAME
echo "source /home/user/anaconda3/etc/profile.d/conda.sh" >> ~/.bashrc
echo "conda activate dagster" >> ~/.bashrc
gnome-terminal --maximize --working-directory=/home/user/projects/$PROJECT_NAME
code /home/user/projects/$PROJECT_NAME/$PROJECT_NAME/__init__.py
code /home/user/projects/$PROJECT_NAME/$PROJECT_NAME/assets.py