Documentation Source:
docs.snowflake.com/en/user-guide/sample-data.md

Documentation Title:
Sample Data Sets | Snowflake Documentation

Documentation Content:
DOCUMENTATION/Getting StartedGuidesDeveloperReferenceReleasesTutorialsStatusOverviewConceptsTutorials4. Sample DataUsageTPC-DSTPC-H

Getting StartedSample DataSample Data Sets¶
=================

Snowflake provides sample data sets, such as the industry-standard TPC-DS and TPC-H benchmarks, for evaluating and testing a broad range of Snowflake’s SQL support.

Sample data sets are provided in a database named SNOWFLAKE\_SAMPLE\_DATA that has been
shared with your accountfrom the Snowflake SFC\_SAMPLES account.
If you do not see the database, you can create it yourself. Refer to Using the Sample Database.

The database contains a schema for each data set, with the sample data stored in the tables in each schema. The database and schemas
do not use any data storage so they do notincur storage charges for your account. You can execute queries on the tables in
these databases just as you would with any other databases in your account. Executing queries requires a running, current warehouse
for your session, which consumes credits.

**Next Topics:**Using the Sample DatabaseSample Data: TPC-DSSample Data: TPC-HSample Data: OpenWeatherMap — *Deprecated*Was this page helpful?

YesNoVisit SnowflakeJoin the conversationDevelop with SnowflakeShare your feedbackRead the latest on our blogGet your own certificationPrivacy NoticeSite Terms© 2024Snowflake, Inc. All Rights Reserved.Related content

Query Data in SnowflakeQuery SyntaxLanguage: **English**EnglishFrançaisDeutsch日本語한국어Português



Documentation Source:
docs.snowflake.com/en/user-guide/sample-data-using.md

Documentation Title:
Using the Sample Database | Snowflake Documentation

Documentation Content:
```
show databaseslike'%sample%';+-------------------------------+-----------------------+------------+------------+-------------------------+--------------+---------+---------+----------------+| created_on                    | name                  | is_default | is_current | origin                  | owner        | comment | options | retention_time ||-------------------------------+-----------------------+------------+------------+-------------------------+--------------+---------+---------+----------------|| 2016-07-14 14:30:21.711 -0700 | SNOWFLAKE_SAMPLE_DATA | N          | N          | SFC_SAMPLES.SAMPLE_DATA | ACCOUNTADMIN |         |         | 1              |+-------------------------------+-----------------------+------------+------------+-------------------------+--------------+---------+---------+----------------+
```
CopyNote that this example illustrates the sample database, SNOWFLAKE\_SAMPLE\_DATA, has been shared with your accountby Snowflake.

The origincolumn in the SHOW DATABASES output (or the Origincolumn in the Databases!page in the interface) displays the fully-qualified name of the shared
database, SFC\_SAMPLES.SAMPLE\_DATA, indicating it originated from the SFC\_SAMPLES account (used by Snowflake to share the sample data).

Querying Tables and Views in the Sample Database¶
-------------------------------------------------

To use a table or view in the sample database, you can either:

* Reference the fully-qualified name of the table in your query (in the form of `snowflake_sample_data.schema_name.object_name`).

OR
Specify the sample database (and schema) for your session using the USE DATABASEand/or USE SCHEMAcommands.


The following two examples illustrate using both approaches to query the lineitemtable in the tpch\_sf1schema:



Documentation Source:
docs.snowflake.com/en/user-guide/querying-semistructured.md

Documentation Title:
Querying Semi-structured Data | Snowflake Documentation

Documentation Content:
```
SELECT*FROMcar_sales;+-------------------------------------------+| SRC                                       ||-------------------------------------------|| {                                         ||   "customer": [                           ||     {                                     ||       "address": "San Francisco, CA",     ||       "name": "Joyce Ridgely",            ||       "phone": "16504378889"              ||     }                                     ||   ],                                      ||   "date": "2017-04-28",                   ||   "dealership": "Valley View Auto Sales", ||   "salesperson": {                        ||     "id": "55",                           ||     "name": "Frank Beasley"               ||   },                                      ||   "vehicle": [                            ||     {                                     ||       "extras": [                         ||         "ext warranty",                   ||         "paint protection"                ||       ],                                  ||       "make": "Honda",                    ||       "model": "Civic",                   ||       "price": "20275",                   ||       "year": "2017"                      ||     }                                     ||   ]                                       || }                                         || {                                         ||   "customer": [                           ||     {                                     ||       "address": "New York, NY",          ||       "name": "Bradley Greenbloom",       ||       "phone": "12127593751"              ||     }                                     ||   ],                                      ||   "date": "2017-04-28",                   ||   "dealership": "Tindel Toyota",          ||   "salesperson": {                        ||     "id": "274",                          ||     "name": "Greg Northrup"               ||   },                                      ||   "vehicle": [                            ||     {                                     ||       "extras": [                         ||         "ext warranty",                   ||         "rust proofing",                  ||         "fabric protection"               ||       ],                                  ||       "make": "Toyota",                   ||       "model": "Camry",                   ||       "price": "23500",                   ||       "year": "2017"                      ||     }                                     ||   ]                                       || }                                         |+-------------------------------------------+
```
CopyTraversing Semi-structured Data¶
--------------------------------

Insert a colon :between the VARIANT column name and any first-level element: :.



Documentation Source:
docs.snowflake.com/en/user-guide/querying-semistructured.md

Documentation Title:
Querying Semi-structured Data | Snowflake Documentation

Documentation Content:
```
CREATEORREPLACETABLEcar_sales(srcvariant)ASSELECTPARSE_JSON(column1)ASsrcFROMVALUES('{ "date" : "2017-04-28", "dealership" : "Valley View Auto Sales","salesperson" : {"id": "55","name": "Frank Beasley"},"customer" : [{"name": "Joyce Ridgely", "phone": "16504378889", "address": "San Francisco, CA"}],"vehicle" : [{"make": "Honda", "model": "Civic", "year": "2017", "price": "20275", "extras":["ext warranty", "paint protection"]}]}'),('{ "date" : "2017-04-28", "dealership" : "Tindel Toyota","salesperson" : {"id": "274","name": "Greg Northrup"},"customer" : [{"name": "Bradley Greenbloom", "phone": "12127593751", "address": "New York, NY"}],"vehicle" : [{"make": "Toyota", "model": "Camry", "year": "2017", "price": "23500", "extras":["ext warranty", "rust proofing", "fabric protection"]}  ]}')v;
```
CopySelect the data:



