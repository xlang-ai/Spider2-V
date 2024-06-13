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
What You Will Learn¶

In this tutorial, you will learn how to:

* Create an event table to store log and trace data.

Snowflake collects log and trace data in the table’s predefined structure.
* Emit log messages and trace data from a user-defined function (UDF).

You can use an API designed for your handler language to emit log messages and trace data from handler code.
* View the collected log and trace data by querying the event table.

You can query the table with a SELECT statement to analyze the collected data.



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
docs.snowflake.com/en/developer-guide/logging-tracing/tracing-python.md

Documentation Title:
Emitting trace events in Python | Snowflake Documentation

Documentation Content:
DOCUMENTATION/Getting StartedGuidesDeveloperReferenceReleasesTutorialsStatusOverviewSnowpark LibrarySnowpark APISnowpark MLSnowpark Code Execution EnvironmentsSnowpark Container Services7. Functions and ProceduresFunction or Procedure?GuidelinesStored ProceduresUser-Defined Functions- Logging and TracingGet Started TutorialEvent Table Set UpEvent Table OperationsEvent Table ColumnsUnhandled Exception MessagesTelemetry Package DependenciesPackagingLimitationsTroubleshootingCostsLoggingIntroductionLog LevelJavaJavaScriptPythonScalaSnowflake ScriptingAccessing Message DataTracingIntroductionTrace EventsTrace LevelJavaJavaScriptPythonScalaSnowflake ScriptingAccessing Trace Data
External Network AccessPackaging Handler Code
Snowflake APIsSnowflake Python APISQL REST APIAppsStreamlit in SnowflakeSnowflake Native App FrameworkExternal System IntegrationExternal FunctionsKafka and Spark ConnectorsSnowflake ScriptingSnowflake Scripting Developer GuideToolsSnowflake CLIGitDriversOverviewReferenceAPI Reference
DeveloperFunctions and ProceduresLogging and TracingPythonEmitting trace events in Python¶
================================

You can use the Snowflake telemetrypackage to emit trace events from a function or procedure handler written in Python.
The package is available from the Anaconda Snowflake channel.

You can access stored trace event data by executing a SELECT command on the event table. For more information, refer to
Accessing Trace Data.

Note

For guidelines to keep in mind when adding trace events, refer to General Guidelines for Adding Trace Events.

For general information about setting up logging and retrieving messages in Snowflake, refer to
Logging Messages from Functions and Procedures.

Before logging from code, you must:

* Set up an event table to collect messages logged from handler code.

For more information, refer to Setting up an Event Table.
* Be sure you have the trace level set so that the data you want are stored in the event table.

For more information, refer to Setting trace level.

Note

For guidelines to keep in mind when adding trace events, refer to General Guidelines for Adding Trace Events.

Adding support for the telemetry package¶
-----------------------------------------

To use telemetry package, you must make the open source
Snowflake telemetry package, which is included with Snowflake, available
to your handler code. The package is available from the Anaconda Snowflake channel.

**For a procedure or function.



