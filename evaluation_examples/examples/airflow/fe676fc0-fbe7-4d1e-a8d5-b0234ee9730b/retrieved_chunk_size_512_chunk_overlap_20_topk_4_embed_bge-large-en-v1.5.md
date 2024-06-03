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
* The full error with the error trace if applicable.
* The full code of the DAG causing the error if applicable.
* What you are trying to accomplish in as much detail as possible.
* What you changed in your environment when the problem started.
Was this page helpful?
----------------------

YesNoSign up for Developer Updates
-----------------------------

Get a summary of new Astro features once a month.

SubmitYou can unsubscribe at any time. By proceeding you agree to our Privacy Policy, our Website Termsand to receive emails from Astronomer.

Edit this pagePreviousDAG writing best practicesNextDynamic tasksAssumed knowledgeGeneral Airflow debugging approachAirflow is not starting on the Astro CLI* Common DAG issues
	DAGs don't appear in the Airflow UIImport errors due to dependency conflictsDAGs are not running correctly
* Common task issues
	Tasks are not running correctlyTasks are failingIssues with dynamically mapped tasks
Missing LogsTroubleshooting connectionsI need more helpLegal·Privacy·Security·Cookie Preferences!!© Astronomer 2023. Various trademarks held by their respective owners.



Documentation Source:
docs.astronomer.io/learn/airflow-databricks.md

Documentation Title:
Orchestrate Databricks jobs with Airflow | Astronomer Documentation

Documentation Content:
Repairing a Databricks Workflow​

The Astro Databricks provider includes functionality to repair a failed Databricks Workflow by making a repair request to the Databricks Jobs API. Databricks expects a single repair request for all tasks that need to be rerun in one cluster, this can be achieved via the Airflow UI by using the operator extra link **Repair All Failed Tasks**. If you would be using Airflow's built in retry functionalitya separete cluster would be created for each failed task.

!If you only want to rerun specific tasks within your Workflow, you can use the **Repair a single failed task**operator extra link on an individual task in the Databricks Workflow.

!Alternative ways to run Databricks with Airflow​
------------------------------------------------

The Astro Databricks provider is under active development, and support for more Databricks task types is still being added. If you want to orchestrate an action in your Databricks environment that is not yet supported by the Astro Databricks provider such as updating a Databricks repository, check the community-managed Databricks providerfor relevant operators.

Additionally, the community-managed Databricks provider contains hooks (for example the DatabricksHook) that simplify interaction with Databricks, including writing your own custom Databricks operators.

You can find several example DAGs that use the community-managed Databricks provider on the Astronomer Registry.

Was this page helpful?
----------------------

YesNoSign up for Developer Updates
-----------------------------

Get a summary of new Astro features once a month.

SubmitYou can unsubscribe at any time. By proceeding you agree to our Privacy Policy, our Website Termsand to receive emails from Astronomer.

**Tags:**IntegrationsDAGsEdit this pagePreviousConnectionNextdbt CloudWhy use Airflow with DatabricksTime to completeAssumed knowledgePrerequisitesStep 1: Configure your Astro projectStep 2: Create Databricks NotebooksStep 3: Configure the Databricks connectionStep 4: Create your DAG* How it works
	ParametersRepairing a Databricks Workflow
Alternative ways to run Databricks with AirflowLegal·Privacy·Security·Cookie Preferences!!© Astronomer 2023. Various trademarks held by their respective owners.



