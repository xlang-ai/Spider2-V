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
The instructions presented in this tutorial were created in February 2023, and the following tools were used:

* Airbyte OSS 0.40.32
* Docker Desktop v4.10.1
* macOS Monterey Version 12.5.1
* MacBook Pro with the Apple M1 Pro Chip
* Airflow v2.5.1 Git Version: .release:2.5.1+49867b660b6231c1319969217bc61917f7cf9829

Install Airbyte
---------------

If you already have a local copy of Airbyte running, then you may skip this section. Otherwise, follow the instructions to deploy Airbyte. 

[Optional] Modify **BASIC\_AUTH\_USERNAME**and **BASIC\_AUTH\_PASSWORD**in the (hidden) **.env**file. For this tutorial I use the following default values: 

`BASIC_AUTH_USERNAME=airbyte
BASIC_AUTH_PASSWORD=password`Once Airbyte is running, in your browser type in localhost:8000, which should prompt you for a username and password as follows:

!

Airbyte OSS login prompt

Create a connection
-------------------

Create a connection that sends data from the **Sample Data (Faker)**source to the **Local JSON**(file system) output. Click on “Create your first connection” as shown below:

!

Create your first connection prompt

‍

You should then see an option to set up a source connection. Select the Faker source from the dropdown as shown below.

!

Select Sample Data (Faker) as a source

‍

After selecting Sample Data as the source, you will see a screen that should look as follows. Click on **Set up source**as shown below. 

!

Configure Sample Data (Faker) as a source

‍

You will then wait a few seconds for the Sample Data source to be verified, at which point you will be prompted to configure the destination that will be used for the connection. Select **Local JSON**as shown below:

!

Select Local JSON as a destination

‍

After selecting Local JSON as the output, you will need to specify where the JSON files should be written.



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
airbyte.com/tutorials/how-to-use-airflow-and-airbyte-together.md

Documentation Title:
A step-by-step guide to setting up and configuring Airbyte and Airflow to work together | Airbyte

Documentation Content:
This should look as follows: 

!

Configure an Airflow connection to Airbyte

The connection parameters are:

* **Connection Id:**Define an identifier that Airflow DAGs can use to communicate with Airbyte. In this example the identifier is given the name **airflow-call-to-airbyte-example**, which will be used in the DAG definition (shown later).
* **Connection Type**: Specifies that this is a connection to Airbyte. Note that if you do not see **Airbyte**in the dropdown menu, then the Docker image has not been correctly built. Adding the Airbyte providerto the Docker image was done earlier in this tutorial.
* **Host**: The host which is running Airbyte. Note the use of **host.docker.internal**, which  resolves to the internal IP address used by the host, as discussed in Docker’s instructions on network interfaces.
* **Login**: The default user to connect to Airbyte is **airbyte**. If you have changed this, then use whichever username you have defined.
* **Password**: If you are using the default then the value is **password**. If you have changed this, then use whichever password you have defined.
* **Port**: By default, Airbyte listens on port **8000**.

Click on **Save**which should take you back to the Connections screen. 

Because the DAG that we will define is also going to manipulate files, we will also create a Files connection. Again, click on the **+**symbol as shown below:

!

Create another Airflow connection

‍

This should take you to a screen that looks like the following:

!

Create an Airflow connection to manipulate files on the local filesystem

The connection parameters are:

* **Connection Id**: As mentioned above this will be used in the DAG to connect to the file system. In this example the value is set to **airflow-file-connector**.
* **Connection Type**: Select **File (path)**. This connector will be used in the DAG to interact with files on the local filesystem.

After saving the above connection, you Connections screen should look as follows:

!



