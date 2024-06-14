Documentation Source:
docs.snowflake.com/en/developer-guide/logging-tracing/tutorials/logging-tracing-getting-started.md

Documentation Title:
Tutorial: Get Started with Logging and Tracing | Snowflake Documentation

Documentation Content:
```
ALTERACCOUNTSETEVENT_TABLE=tutorial_log_trace_db.public.tutorial_event_table;
```
CopyThis statement sets the new event table as the table that Snowflake should use for storing log messages and trace data from handlers
in the current account. You can have only one active event table for an account.

In this section, you created an event table. In the next section, you’ll start emitting log messages that Snowflake stores in the table.

Emit Log Messages¶
------------------

In this section, you’ll create a user-defined function (UDF) with Python handler code that emits log messages. As your code emits log
messages, Snowflake collects the message data and stores it in the event table you created.

Snowflake supports APIs to log messages from each supported handler language. For handlers you write in Python, you can use the
loggingmodule in Python’s standard library.

To create a UDF that emits log messages:

1. Paste and run the following statement to set the log level to INFO.


```
ALTERSESSIONSETLOG_LEVEL=INFO;
```
CopyThis specifies the severity of log messages that Snowflake should capture as the UDF runs. In this case, the level permits all
messages ranging from informational (INFO) to the most severe (FATAL).
2. Paste and run the following statement to create a user-defined function.


```
CREATEORREPLACEFUNCTIONlog_trace_data()RETURNSVARCHARLANGUAGEPYTHONRUNTIME_VERSION=3.8HANDLER='run'AS$$importlogginglogger=logging.getLogger("tutorial_logger")defrun():logger.info("Logging from Python function.")return"SUCCESS"$$;
```
CopyHighlighted lines in the code do the following:


	Import the Python loggingmodule so that the handler code can use it.
	
	Create a logger, which exposes the interface your code will use to log messages.
	
	Log a message at the INFOlevel.
3. Paste and run the following statement to execute the function you just created.


```
SELECTlog_trace_data();
```
CopyThis produces the following output. In addition, as the function executed, it emitted a log message that Snowflake collected in the
event table.



Documentation Source:
docs.snowflake.com/en/developer-guide/logging-tracing/tutorials/logging-tracing-getting-started.md

Documentation Title:
Tutorial: Get Started with Logging and Tracing | Snowflake Documentation

Documentation Content:
```
CREATEORREPLACEWAREHOUSEtutorial_log_trace_whWAREHOUSE_TYPE=STANDARDWAREHOUSE_SIZE=XSMALL;
```
Copy

In this section, you put in place the pieces you need for the tutorial. In the next section, you’ll create an event table for storing
log and trace data.

Create an Event Table¶
----------------------

In this section, you’ll create an event table. As your handler code emits log messages and trace data, Snowflake saves the emitted data in
event table rows. You can query the event table to analyze the data.

You must create an event table to collect log and trace data. An event table always uses the
predefined structuredefined by Snowflake.

Important

To complete this section, you’ll need to be able to use the ACCOUNTADMIN role, which is required when altering an account so that the new event
table is the account’s active event table.

To create the event table and make it the active event table for the account:

1. Paste and run the following statement to create an event table.


```
CREATEORREPLACEEVENT TABLEtutorial_event_table;
```
CopyThis table is where Snowflake stores log and trace data.
2. Paste and run the following statement to alter the account so that the event table you created is the active one for the account.



Documentation Source:
docs.snowflake.com/en/developer-guide/logging-tracing/event-table-setting-up.md

Documentation Title:
Setting up an Event Table | Snowflake Documentation

Documentation Content:
Create an Event Table¶
----------------------

To create an event table for storing log and trace event data, execute the CREATE EVENT TABLEcommand and specify
a name for the event table. You will use the event table name later to enable the table to capture logs produced by stored procedures, UDFs,
and UDTFs in your account.

Note that when you create an event table, you do not specify the columns in the table. An event table already has
a set of predefined columns, as described in Event table columns.

Note

Replication of event tables is not currently supported. Refresh operations for a primary database that contains an event table fail.

You should create the event table in a database that is not enabled for replication. Alternatively, you can enable the
2024\_03 behavior change bundlein your account. After you enable the bundle,
any event tables that are contained in primary databases are skipped during replication and the refresh operation succeeds.

For example, to create an event table with the name my\_events, execute the following statement:


```
CREATEEVENT TABLEmy_database.my_schema.my_events;
```
CopyAssociate the Event Table with the Account¶
-------------------------------------------

To enable storage of log and trace event data from functions and procedures for an account, you must specify that the event table you
created is the active event table for the account.

To specify the active event table for your account, execute the ALTER ACCOUNTcommand, and set the
EVENT\_TABLEparameter to the name of your event table.

Note

In order to execute this command, you must use the ACCOUNTADMIN role.

In addition, you must have bothof the following privileges:

OWNERSHIP privilege for the account.

OWNERSHIP or INSERT privileges for the event table.


See the documentation on the ALTER ACCOUNT commandfor more information on the
privileges needed to execute ALTER ACCOUNT.

For example, to set up the event table named my\_eventsin the schema my\_schemain the database my\_databaseas
the active event table for your account, execute the following statement:



Documentation Source:
docs.snowflake.com/en/developer-guide/logging-tracing/tutorials/logging-tracing-getting-started.md

Documentation Title:
Tutorial: Get Started with Logging and Tracing | Snowflake Documentation

Documentation Content:
What You Will Learn¶

In this tutorial, you will learn how to:

* Create an event table to store log and trace data.

Snowflake collects log and trace data in the table’s predefined structure.
* Emit log messages and trace data from a user-defined function (UDF).

You can use an API designed for your handler language to emit log messages and trace data from handler code.
* View the collected log and trace data by querying the event table.

You can query the table with a SELECT statement to analyze the collected data.



