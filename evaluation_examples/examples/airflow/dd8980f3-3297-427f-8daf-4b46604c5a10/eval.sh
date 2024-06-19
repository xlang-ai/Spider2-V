#!/bin/bash

source /home/user/anaconda3/etc/profile.d/conda.sh
conda activate airflow
cd /home/user/projects/jaffle_shop_astro

# astro dev restart >/dev/null 2>/dev/null
export DAG_ID=jaffle_shop_dag
export CONTAINER=$(astro dev ps | grep "webserver" | awk '{print $1}')

# check whether the DAG is jaffle_shop dbt project
declare -a task_list=(
    "customers.customers_run"
    "customers.customers_test"
    "orders.orders_run"
    "orders.orders_test"
    "raw_customers_seed"
    "raw_orders_seed"
    "raw_payments_seed"
    "stg_customers.stg_customers_run"
    "stg_customers.stg_customers_test"
    "stg_orders.stg_orders_run"
    "stg_orders.stg_orders_test"
    "stg_payments.stg_payments_run"
    "stg_payments.stg_payments_test"
)
jaffle_shop_tasks=$(docker exec -i $CONTAINER airflow tasks list ${DAG_ID})
contains_all=true
for task in "${task_list[@]}"; do
    if [[ ! ${jaffle_shop_tasks} == *"$task"* ]]; then
        contains_all=false
        break
    fi
done
if ${contains_all}; then
    echo "jaffle_shop_dag succeed"
else
    echo "jaffle_shop_dag failed"
    exit 0
fi

# check whether the DAG is not paused
active_flag=$(docker exec -i $CONTAINER airflow dags details -o plain ${DAG_ID} | grep "is_paused" | grep -i "false")
if [ -n "$active_flag" ]; then
    echo "dag active succeed"
else
    echo "dag active failed"
    exit 0
fi

# check whether the DAG can run successfully
# astro run ${DAG_ID} >/dev/null 2>/dev/null # manually run it, but it is not working in this case
run_id=$(docker exec -i $CONTAINER airflow dags trigger ${DAG_ID} -o plain | grep "${DAG_ID}" | awk '{print $3}')
count=0
while true; do
    sleep 5
    count=$(expr $count + 1)
    flag=$(docker exec -i $CONTAINER airflow dags list-runs -o plain --dag-id ${DAG_ID} --no-backfill | grep "${run_id}" | awk '{print $3}')
    if [ "$flag" = "success" ] || [ "$flag" == "failed" ]; then
        if [ "$flag" = "success" ]; then
            echo "astro run dag succeed"
            break
        else
            echo "astro run dag failed"
            exit 0
        fi
    fi
    if [ $count -gt 10 ]; then
        echo "astro run dag failed after 50 seconds"
        exit 0
    fi
done

# check whether the interval is set correctly
interval_flag=$(docker exec -i $CONTAINER airflow dags details -o plain ${DAG_ID} | grep "schedule_interval" | grep "0 10 \* \* \*")
if [ -n "$interval_flag" ]; then
    echo "dag schedule_interval succeed"
else
    echo "dag schedule_interval failed"
fi
