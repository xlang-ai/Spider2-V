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


name=Mychart
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
    chart_name=$(echo $charts | jq -rM ".result | .[${i}] | .slice_name")
    # echo $chart_name
    # echo $name
    if [ "$chart_name" = "$name" ]; then
        flag=true
        echo 1
        chart_id=$(echo $charts | jq -rM ".result | .[${i}] | .id")
	break
    fi
done

if [ $flag = false ]; then
    echo "Table Visualization failed"
    exit 0
fi



infos=$(curl -X GET "http://localhost:8088/api/v1/chart/${chart_id}" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer ${token}")
    
params=$(echo "$infos" | jq -rM ".result | .params")

groupby=$(echo "$params" | jq -rM ".groupby" | jq -rM ".[0]")

metrics=$(echo "$params" | jq -rM ".metrics")
type=$(echo $metrics | jq -rM ".[0] | .label ")


if [ "$groupby" = "Department" ] && [ "$type" = "AVG(Cost)" ]; then
    echo "Table Visualization succeed"
else
    echo "Table Visualization failed"
fi
