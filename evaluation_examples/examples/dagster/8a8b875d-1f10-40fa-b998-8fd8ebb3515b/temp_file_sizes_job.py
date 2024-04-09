import os
from dagster import job, op, get_dagster_logger

@op
def get_file_sizes():
    files = [f for f in os.listdir("./files") if os.path.isfile("./files/" + f)]
    return {f: os.path.getsize("./files/" + f) for f in files}
        
@op
def get_total_file_size(file_sizes):
    return sum(file_sizes.values())
    
@op
def get_max_file_size(file_sizes):
    return max(file_sizes.values())
    
@op
def report_file_stats(total_size, max_size):
    get_dagster_logger().info(f"Total size: {total_size}, max size: {max_size}")
        
@job
def file_sizes_job():
    file_sizes = get_file_sizes()
    report_file_stats(
        get_total_file_size(file_sizes),
        get_max_file_size(file_sizes)
    )
