Documentation Source:
docs.snowflake.com/en/user-guide/ui-snowsight-activity.md

Documentation Title:
Monitor query activity with Query History | Snowflake Documentation

Documentation Content:
Filter Query History¶

Note

You might see incomplete or no results when you use the Query History page. Use filters to help ensure reliable results.

You can filter by the following:

Status of the query, for example to identify long-running queries, failed queries, and queued queries.

* User who performed the query, including:


	All, to see all users for which you have access to view query history.
	
	The user you are signed in as (default)
	
	Individual Snowflake users in your account, if your role can view query history for other users.
Time period during which the query was run, up to 14 days.

* Other filters, including the following:



Documentation Source:
docs.snowflake.com/en/user-guide/ui-snowsight-activity.md

Documentation Title:
Monitor query activity with Query History | Snowflake Documentation

Documentation Content:
DOCUMENTATION/Getting StartedGuidesDeveloperReferenceReleasesTutorialsStatusOverviewConnecting to SnowflakeVirtual warehousesDatabases, Tables, & ViewsData TypesData LoadingData Unloading8. QueriesJoinsSubqueriesQuerying Hierarchical DataCommon Table Expressions (CTE)Querying Semi-structured DataAnalyzing time-series dataWindow FunctionsMatch RecognizeSequencesPersisted Query ResultsDistinct CountsSimilarity EstimationFrequency EstimationEstimating Percentile ValuesMonitor query activity with Query HistoryQuery ProfileQuery HashCancel Statements
Data Sharing & CollaborationSnowflake AI FeaturesSnowflake CortexAlerts & NotificationsSecurityData GovernancePrivacyOrganizations & AccountsBusiness Continuity & Data RecoveryPerformance OptimizationCost & Billing
GuidesQueriesMonitor query activity with Query HistoryMonitor query activity with Query History¶
==========================================

To monitor query activity in your account, you can use:

The Query Historypage in Snowsight.

The QUERY\_HISTORY Viewin the ACCOUNT\_USAGE schema of the SNOWFLAKE database.

The QUERY\_HISTORYfamily of table functions in
INFORMATION\_SCHEMA.


With the Query Historypage in Snowsight, you can do the following:

Monitor queries executed by users in your account.

View details about queries, including performance data. In some cases,
query details are unavailable.

Explore each step of an executed query in the query profile.


The Query History page lets you explore queries executed in your Snowflake account over the last 14 days.

Within a worksheet, you can see the query history for queries that have been run in that worksheet.
See View query history.

Review Query History by using Snowsight¶
----------------------------------------

To access the Query Historypage in Snowsight, do the following:

Sign in to Snowsight.

Select Monitoring» Query History.

Filter your viewto see the most relevant and accurate results.


Note

You might see incomplete or no results when you use the Query Historypage. This is because the page spends a maximum of 15 seconds
retrieving results and returns whatever query information is available at that time. To retrieve results reliably, use filters to reduce
the time it takes to retrieve results to under 15 seconds.



Documentation Source:
docs.snowflake.com/en/user-guide/ui-snowsight-activity.md

Documentation Title:
Monitor query activity with Query History | Snowflake Documentation

Documentation Content:
Considerations for using Query History¶

When reviewing the Query Historyfor your account, consider the following:

Details for queries executed more than 7 days ago do not include Userinformation due to the data retention policy for
sessions. You can use the user filter to retrieve queries run by individual users.
See Filter Query History.

For queries that failed due to syntax or parsing errors, you see instead of the SQL statement that was executed.
If you are granted a role with appropriate privileges, you can set the ENABLE\_UNREDACTED\_QUERY\_SYNTAX\_ERRORparameter to view
the full query text.

Filters and the Startedand End Timecolumns use your current time zone. You can’t change this setting.
Setting the TIMEZONEparameter for the session doesn’t change the time zone used.



Documentation Source:
docs.snowflake.com/en/user-guide/ui-snowsight-filters.md

Documentation Title:
Filter query results in dashboards and worksheets | Snowflake Documentation

Documentation Content:
Troubleshoot failed filter query refreshes¶

Refreshes of the filter query can fail for one of the following reasons:

The user that created or last modified the filter has been dropped or disabled in Snowflake.

The user is inactive because they have not signed in for 3 months.


It is not possible to see which users created or last modified a given filter. If you have filters that are failing to refresh,
you might see successful authentication attempts by the WORKSHEETS\_APP\_USER user followed by failed authentication
attempts from a user in the LOGIN\_HISTORY Viewview of the ACCOUNT\_USAGE schema in the
shared SNOWFLAKE database.

For example, you can use the following query to identify login activity that uses an OAuth access token from the previous two days:


```
SELECT*FROMSNOWFLAKE.ACCOUNT_USAGE.LOGIN_HISTORYWHEREFIRST_AUTHENTICATION_FACTOR='OAUTH_ACCESS_TOKEN'ANDREPORTED_CLIENT_TYPE='SNOWFLAKE_UI'ANDEVENT_TIMESTAMP>DATEADD('DAY',-2,CURRENT_DATE());ORDERBYEVENT_TIMESTAMPDESC;
```
CopyFailed authentication attempts associated with a failed query refresh frequency would happen at the same time each day or each hour,
depending on the custom filter refresh frequency.

Specify a filter in a SQL query¶
--------------------------------

You can use a system filteror a custom filter in a SQL query.
You cannot use a filter in a stored procedure or a user-defined function (UDF).

To add a filter to your SQL query, use one of the following formats:

Specify the filter as part of a SELECT statement, like `SELECT:()`.

* Specify the filter using an equals sign as the comparator. For example:



