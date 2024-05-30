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


slicename=rolling_mean
name=flights
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
    chart_name=$(echo $charts | jq -rM ".result | .[${i}] | .datasource_name_text")
    slice_name=$(echo $charts | jq -rM ".result | .[${i}] | .slice_name")
    # echo $slice_name
    # echo $chart_name
    if [ "$chart_name" = "$name" ] && [ "$slice_name" = "$slicename" ]; then
        flag=true
        chart_id=$(echo $charts | jq -rM ".result | .[${i}] | .id")
	break
    fi
done

if [ $flag = false ]; then
    echo "Create rolling mean linechart failed"
    exit 0
fi



infos=$(curl -X GET "http://localhost:8088/api/v1/chart/${chart_id}" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer ${token}")
    
params=$(echo "$infos" | jq -rM ".result | .params")

groupby=$(echo "$params" | jq -rM ".groupby" | jq -rM ".[0]")

metrics=$(echo "$params" | jq -rM ".metrics")
type=$(echo $metrics | jq -rM ".[0] | .label ")

x_name=$(echo $params | jq -rM .x_axis)
y_name=$(echo $params | jq -rM ".metrics | .[0] | .column | .column_name")

rolling_type=$(echo $params | jq -rM .rolling_type)
rolling_periods=$(echo $params | jq -rM .rolling_periods)

if [ "$x_name" = "Travel Date" ] && [ "$y_name" = "Cost" ]&& [ "$rolling_type" = "mean" ] && [ "$rolling_periods" = "7" ] && [ "$type" = "AVG(Cost)" ]; then
    echo "Create rolling mean linechart succeed"
else
    echo "Create rolling mean linechart failed"
fi
