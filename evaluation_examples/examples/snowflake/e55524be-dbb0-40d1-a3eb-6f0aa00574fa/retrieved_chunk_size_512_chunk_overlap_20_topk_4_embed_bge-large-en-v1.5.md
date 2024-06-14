Documentation Source:
docs.snowflake.com/en/sql-reference/sql/delete.md

Documentation Title:
DELETE | Snowflake Documentation

Documentation Content:
```
SELECT*FROMleased_bicyclesORDERBYbicycle_ID;+------------+-------------+| BICYCLE_ID | CUSTOMER_ID ||------------+-------------||        101 |        1111 ||        103 |        3333 |+------------+-------------+
```
CopyNow suppose that another bicycle(s) is returned:


```
INSERTINTOreturned_bicycles(bicycle_ID)VALUES(103);
```
CopyThe following query shows a USINGclause that contains a subquery (rather than a table) to specify which bicycle\_IDs to remove from
the leased\_bicycles table:


```
BEGINWORK;DELETEFROMleased_bicyclesUSING(SELECTbicycle_IDASbicycle_IDFROMreturned_bicycles)ASreturnedWHEREleased_bicycles.bicycle_ID=returned.bicycle_ID;TRUNCATETABLEreturned_bicycles;COMMITWORK;
```
CopyShow the data after the delete:


```
SELECT*FROMleased_bicyclesORDERBYbicycle_ID;+------------+-------------+| BICYCLE_ID | CUSTOMER_ID ||------------+-------------||        101 |        1111 |+------------+-------------+
```
CopyWas this page helpful?

YesNoVisit SnowflakeJoin the conversationDevelop with SnowflakeShare your feedbackRead the latest on our blogGet your own certificationPrivacy NoticeSite Terms© 2024Snowflake, Inc. All Rights Reserved.On this page

SyntaxRequired parametersOptional parametersUsage notesExamplesLanguage: **English**EnglishFrançaisDeutsch日本語한국어Português



Documentation Source:
docs.snowflake.com/en/user-guide/ui-worksheet.md

Documentation Title:
Using Worksheets for Queries / DML / DDL | Snowflake Documentation

Documentation Content:
Viewing Query Information and Details¶

When a query is executed, a status bar displays the current total query duration. Hover over the bar to see a breakdown of the duration.

!Hover over to view query metrics.

Click the Query IDlink to explore query details. A popover provides links to copy the query ID to your operating system’s temporary memory or to navigate to the query history.

!Click to copy the query ID.

Click to navigate to the query history.

Formatting Queries Using Keyboard Shortcuts¶
--------------------------------------------

The SQL editor in a worksheet supports the following keyboard keys and key combinations for formatting your queries and other SQL statements:

Tab Stops:To insert a tab stop in a line (in 4 character intervals), use the **[TAB]**key:

If the cursor is at the beginning of the line, 4 blank spaces are inserted.

If the cursor is in the line, enough blank spaces are added to reach the next tab stop.

Indents/Outdents:To indent/outdent a line (or multiple lines) 2 blank spaces, place the cursor anywhere in the line (or highlight the desired lines), hold down the **[CMD]**(Mac) or **[CTRL]**(Windows) key and type one or more:

Right square brackets, ], to indent the line(s) the number of brackets typed.

Left square brackets, [, to outdent the line(s) the number of brackets typed.


If a line is indented, all new lines after the indented line are automatically indented the same number of blank spaces.

Comments:To comment out a line (or multiple lines), place the cursor anywhere in the line (or highlight the desired lines), hold down the **[CMD]**(Mac) or **[CTRL]**(Windows) key and type a
forward slash, /.

Text Highlighting:To enable or disable text highlighting in all open worksheets, place the cursor anywhere in a worksheet, hold down the **[SHIFT]+[CMD]**(Mac) or **[SHIFT]+[CTRL]**(Windows)
keys and type the letter K.

Add Multiple Cursors:To add multiple cursors in the same worksheet, hold down the **[CMD]**(Mac) or **[CTRL]**(Windows) key and click in each new location using the mouse left button or
the touchpad.



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
docs.snowflake.com/en/sql-reference/sql/delete.md

Documentation Title:
DELETE | Snowflake Documentation

Documentation Content:
Create tables:


```
CREATETABLEleased_bicycles(bicycle_idINTEGER,customer_idINTEGER);CREATETABLEreturned_bicycles(bicycle_idINTEGER);
```
CopyLoad data:


```
INSERTINTOleased_bicycles(bicycle_ID,customer_ID)VALUES(101,1111),(102,2222),(103,3333),(104,4444),(105,5555);INSERTINTOreturned_bicycles(bicycle_ID)VALUES(102),(104);
```
CopyThis example shows how to use the WHEREclause to delete a specified row(s). This example deletes by bicycle\_ID:


```
DELETEFROMleased_bicyclesWHEREbicycle_ID=105;+------------------------+| number of rows deleted ||------------------------||                      1 |+------------------------+
```
CopyShow the data after the delete:


```
SELECT*FROMleased_bicyclesORDERBYbicycle_ID;+------------+-------------+| BICYCLE_ID | CUSTOMER_ID ||------------+-------------||        101 |        1111 ||        102 |        2222 ||        103 |        3333 ||        104 |        4444 |+------------+-------------+
```
CopyThis example shows how to use the USINGclause to specify rows to be deleted. This USINGclause specifies the returned\_bicycles
table, which lists the IDs of the bicycles to be deleted from the leased\_bicycles table. The WHEREclause joins the leased\_bicycles
table to the returned\_bicycles table, and the rows in leased\_bicycles that have the same bicycle\_ID as the corresponding rows in
returned\_bicycles are deleted.


```
BEGINWORK;DELETEFROMleased_bicyclesUSINGreturned_bicyclesWHEREleased_bicycles.bicycle_ID=returned_bicycles.bicycle_ID;TRUNCATETABLEreturned_bicycles;COMMITWORK;
```
Copy(To avoid trying to remove the same rows again in the future when it might be unnecessary or inappropriate, the returned\_bicycles table is
truncated as part of the same transaction.)

Show the data after the delete:



