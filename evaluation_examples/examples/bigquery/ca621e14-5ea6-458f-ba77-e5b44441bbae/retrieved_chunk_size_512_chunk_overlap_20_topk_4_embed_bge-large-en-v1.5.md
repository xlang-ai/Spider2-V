Documentation Source:
cloud.google.com/bigquery/docs/connected-sheets.md

Documentation Title:
Using Connected Sheets  |  BigQuery  |  Google Cloud

Documentation Content:
Enable the BigQuery API.
 
 
 
 

Enable the API

When you finish this topic, you can avoid continued billing by deleting the
resources you created. See Cleaning upfor more detail.

Open BigQuery datasets from Connected Sheets
--------------------------------------------

The following example uses a public dataset to show you how to connect to
BigQuery from Google Sheets.

Create or open a Google Sheets spreadsheet.

2. Click **Data**, click **Data connectors**, and then click **Connect to
BigQuery**.

**Note:**If you do not see the **Data connectors**option, see
Before you begin.
Click **Get connected**.

Select a Google Cloud project that has billing enabled.

Click **Public datasets**.

In the search box, type **chicago**and then select the
**chicago\_taxi\_trips**dataset.

7. Select the **taxi\_trips**table and then click **Connect**.

!Your spreadsheet should look similar to the following:

!

Start using the spreadsheet. You can create pivot tables, formulas, and charts
using familiar Google Sheets techniques.

Although the spreadsheet shows a preview of only 500 rows, any pivot tables,
formulas, and charts use the entire set of data. The maximum number of rows for
results returned for pivot tables is 50,000. You can also extract the data to a
sheet. The maximum number of rows for results returned for data extracts is
50,000. For more information, see the
Connected Sheets tutorial.

Open tables in Connected Sheets
-------------------------------

To open tables in Connected Sheets from the
Google Cloud console, use one of the following methods:

* Use the **Explorer**pane:


	In the **Explorer**pane, expand the dataset that contains the table
	that you want to open in Google Sheets.
	
	2. Next to the table name, click
	more\_vert**View actions**,
	and then select **Open with >Connected Sheets**:
	
	!
* Use the table toolbar:



Documentation Source:
cloud.google.com/bigquery/docs/samples/bigquery-query-external-sheets-temp.md

Documentation Title:
Query Sheets with a temporary table  |  BigQuery  |  Google Cloud

Documentation Content:
Use a shareable link or grant viewing access to the email address you



Documentation Source:
cloud.google.com/bigquery/docs/samples/bigquery-query-external-sheets-perm.md

Documentation Title:
Query Sheets with a permanent table  |  BigQuery  |  Google Cloud

Documentation Content:
dataset_id = "your-project.your_dataset"



Documentation Source:
cloud.google.com/bigquery/docs/samples/bigquery-pandas-public-data.md

Documentation Title:
Download public table data to DataFrame  |  BigQuery  |  Google Cloud

Documentation Content:
Construct a BigQuery client object.
client = bigquery.Client()



