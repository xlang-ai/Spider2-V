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


name=TravelPrivot
username=superset
password=superset
host=db
port=5432
db_name=superset

charts=$(curl -X GET "http://localhost:8088/api/v1/chart/" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer ${token}")

count=$(echo "$charts" | jq '.result | length')
flag=false

# 遍历 JSON 数组
for (( i=0; i<count; i++ )); do
    # 提取当前 chart 的名称和 columns
    chart_name=$(echo "$charts" | jq -rM ".result[$i].slice_name")
    table_type=$(echo "$charts" | jq -rM ".result[$i].viz_type")

    metric_label=$(echo "$charts" | jq -rM ".result[$i].form_data.metrics[0].label")
    columns=$(echo "$charts" | jq -c ".result[$i].form_data.groupbyColumns")
    comparator=$(echo "$charts" | jq -c ".result[$i].form_data.adhoc_filters[0].comparator" )
    time_grain_sqla=$(echo "$charts" | jq -rM ".result[$i].form_data.time_grain_sqla")
    # z=$["$table_type" = "pivot_table_v2"]
    # echo $z
    # 检查 chart 名称是否匹配
    if [ "$chart_name" = "$name" ] && [ "$table_type" = "pivot_table_v2" ]; then
        # echo $metric_label
        # echo $comparator
        # echo $time_grain_sqla
        
        # 使用 jq 检查 columns 中是否包含所需的字段
        contains_columns=$(echo "$columns" | jq 'contains(["Travel Class", "Department", "Travel Date"])')
        echo $contains_columns
        if [ "$contains_columns" = "true" ] && [ "$comparator" = "\"2011-01-01T00:00:00 : 2011-06-30T00:00:00\"" ] && [ "$time_grain_sqla" = "P1M" ] && [ "$metric_label" = "SUM(Cost)" ]; then
            flag=true
            break
        fi
    fi
done

# 输出结果（可选）
if [ "$flag" = true ]; then
    echo "Create pivot table succeed"
else
    echo "Create pivot table failed"
fi
