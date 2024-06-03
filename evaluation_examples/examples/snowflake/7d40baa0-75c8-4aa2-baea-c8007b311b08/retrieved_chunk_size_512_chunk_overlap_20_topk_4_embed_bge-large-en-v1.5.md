Documentation Source:
docs.snowflake.com/en/user-guide/tutorials/data-load-internal-tutorial.md

Documentation Title:
Tutorial: Bulk loading from a local file system using COPY | Snowflake Documentation

Documentation Content:
CSV¶


```
SELECT*FROMmycsvtable;
```
CopyThe query returns the following results:


```
+----+-----------+------------+----------------------------------+----------------------------------------+----------------+----------------+---------------------------------+------------------+------------+| ID | LAST_NAME | FIRST_NAME | COMPANY                          | EMAIL                                  | WORKPHONE      | CELLPHONE      | STREETADDRESS                   | CITY             | POSTALCODE ||----+-----------+------------+----------------------------------+----------------------------------------+----------------+----------------+---------------------------------+------------------+------------||  6 | Reed      | Moses      | Neque Corporation                | eget.lacus@facilisis.com               | 1-449-871-0780 | 1-454-964-5318 | Ap #225-4351 Dolor Ave          | Titagarh         |      62631 ||  7 | Audrey    | Franks     | Arcu Eu Limited                  | eu.dui@aceleifendvitae.org             | 1-527-945-8935 | 1-263-127-1173 | Ap #786-9241 Mauris Road        | Bergen           |      81958 ||  8 | Jakeem    | Erickson   | A Ltd                            | Pellentesque.habitant@liberoProinmi.ca | 1-381-591-9386 | 1-379-391-9490 | 319-1703 Dis Rd.                | Pangnirtung      |      62399 ||  9 | Xaviera   | Brennan    | Bibendum Ullamcorper Limited     | facilisi.Sed.neque@dictum.edu          | 1-260-757-1919 | 1-211-651-0925 | P.O. Box 146, 8385 Vel Road     | Béziers          |      13082 || 10 | Francis   | Ortega     | Vitae Velit Egestas Associates   | egestas.rhoncus.Proin@faucibus.com     | 1-257-584-6487 | 1-211-870-2111 | 733-7191 Neque Rd.



Documentation Source:
docs.snowflake.com/en/user-guide/tutorials/tasty-bytes-sql-load.md

Documentation Title:
Load and query sample data using SQL | Snowflake Documentation

Documentation Content:
```
USEWAREHOUSEcompute_wh;
```
Copy
Step 4. Create a database, schema, and table¶
---------------------------------------------

A database stores data in tables that you can manage and query. A schema is a logical
grouping of database objects, such as tables and views. For example, a schema might
contain the database objects required for a specific application. For more information,
see Databases, Tables and Views - Overview.

In this tutorial, you create a database named tasty\_bytes\_sample\_data, a
schema named raw\_pos, and a table named menu.

To create the database, schema, and table, do the following:

1. In the open worksheet, place your cursor in the CREATE OR REPLACE DATABASE line,
then select Run.


```
CREATEORREPLACEDATABASEtasty_bytes_sample_data;
```
Copy
2. Place your cursor in the CREATE OR REPLACE SCHEMA line, then select Run.


```
CREATEORREPLACESCHEMAtasty_bytes_sample_data.raw_pos;
```
Copy
3. Place your cursor in the CREATE OR REPLACE TABLE lines, then select Run.


```
CREATEORREPLACETABLEtasty_bytes_sample_data.raw_pos.menu(menu_idNUMBER(19,0),menu_type_idNUMBER(38,0),menu_typeVARCHAR(16777216),truck_brand_nameVARCHAR(16777216),menu_item_idNUMBER(38,0),menu_item_nameVARCHAR(16777216),item_categoryVARCHAR(16777216),item_subcategoryVARCHAR(16777216),cost_of_goods_usdNUMBER(38,4),sale_price_usdNUMBER(38,4),menu_item_health_metrics_objVARIANT);
```
Copy
4. To confirm that the table was created successfully, place your cursor in the SELECT line,
then select Run.



Documentation Source:
docs.snowflake.com/en/user-guide/tutorials/load-from-cloud-tutorial-gcs.md

Documentation Title:
Load data from cloud storage: GCS | Snowflake Documentation

Documentation Content:
```
USEWAREHOUSEcompute_wh;
```
Copy
Step 4. Create a database, schema, and table¶
---------------------------------------------

A database is a repository for your data. The data is stored in tables that you can
manage and query. A schema is a logical grouping of database objects, such as tables
and views. For example, a schema might contain the database objects required for a
specific application. For more information, see Databases, Tables and Views - Overview.

To create a database, a schema, and a table, do the following:

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
CREATEORREPLACESCHEMAcloud_data_db.gcs_dataCOMMENT='Schema for tables loaded from GCS';
```
Copy
3. Place your cursor in the CREATE OR REPLACE TABLE lines, complete the table
definition, add an optional comment, and select Run. For example, the following
table contains six columns:


```
CREATEORREPLACETABLEcloud_data_db.gcs_data.calendar(full_dateDATE,day_nameVARCHAR(10),month_nameVARCHAR(10),day_numberVARCHAR(2),full_yearVARCHAR(4),holidayBOOLEAN)COMMENT='Table to be loaded from GCS calendar data file';
```
Copy
4. To confirm that the table was created successfully, place your cursor in the SELECT line,
then select Run.



Documentation Source:
docs.snowflake.com/en/user-guide/data-load-web-ui.md

Documentation Title:
Loading data using the web interface | Snowflake Documentation

Documentation Content:
Load files from your local machine into an existing table¶

Sign in to Snowsight.

In the navigation menu, select Data» Add Data.

3. On the Add Datapage, select Load data into a Table.

The Load Data into Tabledialog appears.
If you do not have a default warehouse set for your user, select a warehouse.

Select Browse. Add structured or semi-structured data files.

Select a specific database and schema, and then select the table that you want to load data into.

Select Next.

8. Do one of the following:


	Select a file formatfrom the current database.
	
	Select a file type to customize, and then select the relevant settings for your data file.
(Optional) Select what should happen if an error occurs during loading. By default, no data is loaded from the file.

10. Select Load.

Snowsight loads your file and displays the number of rows successfully inserted into the table.
11. Do one of the following:


	To open a worksheet with SQL syntax for querying your table, select Query Data.
	
	To close the dialog, select Done.If your file cannot be loaded, for example, if the columns in the file do not match the columns specified in the table, an error message is displayed. To adjust your settings, select Back.



