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
cloud.google.com/bigquery/docs/quickstarts/load-data-bq.md

Documentation Title:
Load and query data with the bq tool  |  BigQuery  |  Google Cloud

Documentation Content:
4. Ensure that the BigQuery API is enabled.

Enable the APIIf you created a new project, the BigQuery API is automatically
 enabled.
5. In the Google Cloud console, activate Cloud Shell.

Activate Cloud ShellAt the bottom of the Google Cloud console, a
 Cloud Shellsession starts and displays a command-line prompt. Cloud Shell is a shell environment
 with the Google Cloud CLI
 already installed and with values already set for
 your current project. It can take a few seconds for the session to initialize.
Download the source public data file
------------------------------------

1. Download the
baby names zip file.
2. Extract the zip file. It contains a file named `NationalReadMe.pdf`that
describes the dataset schema.
Learn more about the baby names dataset.
3. Open the `yob2010.txt`file. It's a comma-separated value (CSV) file that
contains three columns: name, assigned sex at birth, and number of children
with that name. The file has no header row.
4. Move the file to your working directory.
	* If you're working in Cloud Shell, click
	more\_vert**More**> **Upload**, click **Choose Files**, choose the
	`yob2010.txt`file, and then click **Upload**.
	* If you're working in a local shell, copy or move the file `yob2010.txt`into the directory where you're running the bq tool.

Create a dataset
----------------

1. Create a dataset named `babynames`:

`bq mk babynames`The output is similar to the following:

`Dataset 'myproject:babynames' successfully created.`A dataset name can be up to 1,024 characters long and consist of A-Z, a-z,
0-9, and the underscore. The name cannot start with a number or underscore,
and it cannot have spaces.
2. Confirm that the dataset `babynames`now appears in your project:

`bq ls`The output is similar to the following:

`datasetId
-------------
 babynames`

Load data into a table
----------------------

1.



Documentation Source:
cloud.google.com/bigquery/docs/quickstarts/load-data-bq.md

Documentation Title:
Load and query data with the bq tool  |  BigQuery  |  Google Cloud

Documentation Content:
In the `babynames`dataset, load the source file `yob2010.txt`into a
new table that's named `names2010`:

`bq load babynames.names2010 yob2010.txt name:string,assigned_sex_at_birth:string,count:integer`The output is similar to the following:

`Upload complete.
Waiting on bqjob_r3c045d7cbe5ca6d2_0000018292f0815f_1 ... (1s) Current status: DONE`By default, when you load data, BigQuery expects UTF-8
encoded data. If you have data in ISO-8859-1 (or Latin-1) encoding and
you have problems with it, instruct BigQuery to treat
your data as Latin-1 using `bq load -E=ISO-8859-1`. For more information,
see Encoding.
2. Confirm that the table `names2010`now appears in the `babynames`dataset:

`bq ls babynames`The output is similar to the following. Some columns are omitted to simplify
the output.

`tableId Type
----------- ---------
 names2010 TABLE`
3. Confirm that the table schema of your new `names2010`table is
`name: string`, `assigned_sex_at_birth: string`, and `count: integer`:

`bq show babynames.names2010`The output is similar to the following. Some columns are omitted to simplify
the output.

`Last modified Schema Total Rows Total Bytes
----------------- ------------------------------- ------------ ------------
14 Mar 17:16:45 |- name: string 34089 654791
 |- assigned_sex_at_birth: string
 |- count: integer`

Query table data
----------------

1.



