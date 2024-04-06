#!/bin/bash

curl -s -o assets.html http://localhost:8004/locations/dagster_proj/assets
if [ -s assets.html ] ; then
    echo "Dagster UI succeeded"
else
    echo "Dagster UI failed"
    exit 0
fi