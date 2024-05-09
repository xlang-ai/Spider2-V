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


name=tutorial_flights
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
    echo "Uploading CSV failed"
    exit 0
fi


infos=$(curl -X GET "http://localhost:8088/api/v1/dataset/${table_id}" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer ${token}")
    
flag2=false
# 遍历result.columns数组
echo "$infos" | jq -r '.result.columns[] | @base64' | while read -r item; do
    # 对每个column对象执行操作
    column=$(echo "$item" | base64 --decode)
    column_name=$(echo "$column" | jq -r '.column_name')
    is_dttm=$(echo "$column" | jq -r '.is_dttm')

    if [ "$column_name" = "Travel Date" ] && [ "$is_dttm" = true ]; then
        flag2=true
    break
    fi
done

if [ $flag = true ]; then
    echo "Uploading CSV succeed"
else
    echo "Uploading CSV failed"
fi
