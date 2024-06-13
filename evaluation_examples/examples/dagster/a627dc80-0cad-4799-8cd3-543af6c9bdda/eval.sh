#!/bin/bash

# Define the base directory
BASE_DIR="/home/user/dagster-proj"

# Define the directories and files to check
DIRS=("dagster_proj" "dagster_proj_tests")
FILES=("pyproject.toml" "setup.cfg" "setup.py")

if [ ! -d "${BASE_DIR}" ]; then
    echo "Check project directory failed."
    exit 0
fi

contains_all=true
for dir in "${DIRS[@]}"; do
    if [ ! -d "${BASE_DIR}/${dir}" ]; then
        contains_all=false
    fi
done

if ${contains_all}; then
    echo "Check directories succeeded."
else
    echo "Check directories failed."
    exit 0
fi

contains_all=true
for file in "${FILES[@]}"; do
    if [ ! -f "${BASE_DIR}/${file}" ]; then
        contains_all=false
    fi
done

if ${contains_all}; then
    echo "Check files succeeded."
else
    echo "Check files failed."
    exit 0
fi