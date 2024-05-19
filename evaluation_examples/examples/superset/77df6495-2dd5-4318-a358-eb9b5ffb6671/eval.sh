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


name=flights
username=superset
password=superset
host=db
port=5432
db_name=superset

tables=$(curl -X GET "http://localhost:8088/api/v1/dataset/" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer ${token}")
count=$(echo $tables| jq -rM ".count")


for (( i=0; i<$count ; i++ )) ; do
    table_name=$(echo $tables | jq -rM ".result | .[${i}] | .table_name")
    if [ "$table_name" = "$name" ]; then
        flag=true
        table_id=$(echo $tables | jq -rM ".result | .[${i}] | .id")
	break
    fi
done



infos=$(curl -X GET "http://localhost:8088/api/v1/dataset/${table_id}" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer ${token}")
    
metrics=$(echo $infos | jq -rM ".result | .metrics")
columns=$(echo $infos | jq -rM ".result | .columns")

# Initialize the flag
flag1=false

# Read the metrics using process substitution to avoid subshell issues
while IFS= read -r metric; do
    # Extract and print each field
    id=$(echo "$metric" | jq -r '.id')
    metric_name=$(echo "$metric" | jq -r '.metric_name')
    expression=$(echo "$metric" | jq -r '.expression')
    verbose_name=$(echo "$metric" | jq -r '.verbose_name')
    # Check the condition and set the flag
    if [ "$metric_name" = "SumCost" ] && [ "$expression" = "SUM(\"Cost\")" ]; then
        flag1=true
        break
    fi
done < <(echo "$metrics" | jq -c '.[]')


if [ $flag1 = false ]; then
    echo "Add metric failed"
    exit 0
fi



# Initialize the flag
flag2=false

# Read the metrics using process substitution to avoid subshell issues
while IFS= read -r column; do
    # Extract and print each field
    id=$(echo "$column" | jq -r '.id')
    column_name=$(echo "$column" | jq -r '.column_name')
    expression=$(echo "$column" | jq -r '.expression')
    verbose_name=$(echo "$column" | jq -r '.verbose_name')
    # Check the condition and set the flag
    if [ "$column_name" = "IntCost" ] && [ "$expression" = "CAST(\"Cost\" as INTEGER)" ]; then
        flag2=true
        break
    fi
done < <(echo "$columns" | jq -c '.[]')


if [ $flag2 = true ]; then
    echo "Add semantic layer succeed"
else
    echo "Add semantic layer failed"
fi

