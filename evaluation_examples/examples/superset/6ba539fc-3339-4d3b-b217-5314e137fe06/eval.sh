#!/bin/bash

exec 2>/dev/null

# obtain token
token=$(curl -X POST "http://localhost:8088/api/v1/security/login" \
    -H "Content-Type: application/json" \
    -d '{
        "username": "admin",
        "password": "admin",
        "provider": "db"
    }' | jq -rM ".access_token")


name=SpiderDatabase
username=superset
password=superset
host=db
port=5432
db_name=superset
connections=$(curl -X GET "http://localhost:8088/api/v1/database/" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer ${token}")
count=$(echo $connections | jq -rM ".count")
flag=false
for (( i=0; i<$count ; i++ )) ; do
    conn_name=$(echo $connections | jq -rM ".result | .[${i}] | .database_name")
    if [ "$conn_name" = "$name" ]; then
	flag=true
	conn_id=$(echo $connections | jq -rM ".result | .[${i}] | .id")
	break
    fi
done
if [ $flag = false ]; then
    echo "Enable uploading failed"
    exit 0
fi

infos=$(curl -X GET "http://localhost:8088/api/v1/database/${conn_id}/connection" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer ${token}")

if [ $(echo $infos| jq '.result.allow_file_upload') = true ]; then
    echo "Enable uploading succeed"
else
    echo "Enable uploading failed"
fi
