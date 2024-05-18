#!/bin/bash

exec 2>/dev/null

username=johnwilson@outlook.com
password=Spider2.0
session_id=$(curl -X POST http://localhost:3000/api/session -H 'Content-Type: application/json' -d "{\"username\": \"${username}\", \"password\": \"${password}\"}" | jq -rM .id)

if [ -n "$session_id" ] && [ "$session_id" != "null" ]; then
    echo "Email updation succeeds."
else
    echo "Email updation failed."
    exit 1
fi
