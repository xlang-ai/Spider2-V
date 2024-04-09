#!/bin/bash

cd ~/test-ops-and-jobs
source /home/user/anaconda3/etc/profile.d/conda.sh
conda activate dagster
pip install pytest > /dev/null

pytest test_file_sizes_job.py

curl -s -o file_sizes_job.html http://localhost:3000/locations/__repository__file_sizes_job@file_sizes_job.py/jobs/file_sizes_job
if [ -s file_sizes_job.html ] ; then
    echo "Create dagster job succeeded"
else
    echo "Create dagster job failed"
    exit 0
fi