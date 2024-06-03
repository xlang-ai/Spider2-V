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
docs.snowflake.com/en/user-guide/ui-worksheet.md

Documentation Title:
Using Worksheets for Queries / DML / DDL | Snowflake Documentation

Documentation Content:
Searching for Database Objects¶

Search for databases, schemas, tables, and views using the Find database objectsfield. Note that searches are “starts with” searches, and are also case-insensitive unless the search string is
enclosed in double quotes.

You can also search within a database or schema using the search icon that appears for the item when you hover over it in the object browser.

Managing Warehouses¶
--------------------

Click the context menu to select a different active warehouse for the worksheet. You can resume or suspend the selected warehouse, or resize the warehouse.

!Managing Queries¶
-----------------

Important

The query details and results displayed in the worksheet are only maintained for your current user session. If you log out of the web interface and log back in, the results from your previous
session are no longer displayed in the worksheet; however, you can use the History!page to see queries you executed in previous sessions.



Documentation Source:
docs.snowflake.com/en/user-guide/ui-snowsight-query.md

Documentation Title:
Querying data using worksheets | Snowflake Documentation

Documentation Content:
Append a SQL script to an existing worksheet¶

If you have a SQL script in a file, you can append it to an existing worksheet by doing the following:

Sign in to Snowsight.

Select Projects» Worksheetsto open the list of worksheets.

Open a worksheet.

Hover over the tab for the worksheet and select !, then choose Import SQL from File.

5. Browse to the SQL file on your computer.

The file contents are appended to your worksheet.



Documentation Source:
docs.snowflake.com/en/user-guide/ui-snowsight-worksheets-gs.md

Documentation Title:
Getting started with worksheets | Snowflake Documentation

Documentation Content:
DOCUMENTATION/Getting StartedGuidesDeveloperReferenceReleasesTutorialsStatusOverview2. Connecting to SnowflakeEcosystem- SnowsightGetting started with SnowsightExploring the navigation menuAbout the Snowsight UpgradeUpgrading to SnowsightSearch Snowflake objects and resourcesGetting started with worksheetsManaging and using worksheetsQuerying data with SQL worksheetsUsing Snowflake Copilot in SQL worksheetsVisualizing worksheet resultsVisualizing data with dashboardsFilter query results in worksheets and dashboardsExplore and manage dataManage your user profileManage notification contactsManage support cases
Classic ConsoleSnowSQLVisual Studio Code SQL ExtensionClient DownloadClient ConfigurationConnecting to Third-Party SystemsSnowflake Connector for Google Analytics Aggregate DataSnowflake Connector for Google Analytics Raw DataSnowflake Connector for Google Looker StudioSnowflake Connector for ServiceNow®Snowflake Connector for ServiceNow®v2
Virtual warehousesDatabases, Tables, & ViewsData TypesData LoadingData UnloadingQueriesData Sharing & CollaborationSnowflake AI FeaturesSnowflake CortexAlerts & NotificationsSecurityData GovernancePrivacyOrganizations & AccountsBusiness Continuity & Data RecoveryPerformance OptimizationCost & Billing
GuidesConnecting to SnowflakeSnowsightGetting started with worksheetsGetting started with worksheets¶
================================

View and create worksheets in Snowsight. You can also import existing SQL worksheets from the Classic Console.

SQL worksheets let you write and run SQL statements, explore and filter query results, and visualize the results.
See Querying data using worksheetsand Visualizing worksheet data.
You can also write Snowpark Python in worksheets. See Writing Snowpark Code in Python Worksheets.

Manage your worksheets by organizing them into folders, share worksheets with colleagues that also use Snowflake, and
manage the version history for worksheets. For more details, see Managing and using worksheets in Snowsight.

Viewing worksheets in Snowsight¶
--------------------------------

After signing in to Snowsight, you see the worksheets in your account. If you don’t see any worksheets, you might need to import
worksheets from the Classic Console. See Import worksheets from the Classic Console.

Using the options, you can view recent worksheets opened by you, worksheets that your colleagues have shared with you,
worksheets that you created and own, or folders you created or that your colleagues have shared with you.



