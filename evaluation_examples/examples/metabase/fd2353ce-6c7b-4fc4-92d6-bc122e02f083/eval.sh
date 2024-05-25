#!/bin/bash

exec 2>/dev/null

username=johnwilson@gmail.com
password=Spider2.0
session_id=$(curl -X POST http://localhost:3000/api/session -H 'Content-Type: application/json' -d "{\"username\": \"${username}\", \"password\": \"${password}\"}" | jq -rM .id)

if [ -n "$session_id" ] && [ "$session_id" != "null" ]; then
    echo "Login to metabase succeeds."
else
    echo "Login to metabase failed."
    exit 1
fi

output=$(curl -s -X GET http://localhost:3000/api/api-key -H "X-Metabase-Session: ${session_id}")
api_key_count=$(echo $output | jq -rM "length")
api_key=$(echo $output | jq -rM ".[0]")
name=$(echo $api_key | jq -rM ".name")
group_id=$(echo $api_key | jq -rM ".group.id")
group_name=$(echo $api_key | jq -rM ".group.name")
if [ $api_key_count = 1 ] && [ $name = "main" ] && [ $group_id = 2 ] && [ $group_name = "Administrators" ]; then
    echo "Creating API key succeeds."
    exit 0
else
    echo "Creating API key failed."
    exit 1
fi
