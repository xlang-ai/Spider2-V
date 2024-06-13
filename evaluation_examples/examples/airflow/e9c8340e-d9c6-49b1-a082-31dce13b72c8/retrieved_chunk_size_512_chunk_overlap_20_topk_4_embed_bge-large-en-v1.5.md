Documentation Source:
docs.astronomer.io/astro/release-notes.md

Documentation Title:
Astro release notes | Astronomer Documentation

Documentation Content:
Trigger a DAG from an Astro alert​

You can now configure Astro alertsto trigger any DAG in your Workspace through the Airflow REST API. You can configure the triggered DAG to complete any action, such as sending an alert through a custom communication channel or writing data about the incident to a table.



Documentation Source:
docs.astronomer.io/learn/get-started-with-airflow.md

Documentation Title:
Get started with Apache Airflow, Part 1: Write and run your first DAG | Astronomer Documentation

Documentation Content:
Let's trigger a run of the `example_astronauts`DAG!

1. Before you can trigger a DAG run in Airflow, you have to unpause the DAG. To unpause `example_astronauts`, click the slider button next to its name. Once you unpause it, the DAG starts to run on the schedule defined in its code.

!
While all DAGs can run on a schedule defined in their code, you can manually trigger a DAG run at any time from the Airflow UI. Manually trigger `example_astronauts`by clicking the play button under the **Actions**column. During development, running DAGs on demand can help you identify and resolve issues.


After you press **Play**, the **Runs**and **Recent Tasks**sections for the DAG start to populate with data.

!These circles represent different statesthat your DAG and task runs can be in. However, these are only high-level summaries of your runs that won't make much sense until you learn more about how Airflow works. To get a better picture of how your DAG is running, let's explore some other views in Airflow.

Step 5: Explore the Airflow UI​
-------------------------------

The navigation bar in the Airflow UI contains tabs with different information about your Airflow environment. For more information about what you can find in each tab, see The Airflow UI.

Let's explore the available views in the **DAGs**page. To access different DAG views for `example_astronauts`:

1. Click the name of the DAG to access the **Grid**view, which shows the status of running and completed tasks.

Each column in the grid represents a complete DAG run, and each block in the column represents a specific task instance. This view is useful for seeing DAG runs over time and troubleshooting previously failed task instances.

!Click on a green square to display additional information about the related task instance on the right side of the Airflow UI. The task instance view includes tabs with additional information for the task instance, such as its logs and historic runs. This is one of many available views that show details about your DAG.



Documentation Source:
docs.astronomer.io/astro/alerts74bb.md

Documentation Title:
Set up Astro alerts | Astronomer Documentation

Documentation Content:
* `note`: By default, this is `Triggering DAG on Airflow `.
The following is an example alert payload that would be passed through the API:

`{"dagName":"fail_dag","alertType":"PIPELINE_FAILURE","alertId":"d75e7517-88cc-4bab-b40f-660dd79df216","message":"[Astro Alerts] Pipeline failure detected on DAG fail_dag. \\nStart time: 2023-11-17 17:32:54 UTC. \\nFailed at: 2023-11-17 17:40:10 UTC. \\nAlert notification time: 2023-11-17 17:40:10 UTC. \\nClick link to investigate in Astro UI: https://cloud.astronomer.io/clkya6zgv000401k8zafabcde/dags/clncyz42l6957401bvfuxn8zyxw/fail_dag/c6fbe201-a3f1-39ad-9c5c-817cbf99d123?utm_source=alert\"\\n"}`These parameters are accessible in the triggered DAG using DAG params.

- Create a DAG that you want to run when the alert is triggered. For example, you can use the following DAG to run arbitrary Python code when the alert is triggered:
`importdatetimefromtyping importAnyfromairflow.models.dag importDAGfromairflow.operators.python importPythonOperatorwithDAG(dag_id="register_incident",start_date=datetime.datetime(2023,1,1),schedule=None,):def_register_incident(params:dict[str,Any]):failed_dag =params["dagName"]print(f"Register an incident in my system for DAG {failed_dag}.")PythonOperator(task_id="register_incident",python_callable=_register_incident)`Deploy the DAG to any Deployment in the Workspace where you want to create the alert. The DAG that triggers the alert and the DAG that the alert runs can be in different Deployments, but they must be deployed in the same Workspace.

Create a Deployment API tokenfor the Deployment where you deployed the DAG that the alert will run. Copy the token to use in the next step.



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



