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

output=$(curl -X GET http://localhost:3000/api/database -H "X-Metabase-Session: ${session_id}" | jq -rM '.data')
count=$(echo $output | jq -rM 'length')
for (( i=0; i<$count; i++)); do
    db_info=$(echo $output | jq -rM ".[${i}]")
    name=$(echo $db_info | jq -rM ".name")
    details=$(echo $db_info | jq -rM ".details")
    unfolding=$(echo $details | jq -rM '.["json-unfolding"]')
    if [ "$name" = "PostgresData" ] && [ "$unfolding" = "false" ]; then
        echo "Toggling JSON unfolding succeeds."
        exit 0
    fi
done
echo "Toggling JSON unfolding failed."
exit 1
