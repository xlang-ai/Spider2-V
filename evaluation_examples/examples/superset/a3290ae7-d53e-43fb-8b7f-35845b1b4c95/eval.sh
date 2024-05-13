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


name=annotation
username=superset
password=superset
host=db
port=5432
db_name=superset

tables=$(curl -X GET "http://localhost:8088/api/v1/dataset/" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer ${token}")
count=$(echo $tables| jq -rM ".count")
flag=false

for (( i=0; i<$count ; i++ )) ; do
    table_name=$(echo $tables | jq -rM ".result | .[${i}] | .table_name")
    if [ "$table_name" = "$name" ]; then
        flag=true
        table_id=$(echo $tables | jq -rM ".result | .[${i}] | .id")
	break
    fi
done

if [ $flag = false ]; then
    echo "Register table failed"
    exit 0
fi


infos=$(curl -X GET "http://localhost:8088/api/v1/dataset/${table_id}" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer ${token}")
    
main_dttm_col=$(echo "$infos" | jq -rM ".result | .main_dttm_col")

if [ "$main_dttm_col" = "start_dttm" ]; then
    echo "Register table succeed"
else
    echo "Register table failed"
fi
