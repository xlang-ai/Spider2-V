#!/bin/bash

####################################################################################################
# Please ensure that Chromium or Chrome, VSCode and anaconda3 is installed on your system before running this script.
# The installed anaconda3 should be in the directory /home/user/anaconda3/.
# This script is tested on Ubuntu 22.04 LTS.
####################################################################################################

# ignore all output and error
exec 1>/dev/null
exec 2>/dev/null

# create conda environment and install dagster
source /home/user/anaconda3/etc/profile.d/conda.sh
conda activate dagster
echo "source /home/user/anaconda3/etc/profile.d/conda.sh" >> ~/.bashrc
echo "conda activate dagster" >> ~/.bashrc

PROJECT_NAME=dagster-proj
cd /home/user
unzip -q ${PROJECT_NAME}.zip
rm -f ${PROJECT_NAME}.zip
cd ${PROJECT_NAME}
gnome-terminal --maximize --working-directory=/home/user/${PROJECT_NAME}