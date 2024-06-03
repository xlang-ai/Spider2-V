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
docs.snowflake.com/en/release-notes/bcr-bundles/2023_01/bcr-936.md

Documentation Title:
Query History: Redacted SQL Upon Syntax Error | Snowflake Documentation

Documentation Content:
In order to clarify who can see this text un-redacted, please be aware that the USER who executed the query (no matter what role they
use) can see the query text. However, another user (even if they use the same role used for executing the failed query) will not be able
to see the query text. The entry in the QUERY\_HISTORYview is available for everyone
who has the necessary privileges to check this view.

Ref: 936

Was this page helpful?

YesNoVisit SnowflakeJoin the conversationDevelop with SnowflakeShare your feedbackRead the latest on our blogGet your own certificationPrivacy NoticeSite Terms© 2024Snowflake, Inc. All Rights Reserved.Language: **English**EnglishFrançaisDeutsch日本語한국어Português



Documentation Source:
docs.snowflake.com/en/developer-guide/snowpark/reference/python/latest/api/snowflake.snowpark.QueryRecord-3.md

Documentation Title:
snowflake.snowpark.QueryRecord.query_id | Snowflake Documentation

Documentation Content:
DOCUMENTATION/Getting StartedGuidesDeveloperReferenceReleasesTutorialsStatusOverviewSnowpark SessionInput/OutputDataFrameColumnData TypesRowFunctionsWindowGroupingTable FunctionTableAsyncJobStored ProceduresUser-Defined FunctionsUser-Defined Aggregate FunctionsUser-Defined Table Functions18. ObservabilityQueryHistoryQueryRecordQueryRecord.countQueryRecord.indexQueryHistory.queriesQueryRecord.query\_idQueryRecord.sql\_text
FilesLINEAGEContextExceptions
DeveloperSnowpark APIPythonPython API ReferenceObservabilityQueryRecord.query\_idsnowflake.snowpark.QueryRecord.query\_id¶
=========================================

QueryRecord.query\_id*:str*¶Alias for field number 0

Was this page helpful?

YesNoVisit SnowflakeJoin the conversationDevelop with SnowflakeShare your feedbackRead the latest on our blogGet your own certificationPrivacy NoticeSite Terms© 2024Snowflake, Inc. All Rights Reserved.Language: **English**EnglishFrançaisDeutsch日本語한국어Português



Documentation Source:
docs.snowflake.com/en/sql-reference/sql/undrop-database.md

Documentation Title:
UNDROP DATABASE | Snowflake Documentation

Documentation Content:
```
UNDROPDATABASEmytestdb2;+-------------------------------------------+| status                                    ||-------------------------------------------|| Database MYTESTDB2 successfully restored. |+-------------------------------------------+SHOW DATABASESHISTORY;+---------------------------------+-----------+------------+------------+--------+--------+---------+---------+----------------+------------+| created_on                      | name      | is_default | is_current | origin | owner  | comment | options | retention_time | dropped_on ||---------------------------------+-----------+------------+------------+--------+--------+---------+---------+----------------+------------|| Tue, 17 Mar 2015 16:57:04 -0700 | MYTESTDB  | N          | Y          |        | PUBLIC |         |         |              1 | [NULL]     || Tue, 17 Mar 2015 17:06:32 -0700 | MYTESTDB2 | N          | N          |        | PUBLIC |         |         |              1 | [NULL]     || Wed, 25 Feb 2015 17:30:04 -0800 | SALES1    | N          | N          |        | PUBLIC |         |         |              1 | [NULL]     || Fri, 13 Feb 2015 19:21:49 -0800 | DEMO1     | N          | N          |        | PUBLIC |         |         |              1 | [NULL]     |+---------------------------------+-----------+------------+------------+--------+--------+---------+---------+----------------+------------+
```
CopyWas this page helpful?

YesNoVisit SnowflakeJoin the conversationDevelop with SnowflakeShare your feedbackRead the latest on our blogGet your own certificationPrivacy NoticeSite Terms© 2024Snowflake, Inc. All Rights Reserved.On this page

SyntaxParametersUsage notesExamplesLanguage: **English**EnglishFrançaisDeutsch日本語한국어Português



