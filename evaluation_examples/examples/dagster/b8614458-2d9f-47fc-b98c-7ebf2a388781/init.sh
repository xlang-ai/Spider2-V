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
cd /home/user
source /home/user/anaconda3/etc/profile.d/conda.sh
conda activate dagster
# pip install scikit-learn==1.4.2 # Uncomment this if you have not installed scikit-learn in your snapshot

cd /home/user
# create the target dagster project
PROJECT_NAME=hacker-news-ml-pipeline
unzip $PROJECT_NAME.zip
rm -f $PROJECT_NAME.zip
cd $PROJECT_NAME
code /home/user/$PROJECT_NAME

# start dagster Web UI service
function start_dagster_server() {
    export DAGSTER_HOME=/home/user/.dagster
    dagster dev -p 3000 >start_server.log 2>start_server.log &
    count=0
    while true; do
        sleep 2
        count=$(expr $count + 1)
        cat start_server.log | grep -i "Serving dagster-webserver on"
        if [ $? -eq 0 ]; then
            echo "The dagster server has been started"
            break
        fi
        if [ $count -gt 10 ]; then
            echo "The dagster server has not been started in 20 seconds"
            break
        fi
    done
}
start_dagster_server

code /home/user/$PROJECT_NAME
code /home/user/$PROJECT_NAME/hacker_news_ml_pipeline/assets.py
code /home/user/$PROJECT_NAME/README.md
echo "source /home/user/anaconda3/etc/profile.d/conda.sh" >> ~/.bashrc
echo "conda activate dagster" >> ~/.bashrc