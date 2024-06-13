#!/bin/bash

####################################################################################################
# Please ensure that Chromium or Chrome, VSCode, docker and anaconda3 is installed on your system before running this script.
# The installed anaconda3 should be in the directory /home/user/anaconda3/.
# Docker engine is installed following official docs: https://docs.docker.com/engine/install/ubuntu/
# The current user should be added into group docker.
# The dbt project jaffle_shop.zip should be uploaded to the home directory before running this script.
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

mkdir -p /home/user/projects/astro-project
cd /home/user/projects/astro-project
astro dev init
ASTRO_RUNTIME_VERSION=10.5.0
sed -i "s/astro-runtime:.*$/astro-runtime:${ASTRO_RUNTIME_VERSION}/" Dockerfile
cat >> requirements.txt <<EOF
apache-airflow-providers-postgres==5.10.2
EOF
astro dev start --no-browser > start_server.log 2> start_server.log