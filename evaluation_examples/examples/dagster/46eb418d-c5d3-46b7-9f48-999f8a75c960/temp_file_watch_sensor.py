import os
from dagster import sensor, RunRequest, RunConfig
from .log_file_job import log_file_job, FileConfig

@sensor(job=log_file_job, minimum_interval_seconds=3)
def directory_sensor():
    for filename in os.listdir("/home/user/file-watch-sensor/files/"):
        filepath = os.path.join("/home/user/file-watch-sensor/files/", filename)
        if os.path.isfile(filepath):
            yield RunRequest(
                run_key=filename,
                run_config=RunConfig(
                    ops={"process_file": FileConfig(filename=filename)}
                ),
            )