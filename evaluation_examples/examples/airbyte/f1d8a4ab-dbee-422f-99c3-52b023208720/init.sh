#!/bin/bash

####################################################################################################
# Please ensure that Chromium or Chrome, VSCode, docker and anaconda3 is installed on your system before running this script.
# The installed anaconda3 should be in the directory /home/user/anaconda3/.
# Some images should be pre-downloaded in VM snapshots to accelerate the process.
# Please ensure the initial project is copied to the home directory.
# This script is tested on Ubuntu 22.04 LTS.
####################################################################################################

# ignore all output and error
exec 1>/dev/null
exec 2>/dev/null

# source /home/user/anaconda3/etc/profile.d/conda.sh
# conda activate airbyte
# echo "source /home/user/anaconda3/etc/profile.d/conda.sh" >> ~/.bashrc
# echo "conda activate airbyte" >> ~/.bashrc
PASSWORD=password
echo $PASSWORD | sudo -S systemctl stop postgresql
# configure Postgres
POSTGRES_VERSION=16-alpine
# Start a source Postgres container running at port 2000 on localhost
docker run --rm --name airbyte-source -e POSTGRES_PASSWORD=password -p 2000:5432 -d postgres:${POSTGRES_VERSION}
docker run --rm --name airbyte-destination -e POSTGRES_PASSWORD=password -p 3000:5432 -d postgres:${POSTGRES_VERSION}
# start airbyte local server
function start_airbyte_server() {
    cd /home/user/projects/airbyte
    bash run-ab-platform.sh > start_server.log &
    total_time=0
    while true; do
        sleep 3
        total_time=$(expr ${total_time} + 3)
        msg=$(cat start_server.log | grep -i "Startup completed" | grep "airbyte-worker")
        if [ $? -eq 0 ]; then # the server has been launched
            break
        fi
        if [ ${total_time} -gt 60 ]; then # exceeding maximum waiting time
            echo "Exceeding maximum waiting time 60s for airbyte server to launch!"
            break
        fi
    done
}
start_airbyte_server

# create table

docker exec -i airbyte-source psql -U postgres <<EOF
CREATE TABLE table_one(
  id integer PRIMARY KEY,
  name VARCHAR(200),
  updated_at timestamp DEFAULT NOW() NOT NULL
);
EOF
docker exec -i airbyte-source psql -U postgres <<EOF
CREATE OR REPLACE FUNCTION trigger_set_timestamp()
RETURNS TRIGGER AS \$$
BEGIN
  NEW.updated_at = NOW();
  RETURN NEW;
END;
\$$ LANGUAGE plpgsql;
EOF
docker exec -i airbyte-source psql -U postgres <<EOF
CREATE TRIGGER set_timestamp_on_table_one
  BEFORE UPDATE ON table_one
  FOR EACH ROW
  EXECUTE PROCEDURE trigger_set_timestamp();
EOF
docker exec -i airbyte-source psql -U postgres <<EOF
INSERT INTO table_one(id, name) VALUES(1, 'Eg1 IncApp');
INSERT INTO table_one(id, name) VALUES(2, 'Eg2 IncApp');
EOF
docker exec -i airbyte-source psql -U postgres -c "SELECT * FROM table_one;"
docker exec -i airbyte-source psql -U postgres <<EOF
UPDATE table_one SET name='Eg2a IncAp' WHERE id=2;
SELECT * FROM table_one;
EOF

# create source and destination
# 1. get workspace id
workspace=$(curl -X POST http://localhost:8000/api/v1/workspaces/list -H "Content-Type: application/json" -d {} | jq -rM ".workspaces | .[] | .workspaceId")
# 2. get source definition id
source_name="Postgres"
source_defid=$(curl -X POST http://localhost:8000/api/v1/source_definitions/list -H "Content-Type: application/json" | jq -rM ".sourceDefinitions | .[] | select(.name == \"${source_name}\") | .sourceDefinitionId")
# 3. create source, the connectionConfiguration field is source-specific
curl -X POST http://localhost:8000/api/v1/sources/create -H "Content-Type: application/json" -d "
{
    \"workspaceId\": \"${workspace}\",
    \"connectionConfiguration\": {
        \"host\": \"localhost\",
        \"port\": 2000,
        \"schemas\": [\"public\"],
        \"database\": \"postgres\",
        \"password\": \"password\",
        \"ssl_mode\": {
            \"mode\": \"disable\"
        },
        \"username\": \"postgres\",
        \"tunnel_method\": {
            \"tunnel_method\": \"NO_TUNNEL\"
        },
        \"replication_method\": {
            \"method\": \"Standard\"
        }
    },
    \"sourceDefinitionId\": \"${source_defid}\",
    \"name\": \"${source_name}\", 
    \"sourceName\": \"${source_name}\"
}
"
# 4. get source id and write into file
curl -X POST http://localhost:8000/api/v1/sources/list -H "Content-Type: application/json" -d "{\"workspaceId\": \"${workspace}\"}" | jq -rM ".sources | .[] | select(.sourceName == \"${source_name}\") | .sourceId" > /home/user/srcid.txt
read -r source_id < /home/user/srcid.txt
# 5. get destination definition id
destination_name="Postgres"
destination_defid=$(curl -X POST http://localhost:8000/api/v1/destination_definitions/list -H "Content-Type: application/json" | jq -rM ".destinationDefinitions | .[] | select(.name == \"${destination_name}\") | .destinationDefinitionId")
# 6. create destination, the connectionConfiguration field is destination-specific
curl -X POST http://localhost:8000/api/v1/destinations/create -H "Content-Type: application/json" -d "
{
    \"workspaceId\": \"${workspace}\",
    \"connectionConfiguration\": {
       \"ssl\": false,
       \"host\": \"localhost\",
       \"port\": 3000,
       \"schema\": \"public\",
       \"database\": \"postgres\",
       \"password\": \"password\",
       \"ssl_mode\":{
            \"mode\": \"disable\"
        },
        \"username\": \"postgres\",
        \"tunnel_method\":{
            \"tunnel_method\": \"NO_TUNNEL\"
        },
        \"disable_type_dedupe\": false
    },
    \"destinationDefinitionId\": \"${destination_defid}\",
    \"name\": \"${destination_name}\", 
    \"destinationName\": \"${destination_name}\"
}
"
rm /home/user/settings.json
# 7. get destination id and write into file
curl -X POST http://localhost:8000/api/v1/destinations/list -H "Content-Type: application/json" -d "{\"workspaceId\": \"${workspace}\"}" | jq -rM ".destinations | .[] | select(.destinationName == \"${destination_name}\") | .destinationId" > /home/user/destid.txt
read -r destination_id < /home/user/destid.txt
# 8. create connection
connection=$(cat /home/user/connection.json | sed "s/\${source_id}/${source_id}/" | sed "s/\${destination_id}/${destination_id}/")
curl -X POST http://localhost:8000/api/v1/connections/create -H "Content-Type: application/json" -d "${connection}"
# 9. get connection id
curl -X POST http://localhost:8000/api/v1/connections/list -H "Content-Type: application/json" -d "{\"workspaceId\": \"${workspace}\"}" | jq -rM ".connections | .[] | .connectionId" > /home/user/connid.txt
rm /home/user/connection.json

gnome-terminal --maximize --working-directory=/home/user/


# docker exec -i airbyte-source psql -U postgres <<EOF
# UPDATE table_one SET name='Eg2b IncAp' WHERE id=2;
# EOF