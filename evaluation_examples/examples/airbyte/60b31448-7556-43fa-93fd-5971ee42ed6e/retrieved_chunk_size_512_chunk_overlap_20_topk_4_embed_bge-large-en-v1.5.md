Documentation Source:
airbyte.com/docs.airbyte.com/using-airbyte/getting-started/set-up-a-connection.md

Documentation Title:
Set up a Connection | Airbyte Documentation

Documentation Content:
Skip to main content!!About AirbyteTutorialsSupportCloud StatusTry Airbyte CloudSearch* Airbyte Connectors
Connector CatalogBuild a ConnectorConnector Support Levels* Using Airbyte
* Getting Started
	Core ConceptsAdd a SourceAdd a DestinationSet up a Connection
Configuring ConnectionsManaging Syncs* Managing Airbyte
Deploy AirbyteSelf-Managed EnterpriseUpgrading AirbyteConfiguring AirbyteAccess ManagementAirbyte at ScaleSecurityIntegrating with AirbyteAccount Management* Developer Guides
API documentationTerraform DocumentationUsing PyAirbyteUnderstand AirbyteContribute to AirbyteLicenses* Community
Getting SupportCode of Conduct* Product Updates
RoadmapRelease Notes
Getting StartedSet up a Connection
On this pageSet up a Connection
===================

AvailableCloud AvailableSelf-Managed Community (OSS)AvailableSelf-Managed EnterpriseNow that you've learned how to set up your first sourceand destination, it's time to finish the setup by creating your very first connection!

On the left side of your main Airbyte dashboard, select **Connections**. You will be prompted to choose which source and destination to use for this connection. For this example, we'll use the **Google Sheets**source and the destination you previously set up, either **Local JSON**or **Google Sheets**.

Configure the connection​
-------------------------

Once you've chosen your source and destination you can configure the connection. You'll first be asked a few questions about how your data should sync, these correlate to our sync modes which you can read more about on this page.

Most users select "Mirror Source", which will simply copy the data from the source to the destination where you'll see one row in the destination for each row in the source. If you prefer to Append Historical Changes or take a Full Snapshot with each sync, you can optionally select those options, but keep in mind those will create duplicate records in your destination. The sync mode we choose for all the enabled streams will reflect your selection here.

Next, you can toggle which streams you want to replicate. Our test data consists of three streams, which we've enabled and set to `Incremental - Append + Deduped`sync mode.

!Your sync mode is already determined by your selection above, but you can change the sync mode for an individual stream.



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
airbyte.com/docs.airbyte.com/using-airbyte/getting-started/set-up-a-connection.md

Documentation Title:
Set up a Connection | Airbyte Documentation

Documentation Content:
You can also select a cursor or primary key to enable incremental and/or deduplication. For more information on the nature of each sync mode supported by Airbyte, see this page.

You can also select individual fields to sync on this page. Expand the fields available by clicking any stream. This is helpful when you have security concerns or don't want to sync all the data from the source.
!

Click **Next**to complete your stream setup and move to the connection configuration. This is where you'll set up how often your data will sync and where it will live in the destination. For this demo, we'll set the connection to run at 8 AM every day and sync the connection to a custom namespace with a stream prefix.

noteTo ensure your data is synced to the correct place, see our examples for Destination Namespace

Once you've set up all the connection settings, click "Set up connection". You've successfully set up your first data pipeline with Airbyte. Your first sync is about to begin!

Connection Overview​
--------------------

Once you've finished setting up the connection, you will be automatically redirected to a connection overview containing all the tools you need to keep track of your connection.

!Here's a basic overview of the tabs and their use:

1. The **Status**tab shows you an overview of your connector's sync health.
2. The **Job History**tab allows you to check the logs for each sync. If you encounter any errors or unexpected behaviors during a sync, checking the logs is always a good first step to finding the cause and solution.
3. The **Schema**tab allows you to modify the streams you chose during the connection setup.
4. The **Transformation**tab allows you to set up a custom post-sync transformations using dbt.
5. The **Settings**tab contains the connection settings, and the option to delete the connection if you no longer wish to use it.



Documentation Source:
airbyte.com/docs.airbyte.com/using-airbyte/getting-started/set-up-a-connection.md

Documentation Title:
Set up a Connection | Airbyte Documentation

Documentation Content:
Check the data from your first sync​

Once the first sync has completed, you can verify the sync has completed by checking the data in your destination.

* Cloud
* Self Hosted

If you followed along and created your own connection using a **Google Sheets**destination, you will now see three tabs created in your Google Sheet, `products`, `users`, and `purchases`.

If you followed along and created your own connection using a `Local JSON`destination, you can use this command to check the file's contents to make sure the replication worked as intended (be sure to replace YOUR\_PATH with the path you chose in your destination setup, and YOUR\_STREAM\_NAME with the name of an actual stream you replicated):

cat /tmp/airbyte\_local/YOUR\_PATH/\_airbyte\_raw\_YOUR\_STREAM\_NAME.jsonlYou should see a list of JSON objects, each containing a unique `airbyte_ab_id`, an `emitted_at`timestamp, and `airbyte_data`containing the extracted record.

tipIf you are using Airbyte on Windows with WSL2 and Docker, refer to this guideto locate the replicated folder and file.

What's next?​
-------------

Congratulations on successfully setting up your first connection using Airbyte! We hope that this will be just the first step on your journey with us. We support a large, ever-growing catalog of sources and destinations, and you can even contribute your own.

If you have any questions at all, please reach out to us on Slack. If you would like to see a missing feature or connector added, please create an issue on our Github. Our community's participation is invaluable in helping us grow and improve every day, and we always welcome your feedback.

Thank you, and we hope you enjoy using Airbyte!

Edit this pagePreviousAdd a DestinationNextConfiguring ConnectionsConfigure the connection* Connection OverviewCheck the data from your first sync
What's next?
Was this page helpful?YesNo



