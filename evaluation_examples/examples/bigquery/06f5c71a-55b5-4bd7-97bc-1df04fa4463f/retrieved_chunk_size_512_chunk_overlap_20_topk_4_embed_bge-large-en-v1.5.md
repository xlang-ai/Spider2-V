Documentation Source:
cloud.google.com/bigquery/docs/loading-data-cloud-storage-json.md

Documentation Title:
Loading JSON data from Cloud Storage  |  BigQuery  |  Google Cloud

Documentation Content:
Console

1. In the Google Cloud console, go to the **BigQuery**page.

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
	 **JSONL (Newline delimited JSON)**.
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
	* Option 2: Click add\_box**Add field**and enter the table schema. Specify each field's **Name**,
	 **Type**,
	 and **Mode**.
4.



Documentation Source:
cloud.google.com/bigquery/docs/batch-loading-data.md

Documentation Title:
Batch loading data  |  BigQuery  |  Google Cloud

Documentation Content:
Console

1. Open the BigQuery page in the Google Cloud console.

Go to the BigQuery page
In the **Explorer**panel, expand your project and select a dataset.

Expand the
more\_vert**Actions**option and click **Open**.

In the details panel, click **Create table**add\_box.

5. On the **Create table**page, in the **Source**section:


	* For **Create table from**, select **Upload**.
	* For **Select file**, click **Browse**.
	* Browse to the file, and click **Open**. Note that wildcards
	and comma-separated lists are not supported for local files.
	* For **File format**, select **CSV**, **JSON (newline delimited)**,
	**Avro**, **Parquet**, or **ORC**.
6. On the **Create table**page, in the **Destination**section:


	* For **Project**, choose the appropriate project.
	* For **Dataset**, choose the appropriate dataset.
	* In the **Table**field, enter the name of the table you're
	creating in BigQuery.
	* Verify that **Table type**is set to **Native table**.
7. In the **Schema**section, enter the schemadefinition.


	For CSV and JSON files, you can check the **Auto-detect**option to
	enable schema auto-detect. Schema
	information is self-described in the source data for other supported
	file types.
	
	* You can also enter schema information manually by:
	
	
		+ Clicking **Edit as text**and entering the table schema as a JSON
		array:
		
		**Note:**You can view the schema of an existing table in JSON
		format by entering the following command:
		`bq show --format=prettyjson dataset.table`.
		Using **Add Field**to manually input the schema.
Select applicable items in the **Advanced options**section For information on the available options, see
CSV optionsand JSON options.

9. Optional: In the **Advanced options**choose the write disposition:



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



Documentation Source:
cloud.google.com/bigquery/docs/external-data-drive.md

Documentation Title:
Create Google Drive external tables  |  BigQuery  |  Google Cloud

Documentation Content:
* For JSON or CSV files, you can check the **Auto-detect**option to
	enable schema auto-detect.
	**Auto-detect**is not available for Datastore exports,
	Firestore exports, and Avro files. Schema information for these
	file types is automatically retrieved from the self-describing source
	data.
	* Enter schema information manually by:
		+ Enabling **Edit as text**and entering the table schema as a JSON
		array.
		Note: You can view the schema of an existing table in JSON
		format by entering the following command in the bq command-line tool:
		`bq show --format=prettyjson DATASET.TABLE`.
		+ Using **Add field**to manually input the schema.
Click **Create table**.

If necessary, select your account and then click **Allow**to give the
BigQuery client tools access to Drive.


You can then run a query against the table as if it were a standard
BigQuery table, subject to the limitationson external data sources.

After your query completes, you can download the results as CSV or JSON,
save the results as a table, or save the results to Sheets. See
Download, save, and export datafor more information.



