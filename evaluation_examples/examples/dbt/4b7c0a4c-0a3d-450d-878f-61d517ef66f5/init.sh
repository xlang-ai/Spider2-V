#!/bin/bash

####################################################################################################
# Please ensure that Chromium or Chrome, VSCode and anaconda3 is installed on your system before running this script.
# The installed anaconda3 should be in the directory /home/user/anaconda3/.
# The dbt project jaffle_shop.zip should be uploaded to the home directory before running this script.
# This script is tested on Ubuntu 22.04 LTS.
####################################################################################################

mkdir -p ~/.dbt
mkdir -p ~/projects

source /home/user/anaconda3/etc/profile.d/conda.sh
conda activate dbt
echo "source /home/user/anaconda3/etc/profile.d/conda.sh" >> ~/.bashrc
echo "conda activate dbt" >> ~/.bashrc

cd /home/user/projects
mv /home/user/analytics.zip .
unzip -q analytics.zip
mv analytics/profiles.yml ~/.dbt/
rm -f analytics.zip
dbt build

gnome-terminal --maximize --working-directory=/home/user/projects/analytics
code /home/user/projects/analytics --disable-workspace-trust
