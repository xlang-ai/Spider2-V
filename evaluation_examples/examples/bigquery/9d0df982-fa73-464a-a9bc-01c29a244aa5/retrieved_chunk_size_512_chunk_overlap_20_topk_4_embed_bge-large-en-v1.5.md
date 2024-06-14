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
cloud.google.com/bigquery/docs/analytics-hub-view-subscribe-listings.md

Documentation Title:
View and subscribe to listings  |  BigQuery  |  Google Cloud

Documentation Content:
Required permissions

* Create new datasets: `bigquery.datasets.create`or `bigquery.datasets.*`to
 perform additional actions on datasets.
* Query datasets: `bigquery.jobs.create`or `bigquery.jobs.*`to perform
 additional actions on jobs.
You might also be able to get these permissions with custom rolesor other predefined roles.

Discover listings
-----------------

To discover public and private listings, follow these steps:

1. In the Google Cloud console, go to the **BigQuery**page.

Go to BigQuery
In the **Explorer**pane, click add**Add data**.

3. In the **Add data**dialog, click **Analytics Hub**. The **Analytics Hub**dialog appears containing listings that you can access. For Salesforce Data Cloud listings, there is a button in the
**Explorer**pane that automatically filters related listings.

Alternatively, to open the Analytics Hub dialog you can also go
to Analytics Huband click **Search
listings**.
To filter listings by their name or description, enter the name or
description of the listing in the **Search for listings**field.

5. In the **Filter**section, you can filter listings based on the following
fields:


	**Listings**: select whether you want to view private listings, public
	listings, or listingswithin your org.
	
	**Categories**: select the desired categories.
	
	**Location**: select the desired location. For more information, see
	Supported regions.
	
	**Provider**: select the data provider. Some data providers require you to
	request access to their *commercial datasets*. After requesting access,
	the data provider contacts you to share their datasets.
Browse through the filtered listings.


Subscribe to listings
---------------------

Subscribing to a listinggives you **read-only access**to the data in the listing by creating a linked
datasetin your
project.

**Caution:**We recommend that you don't put data into a project that is within a
VPC Service Controls perimeter. If you do so, then you must add the appropriate
ingress and egress rules.To subscribe to a listing, follow these steps:



Documentation Source:
cloud.google.com/bigquery/docs/bi-engine-looker-studio.md

Documentation Title:
Quickstart using Looker Studio  |  BigQuery  |  Google Cloud

Documentation Content:
Creating your data source

To create your data source:

Open Looker Studio.

2. On the **Reports**page, in the **Start a new report section**, click the
**Blank Report**template. This creates a new untitled report.

!
If prompted, complete the **Marketing Preferences**and the **Account and
Privacy**settings and then click **Save**. You may need to click the **Blank**template again after saving your settings.

4. In the **Add a data source**window, click **Create new data source**.

!
In the **Google Connectors**section, hover over **BigQuery**and then click **Select**.

For **Authorization**, click **Authorize**. This allows Looker Studio
access to your Google Cloud project.

In the **Request for permission**dialog, click **Allow**to give
Looker Studio the ability to view data in BigQuery. You may
not receive this prompt if you previously used Looker Studio.

Leave **My Projects**selected and in the **Project**pane, click the name of
your project.

In the **Dataset**pane, click **biengine\_tutorial**.

In the **Table**pane, click **311\_service\_requests\_copy**.

In the upper right corner of the window, click **Connect**. Once Looker Studio
connects to the BigQuery data source, the table's fields are
displayed. You can use this page to adjust the field properties or to create new
calculated fields.

In the upper right corner, click **Add to report**.

When prompted, click **Add to report**.

In the **Request for permission**dialog, click **Allow**to give
Looker Studio the ability to view and manage files in Google Drive.
You may not receive this prompt if you previously used Looker Studio.



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



