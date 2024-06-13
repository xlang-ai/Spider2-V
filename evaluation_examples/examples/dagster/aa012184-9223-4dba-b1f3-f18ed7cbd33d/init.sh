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

cd /home/user

PROJECT_NAME=file-ops-and-jobs

mkdir -p $PROJECT_NAME/files
code /home/user/$PROJECT_NAME
echo "Hello World!" > $PROJECT_NAME/files/helloworld.txt
echo "Welcome to dagster!" > $PROJECT_NAME/files/welcome.txt
echo "This is the test for ops and jobs." > $PROJECT_NAME/files/ops_and_jobs.txt

mv /home/user/README.md /home/user/$PROJECT_NAME/
code /home/user/$PROJECT_NAME/README.md
touch $PROJECT_NAME/file_sizes_job.py
code /home/user/$PROJECT_NAME/file_sizes_job.py

echo "source /home/user/anaconda3/etc/profile.d/conda.sh" >> ~/.bashrc
echo "conda activate dagster" >> ~/.bashrc