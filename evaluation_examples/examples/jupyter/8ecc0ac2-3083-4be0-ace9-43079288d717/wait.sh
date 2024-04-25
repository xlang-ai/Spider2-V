#!/bin/bash

exec 2>/dev/null

source /home/user/anaconda3/etc/profile.d/conda.sh
conda activate jupyter
token=$(jupyter lab list | sed -n '2p' | sed 's/.*token=\([^ &]*\).*/\1/')

count=0
while true; do
    sleep 3
    status=$(curl -X GET http://localhost:8888/api/kernels -H "Authorization: token ${token}" | jq -rM ".[0].execution_state")
    if [ "${status}" = "idle" ]; then
        echo "JupyterLab is ready."
        exit 0
    fi
    count=$(expr $count + 1)
    if [ $count -gt 10 ]; then
        echo "JupyterLab is ${status} (not idle) after 30s."
        exit 1
    fi
done
