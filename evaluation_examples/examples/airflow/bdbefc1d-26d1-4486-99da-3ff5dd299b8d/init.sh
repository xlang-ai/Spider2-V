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

source /home/user/anaconda3/etc/profile.d/conda.sh
conda activate airflow
echo "source /home/user/anaconda3/etc/profile.d/conda.sh" >> ~/.bashrc
echo "conda activate airflow" >> ~/.bashrc

cd /home/user/projects
mv /home/user/cocktail.zip .
unzip -q cocktail.zip
rm -rf cocktail.zip
cd cocktail
code /home/user/projects/cocktail
gnome-terminal --maximize --working-directory=/home/user/projects/cocktail

# launch the web server, this step may take 30 seconds
astro dev start --no-browser > start_server.log 2> start_server.log
code /home/user/projects/cocktail/dags/cocktail_producer_dag.py
code /home/user/projects/cocktail/dags/cocktail_consumer_dag.py
code /home/user/projects/cocktail/README.md
# unpause two DAGs using REST API
PRODUCER_DAG=cocktail_producer_dag
curl -X PATCH http://localhost:8080/api/v1/dags/${PRODUCER_DAG} -H "Content-Type: application/json" -u admin:admin -d '{
    "is_paused": false
}'
# wait for the producer DAG to finish
wait=0
maximum=10
while [ $wait -lt 10 ]; do
    if [ -f /home/user/projects/cocktail/include/cocktail_info.txt ] && [ -f /home/user/projects/cocktail/cocktail_instructions.txt ]; then
        break
    fi
    sleep 2
    wait=$(expr $wait + 2)
done
CONSUMER_DAG=cocktail_consumer_dag
curl -X PATCH http://localhost:8080/api/v1/dags/${CONSUMER_DAG} -H "Content-Type: application/json" -u admin:admin -d '{
    "is_paused": false
}'