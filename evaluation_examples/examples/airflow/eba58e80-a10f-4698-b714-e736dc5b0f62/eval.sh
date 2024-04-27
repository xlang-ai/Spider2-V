#!/bin/bash

# ensure that no error information is output
exec 2>/dev/null

cd /home/user/Downloads

export TASK_ID_CUSTOM=custom_happiness_check

# Check if "{TASK_ID_CUSTOM}.log" exists
if [ -f "${TASK_ID_CUSTOM}.log" ]; then
    echo "${TASK_ID_CUSTOM} generation succeed"
else
    echo "${TASK_ID_CUSTOM} generation failed"
fi

# Extract "{TASK_ID_CUSTOM}.log" and check if it contains "All tests have passed"
if grep -q "Marking task as SUCCESS." "${TASK_ID_CUSTOM}.log" && grep -q "dag_id=sql_data_quality" "${TASK_ID_CUSTOM}.log" && grep -q "task_id=custom_happiness_check" "${TASK_ID_CUSTOM}.log"; then
    echo "check ${TASK_ID_CUSTOM} succeed"
else
    echo "check ${TASK_ID_CUSTOM} failed"
    exit 0
fi

