#!/bin/bash

####################################################################################################
# Please ensure that Chromium or Chrome, VSCode, docker and anaconda3 is installed on your system before running this script.
# The installed anaconda3 should be in the directory /home/user/anaconda3/.
# Some images should be pre-downloaded in VM snapshots to accelerate the process.
# Please ensure the initial project is copied to the home directory.
# This script is tested on Ubuntu 22.04 LTS.
####################################################################################################

exec 1>/dev/null
exec 2>/dev/null

PASSWORD=password

# ignore all output and error
DB_USER=Tom
DB_NAME=TomDB
DB_PASSWORD=Tom123456
function postgresql_configure() {
    cd /home
    echo $PASSWORD | sudo -S -u postgres createuser --superuser $DB_USER
    echo $PASSWORD | sudo -S -u postgres createdb $DB_NAME
    echo $PASSWORD | sudo -S -u postgres psql -c "ALTER USER \"${DB_USER}\" WITH PASSWORD '$DB_PASSWORD';"
}
postgresql_configure

export MB_DB_TYPE=postgres
export MB_DB_DBNAME=$DB_NAME
export MB_DB_PORT=5432
export MB_DB_USER=$DB_USER
export MB_DB_PASS=$DB_PASSWORD
export MB_DB_HOST=localhost

function start_metabase_server() {
    cd /home/user/projects/metabase
    nohup java -jar metabase.jar > start_server.log 2>&1 &
    count=0
    while true; do
        sleep 5
        cat start_server.log | grep "Metabase Initialization COMPLETE"
        if [ $? -eq 0 ]; then
            echo "Metabase initialization completed."
            break
        fi
        count=$(expr $count + 1)
        if [ $count -gt 6 ]; then
            echo "Metabase initialization failed."
            exit 1
        fi
    done
}
start_metabase_server