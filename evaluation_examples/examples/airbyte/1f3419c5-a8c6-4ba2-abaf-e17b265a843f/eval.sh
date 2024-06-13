#!/bin/bash

exec 2>/dev/null

# source /home/user/anaconda3/etc/profile.d/conda.sh
# conda activate airbyte

expected_result="1|Eg1 IncApp 2|Eg2a IncAp 2|Eg2b IncAp"
actual_result=$(docker exec -i airbyte-destination psql -U postgres -d postgres -t -A -F"|" -c "SELECT id, name FROM public.table_one")
actual_result_clean=$(echo "$actual_result" | sed '/^$/d' | xargs)
expected_result_clean=$(echo "$expected_result" | sed '/^$/d' | xargs)


if [ "${actual_result_clean}" == "${expected_result_clean}" ]; then
    echo "Check table in destination, succeed"
    exit 0
fi
echo "Check table in destination, failed"
# docker exec -it airbyte-destination bash -c "psql -U postgres -c \"\copy (SELECT city, city_code FROM public.table_one) TO '/data/cities.csv' WITH CSV HEADER\" && chmod 666 /data/cities.csv"
