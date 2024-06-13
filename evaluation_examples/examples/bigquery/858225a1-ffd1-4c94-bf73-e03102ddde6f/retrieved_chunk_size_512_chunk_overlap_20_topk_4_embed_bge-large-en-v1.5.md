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
cloud.google.com/bigquery/docs/quickstarts/load-data-console.md

Documentation Title:
Load and query data with the Google Cloud console  |  BigQuery

Documentation Content:
Optional: If you
 select an existing project, make sure that you
 enable
 the BigQuery API. The BigQuery API is automatically
 enabled in new projects.
Create a BigQuery dataset
-------------------------

Use the Google Cloud console to create a dataset that stores the data.

1. In the Google Cloud console, open the BigQuery page.
Go to BigQuery3. In the
 **Explorer**panel, click your project name.
4. Expand the more\_vert**View actions > Create dataset**.
5. On the **Create dataset**page, do the following:
1. For
 **Dataset ID**, enter `babynames`.
2. From the **Data location**list, choose **us (multiple regions in United States)**.
 The public datasets are stored in the `us`multi-region
 location. For simplicity,
 store your
 dataset in the same location.
3. Leave the remaining default settings as they are, and click **Create dataset**.

Download the source data file
-----------------------------

The file that you're downloading contains approximately 7 MB of data about
popular baby names. It's provided by the US Social Security Administration.

For more information about the dataset, see the
Social Security Administration's dataset information page.

1. Download the US Social Security Administration's dataset by opening the
following URL in a new browser tab:

`https://www.ssa.gov/OACT/babynames/names.zip`
2. Extract the file.

For more information about the dataset schema, see the zip file's
`NationalReadMe.pdf`file.
To see what the data looks like, open the `yob2014.txt`file. This file
contains comma-separated values for name, assigned sex at birth, and number
of children with that name. The file has no header row.

Note the location of the `yob2014.txt`file so that you can find it later.



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



Documentation Source:
cloud.google.com/bigquery/docs/quickstarts/load-data-bq.md

Documentation Title:
Load and query data with the bq tool  |  BigQuery  |  Google Cloud

Documentation Content:
Determine the most popular girls' names in the data:

`bq query --use_legacy_sql=false \
 'SELECT
 name,
 count
 FROM
 `babynames.names2010`
 WHERE
 assigned_sex_at_birth = "F"
 ORDER BY
 count DESC
 LIMIT 5;'`The output is similar to the following:

`+----------+-------+
| name | count |
+----------+-------+
| Isabella | 22925 |
| Sophia | 20648 |
| Emma | 17354 |
| Olivia | 17030 |
| Ava | 15436 |
+----------+-------+`
2. Determine the least popular boys' names in the data:

`bq query --use_legacy_sql=false \
 'SELECT
 name,
 count
 FROM
 `babynames.names2010`
 WHERE
 assigned_sex_at_birth = "M"
 ORDER BY
 count ASC
 LIMIT 5;'`The output is similar to the following:

`+----------+-------+
| name | count |
+----------+-------+
| Aamarion | 5 |
| Aarian | 5 |
| Aaqib | 5 |
| Aaidan | 5 |
| Aadhavan | 5 |
+----------+-------+`The minimum count is 5 because the source data omits names with fewer than
5 occurrences.
Clean up
--------

To avoid incurring charges to your Google Cloud account for
 the resources used on this page, delete the Google Cloud project with the
 resources.



