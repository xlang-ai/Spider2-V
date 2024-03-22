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
mkdir -p ~/projects/ && cd ~/projects
source /home/user/anaconda3/etc/profile.d/conda.sh
conda create -n dagster python=3.11 -y
conda activate dagster
pip install dagster

# create the target dagster project
PROJECT_NAME=hacker_news
dagster project scaffold --name $PROJECT_NAME
cd $PROJECT_NAME
pip install -e ".[dev]"

# start dagster Web UI service
dagster dev -p 3000 &
sleep 5

echo "source /home/user/anaconda3/etc/profile.d/conda.sh" >> ~/.bashrc
echo "conda activate dagster" >> ~/.bashrc
gnome-terminal --maximize --working-directory=/home/user/projects/$PROJECT_NAME
code /home/user/projects/$PROJECT_NAME
code /home/user/projects/$PROJECT_NAME/$PROJECT_NAME/assets.py