## File-related Ops and Job

### Create 4 Dagster Ops
These 4 dagster ops all watch the folder `./files` and perform different statistics.
1. `get_file_sizes`:
  - get the sizes of each file
  - return a dictionary, using filename as key, file size as value
2. `get_total_file_size`:
  - calculate the total file size
3. `get_max_file_size`:
  - compute the largest size among all files
4. `report_file_stats`:
  - output the total and largest file sizes in the dagster log
  - logging template: "Total size: {total_size}, max size: {max_size}"

### Create 1 Dagster Job
This dagster job can re-use the dagster ops defined above.
- job: file_sizes_job
- description: it reports the total and largest file sizes in the `./files` directory