Documentation Source:
docs.astronomer.io/learn/debugging-dags.md

Documentation Title:
Debug DAGs | Astronomer Documentation

Documentation Content:
This is especially relevant when running Airflow in Docker or when using the Astro CLI.
* Are your Airflow connectionsset up correctly with correct credentials? See Troubleshooting connections.
* Is the issue with all DAGs, or is it isolated to one DAG?
* Can you collect the relevant logs? For more information on log location and configuration, see the Airflow loggingguide.
* Which versions of Airflow and Airflow providers are you using? Make sure that you're using the correct version of the Airflow documentation.
* Can you reproduce the problem in a new local Airflow instance using the Astro CLI?

Answering these questions will help you narrow down what kind of issue you're dealing with and inform your next steps.

infoYou can debug your DAG code with IDE debugging tools using the `dag.test()`method. See Debug interactively with dag.test().

Airflow is not starting on the Astro CLI​
-----------------------------------------

The 3 most common ways to run Airflow locally are using the Astro CLI, running a standalone instance, or running Airflow in Docker. This guide focuses on troubleshooting the Astro CLI, which is an open source tool for quickly running Airflow on a local machine.

The most common issues related to the Astro CLI are:

* The Astro CLI was not correctly installed. Run `astro version`to confirm that you can successfully run Astro CLI commands. If a newer version is available, consider upgrading.
* The Docker Daemon is not running. Make sure to start Docker Desktop before starting the Astro CLI.
* There are errors caused by custom commands in the Dockerfile, or dependency conflicts with the packages in `packages.txt`and `requirements.txt`.
* Airflow components are in a crash-loop because of errors in custom plugins or XCom backends. View scheduler logs using `astro dev logs -s`to troubleshoot.

To troubleshoot infrastructure issues when running Airflow on other platforms, for example in Docker, on Kubernetes using the Helm Chartor on managed services, please refer to the relevant documentation and customer support.

You can learn more about testing and troubleshooting locallywith the Astro CLI in the Astro documentation.

Common DAG issues​
------------------

This section covers common issues related to DAG code that you might encounter when developing.



Documentation Source:
docs.astronomer.io/learn/testing-airflow.md

Documentation Title:
Test Airflow DAGs | Astronomer Documentation

Documentation Content:
Test DAGs in a CI/CD pipeline​

You can use CI/CD tools to test and deploy your Airflow code. By installing the Astro CLI into your CI/CD process, you can test your DAGs before deploying them to a production environment. See set up CI/CDfor example implementations.

infoAstronomer customers can use the Astro GitHub integration, which allows you to automatically deploy code from a GitHUb repository to an Astro deployment, viewing Git metadata in the Astro UI. See Deploy code with the Astro GitHub integration.

Add test data or files for local testing​
-----------------------------------------

Use the `include`folder of your Astro project to store files for testing locally, such as test data or a dbt project file. The files in your `include`folder are included in your deploys to Astro, but they are not parsed by Airflow. Therefore, you don't need to specify them in `.airflowignore`to prevent parsing.

If you're running Airflow locally, apply your changes by refreshing the Airflow UI.

Debug interactively with dag.test()​
------------------------------------

The `dag.test()`method allows you to run all tasks in a DAG within a single serialized Python process, without running the Airflow scheduler. The `dag.test()`method lets you iterate faster and use IDE debugging tools when developing DAGs.

This functionality replaces the deprecated DebugExecutor. Learn more in the Airflow documentation.



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
docs.astronomer.io/learn/testing-airflow.md

Documentation Title:
Test Airflow DAGs | Astronomer Documentation

Documentation Content:
Use `dag.test()`with the Astro CLI​

If you use the Astro CLI exclusively and do not have the `airflow`package installed locally, you can still debug using `dag.test()`by running `astro dev start`, entering the scheduler container with `astro dev bash -s`, and executing `python `from within the Docker container. Unlike using the base `airflow`package, this testing method requires starting up a complete Airflow environment.



