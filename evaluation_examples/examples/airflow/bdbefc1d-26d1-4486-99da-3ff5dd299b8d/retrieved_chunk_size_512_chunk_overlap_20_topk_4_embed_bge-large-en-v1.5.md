Documentation Source:
docs.astronomer.io/learn/airflow-datasets.md

Documentation Title:
Datasets and data-aware scheduling in Airflow | Astronomer Documentation

Documentation Content:
* Airflow monitors datasets only within the context of DAGs and tasks. It does not monitor updates to datasets that occur outside of Airflow.
* Consumer DAGs that are scheduled on a dataset are triggered every time a task that updates that dataset completes successfully. For example, if `task1`and `task2`both produce `dataset_a`, a consumer DAG of `dataset_a`runs twice - first when `task1`completes, and again when `task2`completes.
* Consumer DAGs scheduled on a dataset are triggered as soon as the first task with that dataset as an outlet finishes, even if there are downstream producer tasks that also operate on the dataset.

Airflow 2.9 added several new features to datasets:

Conditional Dataset SchedulingCombined Dataset and Time-based Scheduling* Datasets are now shown in the **Graph**view of a DAG in the Airflow UI. The `upstream1`DAG in the screenshot below is a consumer of the `dataset0`dataset, and has one task `update_dataset_1`that updates the `dataset1`dataset.

!

For more information about datasets, see Data-aware scheduling.

The **Datasets**tab, and the **DAG Dependencies**view in the Airflow UI give you observability for datasets and data dependencies in the DAG's schedule.

On the **DAGs**view, you can see that your `dataset_downstream_1_2`DAG is scheduled on two producer datasets (one in `dataset_upstream1`and `dataset_upstream2`). When Datasets are provided as a list, the DAG is scheduled to run after all Datasets in the list have received at least one update. In the following screenshot, the `dataset_downstream_1_2`DAG's next run is pending one dataset update. At this point the `dataset_upstream`DAG has run and updated its dataset, but the `dataset_upstream2`DAG has not.

!The **Datasets**tab shows a list of all datasets in your Airflow environment and a graph showing how your DAGs and datasets are connected. You can filter the lists of Datasets by recent updates.



Documentation Source:
docs.astronomer.io/learn/airflow-datasets.md

Documentation Title:
Datasets and data-aware scheduling in Airflow | Astronomer Documentation

Documentation Content:
")f =open("include/cocktail_info.txt","a")f.write(msg)f.close()withDAG(dag_id="datasets_producer_dag",start_date=datetime(2022,10,1),schedule=None,catchup=False,render_template_as_native_obj=True,):get_cocktail =PythonOperator(task_id="get_cocktail",python_callable=get_cocktail_func,op_kwargs={"api":API},)write_instructions_to_file =PythonOperator(task_id="write_instructions_to_file",python_callable=write_instructions_to_file_func,op_kwargs={"response":"{{ ti.xcom_pull(task_ids='get_cocktail') }}"},outlets=[INSTRUCTIONS],)write_info_to_file =PythonOperator(task_id="write_info_to_file",python_callable=write_info_to_file_func,op_kwargs={"response":"{{ ti.xcom_pull(task_ids='get_cocktail') }}"},outlets=[INFO],)get_cocktail >>write_instructions_to_file >>write_info_to_file`A consumer DAG runs whenever the dataset(s) it is scheduled on is updated by a producer task, rather than running on a time-based schedule. For example, if you have a DAG that should run when the `INSTRUCTIONS`and `INFO`datasets are updated, you define the DAG's schedule using the names of those two datasets.

Any DAG that is scheduled with a dataset is considered a consumer DAG even if that DAG doesn't actually access the referenced dataset. In other words, it's up to you as the DAG author to correctly reference and use datasets.



Documentation Source:
docs.astronomer.io/learn/scheduling-in-airflow.md

Documentation Title:
Schedule DAGs in Airflow | Astronomer Documentation

Documentation Content:
Datasets can be updated by any tasks in any DAG of the same Airflow environment, by calls to the dataset endpoint of the Airflow REST API, or manually in the Airflow UI.

In the Airflow UI, the DAG now has a schedule of **Dataset**. The **Next Run**column shows the datasets the DAG depends on and how many of them have been updated.

!To learn more about datasets and data driven scheduling, see Datasets and Data-Aware Scheduling in Airflowguide.

Timetables​
-----------

Timetables, introduced in Airflow 2.2, address the limitations of cron expressions and timedelta objects by allowing users to define their own schedules in Python code. All DAG schedules are ultimately determined by their internal timetable and if a cron expression or timedelta object is not suitable, you can define your own.

Custom timetables can be registered as part of an Airflow plugin. They must be a subclass of `Timetable`, and they should contain the following methods, both of which return a `DataInterval`with a start and an end:

* `next_dagrun_info`: Returns the data interval for the DAG's regular schedule
* `infer_manual_data_interval`: Returns the data interval when the DAG is manually triggered



Documentation Source:
docs.astronomer.io/learn/scheduling-in-airflow.md

Documentation Title:
Schedule DAGs in Airflow | Astronomer Documentation

Documentation Content:
* Simple Dataset Schedule
* Conditional Dataset Schedule
* Time + Dataset Schedule

`# from airflow.datasets import DatasetDATASETS_PATH ="s3://airflow-datasets"dataset1 =Dataset(f"{DATASETS_PATH}/dataset_1.txt")dataset2 =Dataset(f"{DATASETS_PATH}/dataset_2.txt")@dag(dag_id='dataset_dependent_example_dag',catchup=False,start_date=datetime(2024,4,1),schedule=[dataset1,dataset2],# Passing a list of datasets will create an AND condition, # This scheduling option is available in Airflow 2.4+)`This DAG runs when both `dataset1`and `dataset2`is updated at least once.

`# from airflow.datasets import DatasetDATASETS_PATH ="s3://airflow-datasets"dataset1 =Dataset(f"{DATASETS_PATH}/dataset_1.txt")dataset2 =Dataset(f"{DATASETS_PATH}/dataset_2.txt")@dag(dag_id='dataset_dependent_example_dag',catchup=False,start_date=datetime(2024,4,1),schedule=(dataset1 |dataset2),# Use () instead of [] to be able to use conditional dataset scheduling!# This scheduling option is available in Airflow 2.9+)`This DAG runs when either `dataset1`or `dataset2`is updated.

`# from airflow.datasets import Dataset# from airflow.timetables.datasets import DatasetOrTimeSchedule# from airflow.timetables.trigger import CronTriggerTimetableDATASETS_PATH ="s3://airflow-datasets"dataset1 =Dataset(f"{DATASETS_PATH}/dataset_1.txt")dataset2 =Dataset(f"{DATASETS_PATH}/dataset_2.txt")@dag(dag_id='dataset_dependent_example_dag',catchup=False,start_date=datetime(2024,4,1),schedule=DatasetOrTimeSchedule(timetable=CronTriggerTimetable("0 0 * * *",timezone="UTC"),datasets=(dataset1 |dataset2),),# Use () instead of [] to be able to use conditional dataset scheduling!# This scheduling option is available in Airflow 2.9+)`This DAG runs every day at midnight UTC and, additionally, whenever either `dataset1`or `dataset2`is updated.



