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

group_info=$(curl -s -X GET http://localhost:3000/api/permissions/group/3 -H "X-Metabase-Session: ${session_id}")
name=$(echo $group_info | jq -rM ".name")
members=$(echo $group_info | jq -rM ".members")
members_count=$(echo $members | jq -rM "length")
member=$(echo $members | jq -rM ".[0]")
first_name=$(echo $member | jq -rM ".first_name")
last_name=$(echo $member | jq -rM ".last_name")
email=$(echo $member | jq -rM ".email")
if [ "$name" = "Project Users" ] && [ $members_count = 1 ] && [ $first_name = "John" ] && [ $last_name = "Wilson" ] && [ $email = "johnwilson@gmail.com" ]; then
    echo "Adding people to the group succeeds."
    exit 0
else
    echo "Adding people to the group failed."
    exit 1
fi
