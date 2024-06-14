Documentation Source:
docs.snowflake.com/en/user-guide/tutorials/tasty-bytes-python-load.md

Documentation Title:
Load and query sample data using Snowpark Python | Snowflake Documentation

Documentation Content:
```
# Use SQL to create our Blob Stagesession.sql('CREATE OR REPLACE STAGE tasty_bytes_sample_data.public.blob_stage url = "s3://sfquickstarts/tastybytes/" file_format = (type = csv);').collect()
```
CopyThis line creates a stage named blob\_stage. A stage is a location that holds data files to load
into a Snowflake database. This tutorial creates a stage that loads data from an Amazon S3 bucket. The
tutorial uses an existing bucket with a CSV file that contains the data. It loads the data from this CSV
file into the table that is created later in this tutorial. For more information, see Bulk loading from Amazon S3.
3. This step in the worksheet includes the following code:


```
# Define our Menu Schemamenu_schema=StructType([StructField("menu_id",IntegerType()),\
                     StructField("menu_type_id",IntegerType()),\
                     StructField("menu_type",StringType()),\
                     StructField("truck_brand_name",StringType()),\
                     StructField("menu_item_id",IntegerType()),\
                     StructField("menu_item_name",StringType()),\
                     StructField("item_category",StringType()),\
                     StructField("item_subcategory",StringType()),\
                     StructField("cost_of_goods_usd",IntegerType()),\
                     StructField("sale_price_usd",IntegerType()),\
                     StructField("menu_item_health_metrics_obj",VariantType())])
```
CopyThis code creates a StructTypeobject named menu\_schema. This object consists of a listof StructFieldobjects that describe the fields in the CSV file in the stage. For more information,
see Working With Files in a Stage.
4. This step in the worksheet includes the following code:


```
# Create a Dataframe from our Menu file from our Blob Stagedf_blob_stage_read=session.read.schema(menu_schema).csv('@tasty_bytes_sample_data.public.blob_stage/raw_pos/menu/')
```
CopyThis line creates the df\_blob\_stage\_readDataFrame. This DataFrame is configured to read data from
the CSV file located in the specified stage, using the specified menu\_schemaschema. The schema
contains information about the types and names of the columns of data.



Documentation Source:
docs.snowflake.com/en/user-guide/tutorials/load-from-cloud-tutorial.md

Documentation Title:
Load data from cloud storage: Amazon S3 | Snowflake Documentation

Documentation Content:
```
USEWAREHOUSEcompute_wh;
```
Copy
Step 4. Set up a table that you can load¶
-----------------------------------------

A database is a repository for your data. The data is stored in tables that you can
manage and query. A schema is a logical grouping of database objects, such as tables
and views. For example, a schema might contain the database objects required for a
specific application. For more information, see Databases, Tables and Views - Overview.

To create a database, a schema, and a table that you can load, do the following:

1. In the open worksheet, place your cursor in the CREATE OR REPLACE DATABASE line,
enter a name for your database and an optional comment, then select Run. For
example:


```
CREATEORREPLACEDATABASEcloud_data_dbCOMMENT='Database for loading cloud data';
```
Copy
2. Place your cursor in the CREATE OR REPLACE SCHEMA line, enter a name for your schema
and an optional comment, then select Run. For example:


```
CREATEORREPLACESCHEMAcloud_data_db.s3_dataCOMMENT='Schema for tables loaded from S3';
```
Copy
3. Place your cursor in the CREATE OR REPLACE TABLE lines, complete the table
definition, add an optional comment, and select Run. For example, the following
table contains six columns:


```
CREATEORREPLACETABLEcloud_data_db.s3_data.calendar(full_dateDATE,day_nameVARCHAR(10),month_nameVARCHAR(10),day_numberVARCHAR(2),full_yearVARCHAR(4),holidayBOOLEAN)COMMENT='Table to be loaded from S3 calendar data file';
```
Copy
4. To confirm that the table was created successfully, place your cursor in the SELECT line,
then select Run.



Documentation Source:
docs.snowflake.com/en/user-guide/tutorials/load-from-cloud-tutorial.md

Documentation Title:
Load data from cloud storage: Amazon S3 | Snowflake Documentation

Documentation Content:
What you will learn¶

In this tutorial you will learn how to:

Use a role that has the privileges to create and use the Snowflake objects required by this tutorial.

Use a warehouse to access resources.

Create a database and schema.

Create a table.

Create a storage integration for your cloud platform.

Create a stage for your storage integration.

Load data into the table from the stage.

Query the data in the table.

Prerequisites¶
--------------

This tutorial assumes the following:

You have a supported browser.

You have a trial account. If you do not have a trial account yet, you can sign up
for a free trial.
You can choose any Snowflake Cloud Region.

* You have an account that you can use to bulk load data from one of the following
cloud providers:


	AWS S3. See Bulk loading from Amazon S3.
	
	Microsoft Azure. See Bulk loading from Microsoft Azure.
	
	Google Cloud Storage. See Bulk loading from Google Cloud Storage.

Note

This tutorial is only available to users with a trial account. The sample worksheet is not available
for other types of accounts.

Step 1. Sign in using Snowsight¶
--------------------------------

To access Snowsight over the public Internet, do the following:

In a supported web browser, navigate to https://app.snowflake.com.

Provide your account identifieror account URL.
If you’ve previously signed in to Snowsight, you might see an account name that you can select.

Sign in using your Snowflake account credentials.

Step 2. Open the Load data from cloud storage worksheet¶
--------------------------------------------------------

You can use worksheets to write and run SQL commands on your database. Your trial
account has access to a template worksheet for this tutorial. The worksheet has the SQL
commands that you will run to create database objects, load data, and query the
data. Because it is a template worksheet, you will be invited to enter your own values
for certain SQL parameters. For more information about worksheets,
see Getting started with worksheets.

The worksheet for this tutorial is not pre-loaded into the trial account. To open
the worksheet for this tutorial, follow these steps:

1.



Documentation Source:
docs.snowflake.com/en/user-guide/tutorials/tasty-bytes-sql-load.md

Documentation Title:
Load and query sample data using SQL | Snowflake Documentation

Documentation Content:
```
SELECT*FROMtasty_bytes_sample_data.raw_pos.menu;
```
CopyYour output shows the columns of the table you created. At this point in the tutorial, the
table does not have any rows.
Step 5. Create a stage and load the data¶
-----------------------------------------

A stage is a location that holds data files to load into a Snowflake database. This tutorial creates
a stage that loads data from an Amazon S3 bucket. This tutorial uses an existing bucket with
a CSV file that contains the data. You load the data from this CSV file into the table you created
previously. For information, see Bulk loading from Amazon S3.

To create a stage, do the following:

1. In the open worksheet, place your cursor in the CREATE OR REPLACE STAGE lines, then select Run.


```
CREATEORREPLACESTAGEtasty_bytes_sample_data.public.blob_stageurl='s3://sfquickstarts/tastybytes/'file_format=(type=csv);
```
Copy
2. To confirm that the stage was created successfully, place your cursor in the LIST line,
then select Run.


```
LIST@tasty_bytes_sample_data.public.blob_stage/raw_pos/menu/;
```
CopyYour output looks similar to the following image.

!
3. To load the data into the table, place your cursor in the COPY INTO lines, then select Run.


```
COPYINTOtasty_bytes_sample_data.raw_pos.menuFROM@tasty_bytes_sample_data.public.blob_stage/raw_pos/menu/;
```
Copy
Step 6. Query the data¶
-----------------------

Now that the data is loaded, you can run queries on the menutable.

To run a query in the open worksheet, select the line or lines of the SELECT command,
and then select Run.

For example, to return the number of rows in the table, run the following query:


```
SELECTCOUNT(*)ASrow_countFROMtasty_bytes_sample_data.raw_pos.menu;
```
CopyYour output looks similar to the following image.

!Run this query to return the top ten rows in the table:



