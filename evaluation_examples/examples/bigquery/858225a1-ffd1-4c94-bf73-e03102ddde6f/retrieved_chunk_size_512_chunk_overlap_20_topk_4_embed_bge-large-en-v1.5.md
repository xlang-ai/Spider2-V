Documentation Source:
cloud.google.com/bigquery/docs/quickstarts/load-data-console.md

Documentation Title:
Load and query data with the Google Cloud console  |  BigQuery

Documentation Content:
A new **Editor**tab opens.
2. In the **Editor
 tab**, paste the following query. This query
 retrieves the top five names for US babies that were assigned male at birth
 in 2014. `SELECT
 name,
 count
 FROM
 `babynames.names_2014`
 WHERE
 assigned_sex_at_birth = 'M'
 ORDER BY
 count DESC
 LIMIT
 5;`
3. Click **Run**. The results are displayed
 in the **Query results**section. !

You have successfully queried a table in a public dataset and then loaded your
sample data into BigQuery using the Cloud console.

Clean up
--------

To avoid incurring charges to your Google Cloud account for
 the resources used on this page, follow these steps.
 

1. In the Google Cloud console, open the BigQuery page.
Go to BigQuery3. In the **Explorer**panel, click the `babynames`dataset
 that you created.
4. Expand the more\_vert**View actions**option and click **Delete**.
5. In the **Delete dataset**dialog, confirm the delete command: type the word
 `delete`and then click **Delete**.
What's next
-----------

* To learn more about using the Google Cloud console, see
 Using the Google Cloud console.
* To learn more about loading data into BigQuery, see
 Introduction to loading data.
* To learn more about querying data, see
 Overview of querying BigQuery data.
* To learn how to load a JSON file with nested and repeated data, see
 Loading nested and repeated JSON data.
* To learn more about accessing BigQuery programmatically, see
 the REST APIreference or the
 BigQuery client librariespage.
Send feedback
 
 Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-05-13 UTC.

* ### Why Google


	Choosing Google CloudTrust and securityOpen cloudMulticloudGlobal infrastructureCustomers and case studiesAnalyst reportsWhitepapersBlog
* ### Products and pricing



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
Click settings**More**, and then
click **Query settings**.

In the **Resource management**section, select **Batch**.

6. Optional: Specify the destination table and
locationfor the query results:


	1. In the **Destination**section, select
	**Set a destination table for query results**.
	2. For **Dataset**, enter the name of an existing dataset for the
	destination table—for example, `myProject.myDataset`.
	3. For **Table Id**, enter a name for the destination table—for
	example, `myTable`.
	4. If the destination table is an existing table, then for
	**Destination table write preference**, select whether to append or
	overwrite the table with the query results.
	
	If the destination table is a new table, then
	BigQuery creates the table when you run your query.
	5. In the **Additional settings**section, click the
	**Data location**menu, and then select an option.
	
	In this example, the `usa_names`dataset is stored in the US
	multi-region location. If you specify a destination table for this
	query, the dataset that contains the destination table must also be
	in the US multi-region. You cannot query a dataset in one location
	and write the results to a table in another location.
Click **Save**.

8. Click play\_circle**Run**.

If you don't specify a destination table, the query job writes the
output to a temporary (cache) table.



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
cloud.google.com/bigquery/docs/quickstarts/load-data-console.md

Documentation Title:
Load and query data with the Google Cloud console  |  BigQuery

Documentation Content:
Load data into a table
----------------------

Next, load the data into a new table.

1. In the
 **Explorer**panel, click your project name.
2. Next to the **babynames**dataset, click
 **More actions**more\_vertand select **Open**.
3. In the details panel, click
 add\_box**Create
 table**. Unless otherwise indicated, use the default values for all settings.
4. On the **Create table**page, do the following:
1. In the **Source**section, choose **Upload**from the
 **Create table
 from**list.
2. In the **Select file**field, click **Browse**.
3. Navigate to and open your local `yob2014.txt`file, and click **Open**.
4. From the
 **File
 format**list, choose **CSV**
5. In the **Destination**section, enter
 `names_2014`for
 **Table
 name**.
6. In the **Schema**section, click the
 **Edit as
 text**toggle, and paste the following
 schema definition into the text field:
`name:string,assigned_sex_at_birth:string,count:integer`8. Click
 **Create
 table**.

Wait for BigQuery to create the table and load the data.
 When BigQuery finishes loading the data, expand the
 **Personal
 history**and **Project history**panel to review the job details.

Preview table data
------------------

To preview the table data, follow these steps:

1. In the
 **Explorer**panel, expand your project and `babynames`dataset, and then
 select the `names_2014`table.
2. In the details panel, click **Preview**. BigQuery displays the first few
 rows of the table.
!
The **Preview**tab is not available for all table types. For example, the
**Preview**tab is not displayed for external tables or views.


Query table data
----------------

Next, query the table. The process is identical to the previous example,
except that this time, you're querying your table instead of a public table.

1. Click add\_box**Compose new query**. A new **Editor**tab opens.
2.



