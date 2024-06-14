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
cloud.google.com/bigquery/docs/tables.md

Documentation Title:
Create and use tables  |  BigQuery  |  Google Cloud

Documentation Content:
Example 3:

The following example retrieves `table_name`and `ddl`columns from the `INFORMATION_SCHEMA.TABLES`view for the `population_by_zip_2010`table in the
`census_bureau_usa`dataset. This dataset is part of the BigQuery
public dataset program.

Because the table you're querying is in another project, you add the project ID to the dataset in
the following format:
``project_id`.dataset.INFORMATION_SCHEMA.view`.
In this example, the value is
``bigquery-public-data`.census_bureau_usa.INFORMATION_SCHEMA.TABLES`.


```
SELECT
  table_name, ddl
FROM
  `bigquery-public-data`.census_bureau_usa.INFORMATION_SCHEMA.TABLES
WHERE
  table_name = 'population_by_zip_2010';

```
The result is similar to the following:



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
cloud.google.com/bigquery/docs/logistic-regression-prediction.md

Documentation Title:
Build and use a classification model on census data  |  BigQuery  |  Google Cloud

Documentation Content:
SQL

To prepare your sample data, create a viewto
contain the training data. This view is used by the `CREATE MODEL`statement
later in this tutorial.

Run the query that prepares the sample data:

1. In the Google Cloud console, go to the **BigQuery**page.

Go to BigQuery
2. In the query editor, run the following query:


```
CREATE OR REPLACE VIEW
`census.input_data` AS
SELECT
age,
workclass,
marital_status,
education_num,
occupation,
hours_per_week,
income_bracket,
CASE
  WHEN MOD(functional_weight, 10) < 8 THEN 'training'
  WHEN MOD(functional_weight, 10) = 8 THEN 'evaluation'
  WHEN MOD(functional_weight, 10) = 9 THEN 'prediction'
END AS dataframe
FROM
`bigquery-public-data.ml_datasets.census_adult_income`

```
In the **Explorer**pane, expand the `census`dataset and locate the
`input_data`view.

Click the view name to open the information pane. The view schema appears in
the **Schema**tab.



