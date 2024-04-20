#!/bin/bash

# ensure that no error information is output
exec 2>/dev/null

cd /home/user/Downloads

export TASK_ID_COLUMN=check_column
export TASK_ID_TABLE=check_table

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
if grep -q "All tests have passed" "${TASK_ID_COLUMN}.log"; then
    echo "check ${TASK_ID_COLUMN} succeed"
else
    echo "check ${TASK_ID_COLUMN} failed"
    exit 0
fi

# Extract "{TASK_ID_TABLE}.log" and check if it contains "All tests have passed"
if grep -q "All tests have passed" "${TASK_ID_TABLE}.log"; then
    echo "check ${TASK_ID_TABLE} succeed"
else
    echo "check ${TASK_ID_TABLE} failed"
    exit 0
fi

echo "All check succeed"

