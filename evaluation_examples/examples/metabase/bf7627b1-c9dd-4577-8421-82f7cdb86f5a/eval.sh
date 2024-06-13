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

output=$(curl -X GET http://localhost:3000/api/database -H "X-Metabase-Session: ${session_id}" | jq -rM '.data')
count=$(echo $output | jq -rM 'length')

if [ $count -eq 0 ]; then
    echo "Deleting metabase sample database succeeds."
    exit 0
fi

echo "Deleting metabase sample database failed."
exit 1