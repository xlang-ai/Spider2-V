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
airbyte.com/tutorials/how-to-use-airflow-and-airbyte-together.md

Documentation Title:
A step-by-step guide to setting up and configuring Airbyte and Airflow to work together | Airbyte

Documentation Content:
After saving the above connection, you Connections screen should look as follows:

!

The Airflow connections that have just been created

‍

Now that the relevant Airflow connections are defined, they can be used in an Airflow DAG.

Create an Airflow DAG
---------------------

In this section, I present Python code for a simple DAG that performs the following tasks: 

1. **trigger\_airbyte**: Uses AirbyteTriggerSyncOperatorto asynchronously trigger Airbyte to perform a synchronization from the **Sample Data (Faker)**input to the**Local JSON**(file) output using the Airbyte connection that we defined above. Because this is executed asynchronously, it immediately returns along with a job id that is used for determining the completion of the synchronization.
2. **wait\_for\_sync\_completion**: Uses AirbyteJobSensorto wait for Airbyte to complete the synchronization.
3. **raw\_products\_file\_sensor**: Uses FileSensorto confirm that the file created by Airbyte exists. One of the files created by the **Sample Data (Faker)**source is called **\_airbyte\_raw\_products.jsonl**, and this task waits for that file to exist.
4. **mv\_raw\_products\_file**: Uses BashOperatorto rename the raw products file.

The code which demonstrates these steps is given below.



Documentation Source:
airbyte.com/quickstart/airbyte-dbt-and-airflow-stack-with-bigquery.md

Documentation Title:
E-commerce Analytics Stack with Airbyte, dbt, Airflow (ADA) and BigQuery | Airbyte

Documentation Content:
**7. Link Airbyte connection to the Airflow DAG**:

The last step being being able to execute the DAG in Airflow, is to include the connection ID from Airbyte:

1. Visit the Airbyte UI at http://localhost:8000/.
2. In the "Connections" tab, select the "Faker to BigQuery" connection and copy its connection id from the URL.
3. Update the connection\_id in the extract\_data task within orchestration/airflow/dags/elt\_dag.py with this id.

That's it! Airflow has been configured to work with dbt and Airbyte. 🎉

6. Orchestrating with Airflow
-----------------------------

Now that everything is set up, it's time to run your data pipeline!

1. In the Airflow UI, go to the "DAGs" section.
2. Locate elt\_dag and click on "Trigger DAG" under the "Actions" column.

This will initiate the complete data pipeline, starting with the Airbyte sync from Faker to BigQuery, followed by dbt transforming the raw data into staging and marts models. As the last step, it generates dbt docs.

1. Confirm the sync status in the Airbyte UI.
2. After dbt jobs completion, check the BigQuery console to see the newly created views in the transformed\_data dataset.
3. Once the dbt pipeline completes, you can check the dbt docs from the Airflow UI by going to the "Custom Docs" > "dbt" tab.

Congratulations! You've successfully run an end-to-end workflow with Airflow, dbt and Airbyte. 🎉

7. Next Steps
-------------

Once you've gone through the steps above, you should have a working Airbyte, dbt and Airflow (ADA) Stack with BigQuery. You can use this as a starting point for your project, and adapt it to your needs. There are lots of things you can do beyond this point, and these tools are evolving fast and adding new features almost every week.



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



