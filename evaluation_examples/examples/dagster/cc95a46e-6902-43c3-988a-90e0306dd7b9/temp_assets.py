import os
import urllib.request
import json

dir_name = "data"
if not os.path.exists(dir_name):
    os.makedirs(dir_name)

from dagster import AssetExecutionContext, DailyPartitionsDefinition, asset

@asset(partitions_def=DailyPartitionsDefinition(start_date="2024-04-01"))
def apod_asset(context: AssetExecutionContext) -> None:
    partition_date_str = context.partition_key

    url = f"https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&date={partition_date_str}"
    target_location = f"data/{partition_date_str}.json"

    urllib.request.urlretrieve(url, target_location)

    with open(target_location) as f:
        data = json.load(f)

    with open(f"data/apod_url_{partition_date_str}.txt", "w") as f:
        f.write(data["hdurl"])
