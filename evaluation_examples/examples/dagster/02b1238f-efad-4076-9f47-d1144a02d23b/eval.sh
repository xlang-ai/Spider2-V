#!/bin/bash

exec 2>/dev/null

PROJECT_NAME=iris-classification

cd /home/user/$PROJECT_NAME
source /home/user/anaconda3/etc/profile.d/conda.sh
conda activate dagster

export DAGSTER_HOME=~/.dagster

python -c "
import numpy as np
labels = np.load('labels.npy')
if np.all(np.isin(labels, [0, 1, 2])):
    print('Check classification result succeeded')
else:
    print('Check classification result failed')"

dagster asset materialize --select iris_kmeans_notebook -m iris_classification > output.log 2>&1
flag=$(cat output.log | grep -i "RUN_SUCCESS")
if [ -n "$flag" ]; then
    echo "Check asset materialization succeeded"
else
    echo "Check asset materialization failed"
    exit 0
fi