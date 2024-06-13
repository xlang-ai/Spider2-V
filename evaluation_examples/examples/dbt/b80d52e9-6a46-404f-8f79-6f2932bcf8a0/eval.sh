#!/bin/bash

source ~/anaconda3/etc/profile.d/conda.sh
conda activate dbt
cd ~/projects/jaffle_shop

if [ -s target/catalog.json ] && [ -s target/index.html ] ; then
    echo "dbt docs generate succeed"
else
    echo "dbt docs generate failed"
    exit 0
fi

curl -s -o index.html http://localhost:8020
if [ -s index.html ] ; then
    echo "dbt docs serve succeed"
else
    echo "dbt docs serve failed"
    exit 0
fi

diff index.html target/index.html > diff.log
if [ -s diff.log ] ; then
    echo "dbt docs serve failed"
    exit 0
else
    echo "dbt docs serve succeed"
fi
rm -rf diff.log index.html

output=$(dbt docs generate)
flag1=$(echo $output | grep --ignore-case "error")
flag2=$(echo $output | grep "Catalog written to")
if [ -z "$flag1" ] && [ -n "$flag2" ] ; then
    echo "dbt docs generate succeed"
else
    echo "dbt docs generate failed"
fi
