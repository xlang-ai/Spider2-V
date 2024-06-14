Documentation Source:
airbyte.com/quickstart/airbyte-dbt-and-airflow-stack-with-bigquery.md

Documentation Title:
E-commerce Analytics Stack with Airbyte, dbt, Airflow (ADA) and BigQuery | Airbyte

Documentation Content:
3.2. Setting Up Airbyte Connectors Using the UI

Start by launching the Airbyte UI by going to http://localhost:8000/in your browser. Then:

**1. Create a source**:

1. Go to the "Sources" tab and click on "+ New source".
2. Search for “faker” using the search bar and select "Sample Data (Faker)".
3. Adjust the count and optional fields as needed for your use case. You can also leave as is.
4. Click on "Set up source".

**2. Create a destination**:

1. Go to the "Destinations" tab and click on "+ New destination".
2. Search for “bigquery” using the search bar and select BigQuery.
3. Enter the connection details as needed.
4. For simplicity, you can use "Standard Inserts" as the loading method.
5. In the Service Account Key JSON field, enter the contents of the JSON file. Yes, the full JSON.
6. Click on Set up destination.

**3. Create a connection**:

1. Go to the "Connections" tab and click on "+ New connection".
2. Select the source and destination you just created.
3. Enter the connection details as needed.
4. Click on "Set up connection".

That’s it! Your connection is set up and ready to go! 🎉 

4. Setting Up the dbt Project
-----------------------------

dbt (data build tool)allows you to transform your data by writing, documenting, and executing SQL workflows. Setting up the dbt project requires specifying connection details for your data platform, in this case, BigQuery. Here’s a step-by-step guide to help you set this up:



Documentation Source:
airbyte.com/tutorials/building-an-e-commerce-data-pipeline-a-hands-on-guide-to-using-airbyte-dbt-dagster-and-bigquery.md

Documentation Title:
How to build E-commerce Data Pipeline with Airbyte? | Airbyte

Documentation Content:
1. Create a source:

* Go to the Sources tab and click on "+ New source".
* Search for “faker” using the search bar and select "Sample Data (Faker)".
* Adjust the Count and optional fields as needed for your use case. You can also leave as is.
* Click on "Set up source".

!

Look fo Faker source connector

!

Create a Faker source



Documentation Source:
airbyte.com/tutorials/postgres-replication.md

Documentation Title:
Postgres Replication: Data Transfer Efficiency | Airbyte

Documentation Content:
Step 2: Set up an Airbyte Postgres source and destination
---------------------------------------------------------

If you didn’t do it before when deploying Airbyte, go to http://localhost:8000to launch the UI.

Then, click on sources and add a new source. As the connector type, select Postgres. If you used our instructions above to create a Postgres database, fill in the following configuration fields.

* **Host**: localhost
* **Port**: 2000
* **User**: postgres
* **Password**: password
* **DB Name**: postgres

!!We will use the “Standard” replication method to keep things simple for this tutorial. But you can use logical replicationif needed. Follow along with this videoto configure it for Postgres.

We will also use “No Tunnel” as the SSH option. If you want to use SSH, check out our documentation.

Click on "Set up source", and now you’re ready to configure a destination.

Go to destinations and add a new one. Select Postgres as the destination type and fill in with the following details.

* **Host:**localhost
* **Port:**3000
* **User:**postgres
* **Password:**password
* **DB Name:** postgres

!That’s it. You have configured the source and destination.



Documentation Source:
airbyte.com/tutorials/building-an-e-commerce-data-pipeline-a-hands-on-guide-to-using-airbyte-dbt-dagster-and-bigquery.md

Documentation Title:
How to build E-commerce Data Pipeline with Airbyte? | Airbyte

Documentation Content:
3. Create a connection:

* Go to the Connections tab and click on "+ New connection".
* Select the source and destination you just created.
* Enter the connection details as needed.
* For this project, leave the “replication frequency” as “Manual”, since we will orchestrate the syncs with Dagster.
* Click on "Set up connection".

That’s it! Your connection is set up and ready to go! 🎉

‍

!

Establish a connector between Faker and BigQuery

4. Setting Up the dbt Project
-----------------------------

dbt (data build tool)allows you to transform your data by writing, documenting, and executing SQL workflows. Setting up the dbt project requires specifying connection details for your data platform, in this case, BigQuery.



