Documentation Source:
docs.astronomer.io/astro/view-logs.md

Documentation Title:
View Deployment logs | Astronomer Documentation

Documentation Content:
View task logs in the Airflow UI​

- Access the Airflow UI.
* To access the Airflow UI for a Deployment, open the Deployment in the Astro UI and click **Open Airflow**.
* To access the Airflow UI in a local environment, open a browser and go to `http://localhost:8080`.
1. Click a DAG.
2. Click **Graph**.
3. Click a task run.
4. Click **Instance Details**.
5. Click **Log**.

See also​
---------

Export task logs and metrics to DatadogExport task logs to AWS CloudwatchWas this page helpful?
----------------------

YesNoSign up for Developer Updates
-----------------------------

Get a summary of new Astro features once a month.

SubmitYou can unsubscribe at any time. By proceeding you agree to our Privacy Policy, our Website Termsand to receive emails from Astronomer.

Edit this pagePreviousDeployment API keys (Deprecated)NextDAGs* Airflow Component Logs
	Airflow component log levelsView Airflow component logs in the Astro UIView Airflow component logs locally
* Airflow task logs
	Airflow task log levelsView task logs on the Astro UIView task logs in the Airflow UI
See alsoLegal·Privacy·Security·Cookie Preferences!!© Astronomer 2023. Various trademarks held by their respective owners.



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
docs.astronomer.io/learn/logging.md

Documentation Title:
Airflow logging | Astronomer Documentation

Documentation Content:
Skip to main content!!**Docs**DocsFind what you're looking forLearn About AstronomerGet Started FreeHomeAstroAstro CLISoftwareLearnTry AstroOverviewGet started* Airflow concepts
	BasicsDAGsInfrastructure+ Advanced
		Airflow loggingData qualityDeferrable operatorsDynamically generate DAGsIsolated EnvironmentsKubernetesPodOperatorMLOpsPluginsPoolsSetup/ teardown tasksSharing code between multiple projectsTest DAGs
Airflow tutorialsIntegrations & connectionsUse casesAirflow glossarySupport Knowledge BaseOffice HoursWebinarsAstro StatusAirflow conceptsAdvancedAirflow logging
On this pageAirflow logging
===============

Airflow provides an extensive logging system for monitoring and debugging your data pipelines. Your webserver, scheduler, metadata database, and individual tasks all generate logs. You can export these logs to a local file, your console, or to a specific remote storage solution.

In this guide, you'll learn the basics of Airflow logging, including:

* Where to find logs for different Airflow components.
* How to add custom task logs from within a DAG.
* When and how to configure logging settings.
* Remote logging.

You'll also use example code to:

* Send logs to an S3 bucket using the Astro CLI.
* Add multiple handlers to the Airflow task logger.

In addition to standard logging, Airflow provides observability features that you can use to collect metrics, trigger callback functions with task events, monitor Airflow health status, and track errors and user activity. For more information about the monitoring options in Airflow, see Logging & Monitoring. Astro builds on these features, providing more detailed metrics about how your tasks run and use resources in your cloud. To learn more, see Deployment metrics.

Assumed knowledge​
------------------

To get the most out of this guide, you should have an understanding of:

* Basic Airflow concepts. See Introduction to Apache Airflow.
* Airflow core components. See Airflow's components.

Airflow logging​
----------------

Logging in Airflow leverages the Python stdlib `logging`module. The `logging`module includes the following classes:

* Loggers (`logging.Logger`): The interface that the application code directly interacts with.



Documentation Source:
docs.astronomer.io/astro/runtime-release-notes.md

Documentation Title:
Astro Runtime release notes | Astronomer Documentation

Documentation Content:
Astronomer monitoring DAG​

Astro Runtime 4.0.7 includes a monitoring DAG that is pre-installed in the Docker image and enabled for all customers. In addition to existing Deployment health and metrics functionality, this DAG allows the Astronomer team to better monitor the health of your data plane by enabling real-time visibility into whether your workers are healthy and tasks are running.

The `astronomer_monitoring_dag`runs a simple bash task every 5 minutes to ensure that your Airflow scheduler and workers are functioning as expected. If the task fails twice in a row or is not scheduled within a 10-minute interval, Astronomer support receives an alert and will work with you to troubleshoot.

Because this DAG is essential to Astro's managed service, your organization will not be charged for its task runs. For the same reasons, this DAG can't be modified or disabled via the Airflow UI. To modify how frequently this DAG runs, you can specify an alternate schedule as a cron expression by setting `AIRFLOW_MONITORING_DAG_SCHEDULE_INTERVAL`as an environment variable.

Astro Runtime 4.0.6​
--------------------

* Release date: December 2, 2021
* Airflow version: 2.2.2



