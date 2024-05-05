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
conda activate dagster

mkdir -p ~/.dagster
mkdir -p ~/.dagster_cloud_cli
export DAGSTER_HOME=~/.dagster

echo "source /home/user/anaconda3/etc/profile.d/conda.sh" >> ~/.bashrc
echo "conda activate dagster" >> ~/.bashrc
echo "export DAGSTER_HOME=~/.dagster" >> ~/.bashrc