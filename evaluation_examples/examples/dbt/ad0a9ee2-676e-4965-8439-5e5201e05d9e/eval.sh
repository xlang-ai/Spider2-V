#!/bin/bash


cd ~/projects/analytics

output=$(./dbt --version)
flag=$(echo $output | grep "dbt Cloud CLI")

if [ -n "$flag" ]; then
    echo "dbt cloud cli setup succeed"
else
    echo "dbt cloud cli failed"
fi
