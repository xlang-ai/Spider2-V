Documentation Source:
cloud.google.com/bigquery/docs/visualize-jupyter.md

Documentation Title:
Visualize BigQuery data in Jupyter notebooks  |  Google Cloud

Documentation Content:
```
Query complete after 0.07s: 100%|██████████| 4/4 [00:00<00:00, 1440.60query/s]
Downloading: 100%|██████████| 41/41 [00:02<00:00, 20.21rows/s]
country_code      country_name    num_regions
0   TR  Turkey         81
1   TH  Thailand       77
2   VN  Vietnam        63
3   JP  Japan          47
4   RO  Romania        42
5   NG  Nigeria        37
6   IN  India          36
7   ID  Indonesia      34
8   CO  Colombia       33
9   MX  Mexico         32
10  BR  Brazil         27
11  EG  Egypt          27
12  UA  Ukraine        27
13  CH  Switzerland    26
14  AR  Argentina      24
15  FR  France         22
16  SE  Sweden         21
17  HU  Hungary        20
18  IT  Italy          20
19  PT  Portugal       20
20  NO  Norway         19
21  FI  Finland        18
22  NZ  New Zealand    17
23  PH  Philippines    17
...

```
**Note:**Your results might differ from what is above as the `google_trends`dataset being queried is refreshed with new data on an ongoing basis.
5. In the next cell (below the output from the previous cell), enter the
following command to run the same query, but this time save the results to
a new pandas DataFrame that's named `regions_by_country`. You provide that
name by using an argument with the `%%bigquery`magic command.



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



