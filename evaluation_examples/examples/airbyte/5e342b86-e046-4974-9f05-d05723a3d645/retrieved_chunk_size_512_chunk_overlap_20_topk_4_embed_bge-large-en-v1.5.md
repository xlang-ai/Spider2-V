Documentation Source:
airbyte.com/tutorials/how-to-use-airflow-and-airbyte-together.md

Documentation Title:
A step-by-step guide to setting up and configuring Airbyte and Airflow to work together | Airbyte

Documentation Content:
By default the path that you specify will be located inside **/tmp/airbyte\_local**. In this tutorial I set the destination to **/json\_from\_faker**, which means that the data will be copied to**/tmp/airbyte\_local/json\_from\_faker**on the localhost where Airbyte is running. After specifying the Destination Path, click on Set up destination. 

!

Configure the Local JSON destination

‍

This will take you to a page to set up the connection. Set the replication frequency to **Manual**(since we will use Airflow to trigger Airbyte syncs rather than using Airbyte’s scheduler) and then click on **Set up connection**as highlighted in the image below.

!

Specify connection settings

‍

Trigger a sync from the **Sample Data (faker)**source to the **Local JSON**output by clicking on **Sync now**as highlighted in the image below.

!

Manually trigger a sync from the UI

‍

The sync should take a few seconds, at which point you should see that the sync has succeed as shown below.

!

After the sync has completed

‍

You can now confirm if some sample data has been copied to the expected location. As previously mentioned, for this example the JSON data can be seen in **/tmp/airbyte\_local\_json\_from\_faker**. Because there were three streams generated, the following three JSON files should be available: 

`_airbyte_raw_products.jsonl 
_airbyte_raw_users.jsonl
_airbyte_raw_purchases.jsonl`You have now created a simple example connection in Airbyte which can be manually triggered. A manually triggered connection is ideal for situations where you wish to use an external orchestrator. 

In the next section you will see how to trigger a manual sync on this connection by hitting a REST endpoint directly. After that, you will see how Airflow can be used to hit that same endpoint to trigger synchronizations. 

Test the API endpoints with cURL
--------------------------------

Before using the REST endpoint from within Airflow, it is useful to verify that it is working as expected.



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
airbyte.com/docs.airbyte.com/integrations/sources/faker.md

Documentation Title:
Faker | Airbyte Documentation

Documentation Content:
| Feature | Supported?(Yes/No) | Notes |
| --- | --- | --- |
| Full Refresh Sync | Yes |
| --- | --- |
| Incremental Sync | Yes |
| Namespaces | No |

Of note, if you choose `Incremental Sync`, state will be maintained between syncs, and once you hit
`count`records, no new records will be added.

You can choose a specific `seed`(integer) as an option for this connector which will guarantee that
the same fake records are generated each time. Otherwise, random data will be created on each
subsequent sync.



