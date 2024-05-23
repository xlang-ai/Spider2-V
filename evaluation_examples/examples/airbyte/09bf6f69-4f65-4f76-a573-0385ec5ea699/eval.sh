#!/bin/bash
exec 2>/dev/null

file_path="/home/user/Desktop/airbyte_log.txt"

if [ -f "$file_path" ]; then
    echo "Downloading airbyte sync log, succeeded."
else
    echo "Downloading airbyte sync log, failed."
    exit 0
fi