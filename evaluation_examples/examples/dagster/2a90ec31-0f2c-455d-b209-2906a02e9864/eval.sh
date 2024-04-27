#!/bin/bash

cd /home/user/Downloads
source /home/user/anaconda3/etc/profile.d/conda.sh
conda activate dagster

# check if the file env.txt contains 
# DBT_CLOUD_ACCOUNT_ID=222333
# DBT_CLOUD_API_TOKEN=dbtu_ArB_FhZgqoH2P7T8SxdRoXhiNucYJK1q7Fj5nk7CiqJSee6zTA

if [ cat env.txt | grep "DBT_CLOUD_ACCOUNT_ID=222333" ]; then
    echo "Check environment variable DBT_CLOUD_ACCOUNT_ID succeeded"
else
    echo "Check environment variable DBT_CLOUD_ACCOUNT_ID failed"
    exit 0
fi

if [ cat env.txt | grep "DBT_CLOUD_API_TOKEN=dbtu_ArB_FhZgqoH2P7T8SxdRoXhiNucYJK1q7Fj5nk7CiqJSee6zTA" ]; then
    echo "Check environment variable DBT_CLOUD_API_TOKEN succeeded"
else
    echo "Check environment variable DBT_CLOUD_API_TOKEN failed"
    exit 0
fi