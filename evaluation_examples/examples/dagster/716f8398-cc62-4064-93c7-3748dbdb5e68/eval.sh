#!/bin/bash

PROJECT_NAME=movies

cd ~/$PROJECT_NAME
source /home/user/anaconda3/etc/profile.d/conda.sh
conda activate dagster

rm -f /tmp/hollywood_movies.pq /tmp/imdb_movies.pq
dagster asset materialize --select hollywood_movies -m movies > /dev/null 2>&1
dagster asset materialize --select imdb_movies -m movies > /dev/null 2>&1

diff gold_hollywood_movies.pq /tmp/hollywood_movies.pq > /dev/null 2>&1
if [ $? -eq 0 ] ; then
    echo "Check Hollywood movies parquet succeeded"
else
    echo "Check Hollywood movies parquet failed"
fi

diff gold_imdb_movies.pq /tmp/imdb_movies.pq > /dev/null 2>&1
if [ $? -eq 0 ] ; then
    echo "Check IMDB movies parquet succeeded"
else
    echo "Check IMDB movies parquet failed"
fi

curl -s -o parquet.html http://localhost:3000/locations/pandas_assets/resources/parquet
if [ -s parquet.html ] ; then
    echo "Check parquet resource succeeded"
else
    echo "Check parquet resource failed"
    exit 0
fi