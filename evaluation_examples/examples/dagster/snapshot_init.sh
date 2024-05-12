#!/bin/bash

exec 2>/dev/null

PASSWORD=password

# install mysql for some examples
echo $PASSWORD | sudo -S apt install pkg-config build-essential libmysqlclient-dev -y
echo $PASSWORD | sudo -S apt install mysql-server=8.0.36-0ubuntu0.22.04.1 -y # Version may differ on other machines. Not tested.
echo $PASSWORD | sudo -S systemctl enable mysql

# create conda env for dagster
source /home/user/anaconda3/etc/profile.d/conda.sh
conda create -n dagster python=3.11 -y
conda activate dagster
pip install dagster==1.7.2 dagster-cloud==1.7.2 dagster-cloud-cli==1.7.2 dagster-graphql==1.7.2 dagster-pipes==1.7.2 dagster-webserver==1.7.2 dagster-airflow==1.7.2 dagster-dbt==0.23.2 dagster-duckdb==0.23.2 dagster-duckdb-pandas==0.23.2 duckdb==0.10.2 dbt-duckdb==1.7.4 pandas==2.0.3 pytest==8.2.0 pyarrow==16.0.0 apache-airflow==2.9.0 apache-airflow-providers-mysql==5.5.4 mysqlclient==2.2.4 scikit-learn==1.4.2

# some ENV for dagster
mkdir -p /home/user/.dagster
touch /home/user/.dagster/dagster.yaml
echo "export DAGSTER_HOME=/home/user/.dagster" >> /home/user/.bashrc