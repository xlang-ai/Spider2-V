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
docs.snowflake.com/en/user-guide/tutorials/data-load-external-tutorial.md

Documentation Title:
Tutorial: Bulk loading from Amazon S3 using COPY | Snowflake Documentation

Documentation Content:
CSV¶


```
SELECT*FROMmycsvtable;
```
CopyThe query returns the following results:


```
+----+-----------+------------+----------------------------------+----------------------------------------+----------------+----------------+--------------------------------+------------------+------------+| ID | LAST_NAME | FIRST_NAME | COMPANY                          | EMAIL                                  | WORKPHONE      | CELLPHONE      | STREETADDRESS                  | CITY             | POSTALCODE ||----+-----------+------------+----------------------------------+----------------------------------------+----------------+----------------+--------------------------------+------------------+------------||  6 | Reed      | Moses      | Neque Corporation                | eget.lacus@facilisis.com               | 1-449-871-0780 | 1-454-964-5318 | Ap #225-4351 Dolor Ave         | Titagarh         |      62631 ||  7 | Audrey    | Franks     | Arcu Eu Limited                  | eu.dui@aceleifendvitae.org             | 1-527-945-8935 | 1-263-127-1173 | Ap #786-9241 Mauris Road       | Bergen           |      81958 ||  8 | Jakeem    | Erickson   | A Ltd                            | Pellentesque.habitant@liberoProinmi.ca | 1-381-591-9386 | 1-379-391-9490 | 319-1703 Dis Rd.               | Pangnirtung      |      62399 ||  9 | Xaviera   | Brennan    | Bibendum Ullamcorper Limited     | facilisi.Sed.neque@dictum.edu          | 1-260-757-1919 | 1-211-651-0925 | P.O. Box 146, 8385 Vel Road    | Béziers          |      13082 || 10 | Francis   | Ortega     | Vitae Velit Egestas Associates   | egestas.rhoncus.Proin@faucibus.com     | 1-257-584-6487 | 1-211-870-2111 | 733-7191 Neque Rd.



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
docs.snowflake.com/en/user-guide/tutorials/load-from-cloud-tutorial.md

Documentation Title:
Load data from cloud storage: Amazon S3 | Snowflake Documentation

Documentation Content:
```
SELECT*FROMcloud_data_db.s3_data.calendar;
```
CopyThe output shows the columns of the table you created. Currently, the table does not have any rows.
Step 5. Create a storage integration¶
-------------------------------------

Before you can load data from cloud storage, you must configure a storage integration that is
specific to your cloud provider. The following example is specific to Amazon S3 storage.

Storage integrations are named, first-class Snowflake objects that avoid the need for passing explicit cloud
provider credentials such as secret keys or access tokens. Integration objects store an AWS identity
and access management (IAM) user ID.

To create a storage integration for Amazon S3, do the following:

Use the AWS Management Console to create an IAM policy and an IAM role. These resources provide
secure access to your S3 bucket for loading data. You will need these resources
to create a storage integration in Snowflake. After logging into the console, complete
Steps 1 and 2under
Option 1: Configuring a Snowflake storage integration to access Amazon S3.

2. In the open worksheet, place your cursor in the CREATE OR REPLACE STORAGE INTEGRATION lines, define
the required parameters, and select Run. For example:


```
CREATEORREPLACESTORAGEINTEGRATIONs3_data_integrationTYPE=EXTERNAL_STAGESTORAGE_PROVIDER='S3'STORAGE_AWS_ROLE_ARN='arn:aws:iam::631373164455:role/tutorial_role'ENABLED=TRUESTORAGE_ALLOWED_LOCATIONS=('s3://snow-tutorial-bucket/s3data/');
```
CopySet STORAGE\_AWS\_ROLE\_ARN to the unique identifier for the IAM role that you created previously.
You can find this value under IAM > Rolesin the AWS Management Console.
3. Place your cursor in the DESCRIBE INTEGRATION line, specify the name of the storage
integration you created, and select Run.



