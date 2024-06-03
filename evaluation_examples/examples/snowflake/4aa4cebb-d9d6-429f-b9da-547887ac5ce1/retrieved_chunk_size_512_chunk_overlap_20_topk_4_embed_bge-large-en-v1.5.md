Documentation Source:
docs.snowflake.com/en/user-guide/data-load-web-ui.md

Documentation Title:
Loading data using the web interface | Snowflake Documentation

Documentation Content:
Create a table when loading a file¶

You can create a new table when loading a file by taking the following steps.

Note

This feature supports delimited files, JSON, Parquet, Avro, and ORC files. It doesn’t support XML files.

To perform the tasks below, you must have the privileges for creating table.

Sign in to Snowsight.

2. In the navigation menu, select Create» Table» From File.

The Load Data into Tabledialog appears.
In the Load Data into Tabledialog, select or create a database and schema where you want the table to be created. Then select Browseto add a file, or Drag and drop to upload files, or Add from stage.

4. Enter a name for the new table and then select Next.

Snowsight detects the metadata schema for the file and returns the file format and column definitions identified by the INFER\_SCHEMAfunction.
Review the inferred file format, data type, column name, and a sample of column data. Ensure all information is accurate and make updates if needed.

6. Select Load.

Snowsight loads the file and creates a new table for the file.
Loading data using Classic Console¶
-----------------------------------

The Classic Console provides a wizard for loading limited amounts of data into a table from a small set of files.
The wizard performs the same PUT and COPY operations that you would using SQL, but combines the two phases (staging files and loading data)
into a single operation and deleting all staged files after the load completes.

You can load data from files on your local machine or files already staged in an existing cloud storage location on Snowflake, Amazon S3,
Google Cloud Storage, or Microsoft Azure.



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



Documentation Source:
docs.snowflake.com/en/user-guide/data-load-web-ui.md

Documentation Title:
Loading data using the web interface | Snowflake Documentation

Documentation Content:
Load a file from a stage into an existing table¶

Before loading files from a stage into a table, you need to create a stage and upload files onto the stage. For instructions, see Staging files using Snowsight.

Sign in to Snowsight.

In the object explorer, select the stage that you want to load files from.

In the list of the files on the stage, select the file that you want to load into the table.

In the ellipsis dropdown menu of the selected file, select Load into table.

In the Load Data into Tabledialog, select a database, schema, and a table where you want to load the file.

Select Next.

7. Do one of the following:


	Select a file formatfrom the current database.
	
	Select a file type to customize, and then select the relevant settings for your data file.
(Optional) Select what should happen if an error occurs during loading. By default, no data is loaded from the file.

9. Select Load.

Snowsight loads your file from the stage to the table.

Alternatively, you can load a staged file into a table by copying the path of the staged file.

Follow steps 1-3 in the previous procedure.

In the ellipsis dropdown menu of the selected file on the stage, select Copy path.

In the navigation menu, select Data» Add Data.

On the Add Datapage, select Load files into a Stage.

In the object explorer, select the table that you want to load data into.

Select Load Data.

In the Load Data into Tabledialog that appears, select Add from Stage.

8. Paste the path that you copied into the path field, and then select Add.

The staged file name appears.
Select Next.

10. Do one of the following:


	Select a file formatfrom the current database.
	
	Select a file type to customize, and then select the relevant settings for your data file.
(Optional) Select what should happen if an error occurs during loading. By default, no data is loaded from the file.

12. Select Load.

Snowsight loads your file and displays the number of rows successfully inserted into the table.



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



