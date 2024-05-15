#!/bin/bash

exec 2>/dev/null

# check whether adding data from postgres database succeeds
username=johnwilson@gmail.com
password=Spider2.0
session_id=$(curl -X POST http://localhost:3000/api/session -H 'Content-Type: application/json' -d "{\"username\": \"${username}\", \"password\": \"${password}\"}" | jq -rM .id)

if [ -n "$session_id" ] && [ "$session_id" != "null" ]; then
    echo "Login to metabase succeeds."
else
    echo "Login to metabase failed."
    exit 1
fi

output=$(curl -X GET http://localhost:3000/api/dashboard -H "X-Metabase-Session: ${session_id}" | jq -rM '.data')

count=$(echo $output | jq -rM 'length')
for (( i=0; i<$count; i++)); do
    db_info=$(echo $output | jq -rM ".[${i}]")
    name=$(echo $db_info | jq -rM ".name")
    
    if [ "$name" != "New Dashboard" ]; then
        echo "Creating dashboard failed."
        exit 1
    fi
done

output_2=$(curl -X GET http://localhost:3000/api/card -H "X-Metabase-Session: ${session_id}")

count_2=$(echo $output_2 | jq -rM 'length')
for (( i=0; i<$count_2; i++)); do
    db_info_2=$(echo $output_2 | jq -rM ".[${i}]")
    name_2=$(echo $db_info_2 | jq -rM ".name")
    echo "$name_2"
    
    if [ "$name_2" = "question1" ]; then
        echo "Creating dashboard with question succeeds."
        exit 0
    fi
done
echo "Creating dashboard with question failed."
exit 1
