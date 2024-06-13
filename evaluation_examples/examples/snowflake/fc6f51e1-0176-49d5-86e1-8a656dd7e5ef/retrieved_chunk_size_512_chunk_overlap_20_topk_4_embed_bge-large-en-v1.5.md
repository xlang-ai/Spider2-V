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
docs.snowflake.com/en/release-notes/2023/ui/2023-12-12.md

Documentation Title:
December 12–14, 2023 — Snowsight Release Notes | Snowflake Documentation

Documentation Content:
For more details, see Recover worksheets owned by a dropped user.

View Query History in worksheets —– *General Availability*¶
-----------------------------------------------------------

With this release, we are pleased to announce the general availability of Query History in worksheets in Snowsight.
When you view Query History for a worksheet, you can review the queries run in a Snowsight worksheet, as well as the query results.

For more information, see View query history.

Was this page helpful?

YesNoVisit SnowflakeJoin the conversationDevelop with SnowflakeShare your feedbackRead the latest on our blogGet your own certificationPrivacy NoticeSite Terms© 2024Snowflake, Inc. All Rights Reserved.On this page

Recover worksheets for dropped users — PreviewView Query History in worksheets —– General AvailabilityLanguage: **English**EnglishFrançaisDeutsch日本語한국어Português



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
docs.snowflake.com/en/release-notes/2023/7_36.md

Documentation Title:
October 09-10, 2023 — 7.36 Release Notes | Snowflake Documentation

Documentation Content:
Viewing Query History in worksheets — *Preview*¶

With this release, we are pleased to announce the preview of Query History in worksheets in Snowsight. When you view Query History
for a worksheet, you can review the queries run in a Snowsight worksheet, as well as the query results.

For more information, see View query history.

Release Notes Change Log¶
-------------------------



|Announcement

Update


|  |
|*Company name for listing analytics***Added**to *Data Collaboration Updates*


|  |
|*Logging and tracing from handler code — General Availability***Removed**from *New Features*



Was this page helpful?

YesNoVisit SnowflakeJoin the conversationDevelop with SnowflakeShare your feedbackRead the latest on our blogGet your own certificationPrivacy NoticeSite Terms© 2024Snowflake, Inc. All Rights Reserved.On this page

Extensibility UpdatesData Collaboration UpdatesWeb Interface UpdatesRelease Notes Change LogLanguage: **English**EnglishFrançaisDeutsch日本語한국어Português



