Documentation Source:
docs.astronomer.io/learn/debugging-dags.md

Documentation Title:
Debug DAGs | Astronomer Documentation

Documentation Content:
DAGs are not running correctly​

If your DAGs are either not running or running differently than you intended, consider checking the following common causes:

* DAGs need to be unpaused in order to run on their schedule. You can unpause a DAG by clicking the toggle on the left side of the Airflow UI or by using the Airflow CLI.

!If you want all DAGs unpaused by default, you can set `dags_are_paused_at_creation=False`in your Airflow config. If you do this, remember to set `catchup=False`in your DAGs to prevent automatic backfilling of DAG runs. Paused DAGs are unpaused automatically when you manually trigger them.
Double check that each DAG has a unique `dag_id`. If two DAGs with the same id are present in one Airflow instance the scheduler will pick one at random every 30 seconds to display.

Make sure your DAG has a `start_date`in the past. A DAG with a `start_date`in the future will result in a successful DAG run with no task runs. Do not use `datetime.now()`as a `start_date`.

Test the DAG using `astro dev dags test `. With the Airflow CLI, run `airflow dags test `.

If no DAGs are running, check the state of your scheduler
using `astro dev logs -s`.

If too many runs of your DAG are being scheduled after you unpause it, you most likely need to set `catchup=False`in your DAG's parameters.


If your DAG is running, but not on the schedule you expected, review the DAG Schedule DAGs in Airflowguide. If you are using a custom timetable, ensure that the data interval for your DAG run does not precede the DAG start date.

Common task issues​
-------------------

This section covers common issues related to individual tasks you might encounter. If your entire DAG is not working, see the DAGs are not running correctlysection above.



Documentation Source:
docs.astronomer.io/learn/testing-airflow.md

Documentation Title:
Test Airflow DAGs | Astronomer Documentation

Documentation Content:
Setup​

To use `dag.test()`, you only need to add a few lines of code to the end of your DAG file. If you are using a traditional DAG context, call `dag.test()`after your DAG declaration. If you are using the `@dag`decorator, assign your DAG function to a new object and call the method on that object.

* Traditional DAG context
* @dag decorator

`fromairflow.models.dag importDAGfrompendulum importdatetimefromairflow.operators.empty importEmptyOperatorwithDAG(dag_id="simple_classic_dag",start_date=datetime(2023,1,1),schedule="@daily",catchup=False,)asdag:# assigning the context to an object is mandatory for using dag.test()t1 =EmptyOperator(task_id="t1")if__name__ =="__main__":dag.test()``fromairflow.decorators importdagfrompendulum importdatetimefromairflow.operators.empty importEmptyOperator@dag(start_date=datetime(2023,1,1),schedule="@daily",catchup=False,)defmy_dag():t1 =EmptyOperator(task_id="t1")dag_object =my_dag()if__name__ =="__main__":dag_object.test()`You can run the `.test()`method with popular debugging tools such as:

* VSCode.
* PyCharm.
* Tools like The Python Debuggerand the built-in `breakpoint()`function. These allow you to run `dag.test()`from the command line by running `python `.



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



