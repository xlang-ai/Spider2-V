Documentation Source:
docs.snowflake.com/en/user-guide/tutorials/load-from-cloud-tutorial.md

Documentation Title:
Load data from cloud storage: Amazon S3 | Snowflake Documentation

Documentation Content:
Summary and key points¶

In summary, you used a pre-loaded template worksheet in Snowsight to complete the following steps:

Set the role and warehouse to use.

Create a database, schema, and table.

Create a storage integration and configure permissions on cloud storage.

Create a stage and load the data from the stage into the table.

Query the data.


Here are some key points to remember about loading and querying data:

* You need the required permissions to create and manage objects in your account. In this tutorial,
you use the ACCOUNTADMIN system role for these privileges.

This role is not normally used to create objects. Instead, we recommend creating a hierarchy of
roles aligned with business functions in your organization. For more information, see
Using the ACCOUNTADMIN Role.
You need a warehouse for the resources required to create and manage objects and run SQL commands.
This tutorial uses the compute\_whwarehouse included with your trial account.

You created a database to store the data and a schema to group the database objects logically.

You created a storage integration and a stage to load data from a CSV file stored in an AWS S3 bucket.

After the data was loaded into your database, you queried it using a SELECT statement.



Documentation Source:
docs.snowflake.com/en/user-guide/tutorials/load-from-cloud-tutorial.md

Documentation Title:
Load data from cloud storage: Amazon S3 | Snowflake Documentation

Documentation Content:
To open
the worksheet for this tutorial, follow these steps:

1. If you are signing in to your Snowsight trial account for the first time,
select Startunder Load data into Snowflakeon the
Where do you want to start?screen.

If you have left the Where do you want to start?screen, go to the
Worksheetstab and select Continuein the banner.
2. Click anywhere in the middle panel named Load data from cloud storage.

The [Template] Load data from cloud storage worksheetopens, and your browser
looks similar to the following image.

!Step 3. Set the role and warehouse to use¶
------------------------------------------

The role you use determines the privileges you have. In this tutorial, use the
ACCOUNTADMIN system role so that you can view and manage objects in your account.
For more information, see Using the ACCOUNTADMIN Role.

A warehouse provides the compute resources that you need to execute DML operations, load data,
and run queries. These resources include CPU, memory, and temporary storage. Your
trial account has a virtual warehouse (compute\_wh) that you can use for this
tutorial. For more information, see Virtual warehouses.

To set the role and warehouse to use, do the following:

1. In the open worksheet, place your cursor in the USE ROLE line.


```
USEROLEaccountadmin;
```
Copy
2. In the upper-right corner of the worksheet, select Run.

Note

In this tutorial, run SQL statements one at a time. Do not select Run All.
3. Place your cursor in the USE WAREHOUSE line, then select Run.



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



Documentation Source:
docs.snowflake.com/en/user-guide/tutorials/data-load-external-tutorial.md

Documentation Title:
Tutorial: Bulk loading from Amazon S3 using COPY | Snowflake Documentation

Documentation Content:
Creating the database, tables, and warehouse¶

Execute the following statements to create a database, two tables (for csv and json data),
and a virtual warehouse needed for this tutorial. After you complete the tutorial, you can
drop these objects.


```
CREATEORREPLACEDATABASEmydatabase;CREATEORREPLACETEMPORARYTABLEmycsvtable(idINTEGER,last_nameSTRING,first_nameSTRING,companySTRING,emailSTRING,workphoneSTRING,cellphoneSTRING,streetaddressSTRING,citySTRING,postalcodeSTRING);CREATEORREPLACETEMPORARYTABLEmyjsontable(json_dataVARIANT);CREATEORREPLACEWAREHOUSEmywarehouseWITHWAREHOUSE_SIZE='X-SMALL'AUTO_SUSPEND=120AUTO_RESUME=TRUEINITIALLY_SUSPENDED=TRUE;
```
CopyNote the following:

The `CREATEDATABASE`statement creates a database. The database automatically includes a schema named ‘public’.

The `CREATETABLE`statements create target tables for CSV and JSON data. The tables are temporary, that is, they
persist only for the duration of the user session and are not visible to other users.

The `CREATEWAREHOUSE`statement creates an initially suspended warehouse. The
statement also sets `AUTO_RESUME=true`, which starts the warehouse automatically when
you execute SQL statements that require compute resources.

Step 1. Create file format objects¶
-----------------------------------

When you load data files from an S3 bucket into a table, you must describe the format of the file
and specify how the data in the file should be interpreted and processed. For example,
if you are loading pipe-delimited data from a CSV file, you must specify that the file
uses the CSV format with pipe symbols as delimiters.

When you execute the COPY INTO command, you specify this format information. You can
either specify this information as options in the command (e.g.
`TYPE=CSV`, `FIELD_DELIMITER='|'`, etc.) or you can specify a
file format object that contains this format information. You can create a named file
format object using the CREATE FILE FORMATcommand.

In this step, you create file format objects describing the data format of the sample CSV and
JSON data provided for this tutorial.



