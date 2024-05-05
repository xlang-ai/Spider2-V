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

echo $PASSWORD | sudo -S apt install pkg-config build-essential libmysqlclient-dev -y
echo $PASSWORD | sudo -S apt install mysql-server=8.0.36-0ubuntu0.22.04.1 -y # Version may differ on other machines. Not tested.
echo $PASSWORD | sudo -S systemctl start mysql.service

# create conda environment and install dagster
source /home/user/anaconda3/etc/profile.d/conda.sh
conda activate dagster
pip install dagster-airflow==1.7.1 apache-airflow==2.9.0 apache-airflow-providers-mysql==5.5.4 mysqlclient==2.2.4

cd /home/user

mkdir -p ~/.dagster
export DAGSTER_HOME=~/.dagster

# create the target dagster project
PROJECT_NAME=wikipediaPageViews
unzip $PROJECT_NAME.zip
rm -f $PROJECT_NAME.zip
cd $PROJECT_NAME

echo $PASSWORD | sudo -S mysql < database_init.sql
rm -f database_init.sql

code /home/user/$PROJECT_NAME
code /home/user/$PROJECT_NAME/dags/wikipediaPageViews.py
code /home/user/$PROJECT_NAME/README.md
code /home/user/$PROJECT_NAME/dagster_migration.py
echo "source /home/user/anaconda3/etc/profile.d/conda.sh" >> ~/.bashrc
echo "conda activate dagster" >> ~/.bashrc