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


name=games
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

database_name=$(echo $infos | jq -r '.result | .database | .database_name')

if [ "$database_name" != "Games" ]; then
    echo "Uploading CSV failed"
    exit 0
fi


charts=$(curl -X GET "http://localhost:8088/api/v1/chart/" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer ${token}")
count=$(echo $charts| jq -rM ".count")
flag=false

for (( i=0; i<$count ; i++ )) ; do
    chart_name=$(echo $charts | jq -rM ".result | .[${i}] | .datasource_name_text")
    slice_name=$(echo $charts | jq -rM ".result | .[${i}] | .slice_name")
    if [ "$chart_name" = "$name" ] && [ "$slice_name" = "$name" ]; then
        flag=true
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
dashboard_id=$(echo $params | jq -r ".dashboards | .[0]")

if [ "$groupby" != "genre" ] || [ "$type" != "MAX(global_sales)" ]; then
    echo "Creating chart failed"
    exit 0
fi



dashboards=$(curl -X GET "http://localhost:8088/api/v1/dashboard/${dashboard_id}" \
    -H 'accept: application/json' \
    -H "Authorization: Bearer ${token}")
dashboard_name=$(echo $dashboards | jq -rM ".result | .dashboard_title" )

if [ "$dashboard_name" = "MyDashboard" ]; then
    echo "Creating dashboard succeed"
else
    echo "Creating dashboard failed"
fi
