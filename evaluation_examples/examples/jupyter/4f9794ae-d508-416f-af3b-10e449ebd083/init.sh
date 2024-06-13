#!/bin/bash

####################################################################################################
# Please ensure that Chromium or Chrome, VSCode, docker and anaconda3 is installed on your system before running this script.
# The installed anaconda3 should be in the directory /home/user/anaconda3/.
# Some images should be pre-downloaded in VM snapshots to accelerate the process.
# Please ensure the initial project is copied to the home directory.
# This script is tested on Ubuntu 22.04 LTS.
####################################################################################################

# ignore all output and error
exec 1>/dev/null
exec 2>/dev/null

source /home/user/anaconda3/etc/profile.d/conda.sh
conda activate jupyter
echo "source /home/user/anaconda3/etc/profile.d/conda.sh" >> ~/.bashrc
echo "conda activate jupyter" >> ~/.bashrc

cd /home/user/Downloads
unzip sports.zip
rm -rf sports.zip
# pip install -r requirements.txt # have been installed in snapshot_init.sh
python -m ipykernel install --user --name jupyterlab --display-name "Python (jupyterlab)"
