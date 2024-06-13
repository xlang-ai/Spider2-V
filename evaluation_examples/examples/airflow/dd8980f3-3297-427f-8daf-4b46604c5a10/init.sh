#!/bin/bash

####################################################################################################
# Please ensure that Chromium or Chrome, VSCode, docker and anaconda3 is installed on your system before running this script.
# The installed anaconda3 should be in the directory /home/user/anaconda3/.
# Docker engine is installed following official docs: https://docs.docker.com/engine/install/ubuntu/
# The current user should be added into group docker.
# This script is tested on Ubuntu 22.04 LTS.
####################################################################################################

exec 1>/dev/null
exec 2>/dev/null

PASSWORD=password
DB_NAME=jaffle_shop
DB_USER=user
DB_PASSWORD=password

function configure_postgresql() {
    cd /home
    echo $PASSWORD | sudo -S -u postgres createuser --superuser $DB_USER
    echo $PASSWORD | sudo -S -u postgres createdb $DB_NAME
    echo $PASSWORD | sudo -S -u postgres psql -c "ALTER USER \"${DB_USER}\" WITH PASSWORD '$DB_PASSWORD';"
}
configure_postgresql

source /home/user/anaconda3/etc/profile.d/conda.sh
conda activate airflow
echo "source /home/user/anaconda3/etc/profile.d/conda.sh" >> ~/.bashrc
echo "conda activate airflow" >> ~/.bashrc

cd /home/user/projects
mv /home/user/jaffle_shop_astro.zip .
unzip -q jaffle_shop_astro.zip
rm -rf jaffle_shop_astro.zip
cd jaffle_shop_astro
code /home/user/projects/jaffle_shop_astro
gnome-terminal --maximize --working-directory=/home/user/projects/jaffle_shop_astro

# launch the web server, this step may be very slow ~ 2 minutes, please be patient
astro dev start --no-browser > start_server.log 2> start_server.log
code /home/user/projects/jaffle_shop_astro/dags/jaffle_shop_dag.py
code /home/user/projects/jaffle_shop_astro/README.md
# create connection using REST API
curl -X POST http://localhost:8080/api/v1/connections -H "Content-Type: application/json" -u admin:admin -d '{
    "connection_id": "postgres_conn",
    "conn_type": "postgres",
    "host": "172.17.0.1",
    "login": "user",
    "schema": "jaffle_shop",
    "port": 5432,
    "password": "password"
}'