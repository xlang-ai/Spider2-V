Documentation Source:
docs.astronomer.io/astro/manage-dags.md

Documentation Title:
Manage DAG runs from the Astro UI | Astronomer Documentation

Documentation Content:
Skip to main content!!**Docs**DocsFind what you're looking forLearn About AstronomerGet Started FreeHomeAstroAstro CLISoftwareLearnTry AstroOverviewGet startedDevelopDeploy code* Manage Deployments
	Create a DeploymentDeployment settingsExecutorsWorker queuesEnvironment variablesSecrets backendManage DAG runs
Automation & CI/CDObservabilityAdministrationRelease notesBest practicesReferenceAstro APISupport Knowledge BaseOffice HoursWebinarsAstro StatusManage DeploymentsManage DAG runs
On this pageManage DAG runs from the Astro UI
=================================

You can perform some common Airflow UI actions from the Astro UI, including:

* Marking DAG and task runs as succeeded/failed.
* Retrying DAG and task runs.
* Viewing DAG and task run statuses.

These actions are available on the **DAGs**page, where you can see detailed information about a specific DAG. This page compiles the most commonly used information and actions from the Airflow UI into one place so that you can manage your DAGs without switching between the Airflow UI and Astro UI.

!Access the DAGs page in the Astro UI​
-------------------------------------

1. In the Astro UI, select a Deployment.
2. Click **DAGs**.
3. Click the name of the DAG that you want to manage.



Documentation Source:
docs.astronomer.io/learn/get-started-with-airflow.md

Documentation Title:
Get started with Apache Airflow, Part 1: Write and run your first DAG | Astronomer Documentation

Documentation Content:
To run Airflow on alternative ports, run:

`astro config setwebserver.port astro config setpostgres.port `Step 3: Log in to the Airflow UI​
---------------------------------

The Airflow UIis essential for managing Airflow. It contains information about your DAGs and is the best place to create and update Airflow connections to third-party data services.

To access the Airflow UI, open `http://localhost:8080/`in a browser and log in with `admin`for both your username and password.

The default page in the Airflow UI is the **DAGs**page, which shows an overview of all DAGs in your Airflow environment:

!Each DAG is listed with a few of its properties, including tags, owner, previous runs, schedule, timestamp of the last and next run, and the states of recent tasks. Because you haven't run any DAGs yet, the **Runs**and **Recent Tasks**sections are empty. Let's fix that!

Step 4: Trigger a DAG run​
--------------------------

The `example_astronauts`DAG in your Astro project is a simple ETL pipeline with two tasks:

* `get_astronauts`queries the Open Notify APIfor information about astronauts currently in space. The task returns the list of dictionaries containing the name and the spacecraft of all astronauts currently in space, which is passed to the second task in the DAG. This tutorial does not explain how to pass data between tasks, but you can learn more about it in the Pass data between tasksguide.
* `print_astronaut_craft`is a task that uses dynamic mapping to create and run a task instance for each Astronaut in space. Each of these tasks prints a statement about its mapped astronaut. Dynamic task mapping is a versatile feature of Airflow that allows you to create a variable number of tasks at runtime. This feature is covered in more depth in the Create dynamic Airflow tasksguide.

A **DAG run**is an instance of a DAG running on a specific date. Let's trigger a run of the `example_astronauts`DAG!

1.



Documentation Source:
docs.astronomer.io/astro/manage-dags.md

Documentation Title:
Manage DAG runs from the Astro UI | Astronomer Documentation

Documentation Content:
Available actions​

The actions and views on this page are functionally identical to certain actions in the Airflow UI. Use the following table to understand each available Astro UI action and its equivalent action in the Airflow UI.



| User action | **DAGs**page workflow | Equivalent Airflow UI workflow |
| --- | --- | --- |
| Trigger a DAG run. | Click **Run**. | Click the **Play**icon on the **DAGs**page. |
| --- | --- | --- |
| View the DAG run grid. | None. DAG code appears by default. | Click the DAG name on the **DAGs**page. |
| View the graphfor a DAG run. | None. DAG code appears by default. | Click the DAG name on the **DAGs**page, then click **Graph**. |
| View task run logs. | Click the task run in the DAG run grid, then click **Logs**. | Click the DAG name on the **DAGs**page, click the task run in the **Grid**view, then click **Logs**. |
| View DAG code. | None. DAG code appears by default. | Click the DAG name on the **DAGs**page, then click **Code**. |
| Retry a DAG run. | Click the DAG run in the DAG run grid, then click **Retry**. | Click the DAG name on the **DAGs**page, click the DAG run in the **Grid**view, then click **Clear existing tasks**. |
| Retry a task run. | Click the task run in the DAG run grid, click **Retry**, then select additional options for retrying your task(s). | Click the DAG name on the **DAGs**page, click the task run in the **Grid**view, then click **Clear**. |
| Mark a DAG/ task runas success/ failed. | Click the DAG/task run in the DAG run grid, then click **Mark as...**.



Documentation Source:
docs.astronomer.io/astro/migrate-gcc.md

Documentation Title:
Migrate to Astro from Google Cloud Composer | Astronomer Documentation

Documentation Content:
Step 10: Cut over from your source Airflow environment to Astro​
----------------------------------------------------------------

After you successfully deploy your code to Astro, you need to migrate your workloads from your source Airflow environment to Astro on a DAG-by-DAG basis. Depending on how your workloads are set up, Astronomer recommends letting DAG owners determine the order to migrate and test DAGs.

You can complete the following steps in the few days or weeks following your migration set up. Provide updates to your Astronomer Data Engineer as they continue to assist you through the process and any solve any difficulties that arise.

Continue to validate and move your DAGs until you have fully cut over your source Airflow instance. After you finish migrating from your source Airflow environment, repeat the complete migration process for any other Airflow instances in your source Airflow environment.



