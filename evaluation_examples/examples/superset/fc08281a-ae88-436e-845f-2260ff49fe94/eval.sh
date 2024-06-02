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


slicename=Mychart
username=superset
password=superset
host=db
port=5432
db_name=superset

charts=$(curl -X GET "http://localhost:8088/api/v1/chart/" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer ${token}")
count=$(echo $charts| jq -rM ".count")
flag=false

for (( i=0; i<$count ; i++ )) ; do
    # chart_name=$(echo $charts | jq -rM ".result | .[${i}] | .datasource_name_text")
    slice_name=$(echo $charts | jq -rM ".result | .[${i}] | .slice_name")
    # echo $slice_name
    # echo $chart_name
    if [ "$slice_name" = "$slicename" ]; then
        flag=true
        chart_id=$(echo $charts | jq -rM ".result | .[${i}] | .id")
	break
    fi
done



if [ $flag = false ]; then
    echo "Delete chart succeed"
else
    echo "Delete chart failed"
fi


