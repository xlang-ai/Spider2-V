#!/bin/bash
exec 2>/dev/null

PROJECT_NAME=file-watch-sensor
cd /home/user/$PROJECT_NAME
source /home/user/anaconda3/etc/profile.d/conda.sh
conda activate dagster

export DAGSTER_HOME=~/.dagster
rm -rf files
mkdir -p files
echo "Hello World!" > files/helloworld.txt
echo "Welcome to dagster!" > files/welcome.txt
echo "This is the test for sensor." > files/test_sensor.txt

dagster sensor preview directory_sensor
sensor_status=$(dagster sensor list | grep "Sensor: directory_sensor \[RUNNING\]")

curl -s -o directory_sensor.html http://localhost:3000/locations/file_watch_sensor/sensors/directory_sensor

if [ -s directory_sensor.html ] && [ -n "$sensor_status" ]; then
    echo "Check sensor running succeeded"
else
    echo "Check sensor running failed"
    exit 0
fi