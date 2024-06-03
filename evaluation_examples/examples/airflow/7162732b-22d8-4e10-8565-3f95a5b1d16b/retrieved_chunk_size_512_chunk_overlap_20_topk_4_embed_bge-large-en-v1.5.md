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
docs.astronomer.io/learn/cleanup-dag-tutorial.md

Documentation Title:
Clean up the Airflow metadata database using DAGs | Astronomer Documentation

Documentation Content:
* `dry_run`: `true`
	* `tables`: `all_tables`
	* `clean_before_timestamp`: `datetime.now(tz=UTC) - timedelta(days=90)`
Click **Trigger**.

After the task completes, click **Graph**.

Click a task run.

Click **Instance Details**.

Click **Log**.

Check that the `airflow db cleanup`command completed successfully. Note that if you created a new Astro project for this tutorial, the run will not show much data to be deleted.


You can now use this DAG to periodically clean data from the Airflow metadata DB as needed.

Was this page helpful?
----------------------

YesNoSign up for Developer Updates
-----------------------------

Get a summary of new Astro features once a month.

SubmitYou can unsubscribe at any time. By proceeding you agree to our Privacy Policy, our Website Termsand to receive emails from Astronomer.

Edit this pagePreviousCustomize Extra LinksNextCustom XCom backendsWarningsPrerequisitesStep 1: Create your DAGStep 2: Run the DAGLegal·Privacy·Security·Cookie Preferences!!© Astronomer 2023. Various trademarks held by their respective owners.



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
docs.astronomer.io/learn/airflow-ui.md

Documentation Title:
An introduction to the Airflow UI | Astronomer Documentation

Documentation Content:
Browse tab​
-----------

The **Browse**tab links to multiple pages that provide additional insight into and control over your DAG runs and task instances for all DAGs in one place.

!The DAG runs and task instances pages are the easiest way to view and manipulate these objects in aggregate. If you need to re-run tasks in multiple DAG runs, you can do so from this page by selecting all relevant tasks and clearing their status.

!The DAG Dependencies view shows a graphical representation of any cross-DAGand dataset dependencies in your Airflow environment.

!Other views on the **Browse**tab include:

* **Jobs:**Shows a list of all jobs that have been completed. This includes executed tasks as well as scheduler jobs.
* **Audit Logs:**Shows a list of events that have occurred in your Airflow environment that can be used for auditing purposes.
* **Task Reschedules:**Shows a list of all tasks that have been rescheduled.
* **Triggers:**Shows any triggers that occurred in this Airflow environment. To learn more about triggers and related concepts, you can check out the guide on Deferrable Operators.
* **SLA Misses:**Shows any task instances that have missed their SLAs.

Admin tab​
----------

The **Admin**tab links to pages for content related to Airflow administration that are not specific to any particular DAG. Many of these pages can be used to both view and modify your Airflow environment.

!For example, the **Connections**page shows all Airflow connections stored in your environment. Click `+`to add a new connection. For more information, see Managing your Connections in Apache Airflow.

!Similarly, the XComs page shows a list of all XComs stored in the metadata database and allows you to easily delete them.

!Other pages on the **Admin**tab include:

* **Variables:**View and manage Airflow variables.
* **Configurations:**View the contents of your `airflow.cfg`file. Note that this can be disabled by your Airflow admin for security reasons.
* **Plugins:**View any Airflow pluginsdefined in your environment.
* **Providers:**View all Airflow providersincluded in your Airflow environment with their version number.
* **Pools:**View and manage Airflow pools.



