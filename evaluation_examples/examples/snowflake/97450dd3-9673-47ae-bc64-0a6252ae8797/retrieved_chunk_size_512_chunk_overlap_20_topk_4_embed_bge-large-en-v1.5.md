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
docs.snowflake.com/en/developer-guide/jdbc/jdbc-using.md

Documentation Title:
Using the JDBC Driver | Snowflake Documentation

Documentation Content:
```
Stringsql_command="";ResultSetresultSet;StringqueryID="";System.out.println("Create JDBC statement.");Statementstatement=connection.createStatement();sql_command="SELECT PI() * 2";System.out.println("Simple SELECT query: "+sql_command);resultSet=statement.unwrap(SnowflakeStatement.class).executeAsyncQuery(sql_command);queryID=resultSet.unwrap(SnowflakeResultSet.class).getQueryID();System.out.println("INFO: Closing statement.");statement.close();System.out.println("INFO: Closing connection.");connection.close();System.out.println("INFO: Re-opening connection.");connection=create_connection(args);use_warehouse_db_and_schema(connection);resultSet=connection.unwrap(SnowflakeConnection.class).createResultSet(queryID);// Assume that the query isn't done yet.QueryStatusqueryStatus=QueryStatus.RUNNING;while(queryStatus==QueryStatus.RUNNING){Thread.sleep(2000);// 2000 milliseconds.queryStatus=resultSet.unwrap(SnowflakeResultSet.class).getStatus();}if(queryStatus==QueryStatus.FAILED_WITH_ERROR){System.out.format("ERROR %d: %s%n",queryStatus.getErrorMessage(),queryStatus.getErrorCode());}elseif(queryStatus!=QueryStatus.SUCCESS){System.out.println("ERROR: unexpected QueryStatus: "+queryStatus);}else{booleanresult_exists=resultSet.next();if(!result_exists){System.out.println("ERROR: No rows returned.");}else{floatpi_result=resultSet.getFloat(1);System.out.println("pi = "+pi_result);}}
```
Copy### Upload data files directly from a stream to an internal stage¶

You can upload data files using the PUT command. However, sometimes it makes sense to transfer data directly from a
stream to an internal (i.e. Snowflake) stage as a file. (The stagecan be any internal stage type: table stage, user stage, or named stage. The JDBC driver does not support uploading to an external
stage.) Here is the method exposed in the SnowflakeConnectionclass:



Documentation Source:
docs.snowflake.com/en/user-guide/snowflake-client-repository.md

Documentation Title:
Downloading Snowflake Clients, Connectors, Drivers, and Libraries | Snowflake Documentation

Documentation Content:
|Client / Connector / Driver / Library

Download Page


|  |
|SnowSQL (CLI client)SnowSQL Download
|  |
|ODBC DriverODBC Download
|Snowpark APISnowpark Client Download
|DriversDrivers and Libraries
|Scala and Java connectorsDrivers and Libraries
|SnowCDDrivers and Libraries
|Snowpark MLDrivers and Libraries

Snowflake Client Repository¶
----------------------------

To download SnowSQL, the ODBC Driver, the Snowpark Library, or SnowCD over HTTP programmatically (e.g. using curl), use the
Snowflake Client Repository. The Snowflake Client Repository serves the packages for these clients through CDN (Content Delivery
Network) using the following endpoints:

https://sfc-repo.azure.snowflakecomputing.com/index.html(mirror on Azure Blob)

If the endpoint is not specified explicitly, the client upgrader (e.g., the SnowSQL auto-upgrader) uses the AWS endpoint. For instructions on specifying the endpoint, see the installation documentation for the client.

Note

Users can download Snowflake clients from either endpoint regardless of which cloud provider hosts their Snowflake account.

Was this page helpful?

YesNoVisit SnowflakeJoin the conversationDevelop with SnowflakeShare your feedbackRead the latest on our blogGet your own certificationPrivacy NoticeSite Terms© 2024Snowflake, Inc. All Rights Reserved.On this page

Snowflake Developer Center Download PagesSnowflake Client RepositoryLanguage: **English**EnglishFrançaisDeutsch日本語한국어Português



