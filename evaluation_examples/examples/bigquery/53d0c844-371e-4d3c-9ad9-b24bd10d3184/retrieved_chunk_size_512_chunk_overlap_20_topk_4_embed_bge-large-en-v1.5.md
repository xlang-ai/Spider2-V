Documentation Source:
cloud.google.com/bigquery/docs/export-file.md

Documentation Title:
Export query results to a file  |  BigQuery  |  Google Cloud

Documentation Content:
Console

1. In the Google Cloud console, open the BigQuery page.

Go to BigQuery
Click **Compose new query**.

Enter a valid SQL query in the **Query editor**text area.

Optional: To change the processing location, click **More**and select
**Query settings**. For **Data location**,
choose the locationof your data.

Click **Run**.

When the results are returned, click the **Save results**and select
**Google Sheets**.

7. If necessary, follow the prompts to log into your Google Account and
click **Allow**to give BigQuery permission to write the data
to your Google Drive `MY Drive`folder.

After following the prompts, you should receive an email with the
 subject "BigQuery Client Tools connected to your Google
 Account". The email contains information on the permissions you granted
 along with steps to remove the permissions.
8. When the results are saved, a message similar to the following appears
below the query results in the Google Cloud console: `Saved to Sheets as
"results-20190225-103531. Open`. Click the link in the message to view your
results in Google Sheets, or navigate to your `My Drive`folder and open the
file manually.

When you save query results to Google Sheets, the filename begins with
 `results-[DATE]`where `[DATE]`is today's date in the format
 `YYYYMMDD`.

**Note:**Saving results to Google Sheets is not supported by the bq command-line tool
or the API. For more information, see
Using Connected Sheets.### Troubleshoot file exports

When exporting data from BigQuery to Google Sheets, you might
find that some cells in the sheets are blank. This happens when the data you
are writing to the cell exceeds the Google Sheets limit of 50,000 characters.
To resolve this, use a
string functionin the SQL query to split the column with the long data into two or more
columns, then save the result to sheets again.

What's next
-----------

* Learn how to programmatically export a table to a JSON file.
* Learn about quotas for export jobs.
* Learn about BigQuery storage pricing.



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
cloud.google.com/bigquery/docs/writing-results.md

Documentation Title:
Writing query results  |  BigQuery  |  Google Cloud

Documentation Content:
Console

1. Open the BigQuery page in the Google Cloud console.

Go to the BigQuery page
In the **Explorer**panel, expand your project and select a dataset.

Enter a valid SQL query.

4. Click **More**and then select **Query settings**.

!
5. Select the **Set a destination table for query results**option.

!
In the **Destination**section, select the **Dataset**in which you want
to create the table, and then choose a **Table Id**.

7. In the **Destination table write preference**section, choose one of
the following:


	* **Write if empty**— Writes the query results to the table only
	if the table is empty.
	* **Append to table**— Appends the query results to an existing
	table.
	* **Overwrite table**— Overwrites an existing table with the same
	name using the query results.
Optional: For **Data location**, choose
your location.

To update the query settings, click **Save**.

Click **Run**. This creates a query job that writes the
query results to the table you specified.


Alternatively, if you forget to specify a destination table before running
your query, you can copy the cached results table to a permanent table by
clicking the **Save Results**button above the editor.



Documentation Source:
cloud.google.com/bigquery/docs/export-file.md

Documentation Title:
Export query results to a file  |  BigQuery  |  Google Cloud

Documentation Content:
Console

1. In the Google Cloud console, open the BigQuery page.

Go to BigQuery
Enter a valid SQL query in the **Query editor**text area.

Click **Run**.

4. When the results are returned, click **Save Results**.

!
Select **CSV (Google Drive)**or **JSON (Google Drive)**. When you save
results to Google Drive, you cannot choose the location. Results are
always saved to the root "My Drive" location.

6. It may take a few minutes to save the results to Google Drive. When
the results are saved, you receive a dialog message that includes the
filename —
`bq-results-[TIMESTAMP]-[RANDOM_CHARACTERS].[CSV or JSON]`.

!
In the dialog message, click **Open**to open the file, or navigate to
Google Drive and click **My Drive**.

Save query results to Google Sheets
-----------------------------------

Saving query results to Google Sheets is not supported by the bq command-line tool or
the API.

You might get an error when you try to open the BigQuery results
from Google Sheets. This error is due to the Drive SDK API
being unable to access Google Workspace. To resolve the issue,
you must enable your user account to
access Google Sheetswith the Drive SDK API.

To save query results to Google Sheets, use the Google Cloud console:



