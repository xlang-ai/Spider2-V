Documentation Source:
docs.snowflake.com/en/user-guide/ui-snowsight-worksheets.md

Documentation Title:
Managing and using worksheets in Snowsight | Snowflake Documentation

Documentation Content:
Download recovered worksheets owned by a dropped user¶

To recover worksheets owned by a dropped user, download a .tar.gzarchive file of up to 500 worksheets owned by that user.

Note

You must be granted the ACCOUNTADMIN role to recover worksheets of dropped users.

Sign in to Snowsight.

Select Projects» Worksheets.

Select !» Recover Worksheets from Dropped User.

4. In the dialog box, enter the username of a dropped user in your account.

Important

The case and spelling of the username must exactly match the username as it was stored in Snowflake.
5. Select Recover.

Your web browser downloads a .tarfile containing up to 500 worksheets. If the dropped user has more than 500 worksheets,
only the 500 most recently modified worksheets are downloaded.

After downloading worksheets owned by a dropped user, add the recovered worksheets to Snowsight by creating worksheets from
the SQL files.

You must expand the downloaded .tarfile into a folder of .sqlfiles before you can add recovered worksheets to
Snowsight. You can only add one worksheet at a time to Snowsight, and the user who adds the recovered worksheets to
Snowsight becomes the new owner of the worksheets.

See Create worksheets from a SQL filefor details.



Documentation Source:
docs.snowflake.com/en/user-guide/ui-snowsight-worksheets.md

Documentation Title:
Managing and using worksheets in Snowsight | Snowflake Documentation

Documentation Content:
Considerations for recovering worksheets owned by dropped users¶

Considerations when recovering worksheets:

Only the title and contents of the most recently executed version of a worksheet are recovered. Worksheet version history,
sharing recipients and permissions, query results, and worksheet metadata are not recovered.

A maximum of 500 worksheets are recovered. For dropped users with more than 500 worksheets, only the 500 most recently modified worksheets
are recovered.

Only worksheets in Snowsight are recovered. Worksheets in Classic Console owned by dropped users cannot be recovered with
this method.

If multiple dropped users have the same username, worksheets owned by all dropped users with that username are recovered.


If the worksheet recovery fails for unexpected reasons, contact Snowflake Support.

Internal Snowflake objects for worksheets¶
------------------------------------------

Snowflake creates the following internal objects to support using worksheets in Snowsight:



|Object Type

Name


|  |
|Security integration

WORKSHEETS


|  |
|Blobs

WORKSHEETS\_APP


|Database

WORKSHEETS\_APP


|User

WORKSHEETS\_APP\_USER


|Roles

APPADMIN, WORKSHEETS\_APP\_RL



Documentation Source:
docs.snowflake.com/en/user-guide/ui-snowsight-worksheets.md

Documentation Title:
Managing and using worksheets in Snowsight | Snowflake Documentation

Documentation Content:
Stored results for past worksheet versions¶

Note

Available to most accounts. Accounts in U.S. government regions, accounts using Virtual Private Snowflake (VPS), and accounts
that use Private Connectivity to access Snowflake continue to see query results limited to 10,000 rows.

All results for queries executed in worksheets are available for up to 24 hours. After 24 hours, you must run your query again to view
results.

To support contextual statistics and sharing worksheet results, the query results are cached for up to 90 days, or 25 worksheet versions,
whichever is greater. This cache is included in the data storage usage for your account.

Recover worksheets owned by a dropped user¶
-------------------------------------------

If you drop a user, you can recover up to 500 of the worksheets owned by that user. To recover the worksheets, do the following:

Download recovered worksheetsowned by a dropped user.

Create worksheets from a SQL fileto add the recovered worksheets back to Snowflake.


If you want to change ownership or retain access to worksheets before dropping a user, ask that user to share the worksheets.
See Sharing worksheets and folders.



Documentation Source:
docs.snowflake.com/en/sql-reference/sql-all.md

Documentation Title:
All Commands (Alphabetical) | Snowflake Documentation

Documentation Content:
|SHOW SHARES IN REPLICATION GROUPLists shares in a replication group.


|SHOW SNAPSHOTSLists the snapshotsfor which you have access privileges.


|SHOW STAGESLists all the stages for which you have access privileges.


|SHOW STREAMLITSLists the Streamlit objects for which you have access privileges.


|SHOW STREAMSLists the streams for which you have access privileges.


|SHOW TABLESLists the tables for which you have access privileges, including dropped tables that are still within the Time Travel retention period and, therefore, can be undropped.


|SHOW TAGSLists the tag information.


|SHOW TASKSLists the tasks for which you have access privileges.


|SHOW TRANSACTIONSList all running transactions.


|SHOW USER FUNCTIONSLists all user-defined functions (UDFs) for which you have access privileges.


|SHOW USERSLists all users in the system.


|SHOW VARIABLESLists all variablesdefined in the current session.


|SHOW VERSIONSLists the versions defined in the specified application package.


|SHOW VERSIONS IN MODELLists the versions in a machine learning model.


|SHOW VIEWSLists the views, including secure views, for which you have access privileges.


|SHOW WAREHOUSESLists all the warehouses in your account for which you have access privileges.


**T**|TRUNCATE MATERIALIZED VIEWRemoves all rows from a materialized view, but leaves the view intact (including all privileges and constraints on the materialized view).


|TRUNCATE TABLERemoves all rows from a table but leaves the table intact (including all privileges and constraints on the table).


**U**|UNDROP Restores the specified object to the system.


|UNDROP ACCOUNTRestores a dropped accountthat has not yet been permanently deleted (a dropped account that is within its grace period).


|UNDROP DATABASERestores the most recent version of a dropped database.


|UNDROP DYNAMIC TABLERestores the most recent version of a dropped dynamic table.


|UNDROP EXTERNAL VOLUMERestores the most recent version of a dropped external volume.


|UNDROP ICEBERG TABLERestores the most recent version of a dropped Iceberg table.


|UNDROP SCHEMARestore the most recent version of a dropped schema.



