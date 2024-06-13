#!/bin/bash

# ensure that no error information is output
exec 2>/dev/null

cd /home/user/Downloads

export TASK_ID_COLUMN=column_checks
export TASK_ID_TABLE=table_checks

# Check if "{TASK_ID_COLUMN}.log" exists
if [ -f "${TASK_ID_COLUMN}.log" ]; then
    echo "${TASK_ID_COLUMN} generation succeed"
else
    echo "${TASK_ID_COLUMN} generation failed"
fi

# Check if "{TASK_ID_TABLE}.log" exists

if [ -f "${TASK_ID_TABLE}.log" ]; then
    echo "${TASK_ID_TABLE} generation succeed"
else
    echo "${TASK_ID_TABLE} generation failed"
fi

# Extract "{TASK_ID_COLUMN}.log" and check if it contains "All tests have passed"
if cat ${TASK_ID_COLUMN}.log | grep -q "[('bird_name', 'null_check', 0), ('bird_name', 'distinct_check', 5), ('observation_year', 'min', 2018), ('observation_year', 'max', 2022), ('bird_happiness', 'min', 7), ('bird_happiness', 'max', 10)]" && cat ${TASK_ID_COLUMN}.log | grep -q "All tests have passed"; then
    echo "check ${TASK_ID_COLUMN} succeed"
else
    echo "check ${TASK_ID_COLUMN} failed"
    exit 0
fi

# Extract "{TASK_ID_TABLE}.log" and check if it contains "All tests have passed"
if cat ${TASK_ID_TABLE}.log | grep -q "[('average_happiness_check', 1)]" && cat ${TASK_ID_TABLE}.log | grep -q "All tests have passed"; then
    echo "check ${TASK_ID_TABLE} succeed"
else
    echo "check ${TASK_ID_TABLE} failed"
    exit 0
fi

echo "All check succeed"

