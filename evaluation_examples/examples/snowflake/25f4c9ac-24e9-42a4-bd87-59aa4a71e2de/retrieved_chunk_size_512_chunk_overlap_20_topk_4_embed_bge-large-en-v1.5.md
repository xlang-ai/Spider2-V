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
docs.snowflake.com/en/user-guide/ui-worksheet.md

Documentation Title:
Using Worksheets for Queries / DML / DDL | Snowflake Documentation

Documentation Content:
Worksheets are designed to meet all your business and workflow needs, including:

Running ad hoc queries and performing other SQL operations.

Opening multiple, concurrent worksheets, each with its own separate session, allowing you to run queries in different worksheets with different contexts without any degradation in UI performance.

Saving a worksheet for later use.

* Opening a worksheet from your library of saved worksheets.

Note


	Saved worksheets are not accessible outside of the Classic Console.
	
	Saved worksheets cannot currently be shared with other users.
Loading SQL script files from your workstation or network into a worksheet. After you’ve loaded a script file, you can optionally edit and save it to your library of saved worksheets.

* Logging out without losing your work. Snowflake retains the static contents of each worksheet, so you can log in again later and resume working where you left off. Snowflake displays the worksheets
that were open when you logged out.

Note that resized/collapsed panes, width changes to the result/data preview columns, and even the cursor position in the SQL editor, are persisted:


	When switching between open worksheets.
	
	When closing and reopening the same worksheet.
	
	Between user sessions.
* Specifying a different role for each worksheet and switching roles without losing your work. You can execute specific statements in a worksheet, then switch roles before continuing your work
in the same worksheet.

Note

Your current interface role determines the default role for worksheets that you open, but the worksheets are not tied to the interface role. Each worksheet has its own role that can be set
independently.
Logging into Snowflake in another browser or tab. Any worksheet changes you made in one Snowflake instance persist to the other instance after a minute or two. You can continue working in the
other browser (or tab) without re-entering your work.

Refreshing your browser, if necessary. If you’re in the middle of running queries, they will resume running when the refresh is completed. Note that if you log out of Snowflake, any active
queries stop running.



Documentation Source:
docs.snowflake.com/en/sql-reference/transactions.md

Documentation Title:
Transactions | Snowflake Documentation

Documentation Content:
```
create procedure log_message(MESSAGE VARCHAR)
returns varchar
language javascript
AS
$$
    // This is an independent transaction. Anything inserted as part of this
    // transaction is committed or rolled back based on this transaction.
    snowflake.execute (
        {sqlText: "begin transaction"}
        );
    snowflake.execute (
        {sqlText: "insert into log_table values ('" + MESSAGE + "')"}
        );
    snowflake.execute (
        {sqlText: "commit"}
        );

    // Dummy value.
    return "";
$$;

create procedure update_data()
returns varchar
language javascript
AS
$$
    snowflake.execute (
        {sqlText: "begin transaction"}
        );
    snowflake.execute (
        {sqlText: "insert into data_table (id) values (17)"}
        );
    snowflake.execute (
        {sqlText: "call log_message('You should see this saved.')"}
        );
    snowflake.execute (
        {sqlText: "rollback"}
        );

    // Dummy value.
    return "";
$$;

```
CopyCall the stored procedure:


```
begintransaction;callupdate_data();rollback;
```
CopyThe data table is empty because the transaction was rolled back:


```
select*fromdata_table;+----+| ID ||----|+----+
```
CopyHowever, the logging table is not empty; the insert into the logging table was done in a separate transaction from
the insert into data\_table.


```
select*fromlog_table;+----------------------------+| MESSAGE                    ||----------------------------|| You should see this saved. |+----------------------------+
```
Copy### Examples of Scoped Transactions and Stored Procedures¶

The next few examples use the tables and stored procedures shown below. By passing appropriate parameters, the caller
can control where `BEGINTRANSACTION`, COMMIT, and ROLLBACKstatements are executed inside the stored procedures.

Create the tables:


```
create table tracker_1 (id integer, name varchar);
create table tracker_2 (id integer, name varchar);
create table tracker_3 (id integer, name varchar);

```
CopyThis procedure is the enclosing stored procedure, and depending upon the parameters passed to it, can create an
enclosing transaction.



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



