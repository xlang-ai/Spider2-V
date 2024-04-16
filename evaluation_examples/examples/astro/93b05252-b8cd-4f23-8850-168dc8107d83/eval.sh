#!/bin/bash

source /home/user/anaconda3/etc/profile.d/conda.sh
#conda activate astro
cd /home/user/projects/weather/plugins

# # Extract the contents of my_extra_link_plugin.py
# content=$(cat /home/user/projects/weather/plugins/my_extra_link_plugin.py)

# # Check if name = "WTTRWeather" and return "https://wttr.in/HongKong" is present in the file
# if grep -q "name = \"WTTRWeather\"" <<< "$content" && grep -q "return \"https://wttr.in/HongKong\"" <<< "$content"; then
#     echo "\"WTTRWeather\" coding setup succeed."
# else
#     echo "\"WTTRWeather\" coding setup failed."
# fi

# # Check if name = "HTTP file" and return "https://developer.mozilla.org/en-US/docs/Web/HTTP" is present in the file
# if grep -q "name = \"HTTP file\"" <<< "$content" && grep -q "return \"https://developer.mozilla.org/en-US/docs/Web/HTTP\"" <<< "$content"; then
#     echo "\"HTTP file\" coding setup succeed."
# else
#     echo "\"HTTP file\ coding setup failed." 
# fi

cd /home/user/projects/weather
# astro dev restart >/dev/null 2>&1
export DAG_ID=weather_data_dag
export DAG_RUN_ID=$(docker exec -i $(docker ps | grep "webserver" | awk '{print $1}') airflow dags list-runs -o plain --dag-id ${DAG_ID} | grep "manual" | awk '{print $2}')
export TASK_ID=get_hong_kong_weather

RUN_ID=$(echo $DAG_RUN_ID | sed 's/:/%3A/g' | sed 's/+/%2B/g')
echo "localhost:8080/dags/${DAG_ID}/grid?dag_run_id=${RUN_ID}&task_id=${TASK_ID}"
