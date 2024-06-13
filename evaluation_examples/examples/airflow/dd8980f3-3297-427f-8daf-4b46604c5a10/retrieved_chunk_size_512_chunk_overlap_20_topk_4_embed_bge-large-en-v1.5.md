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
Why use Airflow with dbt Core?​
-------------------------------

dbt Core offers the possibility to build modular, reuseable SQL components with built-in dependency management and incremental builds. With Cosmosyou can integrate dbt jobs into your Airflow orchestration environment as a standalone DAG or as a task group within a DAG.

The benefits of using Airflow with dbt Core include:

* Use Airflow's data-aware schedulingand Airflow sensorsto run models depending on other events in your data ecosystem.
* Turn each dbt model into a task, complete with Airflow features like retriesand error notifications, as well as full observability into past runs directly in the Airflow UI.
* Run `dbt test`on tables created by individual models immediately after a model has completed. Catch issues before moving downstream and integrate additional data quality checkswith your preferred tool to run alongside dbt tests.
* Run dbt projects using Airflow connectionsinstead of dbt profiles. You can store all your connections in one place, directly within Airflow or by using a secrets backend.
* Leverage native support for installing and running dbt in a virtual environment to avoid dependency conflicts with Airflow.

Time to complete​
-----------------

This tutorial takes approximately 30 minutes to complete.

Assumed knowledge​
------------------

To get the most out of this tutorial, make sure you have an understanding of:

* The basics of dbt Core. See What is dbt?.
* Airflow fundamentals, such as writing DAGs and defining tasks. See Get started with Apache Airflow.
* How Airflow and dbt concepts relate to each other. See Similar dbt & Airflow concepts.
* Airflow operators. See Operators 101.
* Airflow task groups. See Airflow task groups.
* Airflow connections. See Manage connections in Apache Airflow.

Prerequisites​
--------------

* The Astro CLI.
* Access to a data warehouse supported by dbt Core. See dbt documentationfor all supported warehouses. This tutorial uses a Postgres database.

You do not need to have dbt Core installed locally in order to complete this tutorial.



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



