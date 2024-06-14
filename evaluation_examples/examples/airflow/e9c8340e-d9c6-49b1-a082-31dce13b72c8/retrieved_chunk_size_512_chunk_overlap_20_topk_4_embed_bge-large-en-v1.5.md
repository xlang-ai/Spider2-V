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
docs.astronomer.io/astro/first-dag-cli.md

Documentation Title:
Run your first DAG with the Astro CLI | Astronomer Documentation

Documentation Content:
If your code passes the parse, the Astro CLI deploys your DAGs to Astro. If you run into issues deploying your DAGs, check to make sure that you have the latest version of the Astro CLI. See Upgrade the CLI.

Step 5: Trigger your DAG on Astro​
----------------------------------

Newly-deployed DAGs are paused by default and will not start running automatically. To run one of the example DAGs in your Astro project according to its schedule, you must unpause it from the Airflow UI hosted on your Deployment.

In the Deployment page of the Astro UI, click the **Open Airflow**button.

2. In the main DAGs view of the Airflow UI, click the slider button next to `example-dag-basic`to unpause it. If you hover over the DAG, it says `DAG is Active`. When you do this, the DAG starts to run on the schedule that is defined in its code.

!
3. Manually trigger a DAG run of `example-dag-basic`by clicking the play button in the **Actions**column. When you develop DAGs on Astro, triggering a DAG run instead of waiting for the DAG schedule can help you quickly identify and resolve issues.

After you press **Play**, the **Runs**and **Recent Tasks**sections for the DAG start to populate with data.

!These circles represent different statesthat your DAG and task runs can be in.
Click on the name of the DAG, **example-dag-basic**, to open the **Grid**view for the DAG. To see if your DAG ran successfully, the most recent entry in the grid should have green squares for all of your tasks.

Pause your DAG by clicking the slider button next to `example-dag-basic`. This prevents your example DAG from running automatically and consuming your Deployment resources.



Documentation Source:
docs.astronomer.io/astro/release-notes.md

Documentation Title:
Astro release notes | Astronomer Documentation

Documentation Content:
Trigger a DAG from an Astro alert​

You can now configure Astro alertsto trigger any DAG in your Workspace through the Airflow REST API. You can configure the triggered DAG to complete any action, such as sending an alert through a custom communication channel or writing data about the incident to a table.



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



