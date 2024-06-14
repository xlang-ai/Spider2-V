Documentation Source:
cloud.google.com/bigquery/docs/bigqueryml-mf-explicit-tutorial.md

Documentation Title:
Use BigQuery ML to make recommendations from movie ratings  |  Google Cloud

Documentation Content:
Delete your dataset

Deleting your project removes all datasets and all tables in the project. If you
prefer to reuse the project, you can delete the dataset you created in this
tutorial:

1. If necessary, open the BigQuery page in the Google Cloud console.

Go to the BigQuery page
In the navigation, click the **bqml\_tutorial**dataset you created.

Click **Delete dataset**on the right side of the window.
This action deletes the dataset, the table, and all the data.

In the **Delete dataset**dialog box, confirm the delete command by typing
the name of your dataset (`bqml_tutorial`) and then click **Delete**.



Documentation Source:
cloud.google.com/bigquery/docs/arima-speed-up-tutorial.md

Documentation Title:
Scalable forecasting with millions of time-series in BigQuery  |  Google Cloud

Documentation Content:
Delete your dataset

Deleting your project removes all datasets and all tables in the project. If you
prefer to reuse the project, you can delete the dataset you created in this
tutorial:

1. If necessary, open the BigQuery page in the
Google Cloud console.

Go to the BigQuery page
In the navigation, click the **bqml\_tutorial**dataset you created.

Click **Delete dataset**to delete the dataset, the table, and all of the
data.

In the **Delete dataset**dialog, confirm the delete command by typing
the name of your dataset (`bqml_tutorial`) and then click **Delete**.



Documentation Source:
cloud.google.com/bigquery/docs/bigqueryml-mf-implicit-tutorial.md

Documentation Title:
Use BigQuery ML to make recommendations from Google analytics data  |  Google Cloud

Documentation Content:
Delete your dataset

Deleting your project removes all datasets and all tables in the project. If you
prefer to reuse the project, you can delete the dataset you created in this
tutorial:

1. If necessary, open the BigQuery page in the
Google Cloud console.

Go to the BigQuery page
In the navigation, click the **bqml\_tutorial**dataset you created.

Click **Delete dataset**on the right side of the window.
This action deletes the dataset, the table, and all the data.

In the **Delete dataset**dialog box, confirm the delete command by typing
the name of your dataset (`bqml_tutorial`) and then click **Delete**.



Documentation Source:
cloud.google.com/bigquery/docs/managing-datasets.md

Documentation Title:
Manage datasets  |  BigQuery  |  Google Cloud

Documentation Content:
Console

1. Go to the **BigQuery**page.

Go to BigQuery
In the **Explorer**pane, expand your project and select a dataset.

Expand the
more\_vert**Actions**option and click **Delete**.

In the **Delete dataset**dialog, type `delete`into the field, and then
click **Delete**.


**Note:**When you delete a dataset using the Google Cloud console, the tables
are automatically removed.### SQL

To delete a dataset, use the
`DROP SCHEMA`DDL statement.

The following example deletes a dataset named `mydataset`:

1. In the Google Cloud console, go to the **BigQuery**page.

Go to BigQuery
2. In the query editor, enter the following statement:


```
DROP SCHEMA IF EXISTS mydataset;

```
By default, this only works to delete an empty dataset.
To delete a dataset and all of its contents, use the `CASCADE`keyword:


```
DROP SCHEMA IF EXISTS mydataset CASCADE;

```
Click play\_circle**Run**.


For more information about how to run queries, see Run an interactive query.



