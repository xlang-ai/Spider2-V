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
docs.astronomer.io/learn/airflow-sql-data-quality.md

Documentation Title:
Run data quality checks using SQL check operators | Astronomer Documentation

Documentation Content:
3. Copy and paste the following DAG code into the file:

`"""## Check data quality using SQL check operatorsThis DAG creates a toy table about birds in SQLite to run data quality checks on using the SQLColumnCheckOperator, SQLTableCheckOperator, and SQLCheckOperator."""fromairflow.decorators importdagfromairflow.providers.common.sql.operators.sql import(SQLColumnCheckOperator,SQLTableCheckOperator,SQLCheckOperator,)fromairflow.providers.sqlite.operators.sqlite importSqliteOperatorfrompendulum importdatetime_CONN_ID ="sqlite_conn"_TABLE_NAME ="birds"@dag(start_date=datetime(2023,7,1),schedule=None,catchup=False,template_searchpath=["/usr/local/airflow/include/"],)defsql_data_quality():create_table =SqliteOperator(task_id="create_table",sqlite_conn_id=_CONN_ID,sql=f"""CREATE TABLE IF NOT EXISTS {_TABLE_NAME}(bird_name VARCHAR,observation_year INT,bird_happiness INT);""",)populate_data =SqliteOperator(task_id="populate_data",sqlite_conn_id=_CONN_ID,sql=f"""INSERT INTO {_TABLE_NAME}(bird_name, observation_year, bird_happiness) VALUES('King vulture (Sarcoramphus papa)', 2022, 9),('Victoria Crowned Pigeon (Goura victoria)', 2021, 10),('Orange-bellied parrot (Neophema chrysogaster)', 2021, 9),('Orange-bellied parrot (Neophema chrysogaster)', 2020, 8),(NULL, 2019, 8),('Indochinese green magpie (Cissa hypoleuca)', 2018, 10);""",)column_checks =SQLColumnCheckOperator(task_id="column_checks",conn_id=_CONN_ID,table=_TABLE_NAME,partition_clause="bird_name IS NOT NULL",column_mapping={"bird_name":{"null_check":{"equal_to":0},"distinct_check":{"geq_to":2},},"observation_year":{"max":{"less_than":2023}},"bird_happiness":{"min":{"greater_than":0},"max":{"leq_to":10}},},



Documentation Source:
docs.astronomer.io/learn/airflow-sql-data-quality.md

Documentation Title:
Run data quality checks using SQL check operators | Astronomer Documentation

Documentation Content:
"max":{"leq_to":10}},},)table_checks =SQLTableCheckOperator(task_id="table_checks",conn_id=_CONN_ID,table=_TABLE_NAME,checks={"row_count_check":{"check_statement":"COUNT(*) >= 3"},"average_happiness_check":{"check_statement":"AVG(bird_happiness) >= 9","partition_clause":"observation_year >= 2021",},},)custom_check =SQLCheckOperator(task_id="custom_check",conn_id=_CONN_ID,sql="custom_check.sql",params={"table_name":_TABLE_NAME},)create_table >>populate_data >>[column_checks,table_checks,custom_check]sql_data_quality()`This DAG creates and populates a small SQlite table `birds`with information about birds. Then, three tasks containing data quality checks are run on the table:



Documentation Source:
docs.astronomer.io/learn/airflow-sql-data-quality.md

Documentation Title:
Run data quality checks using SQL check operators | Astronomer Documentation

Documentation Content:
Edit this pagePreviousObject storageNextUse the Astro Python SDKTime to completeAssumed knowledgePrerequisitesStep 1: Configure your Astro projectStep 2: Create a connection to SQLiteStep 3: Add a SQL file with a custom checkStep 4: Create a DAG using SQL check operators* How it works
	SQLColumnCheckOperatorSQLTableCheckOperatorSQLCheckOperator`partition_clause`
Legal·Privacy·Security·Cookie Preferences!!© Astronomer 2023. Various trademarks held by their respective owners.



