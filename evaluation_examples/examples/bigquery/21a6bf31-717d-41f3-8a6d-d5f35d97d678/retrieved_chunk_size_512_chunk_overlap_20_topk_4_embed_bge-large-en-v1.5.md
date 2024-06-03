Documentation Source:
cloud.google.com/bigquery/docs/samples/bigquery-browse-table.md

Documentation Title:
Preview table data  |  BigQuery  |  Google Cloud

Documentation Content:
table_id = "your-project.your_dataset.your_table_name"



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
cloud.google.com/bigquery/docs/bigquery-web-ui.md

Documentation Title:
Explore the Google Cloud console  |  BigQuery

Documentation Content:
Run query demo guide

The **Get started**section contains the demo guide for running a sample
query on a Google Trends public dataset.

To run the demo guide, follow these steps. To exit the demo at any time,
click close**Close tour**.

1. In the Google Cloud console, go to the
**BigQuery**page.

Go to BigQuery
Ensure that you are on the BigQuery
welcome page: click !**Welcome**.

3. Click search**Open this query**.

The `bigquery-public-data`project is automatically added to the **Explorer**pane. The public project and the `google_trends`dataset are expanded, and
the **Google Trends Data**dialog highlights the starred `top_terms`table.
Additionally, the query editor is opened with a predefined query.

!
In the **Google Trends Data**dialog, click **Next**.

5. In the **Google Trends Query**dialog, click **Next**.

To return to the previous step, click **Back**in the dialog.
6. In the **Run this query**dialog, click **Try it**.

To return to the previous step, click **Back**in the dialog.
7. In the **Query results**dialog, click **Done**.

!

You can run this demo multiple times.

To view the Google Trends public dataset, in the welcome page, click
**View dataset**.



Documentation Source:
cloud.google.com/bigquery/docs/visualize-looker-studio.md

Documentation Title:
Analyze data with Looker Studio  |  BigQuery  |  Google Cloud

Documentation Content:
```
SELECT
  *
FROM
  `bigquery-public-data.austin_bikeshare.bikeshare_trips`
LIMIT
  1000;

```
Click play\_circle**Run**.

8. In the **Query results**section, click **Explore data**, and then click
**Explore with Looker Studio**.

!
On the **Welcome to Looker Studio**page, click
**Get Started**if you agree to the Google Looker Studio and
Google Terms of Service.

10. On the **Authorize Looker Studio access**page, click **Authorize**to authorize the connection if you agree to the terms of service, and
then select your marketing preferences. Only you can view data in your
report unless you grant others permission to view the data.

The report editor displays your query results as
Looker Studio charts.

The following image shows some features of a Looker Studio report:

!**Legend**:

1. Looker Studio logo and report name.
	* To go to the **Looker Studio**page, click the
	logo.
	* To edit the report name, click the name.
2. Looker Studio toolbar. The
**Add a chart**tool is highlighted.
3. Report title. To edit the text, click the text box.
4. Table (selected). You can interact with a selected
chart by using the options in the chart header.
5. Bar chart (not selected).
6. **Chart**properties pane. For a selected table,
you can configure its data properities and appearance
on the **Setup**and **Style**tabs.
7. **Data**pane. In this pane, you can access the
fields and data sources to use in your report.
	* To add data to a chart, drag fields from the
	**Data**pane onto the chart.
	* To create a chart, drag a field from the **Data**pane onto the canvas.
8. **Save and share**. Save this report so you can view,
edit, and share it with others later. Before you save
the report, review the data source settings and the
credentials that the data sources use.



