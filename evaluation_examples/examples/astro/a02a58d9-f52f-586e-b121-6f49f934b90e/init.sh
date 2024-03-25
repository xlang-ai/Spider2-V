#!/bin/bash

####################################################################################################
# Please ensure that Chromium or Chrome, VSCode, docker and anaconda3 is installed on your system before running this script.
# The installed anaconda3 should be in the directory /home/user/anaconda3/.
# The current user should be added into group docker.
# The dbt project jaffle_shop.zip should be uploaded to the home directory before running this script.
# This script is tested on Ubuntu 20.04 LTS.
####################################################################################################

mkdir -p ~/.dbt
mkdir -p ~/projects/astro-jaffle-shop

PASSWORD=password
DB_NAME=jaffle_shop
DB_USER=user
DB_PASSWORD=password

function install_postgres() {
    cd /home
    echo $PASSWORD | sudo -S apt-get install postgresql postgresql-contrib -y >/dev/null 2>&1
    sudo -u postgres createuser --superuser $DB_USER
    sudo -u postgres createdb $DB_NAME
    sudo -u postgres psql -c "ALTER USER \"${DB_USER}\" WITH PASSWORD '$DB_PASSWORD';"
    # allow connection from any IP (including docker container) and set authentification method
    config_file=$(echo $PASSWORD | sudo -S -u postgres psql -tc "SHOW config_file" | awk 'NR==1 {print $1}')
    echo $PASSWORD | sudo -S bash -c "echo \"listen_addresses = '*'\" >> ${config_file}"
    hba_file=$(echo $PASSWORD | sudo -S -u postgres psql -tc "SHOW hba_file" | awk 'NR==1 {print $1}')
    echo $PASSWORD | sudo -S bash -c "echo \"host    all             all             172.16.0.0/14           scram-sha-256\" >> ${hba_file}"
    sudo systemctl restart postgresql
}
install_postgres

function create_astro_env() {
    source /home/user/anaconda3/etc/profile.d/conda.sh
    conda create -n astro python=3.11 -y >/dev/null 2>&1
    conda activate astro
    pip install dbt-core dbt-postgres >/dev/null 2>&1
    echo $PASSWORD | sudo -S bash -c "curl -sSL install.astronomer.io | bash -s >/dev/null 2>&1"
    echo "source /home/user/anaconda3/etc/profile.d/conda.sh" >> ~/.bashrc
    echo "conda activate astro" >> ~/.bashrc
}
create_astro_env

cd /home/user/projects/astro-jaffle-shop
mv /home/user/jaffle_shop.zip .
unzip -q jaffle_shop.zip
mv jaffle_shop/profiles.yml ~/.dbt/
mv jaffle_shop/.astro .
rm -f jaffle_shop.zip
cd jaffle_shop
{ dbt debug ; dbt seed ; dbt run ; dbt test ; } >/dev/null 2>&1

code /home/user/projects/astro-jaffle-shop
gnome-terminal --maximize --working-directory=/home/user/projects/astro-jaffle-shop