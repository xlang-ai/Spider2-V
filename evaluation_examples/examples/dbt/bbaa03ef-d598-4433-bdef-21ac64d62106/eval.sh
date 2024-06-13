#!/bin/bash

source ~/anaconda3/etc/profile.d/conda.sh
conda activate dbt

cd ~/projects
mv /home/user/jaffle_shop_test.zip .
unzip -q jaffle_shop_test.zip

cd ~/projects/jaffle_shop
for (( i = 0 ; i <= 10 ; i++ )) ; do
    db_path=/home/user/projects/jaffle_shop_test/jaffle_shop_test${i}.duckdb
    mv $db_path ./jaffle_shop.duckdb
    output=$(dbt test)
    flag1=$(echo $output | grep "Nothing to do")
    flag2=$(echo $output | grep "Completed successfully")
    flag3=$(echo $output | grep "ERROR=0")
    case "$i" in
        0|10)
            if [ -z "$flag1" ] && [ -n "$flag2" ] && [ -n "$flag3" ]; then
                echo "dbt test (i=${i}) succeed"
            else
                echo "dbt test (i=${i}) failed"
                break
            fi
            ;;
        *)
            if [ -z "$flag1" ] && [ -z "$flag2" ] && [ -z "$flag3" ]; then
                echo "dbt test (i=${i}) succeed"
            else
                echo "dbt test (i=${i}) failed"
                break
            fi
            ;;
    esac
done
