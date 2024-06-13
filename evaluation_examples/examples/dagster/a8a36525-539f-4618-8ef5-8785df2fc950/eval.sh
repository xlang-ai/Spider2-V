#!/bin/bash

PROJECT_NAME=iris-analysis

cd /home/user/$PROJECT_NAME
source /home/user/anaconda3/etc/profile.d/conda.sh
conda activate dagster

export DAGSTER_HOME=~/.dagster

python -c "import duckdb; conn = duckdb.connect('iris_db.duckdb'); conn.sql('COPY (SELECT * FROM iris_virginica) TO \'iris_virginica.csv\' (HEADER 1, FORMAT CSV);')"

if diff -i iris_virginica.csv gold_iris_virginica.csv > /dev/null; then
    echo "Check table succeeded"
else
    echo "Check table failed"
fi