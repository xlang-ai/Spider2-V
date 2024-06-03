Documentation Source:
docs.astronomer.io/learn/operator-extra-link-tutorial.md

Documentation Title:
Customize Operator Extra Links | Astronomer Documentation

Documentation Content:
This link will appear on every task instance created by this operator.

Create a new Python file named `plugin_test_dag.py`in the `dags`folder of your Airflow project.

2. Copy and paste the following DAG code into your file:

`fromairflow.models.dag importDAGfromairflow.providers.http.operators.http importSimpleHttpOperatorfrompendulum importdatetimewithDAG(dag_id="plugin_test_dag",start_date=datetime(2022,11,1),schedule=None,catchup=False):call_api_simple =SimpleHttpOperator(task_id="call_api_simple",http_conn_id="random_user_api_conn",method="GET")`

This DAG has one SimpleHttpOperator task that posts a GET request to an API as defined in the `random_user_api_conn`connection.

Step 3: Add a static operator extra link​
-----------------------------------------

Create an Airflow pluginto add an extra link to the operator.

Create a new Python file named `my_extra_link_plugin.py`in the `plugins`folder of your Airflow project.

2. Copy paste the following code into your file.

`fromairflow.plugins_manager importAirflowPluginfromairflow.models.baseoperator importBaseOperatorLinkfromairflow.providers.http.operators.http importSimpleHttpOperator# define the extra linkclassHTTPDocsLink(BaseOperatorLink):# name the link button in the UIname ="HTTP docs"# add the button to one or more operatorsoperators =[SimpleHttpOperator]# provide the linkdefget_link(self,operator,*,ti_key=None):return"https://developer.mozilla.org/en-US/docs/Web/HTTP"# define the plugin classclassAirflowExtraLinkPlugin(AirflowPlugin):name ="extra_link_plugin"operator_extra_links =[HTTPDocsLink(),]`

This script accomplishes the following:

* Defines an operator extra link called `HTTPDocsLink`which will create an extra link button with the name `HTTP docs`. Customize this string to change the name on the button displayed in the UI.
* Adds the `SimpleHttpOperator`to the list of operators this extra link will be applied to. You can add as many operators as you'd like, including custom operators.
* Defines the `get_link()`method which determines the website the operator extra link will link to.



Documentation Source:
docs.astronomer.io/learn/operator-extra-link-tutorial.md

Documentation Title:
Customize Operator Extra Links | Astronomer Documentation

Documentation Content:
You can change this function to any Python function that returns a valid link. See Step 9for instructions on how to make this link dynamically change between task instances.
* Creates an instance of the `AirflowPlugin`class which will be automatically picked up by Airflow to install the plugin named `extra_link_plugin`in your Airflow instance.
* Adds the `HTTPDocsLink`plugin to the `extra_link_plugin`. You can add several operator extra links to the same Airflow plugin.

Step 4: Add an HTTP connection​
-------------------------------

Run `astro dev start`in your Astro project directory to start up Airflow. If your Airflow instance is already running, use `astro dev restart`to restart it in order to load any changes made in the `plugins`folder.

2. Add an HTTP connection called `random_user_api_conn`to `http://randomuser.me/api/`in the Airflow UI. This API will return data about a randomly generated user persona. Feel free to use a different API, the content returned will not be relevant for this tutorial. Learn more about connections in the Manage connections in Apache Airflowguide.

!

Step 5: Use your static operator extra link​
--------------------------------------------

Run the `plugins_test_dag`.

2. In the **Grid**view, click the green square representing the successful run of the `call_api_simple`task. Select the **Details**tab and scroll down to see the extra link button called **HTTP docs**.

!
Click on the button to visit the HTTP docs on Mozilla.



Documentation Source:
docs.astronomer.io/learn/operator-extra-link-tutorial.md

Documentation Title:
Customize Operator Extra Links | Astronomer Documentation

Documentation Content:
Step 10: See your new extra link in action​
-------------------------------------------

Your second extra link has now been added to the CatHttpOperator.

In the Airflow UI, run `plugins_test_dag`again.

Navigate to the Graph View and click on the `call_api_cat`task.

3. Click the HTTP Cat button to find the response of your last API call illustrated with a fitting cat.

!
4. (Optional) See all your plugins listed under **Admin**-> **Plugins**.

!

Conclusion​
-----------

Congratulations! You added two operator extra links as an Airflow plugin. On the way you also learned how to modify an existing operator to pass an additional value to XCom.

tipExtra links can be also be added to operators when creating an Airflow provider. If you want to add an operator extra link to a custom operator as part of a provider package, make sure you install it with the rest of the package using a setup.py file or `wheels`.

In general, adding an operator extra link via plugin as described in this tutorial is easier for use in a limited number of Airflow instances. However, if you are planning to use the extra link in a large number of deployments, consider adding them to an Airflow provider instead.

Was this page helpful?
----------------------

YesNoSign up for Developer Updates
-----------------------------

Get a summary of new Astro features once a month.

SubmitYou can unsubscribe at any time. By proceeding you agree to our Privacy Policy, our Website Termsand to receive emails from Astronomer.

Edit this pagePreviousCreate Airflow listenersNextClean up the metadata databaseTime to completeAssumed knowledgePrerequisitesStep 1: Create an Astro projectStep 2: Create a DAG using the SimpleHttpOperatorStep 3: Add a static operator extra linkStep 4: Add an HTTP connectionStep 5: Use your static operator extra linkStep 6: Create a custom operatorStep 7: Create a DAG with your custom operatorStep 8: Run your DAG and view modified XComsStep 9: Add a dynamic extra link to your custom operatorStep 10: See your new extra link in actionConclusionLegal·Privacy·Security·Cookie Preferences!!© Astronomer 2023. Various trademarks held by their respective owners.



Documentation Source:
docs.astronomer.io/astro/create-and-link-connections.md

Documentation Title:
Create Airflow connections in the Astro UI | Astronomer Documentation

Documentation Content:
Link connections to Deployments​
--------------------------------

After you create a connection at the Workspace level, you can link it to multiple Deployments. Linking connections is useful for standardizing external resource usage across your entire team.

For the most flexibility, you can set default connections and override the connection details per-Deployment based on details like the Deployment's usage and environment type (production or development).



