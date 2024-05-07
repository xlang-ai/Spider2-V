#!/bin/bash

####################################################################################################
# Please ensure that Chromium or Chrome, VSCode and anaconda3 is installed on your system before running this script.
# The installed anaconda3 should be in the directory /home/user/anaconda3/.
# This script is tested on Ubuntu 22.04 LTS.
####################################################################################################

# ignore all output and error
exec 1>/dev/null
exec 2>/dev/null

PASSWORD=password

# create conda environment and install dagster
source /home/user/anaconda3/etc/profile.d/conda.sh
conda activate dagster

cd /home/user
# create the target dagster project
PROJECT_NAME=wikipediaPageViews
unzip $PROJECT_NAME.zip
rm -f $PROJECT_NAME.zip
cd $PROJECT_NAME
code /home/user/$PROJECT_NAME

echo $PASSWORD | sudo -S ls > /dev/null
sudo -S mysql < database_init.sql
rm -f database_init.sql

touch /tmp/sqlserver_query.sql

code /home/user/$PROJECT_NAME/dags/wikipediaPageViews.py
code /home/user/$PROJECT_NAME/README.md
code /home/user/$PROJECT_NAME/dagster_migration.py
echo "source /home/user/anaconda3/etc/profile.d/conda.sh" >> ~/.bashrc
echo "conda activate dagster" >> ~/.bashrc