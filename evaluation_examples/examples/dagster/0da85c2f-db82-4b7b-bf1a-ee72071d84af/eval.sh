#!/bin/bash

exec 2>/dev/null

PROJECT_NAME=sklearn-dagster

cd /home/user/$PROJECT_NAME
source /home/user/anaconda3/etc/profile.d/conda.sh
conda activate dagster

export DAGSTER_HOME=~/.dagster

# Extract the last run ID
run_id=$(dagster run list | grep -oP 'Run: \K.*' | head -n 1)

features_check=$(python -c "import pandas as pd; import pickle; f = open('/home/user/.dagster/storage/$run_id/get_features_from_train/result', 'rb'); df = pickle.load(f); print(set(df.columns) == {'Parch', 'Embarked', 'Name', 'Sex', 'Age', 'Fare'})")

if [ "$features_check" == "True" ]; then
    echo "Check features succeeded"
else
    echo "Check features failed"
    exit 0
fi

accuracy_check=$(python -c "import numpy as np; result = np.load('/home/user/.dagster/storage/$run_id/get_accuracy_score/result', allow_pickle=True); print(type(result) == float and result > 0 and result < 1)")

if [ "$accuracy_check" == "True" ]; then
    echo "Check accuracy score succeeded"
else
    echo "Check accuracy score failed"
    exit 0
fi

dagster schedule list | grep -v "dagster.code_server" > output.log
declare -a schedule_list=(
    "\[RUNNING\]"
    "Cron Schedule: 0 \* \* \* 1-5"
)
for schedule_info in "${schedule_list[@]}"; do
    flag=$(cat output.log | grep -i "${schedule_info}")
    if [ -z "$flag" ] ; then
        echo "Check schedule failed"
        exit 0
    fi
done
echo "Check schedule succeeded"
