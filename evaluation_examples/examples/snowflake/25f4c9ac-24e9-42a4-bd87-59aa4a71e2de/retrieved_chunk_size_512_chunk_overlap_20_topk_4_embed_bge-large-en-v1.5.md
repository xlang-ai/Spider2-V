Documentation Source:
docs.snowflake.com/en/sql-reference/sql/rollback.md

Documentation Title:
ROLLBACK | Snowflake Documentation

Documentation Content:
DOCUMENTATION/Getting StartedGuidesDeveloperReferenceReleasesTutorialsStatusOverviewSQL Data Types Reference3. SQL Command ReferenceQuery SyntaxQuery OperatorsGeneral DDLGeneral DMLAll Commands (Alphabetical)AccountsUsers, Roles, & PrivilegesIntegrationsReplication & FailoverSessions- TransactionsBEGINCOMMITDESCRIBE TRANSACTIONROLLBACKSHOW LOCKSSHOW TRANSACTIONS
Virtual Warehouses & Resource MonitorsDatabases, Schemas, & SharesTables, Views, & SequencesFunctions, Procedures, & ScriptingStreams & TasksClasses & InstancesMachine Learning ModelsListingsSecurityData GovernancePrivacyData Loading & UnloadingFile StagingAlertsNative Apps FrameworkStreamlitSnowpark Container Services
Function and Stored Procedure ReferenceClass ReferenceScripting ReferenceGeneral ReferenceAPI Reference
ReferenceSQL Command ReferenceTransactionsROLLBACKROLLBACK¶
=========

Rolls back an open transaction in the current session.

See also:BEGIN, COMMIT, SHOW TRANSACTIONS, DESCRIBE TRANSACTION

Syntax¶
-------


```
ROLLBACK[WORK]
```
CopyParameters¶
-----------

WORKOptional keyword that provides compatibility with other database systems.

Examples¶
---------

Begin a transaction, insert some values into a table, and then complete the transaction by rolling back the changes made in the
transaction:


```
SELECTCOUNT(*)FROMA1;----------+COUNT(*) |----------+0        |----------+BEGINNAMET4;SELECTCURRENT_TRANSACTION();-----------------------+CURRENT_TRANSACTION() |-----------------------+1432071523422         |-----------------------+INSERTINTOA1VALUES(1),(2);-------------------------+number of rows inserted |-------------------------+2                       |-------------------------+ROLLBACK;SELECTCOUNT(*)FROMA1;----------+COUNT(*) |----------+0        |----------+SELECTCURRENT_TRANSACTION();-----------------------+CURRENT_TRANSACTION() |-----------------------+[NULL]                |-----------------------+SELECTLAST_TRANSACTION();--------------------+LAST_TRANSACTION() |--------------------+1432071523422      |--------------------+
```
CopyWas this page helpful?

YesNoVisit SnowflakeJoin the conversationDevelop with SnowflakeShare your feedbackRead the latest on our blogGet your own certificationPrivacy NoticeSite Terms© 2024Snowflake, Inc. All Rights Reserved.On this page

SyntaxParametersExamplesLanguage: **English**EnglishFrançaisDeutsch日本語한국어Português



Documentation Source:
docs.snowflake.com/en/user-guide/ui-snowsight-worksheets-gs.md

Documentation Title:
Getting started with worksheets | Snowflake Documentation

Documentation Content:
Create worksheets from a SQL file¶

To create a SQL worksheet from an existing SQL file, do the following:

Sign in to Snowsight.

Select Projects» Worksheetsto open the list of worksheets.

Select the …more menu » Create Worksheet from SQL File.

Browse to the SQL file to upload.

A new worksheet opens with a title that matches the file name.


You can also add a SQL file to an existing SQL worksheet. Refer to Append a SQL script to an existing worksheet.

Opening worksheets in tabs¶
---------------------------

You can use tabs to refer to multiple active worksheets and explore the databases and schemas in Snowflake while writing SQL
statements or Python code in Snowsight. Your scroll position is preserved in each tab, making comparisons across worksheets easier
to perform. Worksheet tabs are preserved across sessions, so you can pick up your work where you left off.

To open your Snowsight worksheets in tabs, do the following:

Sign in to Snowsight.

Select Projects» Worksheets.

Select an existing worksheet, or select + Worksheetto open a new worksheet. A worksheet opens in a tab.

Select a role to run the worksheet as, and select a warehouse to allocate the compute resources for your query.

In the Worksheetsmenu, select an existing worksheet or select +to open a new worksheet tab. By default, the new worksheet
uses your default role and warehouse.

(Optional) Make changes to the role or warehouse used to run the new worksheet.


After you open a worksheet, you can update the contents,
run SQL statementsor
write Python code, and manage the worksheet.

Was this page helpful?

YesNoVisit SnowflakeJoin the conversationDevelop with SnowflakeShare your feedbackRead the latest on our blogGet your own certificationPrivacy NoticeSite Terms© 2024Snowflake, Inc. All Rights Reserved.On this page

Viewing worksheets in SnowsightImport worksheets from the Classic ConsoleCreate worksheets in SnowsightOpening worksheets in tabsRelated content

Getting started with SnowsightManaging and using worksheets in SnowsightQuerying data using worksheetsVisualizing worksheet dataLanguage: **English**EnglishFrançaisDeutsch日本語한국어Português



Documentation Source:
docs.snowflake.com/en/sql-reference/transactions.md

Documentation Title:
Transactions | Snowflake Documentation

Documentation Content:
```
create procedure sp2_inner(
    USE_BEGIN varchar,
    USE_COMMIT_OR_ROLLBACK varchar)
returns varchar
language javascript
AS
$$
    snowflake.execute (
        {sqlText: "insert into tracker_2 values (21, 'p2_alpha')"}
        );

    if (USE_BEGIN != '')  {
        snowflake.execute (
            {sqlText: USE_BEGIN}
            );
        }
    snowflake.execute (
        {sqlText: "insert into tracker_3 values (22, 'p2_bravo')"}
        );
    if (USE_COMMIT_OR_ROLLBACK != '')  {
        snowflake.execute (
            {sqlText: USE_COMMIT_OR_ROLLBACK}
            );
        }

    snowflake.execute (
        {sqlText: "insert into tracker_2 values (23, 'p2_charlie')"}
        );

    // Dummy value.
    return "";
$$;

```
Copy#### Commit the Middle Level of Three Levels¶

This example contains 3 transactions. This example commits the “middle” level (the transaction enclosed by the
outer-most transaction and enclosing the inner-most transaction). This rolls back the outer-most and
inner-most transactions.


```
begin transaction;
insert into tracker_1 values (00, 'outer_alpha');
call sp1_outer('begin transaction', 'begin transaction', 'rollback', 'commit');
insert into tracker_1 values (09, 'outer_charlie');
rollback;

```
CopyThe result is that only the rows in the middle transaction (12, 21, and 23) are committed. The rows in the outer
transaction and the inner transaction are not committed.



Documentation Source:
docs.snowflake.com/en/sql-reference/transactions.md

Documentation Title:
Transactions | Snowflake Documentation

Documentation Content:
```
-- Should return only 12, 21, 23.
select id, name from tracker_1
union all
select id, name from tracker_2
union all
select id, name from tracker_3
order by id;
+----+------------+
| ID | NAME       |
|----+------------|
| 12 | p1_bravo   |
| 21 | p2_alpha   |
| 23 | p2_charlie |
+----+------------+

```
Copy#### Roll Back the Middle Level of Three Levels¶

This example contains 3 transactions. This example rolls back the “middle” level (the transaction enclosed by the
outer-most transaction and enclosing the inner-most transaction). This commits the outer-most and inner-most
transactions.


```
begin transaction;
insert into tracker_1 values (00, 'outer_alpha');
call sp1_outer('begin transaction', 'begin transaction', 'commit', 'rollback');
insert into tracker_1 values (09, 'outer_charlie');
commit;

```
CopyThe result is that all rows except the rows in the middle transaction (12, 21, and 23) are committed.


```
select id, name from tracker_1
union all
select id, name from tracker_2
union all
select id, name from tracker_3
order by id;
+----+---------------+
| ID | NAME          |
|----+---------------|
|  0 | outer_alpha   |
|  9 | outer_charlie |
| 11 | p1_alpha      |
| 13 | p1_charlie    |
| 22 | p2_bravo      |
+----+---------------+

```
Copy### Using Error Handling with Transactions in Stored Procedures¶

The following code shows simple error handling for a transaction in a stored procedure. If the parameter value ‘fail’
is passed, the stored procedure tries to delete from two tables that exist and one table that doesn’t exist, and the
stored procedure catches the error and returns an error message. If the parameter value ‘fail’ is not passed, the
procedure tries to delete from two tables that do exist, and succeeds.

Create the tables and stored procedure:



