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



Documentation Source:
cloud.google.com/bigquery/docs/quickstarts/query-public-dataset-console.md

Documentation Title:
Query a public dataset with the Google Cloud console  |  BigQuery

Documentation Content:
4. Ensure that the BigQuery API is enabled.

Enable the APIIf you created a new project, the BigQuery API is automatically
 enabled.
Open a public dataset
---------------------

BigQuery public datasets are available by default in the
Google Cloud console.

In the following example, you access datasets in the public project
`bigquery-public-data`.

1. In the Google Cloud console, go to the
**BigQuery**page.

Go to BigQuery
In the **Explorer**pane, click **+Add**.

In the **Add**dialog, search `public datasets`, and then click !**Public Datasets**.

4. Select a dataset, and then click **View dataset**.

In the **Explorer**pane, your dataset is selected and you can view its
details.
5. Optional: Click more\_vert**View actions**next to your dataset to view more options.

Each dataset contains tables, which you can view by clicking
arrow\_right**Toggle node**next to any dataset.

Query a public dataset
----------------------

In the following steps, you query the USA Names public dataset to determine
the most common names in the United States between 1910 and 2013:

1. In the Google Cloud console, go to the
**BigQuery**page.

Go to BigQuery
2. Go to the
**Editor**field.

If the **Editor**field is not visible, then click
add\_box**Compose new query**.

!
3. In the **Editor**field, copy the following
query:

`SELECT
 name,
 SUM(number) AS total
FROM
 `bigquery-public-data.usa_names.usa_1910_2013`
GROUP BY
 name
ORDER BY
 total DESC
LIMIT
 10;`If the query is valid, then a check mark appears along with the amount of
data that the query processes. If the query is invalid, then an
exclamation point appears along with an error message.

!
4. Click
**Run**.

The most common names are listed in the **Query results**section.
The table's header row contains each column name that you selected in the
query.

!



Documentation Source:
cloud.google.com/bigquery/docs/data-canvas.md

Documentation Title:
Analyze with data canvas  |  BigQuery  |  Google Cloud

Documentation Content:
Example 3

**Prompt 1**
```
Find data about USA names
```
**Potential result**BigQuery data canvas generates a list of tables. For this example, we are going to
select the `bigquery-public-data.usa_names.usa_1910_current`table.

Click **Query**to query the data. Enter a prompt to query the data.

**Potential result**BigQuery data canvas generates the following query:


```
SELECT
  state,
  gender,
  year,
  name,
  number
FROM
  `bigquery-public-data.usa_names.usa_1910_current`

```
BigQuery data canvas generates the results of the query. We are going to ask an
additional query to filter this data. Click **Query these results**.

**Prompt 2**
```
Get me the top 10 most popular names in 1980
```
**Potential result**BigQuery data canvas generates the following query:



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



