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


name=public.users
username=postgres
password=password
host=172.17.0.1
port=2000
db_name=data-db

charts=$(curl -X GET "http://localhost:8088/api/v1/chart/" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer ${token}")
count=$(echo ${charts}| jq -rM ".count")
flag=false

for (( i=0; i<${count} ; i++ )) ; do
    chart_name=$(echo ${charts} | jq -rM ".result | .[${i}] | .datasource_name_text")
    if [ "${chart_name}" = "${name}" ]; then
        flag=true
        chart_id=$(echo ${charts} | jq -rM ".result | .[${i}] | .id")
        echo "yes"
	break
    fi
done


if [ ${flag} = false ]; then
    echo "Table Visualization failed"
    exit 0
fi


infos=$(curl -X GET "http://localhost:8088/api/v1/chart/${chart_id}" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer ${token}")


params=$(echo ${infos} | jq -rM ".result | .params")
table_name=$(echo ${infos} | jq -rM ".result | .slice_name")
viz_type=$(echo ${params} | jq -rM ".viz_type")
metric=$(echo ${params} | jq -rM ".metric")
if [ "${table_name}" = "Users" ] && [ "${viz_type}" = "big_number_total" ] && [ "${metric}" = "count" ]; then
    echo "Table Visualization succeed"
else
    echo "Table Visualization failed"
fi