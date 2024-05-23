#!/bin/bash

exec 2>/dev/null

cd /home/user/projects/cocktail
export PRODUCER=cocktail_producer_dag
export CONSUMER=cocktail_consumer_dag
export CONTAINER=$(astro dev ps | grep "webserver" | awk '{print $1}')

current_time=$(date -u +"%Y-%m-%dT%H:%M:%S.%N%:z")
# manually triggered the producer DAG
astro run ${PRODUCER}>/dev/null 2>/dev/null
producer_time=$(docker exec ${CONTAINER} airflow dags list-runs -o plain --dag-id ${PRODUCER} --start-date ${current_time} | grep "${PRODUCER}" | grep -m 1 "manual" | grep "success" | awk '{print $4}')
if [ -z "$producer_time" ]; then
    echo "Producer DAG manually triggering failed"
    exit 0
fi

count=0
triggered=false
maximum_wait_time=10
while [ $count -lt $maximum_wait_time ]; do
    consumer_record=$(docker exec ${CONTAINER} airflow dags list-runs -o plain --dag-id ${CONSUMER} --start-date ${producer_time} | grep "${CONSUMER}" | grep "success")
    if [ -n "$consumer_record" ]; then
        triggered=true
        break
    fi
    sleep 3
    count=$(expr $count + 3)
done
if [ "$triggered" = false ]; then
    echo "Consumer DAG not triggered after 10 seconds, failed"
    exit 0
fi

file1="include/cocktail_info.txt"
file2="include/cocktail_instructions.txt"
expected_file="merged_cocktail.txt"
result_file="include/cocktail.txt"
cat $file1 > $expected_file
cat $file2 >> $expected_file
difference=$(diff -Z $expected_file $result_file)
if [ -z "$difference" ]; then
    echo "Astro DAG data-aware schedule succeed"
else
    echo "Astro DAG data-aware schedule failed"
fi