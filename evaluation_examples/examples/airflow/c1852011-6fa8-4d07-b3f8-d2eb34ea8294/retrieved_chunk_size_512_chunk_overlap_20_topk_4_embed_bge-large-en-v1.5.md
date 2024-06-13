Documentation Source:
docs.astronomer.io/learn/custom-airflow-ui-docs-tutorial.md

Documentation Title:
Create DAG documentation in Apache Airflow | Astronomer Documentation

Documentation Content:
!Conclusion​
-----------

Congratulations! You now know how to add fancy documentation to both your DAGs and your Airflow tasks.

Was this page helpful?
----------------------

YesNoSign up for Developer Updates
-----------------------------

Get a summary of new Astro features once a month.

SubmitYou can unsubscribe at any time. By proceeding you agree to our Privacy Policy, our Website Termsand to receive emails from Astronomer.

Edit this pagePreviousUse the Astro Python SDKNextIntegrations & connectionsTime to completeAssumed knowledgePrerequisitesStep 1: Create an Astro projectStep 2: Create a new DAGStep 3: Add docs to your DAGStep 4: Add docs to a taskStep 5: Add notes to a task instance and DAG runConclusionLegal·Privacy·Security·Cookie Preferences!!© Astronomer 2023. Various trademarks held by their respective owners.



Documentation Source:
docs.astronomer.io/learn/custom-airflow-ui-docs-tutorial.md

Documentation Title:
Create DAG documentation in Apache Airflow | Astronomer Documentation

Documentation Content:
Add the following code containing reStructuredText:

`doc_rst_task ="""===========This feature is pretty neat===========* there are many ways to add docs* luckily Airflow supports a lot of them.. note:: `Learn more about rst here! `__"""`
Create a task definition as shown in the following snippet. The task definition includes parameters for specifying each of the documentation strings you created. Pick the coding style you're most comfortable with.


* TaskFlow API
* Traditional syntax

`@task(doc_md=doc_md_task,doc=doc_monospace_task,doc_json=doc_json_task,doc_yaml=doc_yaml_task,doc_rst=doc_rst_task)deftell_me_what_to_do():response =requests.get("https://www.boredapi.com/api/activity")returnresponse.json()["activity"]tell_me_what_to_do()``tell_me_what_to_do =PythonOperator(task_id="tell_me_what_to_do",python_callable=query_api,doc_md=doc_md_task,doc=doc_monospace_task,doc_json=doc_json_task,doc_yaml=doc_yaml_task,doc_rst=doc_rst_task)`Go to the Airflow UI and run your DAG.

In the **Grid**view, click on the green square for your task instance.

3. Click on **Task Instance Details**.

!
4. See the docs under their respective attribute:

!

Step 5: Add notes to a task instance and DAG run​
-------------------------------------------------

You can add notes to task instances and DAG runs from the **Grid**view in the Airflow UI. This feature is useful if you need to share contextual information about a DAG or task run with your team, such as why a specific run failed.

Go to the **Grid View**of the `docs_example_dag`DAG you created in Step 2.

Select a task instance or DAG run.

Click **Details**> **Task Instance Notes**or **DAG Run notes**> **Add Note**.

Write a note and click **Save Note**.



Documentation Source:
docs.astronomer.io/learn/custom-airflow-ui-docs-tutorial.md

Documentation Title:
Create DAG documentation in Apache Airflow | Astronomer Documentation

Documentation Content:
Copy and paste one of the following DAGs based on which coding style you're most comfortable with.


* TaskFlow API
* Traditional syntax

`fromairflow.decorators importtask,dagfrompendulum importdatetimeimportrequests@dag(start_date=datetime(2022,11,1),schedule="@daily",catchup=False)defdocs_example_dag():@taskdeftell_me_what_to_do():response =requests.get("https://www.boredapi.com/api/activity")returnresponse.json()["activity"]tell_me_what_to_do()docs_example_dag()``fromairflow.models.dag importDAGfromairflow.operators.python importPythonOperatorfrompendulum importdatetimeimportrequestsdefquery_api():response =requests.get("https://www.boredapi.com/api/activity")returnresponse.json()["activity"]withDAG(dag_id="docs_example_dag",start_date=datetime(2022,11,1),schedule=None,catchup=False,):tell_me_what_to_do =PythonOperator(task_id="tell_me_what_to_do",python_callable=query_api,)`This DAG has one task called `tell_me_what_to_do`, which queries an APIthat provides a random activity for the day and prints it to the logs.

Step 3: Add docs to your DAG​
-----------------------------

You can add Markdown-based documentation to your DAGs that will render in the **Grid**, **Graph**and **Calendar**pages of the Airflow UI.

1. In your `docs_example_dag.py`file, add the following doc string above the definition of your DAG:

`doc_md_DAG ="""### The Activity DAGThis DAG will help me decide what to do today. It uses the BoredAPI to do so.Before I get to do the activity I will have to:- Clean up the kitchen.- Check on my pipelines.- Water the plants.Here are some happy plants:"""`This doc string is written in Markdown. It includes a title, a link to an external website, a bulleted list, as well as an image which has been formatted using HTML. To learn more about Markdown, see The Markdown Guide.
Add the documentation to your DAG by passing `doc_md_DAG`to the `doc_md`parameter of your DAG class as shown in the code snippet below:



Documentation Source:
docs.astronomer.io/learn/custom-airflow-ui-docs-tutorial.md

Documentation Title:
Create DAG documentation in Apache Airflow | Astronomer Documentation

Documentation Content:
* TaskFlow API
* Traditional syntax

`@dag(start_date=datetime(2022,11,1),schedule="@daily",catchup=False,doc_md=doc_md_DAG)defdocs_example_dag():``withDAG(dag_id="docs_example_dag",start_date=datetime(2022,11,1),schedule="@daily",catchup=False,doc_md=doc_md_DAG):`- Go to the **Grid**view and click on the **DAG Docs**banner to view the rendered documentation.

!
tipAirflow will automatically pick up a doc string written directly beneath the definition of the DAG context and add it as **DAG Docs**.
Additionally, using `with DAG():`lets you pass the filepath of a markdown file to the `doc_md`parameter. This can be useful if you want to add the same documentation to several of your DAGs.

Step 4: Add docs to a task​
---------------------------

You can also add docs to specific Airflow tasks using Markdown, Monospace, JSON, YAML or reStructuredText. Note that only Markdown will be rendered and other formats will be displayed as rich content.

To add documentation to your task, follow these steps:

1. Add the following code with a string in Markdown format:

`doc_md_task ="""### Purpose of this taskThis task **boldly** suggests a daily activity."""`
2. Add the following code with a string written in monospace format:

`doc_monospace_task ="""If you don't like the suggested activity you can always just go to the park instead."""`
3. Add the following code with a string in JSON format:

`doc_json_task ="""{"previous_suggestions": {"go to the gym": ["frequency": 2, "rating": 8],"mow your lawn": ["frequency": 1, "rating": 2],"read a book": ["frequency": 3, "rating": 10],}}"""`
4. Add the following code with a string written in YAML format:

`doc_yaml_task ="""clothes_to_wear: sportsgear: |- climbing: true- swimming: false"""`
5.



