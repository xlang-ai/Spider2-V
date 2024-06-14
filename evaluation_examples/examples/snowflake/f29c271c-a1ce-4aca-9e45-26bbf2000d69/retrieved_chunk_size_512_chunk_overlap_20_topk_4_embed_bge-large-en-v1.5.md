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
docs.snowflake.com/en/user-guide/data-load-web-ui.md

Documentation Title:
Loading data using the web interface | Snowflake Documentation

Documentation Content:
Creating a new table when loading a local or staged file. Snowsight uses the INFER\_SCHEMAtable function to automatically detect the file metadata schema, retrieve the column definitions, and generate a new table. This feature doesn’t support XML files.


You can load data from individual files up to 250 MB in size.

Note

To use Snowsight to load data, you must use a role that has the OWNERSHIP privilege on the table that you want to load data into and the USAGE privilege on the database and schema that contain the table. See Table privileges.

If you want to use a named file format, your role must also have the USAGE privilege on that specific file format.



