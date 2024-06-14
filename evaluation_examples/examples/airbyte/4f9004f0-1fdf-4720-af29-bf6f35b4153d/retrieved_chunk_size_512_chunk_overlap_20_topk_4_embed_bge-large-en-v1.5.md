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
airbyte.com/tutorials/elt-pipeline-prefect-airbyte-dbt.md

Documentation Title:
Orchestrate ELT pipelines with Prefect, Airbyte and dbt | Airbyte

Documentation Content:
In this recipe we’ll create a Prefect flow to orchestrate Airbyte and dbt.

**Airbyte**is a data integration tool that allows you to extract data from APIs and databases and load it to data warehouses, data lakes, and databases. In this recipe, we’ll use Airbyte to replicate data from the GitHub API into a Snowflake warehouse.

**dbt**is a data transformation tool that allows you to transform data within a data warehouse more effectively. We’ll use dbt in this recipe to transform data from multiple sources into one table to find common contributors between our three repositories.

Prerequisites
-------------

In order to follow the steps in this recipe you’ll need to make sure that you have the following installed on your local machine:

* Docker and Docker Compose
* Python 3.8+
Set up Snowflake
----------------

For this tutorial, you can set up a Snowflake account if you don’t already have one. Snowflake has a generous free tier, so no cost will be incurred while going through this recipe. Airbyte requires some resources to be created in Snowflake to enable data replication from GitHub. You can refer to the Airbyte Snowflake destination documentationfor the steps necessary to configure Snowflake to allow Airbyte to load data in.



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



