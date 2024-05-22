#!/bin/bash

####################################################################################################
# Please ensure that Chromium or Chrome, VSCode and anaconda3 is installed on your system before running this script.
# The installed anaconda3 should be in the directory /home/user/anaconda3/.
# The raw data jaffle-shop-data.zip should be uploaded to the home directory before running this script.
# This script is tested on Ubuntu 22.04 LTS.
####################################################################################################

mkdir -p ~/.dbt
mkdir -p ~/projects

source /home/user/anaconda3/etc/profile.d/conda.sh
conda activate dbt

echo "source /home/user/anaconda3/etc/profile.d/conda.sh" >> ~/.bashrc
echo "conda activate dbt" >> ~/.bashrc

mv /home/user/jaffle-shop-data.zip /home/user/projects/
gnome-terminal --maximize --working-directory=/home/user/projects/
