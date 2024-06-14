Documentation Source:
docs.snowflake.com/en/user-guide/ui-snowsight-filters.md

Documentation Title:
Filter query results in dashboards and worksheets | Snowflake Documentation

Documentation Content:
For Display Name, enter a name for the filter. This name appears on the filter when selecting the filter on a worksheet or dashboard.
	
	For SQL Keyword, enter a unique keyword to insert into queries. Use the format :, without spaces.
	For example: :page\_path.
	
	For Description, enter a description of the filter.
	
	For Role, select a role to associate with the filter and run the query used to populate filter values, if the filter is based
	on a query. Only roles with permissions to create custom filters appear in the drop-down list.
	See Manage ownership of custom filtersfor more details.
	
	For Warehouse, select a warehouse to use to refresh filter values, if the filter is based on a query.
	The owner role for the filter must have the USAGE privilege on the warehouse you select.
	If you want to run and validate your query as part of these steps, the warehouse must be running.
	
	6. For Options via, choose whether the filter values are populated by a query or a list:
	
	
		If you select Query, select Write Queryand see Write a query to populate a filterfor guidance writing a
		filter query.
		
		* If you select List, do the following:
		
		
			Select Edit List.
			
			Optionally, for Name, enter a name for the list item. The name appears in the drop-down list for the filter.
			If you do not provide a name, the Valueis used.
			
			For Value, enter the value of the column name to use in the filter.
			
			Continue adding name and value pairs until your list is complete, then select Save.
In the Add Filterdialog, for Value Type, choose whether the list items are Textor Numbertypes of data.

If you want users to be able to select multiple items in the drop-down list of filter options,
turn on the toggle for Multiple values can be selected.

8. If you want users to be able to see results for all items in the column, turn on the toggle for Include an “All” option, then select
how you want the Alloption to function:



Documentation Source:
docs.snowflake.com/en/user-guide/ui-snowsight-filters.md

Documentation Title:
Filter query results in dashboards and worksheets | Snowflake Documentation

Documentation Content:
DOCUMENTATION/Getting StartedGuidesDeveloperReferenceReleasesTutorialsStatusOverview2. Connecting to SnowflakeEcosystem- SnowsightGetting started with SnowsightExploring the navigation menuAbout the Snowsight UpgradeUpgrading to SnowsightSearch Snowflake objects and resourcesGetting started with worksheetsManaging and using worksheetsQuerying data with SQL worksheetsUsing Snowflake Copilot in SQL worksheetsVisualizing worksheet resultsVisualizing data with dashboardsFilter query results in worksheets and dashboardsExplore and manage dataManage your user profileManage notification contactsManage support cases
Classic ConsoleSnowSQLVisual Studio Code SQL ExtensionClient DownloadClient ConfigurationConnecting to Third-Party SystemsSnowflake Connector for Google Analytics Aggregate DataSnowflake Connector for Google Analytics Raw DataSnowflake Connector for Google Looker StudioSnowflake Connector for ServiceNow®Snowflake Connector for ServiceNow®v2
Virtual warehousesDatabases, Tables, & ViewsData TypesData LoadingData UnloadingQueriesData Sharing & CollaborationSnowflake AI FeaturesSnowflake CortexAlerts & NotificationsSecurityData GovernancePrivacyOrganizations & AccountsBusiness Continuity & Data RecoveryPerformance OptimizationCost & Billing
GuidesConnecting to SnowflakeSnowsightFilter query results in worksheets and dashboardsFilter query results in dashboards and worksheets¶
==================================================

You can filter your query results in dashboards and SQL worksheets using system filters, available to all roles in Snowflake,
or with custom filters created by administrators.

Create custom filters¶
----------------------

Custom filters let you change the results of a query without directly editing the query.

Filters are implemented as special keywords that resolve as a subquery or list of values, which are then used in the execution of a query.
As a result, there are some limitations when using a filter in a SQL query. See Specify a filter in a SQL query.

Note

Anyone in your account can view and use a custom filter after it is created. A custom filter has an associated role,
but that role does not limit filter visibility.



Documentation Source:
docs.snowflake.com/en/user-guide/ui-snowsight-filters.md

Documentation Title:
Filter query results in dashboards and worksheets | Snowflake Documentation

Documentation Content:
Write a query to populate a filter¶

To populate a list of filter options from a query, your query must follow certain guidelines:

Must return the columns nameand value.

Can return the optional column description.

Can return other columns, but those do not appear in the drop-down filter list.


A filter can only run one query at a time. You cannot run multiple queries to generate the list of filter options, for example by running
one query to return the namecolumn and a second query to return the valuecolumn.

Note

The query used to populate a list of filter options is run as the user that created (or last modified) the filter.
Because anyone in your account can view and use a custom filter after it is created, make sure that the list of
filter options produced by your query do not contain protected or sensitive data.

After you write your filter query and add it in the New filterdialog, do the following to finish setting up your query filter:

Select Doneto save your filter query and return to the Add Filterdialog.

Optionally change the default refresh option from Refresh hourlyto Never refreshor Refresh daily. For details
and considerations for filter refresh options, see Manage refresh frequency for a custom filter.

Return to the steps for creating a custom filter to finish creating your filter. See Create a custom filter.

Review and manage custom filters in an account¶
-----------------------------------------------

To review custom filters in your account, open a worksheet or dashboard and then select !.

To make changes to any filters, such as changing the refresh frequency for the query used to populate a custom filter list,
you must have the ACCOUNTADMIN role or a role with permissions to manage filters.
See Manage refresh frequency for a custom filter.



Documentation Source:
docs.snowflake.com/en/user-guide/ui-snowsight-filters.md

Documentation Title:
Filter query results in dashboards and worksheets | Snowflake Documentation

Documentation Content:
Create a custom filter¶

You must use Snowsight to create a filter, and you must use a role with permissions to create custom filters.

To create a custom filter, do the following:

Sign in to Snowsight.

Select Projects» Worksheetsto open the list of worksheets and open a worksheet,
or select Projects» Dashboardsto open the list of dashboards and open a dashboard.

Select !and, if in a worksheet, select Manage Filters.

In the Filtersdialog that appears, select + Filter.

5. To add a filter, complete the following:



