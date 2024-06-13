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
mv /home/user/jaffle_shop.zip .
unzip -q jaffle_shop.zip
mv jaffle_shop/profiles.yml ~/.dbt/
rm -f jaffle_shop.zip

gnome-terminal --maximize --working-directory=/home/user/projects/jaffle_shop
code /home/user/projects/jaffle_shop --disable-workspace-trust
