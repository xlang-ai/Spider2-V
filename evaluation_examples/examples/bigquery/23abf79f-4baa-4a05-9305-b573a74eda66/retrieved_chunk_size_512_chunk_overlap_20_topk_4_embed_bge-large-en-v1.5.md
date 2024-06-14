Documentation Source:
cloud.google.com/bigquery/docs/google-ads-transfer.md

Documentation Title:
Google Ads transfers  |  BigQuery  |  Google Cloud

Documentation Content:
Migrate Google Ads data to MCCs

To migrate your existing Google Ads data in BigQuery Data Transfer Service to the
MCC structure, you can set up a backfillto add your existing data to the tables created by the transfer configuration
linked to the manager account. Note that when you schedule a backfill, match
tables are not updated.

Troubleshoot Google Ads transfer setup
--------------------------------------

If you are having issues setting up your transfer, see
Google Ads transfer issuesin Troubleshooting transfer configurations.

Query your data
---------------

When your data is transferred to BigQuery Data Transfer Service, the data is
written to ingestion-time partitioned tables. For more information, see
Introduction to partitioned tables.

If you query your tables directly instead of using the auto-generated views, you
must use the `_PARTITIONTIME`pseudo-column in your query. For more information,
see Querying partitioned tables.

Google Ads sample queries
-------------------------

You can use the following Google Ads sample queries to analyze your transferred
data. You can also use the queries in a visualization tool such as
Looker Studio.
These queries are provided to help you get started on querying your Google Ads
data with BigQuery Data Transfer Service. For additional questions about what you can
do with these reports, contact your Google Ads technical representative.

In each of the following queries, replace datasetwith your dataset
name. Replace customer\_idwith your Google Ads Customer ID.

If you query your tables directly instead of using the auto-generated
views, you must use the `_PARTITIONTIME`pseudo-column in your query. For more
information, see Querying partitioned tables.



Documentation Source:
cloud.google.com/bigquery/docs/google-ads-transfer.md

Documentation Title:
Google Ads transfers  |  BigQuery  |  Google Cloud

Documentation Content:
Console

1. Go to the BigQuery page in the Google Cloud console.

Go to the BigQuery page
Click sync\_alt**Data transfers**.

Click add**Create transfer**.

In the **Source type**section, for **Source**, choose
**Google Ads**.

In the **Transfer config name**section, for **Display name**, enter a
name for the transfer such as `My Transfer`. The transfer name can be
any value that lets you identify the transfer if you need
to modify it later.

6. In the **Schedule options**section:


	* For **Repeat frequency**, choose an option for how often to run the
	transfer. If you select **Days**, provide a valid time in UTC.
	
	
		+ Hours
		+ Days
		+ On-demand
	If applicable, select either **Start now**or **Start at set time**and provide a start date and run time.
In the **Destination settings**section, for **Dataset**,
select the dataset that you created to store your data.

8. In the **Data source details**section:


	1. For **Customer ID**, enter your Google Ads customer ID:
	
	!
	Optional: Select options to exclude removed or deactivated items and
	include tables new to Google Ads.
	
	Optional: Enter a comma-separated list of tables to include, for example
	`Campaign, AdGroup`. Prefix this list with the `-`character to exclude certain
	tables, for example `-Campaign, AdGroup`. All tables are included by
	default.
	
	Optional: Select the option to include tables specific to PMax
	reports. For more information about PMax support, see PMax
	support.
	
	Optional: For **Refresh window**, enter a value between 1 and 30.
9. In the **Service Account**menu, select a service accountfrom the service accounts associated with your
Google Cloud project. You can associate a service account with
your transfer instead of using your user credentials. For more
information about using service accounts with data transfers, see
Use service accounts.



Documentation Source:
cloud.google.com/bigquery/docs/samples/bigquerydatatransfer-create-ads-transfer.md

Documentation Title:
Load data from Google Ads  |  BigQuery  |  Google Cloud

Documentation Content:
append jobRevoke access to a datasetRun a legacy SQL query with pandas-gbqRun a query and get total rowsRun a query with batch priorityRun a query with GoogleSQLRun a query with legacy SQLRun a query with pandas-gbqRun queries using the BigQuery DataFrames bigframes.pandas APIsSave query resultsSet hive partitioning optionsset the service endpointSet user agentStreaming insertStreaming insert with complex data typesStruct parametersTable existsTimestamp parametersTutorial: Visualizing BigQuery Data in a Jupyter NotebookUndeleteUpdate a descriptionUpdate a labelUpdate a materialized viewUpdate a model descriptionUpdate a routineUpdate a tableUpdate a table descriptionUpdate a view queryUpdate an expiration timeUpdate dataset accessUpdate default table expiration timesUpdate IAM policyUpdate partition expirationUpdate table with DMLUpdate the require partition filterWrite to destination tableBigQuery Connection SamplesCreate a Cloud SQL connectionCreate an AWS connectionDelete a connectionGet connection metadataList connectionsList connectionsShare a connectionUpdate connection metadataBigQuery Data Transfer Service SamplesCopy a datasetCreate a scheduled queryCreate a scheduled query with a service accountCreate a transfer configuration with run notificationsDelete a scheduled queryDelete a transfer configurationDisable a transfer configurationGet configuration metadataGet transfer run metadataList run historyList supported data sourcesList transfer configurationsLoad data from Amazon RedshiftLoad data from Amazon S3Load data from Campaign ManagerLoad data from Cloud StorageLoad data from Google Ad ManagerLoad data from Google AdsLoad data from Google PlayLoad data from TeradataLoad data from YouTube Channel reportsLoad data from YouTube Content Owner reportsRe-enable a transfer configurationSchedule a backfill runUpdate configuration metadataUpdate transfer configuration credentialsBigQuery Migration SamplesDemonstrate batch query translationBigQuery Reservation SamplesReport capacity commitments and reservationsBigQuery Storage SamplesAppend buffered recordsAppend committed recordsAppend data for a complex schemaAppend pending recordsAppend records using default clientAppend rows with a static protocol bufferDownload table data in the Arrow data formatDownload table data in the Avro data formatAI solutions, generative AI, and ML
 Application development
 Application hosting
 Compute
 Data analytics and pipelines
 Databases
 Distributed, hybrid, and multicloud
 Industry solutions
 Networking
 Observability and monitoring
 Security
 Storage
 Access and resources management
 Cloud SDK, languages, frameworks,



Documentation Source:
cloud.google.com/bigquery/docs/loading-data-cloud-storage-csv.md

Documentation Title:
Loading CSV data from Cloud Storage  |  BigQuery  |  Google Cloud

Documentation Content:
Console

To follow step-by-step guidance for this task directly in the
 Cloud Shell Editor, click **Guide me**:


Guide me1. In the Google Cloud console, go to the **BigQuery**page.

Go to BigQuery
2. In the **Explorer**pane, expand your project, and then select a dataset.
3. In the **Dataset info**section, click add\_box**Create table**.
4. In the **Create table**panel, specify the following details:
1. In the **Source**section, select **Google Cloud Storage**in the **Create table from**list.
 Then, do the following:
	1. Select a file from the Cloud Storage bucket, or enter the
	 Cloud Storage URI.
	 You cannot include multiple URIs
	 in the Google Cloud console, but wildcardsare supported. The Cloud Storage bucket must be in the same
	 location as the dataset that contains the table you want to create, append, or
	 overwrite.
	 
	
	 
	
	!
	2. For **File format**, select
	 **CSV**.
2. In the **Destination**section, specify the following details:
	1. For **Dataset**, select the dataset in which you want to create the
	 table.
	2. In the **Table**field, enter the name of the table that you want to create.
	3. Verify that the **Table type**field is set to **Native table**.
3. In the **Schema**section, enter the schemadefinition.
 To enable the auto detectionof a schema,
 select **Auto detect**.



 

 You can enter schema information manually by using one of
 the following methods:
	* Option 1: Click **Edit as text**and paste the schema in the form of a
	 JSON array. When you use a JSON array, you generate the schema using the
	 same process as creating a JSON schema file.
	 You can view the schema of an existing table in JSON format by entering the following
	 command:
	 
	```
	bq show--format=prettyjson dataset.table
	```
	* Option 2: Click add\_box**Add field**and enter the table schema.



