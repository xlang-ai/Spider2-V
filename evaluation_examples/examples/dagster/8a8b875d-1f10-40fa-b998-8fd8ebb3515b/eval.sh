#!/bin/bash
exec 2>/dev/null

PROJECT_NAME=file-ops-and-jobs

cd ~/$PROJECT_NAME
source /home/user/anaconda3/etc/profile.d/conda.sh
conda activate dagster

rm -rf $PROJECT_NAME/files
mkdir -p $PROJECT_NAME/files
echo "Hello World!" > $PROJECT_NAME/files/helloworld.txt
echo "Welcome to dagster!" > $PROJECT_NAME/files/welcome.txt
echo "This is the test for ops and jobs." > $PROJECT_NAME/files/ops_and_jobs.txt

pytest test_file_sizes_job.py

curl -s -o file_sizes_job.html http://localhost:3000/locations/__repository__file_sizes_job@file_sizes_job.py/jobs/file_sizes_job
if [ -s file_sizes_job.html ] ; then
    echo "Create dagster job succeeded"
else
    echo "Create dagster job failed"
    exit 0
fi