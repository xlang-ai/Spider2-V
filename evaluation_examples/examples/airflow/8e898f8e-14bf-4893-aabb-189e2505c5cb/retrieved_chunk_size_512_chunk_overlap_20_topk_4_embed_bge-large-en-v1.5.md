Documentation Source:
docs.astronomer.io/astro/airflow-api.md

Documentation Title:
Make requests to the Airflow REST API | Astronomer Documentation

Documentation Content:
* **Connection Id**: `http_conn`
	* **Connection Type**: HTTP
	* **Host**: ``
	* **Schema**: `https`
	* **Extras**:`{"Content-Type":"application/json","Authorization":"Bearer "}`See Manage connections in Apache Airflow.

infoIf the `HTTP`connection type is not available, double check that the HTTP provideris installed in your Airflow environment. If it's not, add `apache-airflow-providers-http`to the `requirements.txt`file of our Astro project and redeploy it to Astro.

- In your triggering DAG, add the following task. It uses the SimpleHttpOperatorto make a request to the `dagRuns`endpoint of the Deployment that contains the DAG to trigger.

`fromdatetime importdatetimefromairflow.models.dag importDAGfromairflow.providers.http.operators.http importSimpleHttpOperatorwithDAG(dag_id="triggering_dag",schedule=None,start_date=datetime(2023,1,1)):SimpleHttpOperator(task_id="trigger_external_dag",log_response=True,method="POST",# Change this to the DAG_ID of the DAG you are triggeringendpoint=f"api/v1/dags//dagRuns",http_conn_id="http_conn",data={"logical_date":"{{ logical_date }}",# if you want to add parameters:# params: '{"foo": "bar"}'})`
Was this page helpful?
----------------------

YesNoSign up for Developer Updates
-----------------------------

Get a summary of new Astro features once a month.

SubmitYou can unsubscribe at any time. By proceeding you agree to our Privacy Policy, our Website Termsand to receive emails from Astronomer.

Edit this pagePreviousUpgrade Astro RuntimeNextOverviewPrerequisitesStep 1: Retrieve your access tokenStep 2: Retrieve the Deployment URLStep 3: Make an Airflow API request* Example API Requests
	List DAGsTrigger a DAG runTrigger a DAG run by datePause a DAGTrigger DAG runs across Deployments
Legal·Privacy·Security·Cookie Preferences!!© Astronomer 2023. Various trademarks held by their respective owners.



Documentation Source:
docs.astronomer.io/learn/get-started-with-airflow-part-2.md

Documentation Title:
Get started with Apache Airflow, Part 2: Providers, connections, and variables | Astronomer Documentation

Documentation Content:
4. Enter your **GitHub Access Token**in the GitHub Access Token field. If you need to create a token, you can follow the official GitHub documentation.
5. Save the connection by clicking the **Save**button.

Note that the option to test connections is only available for selected connection types and disabled by default in Airflow 2.7+, see Test a connection.

Step 5: Create an HTTP connection​
----------------------------------

1. In the **Connections**view, click **+**to create a new connection.
2. Name the connection `open_notify_api_conn`and select a **Connection Type**of `HTTP`.
3. Enter the host URL for the API you want to query in the **Host**field. For this tutorial we use the Open Notify API, which has an endpoint returning the current location of the ISS. The host for this API is `http://api.open-notify.org`.
4. Click **Save**.

You should now have two connections as shown in the following screenshot:

!Step 6: Review the DAG code​
----------------------------

Now that your Airflow environment is configured correctly, look at the DAG code you copied from the repository to see how your new variable and connections are used at the code level.

At the top of the file, the DAG is described in a docstring. It's highly recommended to always document your DAGs and include any additional connections or variables that are required for the DAG to work.

`"""## Find the International Space StationThis DAG waits for a specific commit message to appear in a GitHub repository, and then pulls the current location of the International Space Station from an APIand print it to the logs.This DAG needs a GitHub connection with the name `my_github_conn` and an HTTP connection with the name `open_notify_api_conn`and the host `https://api.open-notify.org/` to work.Additionally you need to set an Airflow variable with the name `open_notify_api_endpoint` and the value `iss-now.json`."""`After the docstring, all necessary packages are imported. Notice how both the HttpOperator as well as the GithubSensor are part of provider packages.



Documentation Source:
docs.astronomer.io/astro/airflow-api.md

Documentation Title:
Make requests to the Airflow REST API | Astronomer Documentation

Documentation Content:
cURL​

`curl-XGET https:///api/v1/dags \-H'Cache-Control: no-cache'\-H'Authorization: Bearer '`#### Python​

`importrequeststoken =""deployment_url =""response =requests.get(url=f"https://{deployment_url}/api/v1/dags",headers={"Authorization":f"Bearer {token}"})print(response.json())# Prints data about all DAGs in your Deployment`### Trigger a DAG run​

You can trigger a DAG run by executing a `POST`request to Airflow's `dagRuns`endpoint.

This will trigger a DAG run for the DAG you specify with a `logical_date`value of `NOW()`, which is equivalent to clicking the **Play**button in the main **DAGs**view of the Airflow UI.



Documentation Source:
docs.astronomer.io/astro/airflow-api.md

Documentation Title:
Make requests to the Airflow REST API | Astronomer Documentation

Documentation Content:
cURL​

`curl-XPATCH https:///api/v1/dags/\-H'Content-Type: application/json'\-H'Cache-Control: no-cache'\-H'Authorization: Bearer '\-d'{"is_paused": true}'`#### Python​

`importrequeststoken =""deployment_url =""dag_id =""response =requests.patch(url=f"https://{deployment_url}/api/v1/dags/{dag_id}",headers={"Authorization":f"Bearer {token}","Content-Type":"application/json"},data='{"is_paused": true}')print(response.json())# Prints data about the DAG with id `### Trigger DAG runs across Deployments​

You can use the Airflow REST API to make a request in one Deployment that triggers a DAG run in a different Deployment. This is sometimes necessary when you have interdependent workflows across multiple Deployments. On Astro, you can do this for any Deployment in any Workspace or cluster.

This topic has guidelines on how to trigger a DAG run, but you can modify the example DAG provided to trigger any request that's supported in the Airflow REST API.

Create a Deployment API tokenfor the Deployment that contains the DAG you want to trigger.

2. In the Deployment that contains the triggering DAG, create an Airflow HTTP connectionwith the following values:



