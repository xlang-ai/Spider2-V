Documentation Source:
docs.astronomer.io/learn/airflow-sql-data-quality.md

Documentation Title:
Run data quality checks using SQL check operators | Astronomer Documentation

Documentation Content:
You can use an in-memory SQLite database for which you'll need to install the SQLite provider. Note that currently the operators cannot support BigQuery `job_id`s.
* A love for birds.

Step 1: Configure your Astro project​
-------------------------------------

To use SQL check operators, install the Common SQL providerin your Astro project.

1. Run the following commands to create a new Astro project:

`$ mkdirastro-sql-check-tutorial &&cdastro-sql-check-tutorial$ astro dev init`
2. Add the Common SQL provider and the SQLite provider to your Astro project `requirements.txt`file.

`apache-airflow-providers-common-sql==1.5.2apache-airflow-providers-sqlite==3.4.2`

Step 2: Create a connection to SQLite​
--------------------------------------

In the Airflow UI, go to **Admin**> **Connections**and click **+**.

2. Create a new connection named `sqlite_conn`and choose the `SQLite`connection type. Enter the following information:


	* **Connection Id**: `sqlite_conn`.
	* **Connection Type**: `SQLite`.
	* **Host**: `/tmp/sqlite.db`.

Step 3: Add a SQL file with a custom check​
-------------------------------------------

In your `include`folder, create a file called `custom_check.sql`.

Copy and paste the following SQL statement into the file:


`WITHall_combinations_unique AS(SELECTDISTINCTbird_name,observation_year AScombos_uniqueFROM'{{ params.table_name }}')SELECTCASEWHENCOUNT(*)=COUNT(combos_unique)THEN1ELSE0ENDASis_uniqueFROM'{{ params.table_name }}'JOINall_combinations_unique;`This SQL statement returns 1 if all combinations of `bird_name`and `observation_year`in a templated table are unique, and 0 if not.

Step 4: Create a DAG using SQL check operators​
-----------------------------------------------

Start Airflow by running `astro dev start`.

Create a new file in your `dags`folder called `sql_data_quality.py`.

3.



Documentation Source:
docs.astronomer.io/learn/debugging-dags.md

Documentation Title:
Debug DAGs | Astronomer Documentation

Documentation Content:
* Increase the resources available to your workers (if using the Celery executor) or scheduler (if using the local executor).
* If you're using the Kubernetes executor and a task fails very quickly (in less than 15 seconds), the pod running the task spins down before the webserver has a chance to collect the logs from the pod. If possible, try building in some wait time to your task depending on which operator you're using. If that isn't possible, try to diagnose what could be causing a near-immediate failure in your task. This is often related to either lack of resources or an error in the task configuration.
* Increase the CPU or memory for the task.
* Ensure that your logs are retained until you need to access them. If you are an Astronomer customer see our documentation on how to View logs.
* Check your scheduler and webserver logs for any errors that might indicate why your task logs aren't appearing.

Troubleshooting connections​
----------------------------

Typically, Airflow connections are needed to allow Airflow to communicate with external systems. Most hooks and operators expect a defined connection parameter. Because of this, improperly defined connections are one of the most common issues Airflow users have to debug when first working with their DAGs.

While the specific error associated with a poorly defined connection can vary widely, you will typically see a message with "connection" in your task logs. If you haven't defined a connection, you'll see a message such as `'connection_abc' is not defined`.

The following are some debugging steps you can try:

Review Manage connections in Apache Airflowto learn how connections work.

Make sure you have the necessary provider packages installed to be able to use a specific connection type.

Change the `_default`connection to use your connection details or define a new connection with a different name and pass the new name to the hook or operator.

Define connections using Airflow environment variables instead of adding them in the Airflow UI. Make sure you're not defining the same connection in multiple places. If you do, the environment variable takes precedence.

Test if your credentials work when used in a direct API call to the external tool.

* Test your connections using the Airflow UI or the Airflow CLI. See Testing connections.

!

noteTesting connections is disabled by default in Airflow 2.7+.



Documentation Source:
docs.astronomer.io/learn/debugging-dags.md

Documentation Title:
Debug DAGs | Astronomer Documentation

Documentation Content:
!

noteTesting connections is disabled by default in Airflow 2.7+. You can enable connection testing by defining the environment variable `AIRFLOW__CORE__TEST_CONNECTION=Enabled`in your Airflow environment. Astronomer recommends not enabling this feature until you are sure that only highly trusted UI/API users have "edit connection" permissions.

To find information about what parameters are required for a specific connection:

* Read provider documentation in the Astronomer Registryto access the Apache Airflow documentation for the provider. Most commonly used providers will have documentation on each of their associated connection types. For example, you can find information on how to set up different connections to Azure in the Azure provider docs.
* Check the documentation of the external tool you are connecting to and see if it offers guidance on how to authenticate.
* View the source code of the hook that is being used by your operator.

You can also test connections from within your IDE by using the `dag.test()`method. See Debug interactively with dag.test()and How to test and debug your Airflow connections.

I need more help​
-----------------

The information provided here should help you resolve the most common issues. If your issue was not covered in this guide, try the following resources:

* If you are an Astronomer customer contact our customer support.
* Post your question to Stack Overflow, tagged with `airflow`and other relevant tools you are using. Using Stack Overflow is ideal when you are unsure which tool is causing the error, since experts for different tools will be able to see your question.
* Join the Apache Airflow Slackand open a thread in `#newbie-questions`or `#troubleshooting`. The Airflow slack is the best place to get answers to more complex Airflow specific questions.
* If you found a bug in Airflow or one of its core providers, please open an issue in the Airflow GitHub repository. For bugs in Astronomer open source tools please open an issue in the relevant Astronomer repository.

To get more specific answers to your question, include the following information in your question or issue:

* Your method for running Airflow (Astro CLI, standalone, Docker, managed services).
* Your Airflow version and the version of relevant providers.
* The full error with the error trace if applicable.



Documentation Source:
docs.astronomer.io/learn/airflow-sql-data-quality.md

Documentation Title:
Run data quality checks using SQL check operators | Astronomer Documentation

Documentation Content:
3. Copy and paste the following DAG code into the file:

`"""## Check data quality using SQL check operatorsThis DAG creates a toy table about birds in SQLite to run data quality checks on using the SQLColumnCheckOperator, SQLTableCheckOperator, and SQLCheckOperator."""fromairflow.decorators importdagfromairflow.providers.common.sql.operators.sql import(SQLColumnCheckOperator,SQLTableCheckOperator,SQLCheckOperator,)fromairflow.providers.sqlite.operators.sqlite importSqliteOperatorfrompendulum importdatetime_CONN_ID ="sqlite_conn"_TABLE_NAME ="birds"@dag(start_date=datetime(2023,7,1),schedule=None,catchup=False,template_searchpath=["/usr/local/airflow/include/"],)defsql_data_quality():create_table =SqliteOperator(task_id="create_table",sqlite_conn_id=_CONN_ID,sql=f"""CREATE TABLE IF NOT EXISTS {_TABLE_NAME}(bird_name VARCHAR,observation_year INT,bird_happiness INT);""",)populate_data =SqliteOperator(task_id="populate_data",sqlite_conn_id=_CONN_ID,sql=f"""INSERT INTO {_TABLE_NAME}(bird_name, observation_year, bird_happiness) VALUES('King vulture (Sarcoramphus papa)', 2022, 9),('Victoria Crowned Pigeon (Goura victoria)', 2021, 10),('Orange-bellied parrot (Neophema chrysogaster)', 2021, 9),('Orange-bellied parrot (Neophema chrysogaster)', 2020, 8),(NULL, 2019, 8),('Indochinese green magpie (Cissa hypoleuca)', 2018, 10);""",)column_checks =SQLColumnCheckOperator(task_id="column_checks",conn_id=_CONN_ID,table=_TABLE_NAME,partition_clause="bird_name IS NOT NULL",column_mapping={"bird_name":{"null_check":{"equal_to":0},"distinct_check":{"geq_to":2},},"observation_year":{"max":{"less_than":2023}},"bird_happiness":{"min":{"greater_than":0},"max":{"leq_to":10}},},



