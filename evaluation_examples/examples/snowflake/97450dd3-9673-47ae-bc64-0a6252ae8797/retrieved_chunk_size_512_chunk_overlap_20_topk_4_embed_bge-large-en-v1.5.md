Documentation Source:
docs.snowflake.com/en/user-guide/spark-connector-qubole.md

Documentation Title:
Configuring Snowflake for Spark in Qubole | Snowflake Documentation

Documentation Content:
Repeat these steps for each Snowflake database that you want to add as a data store. Or you can edit the data store to change the Snowflake database or any other properties for the data store (e.g.
change the virtual warehouse used for queries).

Note

After adding a Snowflake data store, restart the Spark cluster (if you are using an already-running Spark cluster). Restarting the Spark cluster installs the .jarfiles for the Snowflake
Connector for Spark and the Snowflake JDBC Driver.

Verifying the Snowflake Data Store in Qubole¶
---------------------------------------------

To verify that the Snowflake data store was created and has been activated, click on the dropdown list in the upper-left of the Explorepage. A green dot indicates that the data store has
been activated.

You should also verify that the table explorer widget in the left pane of the Explorepage displays all of the tables in the Snowflake database specified in the data store.

Query Pushdown in Qubole¶
-------------------------

Spark queries benefit from Snowflake’s automatic query pushdown optimization, which improves performance. By default, Snowflake query pushdown is enabled in Qubole.

For more details about query pushdown, see Pushing Spark Query Processing to Snowflake(Snowflake Blog).

Was this page helpful?

YesNoVisit SnowflakeJoin the conversationDevelop with SnowflakeShare your feedbackRead the latest on our blogGet your own certificationPrivacy NoticeSite Terms© 2024Snowflake, Inc. All Rights Reserved.On this page

PrerequisitesPreparing an External Location for Long-running QueriesAdding Snowflake as a Data Store in the QDS UIVerifying the Snowflake Data Store in QuboleQuery Pushdown in QuboleRelated info

Qubole Quickstart Guide(Qubole Documentation)

Qubole-Snowflake Integration Guide(Qubole Documentation)

Language: **English**EnglishFrançaisDeutsch日本語한국어Português



Documentation Source:
docs.snowflake.com/en/user-guide/spark-connector-use.md

Documentation Title:
Using the Spark Connector | Snowflake Documentation

Documentation Content:
```
importjava.sql.Connection;importjava.sql.DriverManager;importjava.sql.ResultSet;importjava.sql.ResultSetMetaData;importjava.sql.SQLException;importjava.sql.Statement;importjava.util.Properties;publicclassSnowflakeJDBCExample{publicstaticvoidmain(String[]args)throwsException{StringjdbcUrl="jdbc:snowflake://myorganization-myaccount.snowflakecomputing.com/";Propertiesproperties=newProperties();properties.put("user","peter");properties.put("password","test");properties.put("account","myorganization-myaccount");properties.put("warehouse","mywh");properties.put("db","mydb");properties.put("schema","public");// get connectionSystem.out.println("Create JDBC connection");Connectionconnection=DriverManager.getConnection(jdbcUrl,properties);System.out.println("Done creating JDBC connection\n");// create statementSystem.out.println("Create JDBC statement");Statementstatement=connection.createStatement();System.out.println("Done creating JDBC statement\n");// create a tableSystem.out.println("Create my_variant_table table");statement.executeUpdate("create or replace table my_variant_table(json VARIANT)");statement.close();System.out.println("Done creating demo table\n");connection.close();System.out.println("Close connection\n");}}
```
Copy
2. Instead of using SaveMode.Overwrite, use SaveMode.Append, to reuse the existing table. When the string value representing JSON is loaded into Snowflake, because the target column is of type VARIANT, it is parsed as JSON. For example:


```
df.write.format(SNOWFLAKE_SOURCE_NAME).options(sfOptions).option("dbtable","my_variant_table").mode(SaveMode.Append).save()
```
Copy



Documentation Source:
docs.snowflake.com/en/developer-guide/snowpark/reference/scala/com/snowflake/snowpark/index.md

Documentation Title:

   Snowpark 1.12.1  - com.snowflake.snowpark
  

Documentation Content:
package
 snowpark

** ** Ordering
 Alphabetic
 Visibility
 Public
 All
 ### Type Members

1. ** class
 AsyncJob
 extends
 AnyRef
 Provides a way to track an asynchronous query in Snowflake.
 

Provides a way to track an asynchronous query in Snowflake.
 

You can use this object to check the status of an asynchronous query and retrieve the results.
 

To check the status of an asynchronous query that you submitted earlier,
call
 Session.createAsyncJob, and pass in the query ID. This returns an
 `AsyncJob` object
that you can use to check the status of the query and retrieve the query results.
 

Example 1: Create an AsyncJob by specifying a valid
 `` , check whether
the query is running or not, and get the result rows.
 


```
valasyncJob = session.createAsyncJob()
println(s"Is query ${asyncJob.getQueryId()} running? ${asyncJob.isRunning()}")
valrows = asyncJob.getRows()
```
Example 2: Create an AsyncJob by specifying a valid
 `` and cancel the query if
it is still running.
 


```
session.createAsyncJob().cancel()
```
Since
 0.11.0
2. ** class
 CaseExpr
 extends
 ColumnRepresents a
 CASEexpression.
 

Represents a
 CASEexpression.
 

To construct this object for a CASE expression, call the
 functions.when. specifying a condition and the
corresponding result for that condition. Then, call the
 whenand
 otherwisemethods to
specify additional conditions and results.
 

For example:



Documentation Source:
docs.snowflake.com/en/release-notes/clients-drivers/jdbc-2022.md

Documentation Title:
JDBC Driver release notes for 2022 | Snowflake Documentation

Documentation Content:
New features and updates¶

* Upgraded the following libraries:


	arrow from version 8.0.0 to 9.0.0
	
	jacksondatabind from version 2.13.2.2 to 2.13.4.2
	
	google-cloud-storage from version 2.5.0 to 2.6.2
The Statement.getMoreResults()function now returns TRUE when more statements are available to iterate
through in a multi-statement query.

The Statement.getupdateCount()function now returns 0 instead of -1 for non-DML queries.

Version 3.13.23 (September 30, 2022)¶
-------------------------------------



