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


name=Myannotation
username=superset
password=superset
host=db
port=5432
db_name=superset


annotation=$(curl -X GET "http://localhost:8088/api/v1/annotation_layer/" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer ${token}")
count=$(echo $annotation| jq -rM ".count")
flag=false

for (( i=0; i<$count ; i++ )) ; do
    annotation_name=$(echo $annotation | jq -rM ".result | .[${i}] | .name")
    if [ "$annotation_name" = "$name" ]; then
        flag=true
        table_id=$(echo $tables | jq -rM ".result | .[${i}] | .id")
	break
    fi
done

if [ $flag = true ]; then
    echo "Create annotation layer succeed"
else
    echo "Create annotation layer failed"
fi
