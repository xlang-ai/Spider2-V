Documentation Source:
docs.snowflake.com/en/user-guide/sample-data-using.md

Documentation Title:
Using the Sample Database | Snowflake Documentation

Documentation Content:
```
selectcount(*)fromsnowflake_sample_data.tpch_sf1.lineitem;+----------+| COUNT(*) ||----------||  6001215 |+----------+useschemasnowflake_sample_data.tpch_sf1;selectcount(*)fromlineitem;+----------+| COUNT(*) ||----------||  6001215 |+----------+
```
CopyNote

You must have a running, current warehouse in your session to perform queries. You set the current warehouse in a session using the USE WAREHOUSEcommand (or within the Worksheet in the web interface.)

Using the Tutorial SQL Scripts¶
-------------------------------

Snowflake provides a set of tutorials, which are annotated SQL statements that query the sample data sets to answer a set of practical business questions.

To access the tutorials from Classic Console:

1. In the Worksheets!page, click on the down-arrow next to the worksheet tabs and select Open Tutorials:

!
2. The Open Worksheetdialog displays the list of available tutorials. In the dialog, select a tutorial and click on the Openbutton:

!
3. A new worksheet is created containing the contents of the tutorial:

!

You can then execute the queries in the tutorial as you would in any worksheet. You can also alter the tutorial in the worksheet and save it as a custom worksheet.

Was this page helpful?

YesNoVisit SnowflakeJoin the conversationDevelop with SnowflakeShare your feedbackRead the latest on our blogGet your own certificationPrivacy NoticeSite Terms© 2024Snowflake, Inc. All Rights Reserved.On this page

Viewing the Sample DatabaseQuerying Tables and Views in the Sample DatabaseUsing the Tutorial SQL ScriptsLanguage: **English**EnglishFrançaisDeutsch日本語한국어Português



Documentation Source:
docs.snowflake.com/en/user-guide/tutorials/tasty-bytes-sql-load.md

Documentation Title:
Load and query sample data using SQL | Snowflake Documentation

Documentation Content:
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

Step 2. Open the SQL worksheet for loading and querying data¶
-------------------------------------------------------------

You can use worksheets to write and run SQL commands on your Snowflake database. Your trial account has access
to a pre-loaded worksheet for this tutorial. The worksheet has the SQL commands that
you will run to create a database, load data into it, and query the data. For more information
about worksheets, see Getting started with worksheets.

To open the pre-loaded tutorial worksheet:

Select Projects» Worksheetsto open the list of worksheets.

2. Open [Tutorial] Using SQL to load and query sample data.

Your worksheet looks similar to the following image.

!Step 3. Set the role and warehouse to use¶
------------------------------------------

The role you use determines the privileges you have. In this tutorial, use the
ACCOUNTADMIN system role so that you can view and manage objects in your account.
For more information, see Using the ACCOUNTADMIN Role.

A warehouse provides the required resources to create and manage objects and run
SQL commands. These resources include CPU, memory, and temporary storage. Your
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
docs.snowflake.com/en/user-guide/tutorials/snowflake-in-20minutes.md

Documentation Title:
Snowflake in 20 minutes | Snowflake Documentation

Documentation Content:
Retrieve all data¶

Return all rows and columns from the table:


```
SELECT*FROMemp_basic;
```
CopyThe following is a partial result:


```
+------------+--------------+---------------------------+-----------------------------+--------------------+------------+| FIRST_NAME | LAST_NAME    | EMAIL                     | STREETADDRESS               | CITY               | START_DATE ||------------+--------------+---------------------------+-----------------------------+--------------------+------------|| Arlene     | Davidovits   | adavidovitsk@sf_tuts.com  | 7571 New Castle Circle      | Meniko             | 2017-05-03 || Violette   | Shermore     | vshermorel@sf_tuts.com    | 899 Merchant Center         | Troitsk            | 2017-01-19 || Ron        | Mattys       | rmattysm@sf_tuts.com      | 423 Lien Pass               | Bayaguana          | 2017-11-15 |.........| Carson     | Bedder       | cbedderh@sf_tuts.co.au    | 71 Clyde Gallagher Place    | Leninskoye         | 2017-03-29 || Dana       | Avory        | davoryi@sf_tuts.com       | 2 Holy Cross Pass           | Wenlin             | 2017-05-11 || Ronny      | Talmadge     | rtalmadgej@sf_tuts.co.uk  | 588 Chinook Street          | Yawata             | 2017-06-02 |+------------+--------------+---------------------------+-----------------------------+--------------------+------------+
```
Copy### Insert additional data rows¶

In addition to loading data from staged files into a table, you can insert rows directly into a table using the INSERTDML command.

For example, to insert two additional rows into the table:



Documentation Source:
docs.snowflake.com/en/user-guide/ui-snowsight-filters.md

Documentation Title:
Filter query results in dashboards and worksheets | Snowflake Documentation

Documentation Content:
Example: Working with date filters¶

For example, given a table with order data, such as the ORDERS table in the SNOWFLAKE\_SAMPLE\_DATA database and TPCH\_SF1 schema, you
might want to query the table and group the results by a specific time bucket, such as by day or by week, and specify a specific date range
for which to retrieve results.

To do so, you can write a query as follows:


```
SELECTCOUNT(O_ORDERDATE)asorders,:datebucket(O_ORDERDATE)asbucketFROMSNOWFLAKE_SAMPLE_DATA.TPCH_SF1.ORDERSWHEREO_ORDERDATE=:daterangeGROUPBY:datebucket(O_ORDERDATE)ORDERBYbucket;
```
CopyIn this example, you:

Count the number of orders and retrieve details about the order date from the ORDERS table.

Filter your results by a specific date range by including the :daterangesystem filter in your WHERE clause.

Group your results by a specific period of time by including the :datebucketsystem filter in your GROUP BY clause.

Sort the results from earliest to latest time period by including the ORDER BY clause.


When you add filters to your query, corresponding filter buttons appear at the top of your worksheet or dashboard:

!To manipulate the results that you see from your query, use the filters to select specific values.

For this example, set the Group byfilter, which corresponds to the date bucket filter, to group by Day. Set the other
filter, which corresponds to the date range filter, to `Alltime`.

When you select Applyand apply the filter to your results, the results are grouped by day and results like the following output
appear:


```
+--------+------------+| orders |  buckets   |+--------+------------+|    621 | 1992-01-01 ||    612 | 1992-01-02 ||    598 | 1992-01-03 ||    670 | 1992-01-04 |+--------+------------+
```
You can select a different date bucket to show a different grouping of data. For example, to view weekly order data, set the Group byfilter to Weekand select Apply. Results like the following output appear:


