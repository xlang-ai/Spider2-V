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
docs.astronomer.io/learn/airflow-ui.md

Documentation Title:
An introduction to the Airflow UI | Astronomer Documentation

Documentation Content:
Audit Logs​

The **Audit Logs**tab shows a list of events that have occurred in your Airflow environment relating to the DAG, DAG run or task instance you have selected.

!### Run Duration​

The **Run Duration**tab shows a bar chart of the duration of each DAG run over time.

!### Logs​

To access the logsof a specific task instance, click on the **Logs**tab which appears as soon as you select a task instance. By default the logs of the task execution are shown, while the **Pre task execution logs**and the **Post task execution logs**are collapsed and can be expanded by clicking on the respective log item.

!Cluster activity tab​
---------------------

The cluster activity tab shows aggregated metrics for the entire Airflow cluster. It includes live metrics, such as currently occupied slots in different pools, unpaused DAGs, and scheduler health.
It also includes historical metrics like the states of past DAG runs and task instances, as well as how each DAG run was triggered.

!Datasets tab​
-------------

The **Dataset**tab links to a page showing all datasets that have been produced in the Airflow environment, as well as all dependencies between datasets and DAGs in a graph.

!Click a dataset to open the history of all updates to the dataset that were recorded in the Airflow environment. You can use the Play button to manually trigger an update to a Dataset.

!Security tab​
-------------

Astro does not support the Security tabOn Astro, role-based access control is managed at the platform level. As a result, the Security tab is not needed and is not available on Airflow deployments on Astro.

The **Security**tab links to multiple pages, including **List Users**and **List Roles**, that you can use to review and manage Airflow role-based access control (RBAC). For more information on working with RBAC, see Security.

!If you are running Airflow on Astronomer, the Astronomer RBAC will extend into Airflow and take precedence. There is no need for you to use Airflow RBAC in addition to Astronomer RBAC. Astronomer RBAC can be managed from the Astronomer UI, so the **Security**tab might be less relevant for Astronomer users.



Documentation Source:
docs.astronomer.io/learn/get-started-with-airflow.md

Documentation Title:
Get started with Apache Airflow, Part 1: Write and run your first DAG | Astronomer Documentation

Documentation Content:
After your DAG runs, there should be a green bar representing a successful run of the DAG.

!
The `my_astronauts_dag`is scheduled to run whenever the `current_astronauts`dataset is updated by a successful run of the `get_astronauts`task in the `example_astronauts`DAG. Trigger another manual run of the `example_astronauts`DAG to see the `my_astronauts_dag`run again after the `get_astronauts`task completes.


Step 8: View task logs​
-----------------------

When one of your tasks prints something, the output appears in Airflow task logs. Task logs are an important feature for troubleshooting DAGs. If a task in your DAG fails, task logs are the best place to investigate why.

1. In the Airflow UI, open the **Grid**view.
2. Click the `print_num_people_in_space`task to access details of the task instance.
3. Click the **Logs**tab.

In the log output, you should see the statement telling you about the number of people currently in space. The log output should look similar to the following:

`[2024-02-27, 13:57:07 UTC] {logging_mixin.py:188} INFO - There are currently 7 people in space.[2024-02-27, 13:57:07 UTC] {python.py:202} INFO - Done. Returned value was: None[2024-02-27, 13:57:07 UTC] {taskinstance.py:1149} INFO - Marking task as SUCCESS. dag_id=my_astronauts_dag, task_id=print_num_people_in_space, execution_date=20240227T135707, start_date=20240227T135707, end_date=20240227T135707`Repeat steps 1-3 for the `print_reaction`task.



Documentation Source:
docs.astronomer.io/astro/view-logs.md

Documentation Title:
View Deployment logs | Astronomer Documentation

Documentation Content:
View Airflow component logs locally​

To show logs for your Airflow scheduler, webserver, or triggerer locally, run the following Astro CLI command:

astro dev logsAfter you run this command, the most recent logs for these components appear in your terminal window.

By default, running `astro dev logs`shows logs for all Airflow components. To see logs only for a specific component, add any of the following flags to your command:

`--scheduler``--webserver``--triggerer`
To continue monitoring logs, run `astro dev logs --follow`. The `--follow`flag ensures that the latest logs continue to appear in your terminal window. For more information about this command, see CLI Command Reference.

Airflow task logs​
------------------

Airflow task logs can help you troubleshoot a specific task instance that failed or retried. Based on your preference, you can choose to use to access task logs in the Astro UI or the Airflow UI. Both provide filters, search, and download options for task logs and share other information about your DAG performance on the same page.

Task logs for Astro Deployments are retained for 90 days. The task log retention policy is not currently configurable.

You can also access local Airflow task logs in your local Airflow UIor printed to the terminal.



