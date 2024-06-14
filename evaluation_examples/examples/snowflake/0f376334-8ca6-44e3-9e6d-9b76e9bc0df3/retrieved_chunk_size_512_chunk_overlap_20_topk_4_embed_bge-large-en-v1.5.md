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
You can also perform other tasks on this page, including:

Resizing the current warehouse to dynamically increase or decrease the compute resources utilized for executing your queries and other DML statements.

Exporting the result for a selected query/statement (if the result is still available). For more information, see Exporting Query Results.

Saving and Managing Worksheets¶
-------------------------------

Snowflake automatically saves worksheets as you type and persists the current state of a worksheet between user sessions. To organize your worksheets, double-click on the worksheet label in the tab
(e.g. `Worksheet2`) and type a new, more meaningful name for the worksheet (e.g. `SalesAnalysis`).

To open a closed worksheet, click the down-arrow to the right of the open worksheet tabs, and click Open Worksheet. The Open Worksheetdialog opens.

!Search for worksheets by label.

Delete selected worksheets.

3. Click on a row to select a single worksheet.

Click the **CMD**(Mac) or **CTRL**(Windows) key once and then click on multiple rows to select multiple worksheets.
Double-click a label to edit it.

Open selected worksheets.


The Open Worksheetdialog supports the following actions:



|Action

Steps


|  |
|Search for individual worksheets by label.

Enter text in the Searchfield. The list of existing worksheets is filtered automatically.


|  |
|Edit worksheet labels.

Double-click on a worksheet label, and edit the text. Worksheet labels are limited to 255 characters.


|Open or delete one or more worksheets.

1. Select a single worksheet by clicking on the table row for the worksheet.

To select multiple worksheets, click the CMD (Mac) or CTRL (Windows) key once and then click on multiple table rows.
Click on the Openbutton to open the worksheets in separate tabs, orclick on the Deletebutton to delete the worksheets.



Using the Object Browser¶
-------------------------

!Preview table data.

Double-click to insert name into SQL editor.



Documentation Source:
docs.snowflake.com/en/user-guide/ui-snowsight-query.md

Documentation Title:
Querying data using worksheets | Snowflake Documentation

Documentation Content:
Running worksheets in folders¶

Folders no longer have a role assigned to them. An owner or editor of a worksheet in a folder can change the worksheet to run as any role.
You can also add USE ROLEto a worksheet in a folder to run different statements in the worksheet as different roles.

When you create a worksheet inside a folder, the worksheet is created with the role of your current session.

Note

To run a worksheet in a folder that was shared with you, even if you have View and Runor Editpermissions on the folder,
you must use the same role as the worksheet. If you do not have the same role, duplicate the worksheet and run it as one of your own roles.

Exploring the worksheet results¶
--------------------------------

Note

Available to most accounts. Accounts in U.S. government regions, accounts using Virtual Private Snowflake (VPS), and accounts
that use Private Connectivity to access Snowflake continue to see query results limited to 10,000 rows.

When you run one query or all queries in a worksheet, you see the query results.

The query results display as a table. You can navigate the query results with the arrow keys on your keyboard, as you would with a
spreadsheet. You can select columns, cells, rows, or ranges in the results table. You can copy and paste any selection.

For up to 1 million rows of results, you can review generated statistics that display contextual information for any selection,
as well as overall statistics. See Automatic contextual statisticsfor more details.

If you want to view your results as a chart, select Chart. For more details about charts, see
Visualizing worksheet data.

Query results are cached. For more details, see Stored results for past worksheet versionsand
Managing worksheet history and versions.



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



