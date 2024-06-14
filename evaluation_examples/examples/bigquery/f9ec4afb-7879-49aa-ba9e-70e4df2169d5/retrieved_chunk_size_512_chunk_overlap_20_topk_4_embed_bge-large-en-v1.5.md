Documentation Source:
cloud.google.com/bigquery/docs/analyze-data-tableau.md

Documentation Title:
Quickstart: Analyze BigQuery data with BI Engine and Tableau  |  BigQuery: Cloud Data Warehouse  |  Google Cloud

Documentation Content:
Required permissions

To get the permissions that you need to execute queries, run jobs, and view data,
 
 ask your administrator to grant you the
 
 
 BigQuery Admin(`roles/bigquery.admin`) IAM role.
 

 
 
 For more information about granting roles, see Manage access.
 
 

You might also be able to get
 the required permissions through custom
 rolesor other predefined
 roles.
 

Additional permissions might be needed if you have are using a custom OAuth
client in Tableau to connect to BigQuery. For more information,
see Troubleshooting Errors.

Create a BigQuery dataset
-------------------------

The first step is to create a BigQuery dataset to store your
BI Engine-managed table. To create your dataset, follow these
steps:

1. In the Google Cloud console, go to the BigQuery page.

Go to BigQuery
In the navigation panel, in the **Explorer**panel, click your project
name.

In the details panel, click more\_vert**View actions**, and then click **Create dataset**.

4. On the **Create dataset**page, do the following:


	* For **Dataset ID**, enter `biengine_tutorial`.
	For **Data location**, choose **us (multiple regions in United
	States)**, the multi-region
	locationwhere public datasets
	are stored.
	
	* For this tutorial, you can select **Enable table expiration**, and then
	specify the number of days before the table expires.
	
	!
Leave all of the other default settings in place and click **Create dataset**.


Create a table by copying data from a public dataset
----------------------------------------------------

This tutorial uses a dataset available through the
Google Cloud Public Dataset Program. Public datasets
are datasets that BigQuery hosts for you to access and integrate
into your applications.

In this section, you create a table by copying data from the
San Francisco 311 service requestsdataset. You can explore the dataset by using the
Google Cloud console.



Documentation Source:
cloud.google.com/bigquery/docs/running-queries.md

Documentation Title:
Run a query  |  BigQuery  |  Google Cloud

Documentation Content:
Console

1. Go to the **BigQuery**page.

Go to BigQuery
Click add\_box**Compose a new query**.

3. In the query editor, enter a valid GoogleSQL query.

For example, query the
BigQuery public dataset `usa_names`to determine the most common names in the United States between the
years 1910 and 2013:

`SELECT
 name, gender,
 SUM(number) AS total
FROM
 `bigquery-public-data.usa_names.usa_1910_2013`
GROUP BY
 name, gender
ORDER BY
 total DESC
LIMIT
 10;`
4. Optional: Specify the destination table and
locationfor the query results:


	1. In the query editor, click
	settings**More**, and then
	click **Query settings**.
	2. In the **Destination**section, select
	**Set a destination table for query results**.
	3. For **Dataset**, enter the name of an existing dataset for the
	destination table—for example, `myProject.myDataset`.
	4. For **Table Id**, enter a name for the destination table—for
	example, `myTable`.
	5. If the destination table is an existing table, then for
	**Destination table write preference**, select whether to append or
	overwrite the table with the query results.
	
	If the destination table is a new table, then
	BigQuery creates the table when you run your query.
	6. In the **Additional settings**section, click the
	**Data location**menu, and then select an option.
	
	In this example, the `usa_names`dataset is stored in the US
	multi-region location. If you specify a destination table for this
	query, the dataset that contains the destination table must also be
	in the US multi-region. You cannot query a dataset in one location
	and write the results to a table in another location.
	Click **Save**.
5. Click play\_circle**Run**.

If you don't specify a destination table, the query job writes the
output to a temporary (cache) table.

You can now explore the query results in the **Results**tab of the
**Query results**pane.



Documentation Source:
cloud.google.com/bigquery/docs/samples/bigquery-query-destination-table.md

Documentation Title:
Save query results  |  BigQuery  |  Google Cloud

Documentation Content:
bigquery.query(queryConfig);

 // The results are now saved in the destination table.

 System.out.println("Saved query ran successfully");
 } catch (BigQueryException | InterruptedException e) {
 System.out.println("Saved query did not run \n" + e.toString());
 }
 }
}`Node.jsBefore trying this sample, follow the Node.jssetup instructions in the
 BigQuery quickstart using
 client libraries.
 
 
 
 For more information, see the
 BigQuery Node.jsAPI
 reference documentation.
 
 

To authenticate to BigQuery, set up Application Default Credentials.
 For more information, see
 
 Set up authentication for client libraries.
 
 

`// Import the Google Cloud client library
const {BigQuery} = require('@google-cloud/bigquery');
const bigquery = new BigQuery();

async function queryDestinationTable() {
 // Queries the U.S. given names dataset for the state of Texas
 // and saves results to permanent table.

 /**
 * TODO(developer): Uncomment the following lines before running the sample.
 */
 // const datasetId = 'my_dataset';
 // const tableId = 'my_table';

 // Create destination table reference
 const dataset = bigquery.dataset(datasetId);
 const destinationTable = dataset.table(tableId);

 const query = `SELECT name
 FROM \`bigquery-public-data.usa_names.usa_1910_2013\`
 WHERE state = 'TX'
 LIMIT 100`;

 // For all options, see https://cloud.google.com/bigquery/docs/reference/v2/tables#resource
 const options = {
 query: query,
 // Location must match that of the dataset(s) referenced in the query.
 location: 'US',
 destination: destinationTable,
 };

 // Run the query as a job
 const [job] = await bigquery.createQueryJob(options);

 console.log(`Job ${job.id} started.`);
 console.log(`Query results loaded to table ${destinationTable.id}`);
}`PythonBefore trying this sample, follow the Pythonsetup instructions in the
 BigQuery quickstart using
 client libraries.
 
 
 
 For more information, see the
 BigQuery PythonAPI
 reference documentation.
 
 

To authenticate to BigQuery, set up Application Default Credentials.
 For more information, see
 
 Set up authentication for client libraries.
 
 

`from google.cloud import bigquery



Documentation Source:
cloud.google.com/bigquery/docs/analyze-data-tableau.md

Documentation Title:
Quickstart: Analyze BigQuery data with BI Engine and Tableau  |  BigQuery: Cloud Data Warehouse  |  Google Cloud

Documentation Content:
Create your table

To create your table, follow these steps:

1. In the Google Cloud console, go to the BigQuery page.

Go to BigQuery
In the **Explorer**panel, search for `san_francisco_311`.

In the **Explorer**panel, expand **san\_francisco\_311**and click the
**311\_service\_requests**table.

4. In the Explorer toolbar, click **Copy**.

!
5. In the **Copy table**dialog, in the **Destination**section, do the
following:


	* For **Project name**, click **Browse**, and then select your project.
	* For **Dataset name**, select **biengine\_tutorial**.
	* For **Table name**, enter `311_service_requests_copy`.
	
	!
Click **Copy**.

Optional: After the copy job is complete, verify the table contents by expanding
**PROJECT\_NAME>biengine\_tutorial**and
clicking **311\_service\_requests\_copy >Preview**. Replace
PROJECT\_NAMEwith name of your Google Cloud project
for this tutorial.


Create your BI Engine reservation
---------------------------------

1. In the Google Cloud console, under **Administration**go to the
**BI Engine**page.

Go to the BI Engine page**Note:**If prompted to enable **BigQuery Reservation API**, click **Enable**.
Click add**Create reservation**.

3. On the **Create Reservation**page, configure your BI Engine
reservation:


	* In the **Project**list, verify your Google Cloud project.
	* In the **Location**list, select a location. The location should
	match the
	location of the datasetsthat you're querying.
	* Adjust the **GiB of Capacity**slider to the amount of memory capacity
	that you're reserving. The following example sets the capacity to
	2 GiB. The maximum is 250 GiB.
	
	!
Click **Next**.

5. In the **Preferred Tables**section, optionally specify tables for
acceleration with BI Engine. To find table names, do the
following:



