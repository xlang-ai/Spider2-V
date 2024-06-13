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

user_info=$(curl -s -X GET http://localhost:3000/api/user/current -H "X-Metabase-Session: ${session_id}")
first_name=$(echo $user_info | jq -rM ".first_name")
last_name=$(echo $user_info | jq -rM ".last_name")
is_active=$(echo $user_info | jq -rM ".is_active")
if [ "$first_name" != "John" ] || [ "$last_name" != "Wilson" ] || [ "$is_active" != "true" ]; then
    echo "Login setup to metabase failed."
    exit 1
fi

properties=$(curl -X GET http://localhost:3000/api/session/properties -H "X-Metabase-Session: ${session_id}")
site_locale=$(echo $properties | jq -rM '.["site-locale"]')
site_name=$(echo $properties | jq -rM '.["site-name"]')
if [ "$site_locale" != "en" ] || [ "$site_name" != "Google" ]; then
    echo "Login setup to metabase failed."
    exit 1
fi

settings=$(curl -X GET http://localhost:3000/api/setting -H "X-Metabase-Session: ${session_id}")
tracking=$(echo $settings | jq '.[] | select(.key == "anon-tracking-enabled") | .value')
if [ "$tracking" != "false" ] ; then
    echo "Allow anonymous tracking, failed."
    exit 1
fi

output=$(curl -X GET http://localhost:3000/api/database -H "X-Metabase-Session: ${session_id}" | jq -rM '.data')
count=$(echo $output | jq -rM 'length')
for (( i=0; i<$count; i++)); do
    db_info=$(echo $output | jq -rM ".[${i}]")
    name=$(echo $db_info | jq -rM ".name")
    db_name=$(echo $db_info | jq -rM ".details.dbname")
    db_port=$(echo $db_info | jq -rM ".details.port")
    db_host=$(echo $db_info | jq -rM ".details.host")
    db_user=$(echo $db_info | jq -rM ".details.user")
    db_engine=$(echo $db_info | jq -rM ".engine")
    is_sample=$(echo $db_info | jq -rM ".is_sample")
    if [ "$name" = "PostgresData" ] && [ "$db_name" = "metabase" ] && [ "$db_port" = "5432" ] && [ "$db_host" = "localhost" ] && [ "$db_user" = "user" ] && [ "$db_engine" = "postgres" ] && [ "$is_sample" = "false" ]; then
        echo "Adding data into metabase succeeds."
        exit 0
    fi
done
echo "Adding data into metabase failed."
exit 1
