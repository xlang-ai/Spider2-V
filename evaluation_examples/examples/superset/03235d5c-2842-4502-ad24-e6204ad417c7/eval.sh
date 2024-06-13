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

#csrf_token=$(curl -c /home/user/cookies.txt -X GET "http://localhost:8088/api/v1/security/csrf_token/" \
#    -H "Authorization: Bearer ${token}" \
#    -H "Content-Type: application/json" | jq -rM ".result")
#echo $csrf_token

name=MyPostgresConn
username=superset
password=superset
host=db
port=5432
db_name=superset
connections=$(curl -X GET "http://localhost:8088/api/v1/database/" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer ${token}")
count=$(echo $connections | jq -rM ".count")
flag=false
for (( i=0; i<$count ; i++ )) ; do
    conn_name=$(echo $connections | jq -rM ".result | .[${i}] | .database_name")
    if [ "$conn_name" = "$name" ]; then
	flag=true
	conn_id=$(echo $connections | jq -rM ".result | .[${i}] | .id")
	break
    fi
done
if [ $flag = false ]; then
    echo "Build connection failed"
    exit 0
fi

infos=$(curl -X GET "http://localhost:8088/api/v1/database/${conn_id}/connection" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer ${token}")
test_username=$(echo $infos | jq -rM ".result.parameters.username")
test_host=$(echo $infos | jq -rM ".result.parameters.host")
test_port=$(echo $infos | jq -rM ".result.parameters.port")
test_db_name=$(echo $infos | jq -rM ".result.parameters.database")
if [ "$test_username" = "$username" ] && [ "$test_host" = "$host" ] && [ "$test_port" = "$port" ] && [ "$test_db_name" = "$db_name" ]; then
    echo "Build connection succeed"
else
    echo "Build connection failed"
fi

# this API is used to test the connection itself, not whether the connection is built
#msg=$(curl -b /home/user/cookies.txt -X POST "http://localhost:8088/api/v1/database/test_connection/" \
#     -H "Authorization: Bearer ${token}" \
#     -H "X-CSRFToken: ${csrf_token}" \
#     -H "Content-Type: application/json" \
#     -d "{
#         \"sqlalchemy_uri\": \"postgresql://${username}:${password}@${host}:${port}/${db_name}\"
#     }" | jq -rM ".message")
#if [ "$msg" = "OK" ]; then
#    echo "Test connection succeed"
#else
#    echo "Test connection failed"
#fi
