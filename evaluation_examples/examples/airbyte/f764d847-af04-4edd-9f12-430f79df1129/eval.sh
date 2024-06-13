#!/bin/bash
exec 2>/dev/null

file_path="/home/user/Desktop/airbyte_log.txt"

KEYWORDS=("START CHECK" "END CHECK" "START REPLICATION" "END REPLICATION")
for keyword in "${KEYWORDS[@]}"; do
    if ! grep -q "$keyword" "${file_path}"; then
        echo "keyword found: ${keyword}, failed."
        exit 1
    fi
done

if [ -f "$file_path" ]; then
    echo "Downloading airbyte sync log, succeeded."
else
    echo "Downloading airbyte sync log, failed."
    exit 0
fi