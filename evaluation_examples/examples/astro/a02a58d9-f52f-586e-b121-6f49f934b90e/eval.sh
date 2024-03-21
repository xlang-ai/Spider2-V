#!/bin/bash

source /home/user/anaconda3/etc/profile.d/conda.sh
conda activate astro
cd /home/user/projects/astro-jaffle-shop

DAG_ID=jaffle_shop_dag

# check whether the DAG is written correctly
astro run ${DAG_ID} >output.log 2>/dev/null
output=$(tail -n 5 output.log)
# TOTAL=10 is combined with jaffle_shop project
flag1=$(echo $output | grep "PASS=10 .* ERROR=0 .* TOTAL=10")
flag2=$(echo $output | grep "SUCCESS")
if [ -n "$flag1" ] && [ -n "$flag2" ]; then
    echo "astro run dag succeed"
else
    echo "astro run dag failed"
    exit 0
fi

astro dev start >/dev/null 2>/dev/null
container=$(astro dev ps | grep webserver | awk '{print $1}')
active_flag=$(docker exec -i $container airflow dags details -o plain ${DAG_ID} | grep is_active | grep -i true)
if [ -n "$active_flag" ]; then
    echo "dag active succeed"
else
    echo "dag active failed"
    exit 0
fi

interval_flag=$(docker exec -i $container airflow dags details -o plain ${DAG_ID} | grep schedule_interval | grep '0 10 \* \* \*')
if [ -n "$interval_flag" ]; then
    echo "dag schedule_interval succeed"
else
    echo "dag schedule_interval failed"
fi
