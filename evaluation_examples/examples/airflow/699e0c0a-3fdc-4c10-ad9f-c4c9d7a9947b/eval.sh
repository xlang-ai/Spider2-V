#!/bin/bash

source /home/user/anaconda3/etc/profile.d/conda.sh
conda activate astro
cd /home/user/projects/astro_Project

# Navigate to the project directory
cd ~/projects/astro_Project

if [ $? -ne 0 ]; then
    echo "Project directory navigation failed."
    exit 0
fi

# Check the existence of Airflow project
if ! test -f "$HOME/projects/astro_Project/airflow_settings.yaml"; then
    echo "Airflow project creation failed."
    exit 0
fi
echo "Airflow project creation succeed."

# Check if Airflow webserver is running on port 8002
output=$(docker ps | grep "airflow" | grep "8002")
if [ -n "$output" ]; then
    echo "Airflow webserver running on port 8002 succeed."
else
    echo "Airflow webserver running on port 8002 failed."
    exit 0
fi