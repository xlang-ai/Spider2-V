Documentation Source:
docs.astronomer.io/learn/airflow-dbt.md

Documentation Title:
Orchestrate dbt Core jobs with Airflow and Cosmos | Astronomer Documentation

Documentation Content:
Step 4: Write your Airflow DAG​
-------------------------------

The DAG you'll write uses Cosmos to create tasks from existing dbt models and the PostgresOperatorto query a table that was created. You can add more upstream and downstream tasks to embed the dbt project within other actions in your data ecosystem.

In your `dags`folder, create a file called `my_simple_dbt_dag.py`.

2. Copy and paste the following DAG code into the file:

`"""### Run a dbt Core project as a task group with CosmosSimple DAG showing how to run a dbt project as a task group, usingan Airflow connection and injecting a variable into the dbt project.



Documentation Source:
docs.astronomer.io/learn/airflow-dbt.md

Documentation Title:
Orchestrate dbt Core jobs with Airflow and Cosmos | Astronomer Documentation

Documentation Content:
In the `my_simple_dbt_project`folder add your `dbt_project.yml`. This configuration file needs to contain at least the name of the project. This tutorial additionally shows how to inject a variable called `my_name`from Airflow into your dbt project.

`name:'my_simple_dbt_project'vars:my_name:"No entry"`
4. Add your dbt models in a subfolder called `models`in the `my_simple_dbt_project`folder. You can add as many models as you want to run. This tutorial uses the following two models:

`model1.sql`:

SELECT'{{ var("my\_name") }}'asname`model2.sql`:

SELECT\*FROM{{ ref('model1')}}`model1.sql`selects the variable `my_name`. `model2.sql`depends on `model1.sql`and selects everything from the upstream model.

You should now have the following structure within your Astro project:

`.└── dags└── dbt└── my_simple_dbt_project├── dbt_project.yml└── models├── model1.sql└── model2.sql`Step 3: Create an Airflow connection to your data warehouse​
------------------------------------------------------------

Cosmos allows you to apply Airflow connections to your dbt project.

Start Airflow by running `astro dev start`.

In the Airflow UI, go to **Admin**-> **Connections**and click **+**.

3. Create a new connection named `db_conn`. Select the connection type and supplied parameters based on the data warehouse you are using. For a Postgres connection, enter the following information:


	* **Connection ID**: `db_conn`.
	* **Connection Type**: `Postgres`.
	* **Host**: Your Postgres host address.
	* **Schema**: Your Postgres database.
	* **Login**: Your Postgres login username.
	* **Password**: Your Postgres password.
	* **Port**: Your Postgres port.

infoIf a connection type for your database isn't available, you might need to make it available by adding the relevant provider packageto `requirements.txt`and running `astro dev restart`.



Documentation Source:
docs.astronomer.io/learn/airflow-dbt.md

Documentation Title:
Orchestrate dbt Core jobs with Airflow and Cosmos | Astronomer Documentation

Documentation Content:
This DAG injects `YOUR_NAME`for the `my_name`variable. If your dbt project contains dbt tests, they will be run directly after a model has completed. Note that it is a best practice to set `retries`to at least 2 for all tasks that run dbt models.

tipIn some cases, especially in larger dbt projects, you might run into a `DagBag import timeout`error.
This error can be resolved by increasing the value of the Airflow configuration core.dagbag\_import\_timeout.

1. Run the DAG manually by clicking the play button and view the DAG in the graph view. Double click the task groups in order to expand them and see all tasks.

!
Check the XComreturned by the `query_table`task to see your name in the `model2`table.


infoThe DbtTaskGroup class populates an Airflow task group with Airflow tasks created from dbt models inside of a normal DAG. To directly define a full DAG containing only dbt models use the `DbtDag`class, as shown in the Cosmos documentation.

Congratulations! You've run a DAG using Cosmos to automatically create tasks from dbt models. You can learn more about how to configure Cosmos in the Cosmos documentation.

Alternative ways to run dbt Core with Airflow​
----------------------------------------------

While using Cosmos is recommended, there are several other ways to run dbt Core with Airflow.



Documentation Source:
docs.astronomer.io/learn/airflow-dbt-cloud.md

Documentation Title:
Orchestrate dbt Cloud jobs with Airflow | Astronomer Documentation

Documentation Content:
View the dbt documentationfor an up-to-date list of adapters.

Step 1: Configure your Astro project​
-------------------------------------

An Astro project contains all of the files you need to run Airflow locally.

1. Create a new Astro project:

`$ mkdirastro-dbt-cloud-tutorial &&cdastro-dbt-cloud-tutorial$ astro dev init`
2. Add the dbt Cloud providerto your `requirements.txt`file.

apache-airflow-providers-dbt-cloud
3. Run the following command to start your Astro project:

$ astro dev start

Step 2: Configure a dbt connection​
-----------------------------------

In the Airflow UI, go to **Admin**-> **Connections**and click **+**.

2. Create a new connection named `dbt_conn`and choose the `dbt Cloud`connection type. Configure the following values for the connection:


	* **Tenant**: The URL under which your API cloud is hosted. The default value is `cloud.getdbt.com`.
	* **Account ID**: (Optional) The default dbt account to use with this connection.
	* **API Token**: A dbt user token.

Step 3: Configure a dbt Cloud job​
----------------------------------

In the dbt Cloud UI, create one dbt Cloud job. The contents of this job do not matter for this tutorial. Optionally, you can use the jaffle shop example from dbt's Quickstart documentation. Copy the dbt Cloud `job_id`for use in the next step.

Step 4: Write a dbt Cloud DAG​
------------------------------

In your `dags`folder, create a file called `check_before_running_dbt_cloud_job.py`.

2. Copy the following code into the file, making sure to replace ``with the `job_id`you copied.



