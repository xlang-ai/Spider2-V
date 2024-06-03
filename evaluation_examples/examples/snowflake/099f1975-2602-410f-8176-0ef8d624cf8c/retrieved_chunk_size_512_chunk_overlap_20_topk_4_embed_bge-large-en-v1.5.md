Documentation Source:
docs.snowflake.com/en/user-guide/ui-snowsight-visualizations.md

Documentation Title:
Visualizing worksheet data | Snowflake Documentation

Documentation Content:
```
SELECTCOUNT(O_ORDERDATE)asorders,O_ORDERDATEasdateFROMSNOWFLAKE_SAMPLE_DATA.TPCH_SF1.ORDERSWHEREO_ORDERDATE=:daterangeGROUPBY:datebucket(O_ORDERDATE),O_ORDERDATEORDERBYO_ORDERDATELIMIT10;
```
CopyCharts and new query results¶
-----------------------------

Your chart updates automatically as long as the columns used by the chart are available in the query results. If a column name changes, you
must update the chart to use the new column name. Charts indicate any columns that cannot be found.

Aggregate and bucket data¶
--------------------------

Charts simplify grouping numbers, dates, and timestamps of more or less continuous values into various *buckets*. For example, suppose your
query retrieves per-day data over a period of time. Without modifying your query, you can easily select a different bucket of time (e.g.
weekly or monthly data) in the inspector panel to change the time dimension of the results displayed in the chart.

Charts can bucket by date, week, month, and year for date columns. For numeric columns, charts can bucket by integer values.

Charts use aggregation functions to determine a single value from multiple data points in a bucket. These functions are as follows:

average

count

minimum

maximum

median

mode

sum

Download charts¶
----------------

Snowsight provides PNG-formatted files of charts.

To download a chart, select Download chart(!).

Was this page helpful?

YesNoVisit SnowflakeJoin the conversationDevelop with SnowflakeShare your feedbackRead the latest on our blogGet your own certificationPrivacy NoticeSite Terms© 2024Snowflake, Inc. All Rights Reserved.On this page

Create a chartModify a chartCharts and new query resultsAggregate and bucket dataDownload chartsRelated content

Getting started with SnowsightManaging and using worksheets in SnowsightGetting started with worksheetsQuerying data using worksheetsVisualizing data with dashboardsLanguage: **English**EnglishFrançaisDeutsch日本語한국어Português



Documentation Source:
docs.snowflake.com/en/user-guide/ui-snowsight-visualizations.md

Documentation Title:
Visualizing worksheet data | Snowflake Documentation

Documentation Content:
You can also visualize your data using dashboards.

Create a chart¶
---------------

When you run a query in a worksheet, you can display a chart based on the results.

Open a worksheet.

Run the worksheet.

Above the results table for the query, select Chart.

Modify a chart¶
---------------

When you select a chart to visualize your worksheet results, Snowsight automatically generates a chart for you based on the
query results. Each query supports one type of chart at a time.

Hover over the chart to view details about each data point. For example, you can view your results as a line chart:

!You can modify the type of chart used to display your query results.

- Select the chart type to choose a different type, for example, Bar.

!
You can manage the columns in your chart with the Datasection:

!Select a column to modify the column attributes:

Add or remove columns.

Choose a different column in the query results to use in the chart.

* Modify how column data is represented in the chart. For example, change the bucketing for a time column from day to minutes.

!You can modify the column attributes to configure how data in that column is rendered in the chart. See Aggregate and bucket datafor more details about managing aggregate data.

Style your chart in the Appearancesection. The available settings depend on the type of chart. For example, for a heatgrid
chart:

!The exact content of your charts depends on your query results. To generate the examples in this topic, use the following query based
on the Snowflake sample data:



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
docs.snowflake.com/en/user-guide/sample-data-using.md

Documentation Title:
Using the Sample Database | Snowflake Documentation

Documentation Content:
```
selectcount(*)fromsnowflake_sample_data.tpch_sf1.lineitem;+----------+| COUNT(*) ||----------||  6001215 |+----------+useschemasnowflake_sample_data.tpch_sf1;selectcount(*)fromlineitem;+----------+| COUNT(*) ||----------||  6001215 |+----------+
```
CopyNote

You must have a running, current warehouse in your session to perform queries. You set the current warehouse in a session using the USE WAREHOUSEcommand (or within the Worksheet in the web interface.)

Using the Tutorial SQL Scripts¶
-------------------------------

Snowflake provides a set of tutorials, which are annotated SQL statements that query the sample data sets to answer a set of practical business questions.

To access the tutorials from Classic Console:

1. In the Worksheets!page, click on the down-arrow next to the worksheet tabs and select Open Tutorials:

!
2. The Open Worksheetdialog displays the list of available tutorials. In the dialog, select a tutorial and click on the Openbutton:

!
3. A new worksheet is created containing the contents of the tutorial:

!

You can then execute the queries in the tutorial as you would in any worksheet. You can also alter the tutorial in the worksheet and save it as a custom worksheet.

Was this page helpful?

YesNoVisit SnowflakeJoin the conversationDevelop with SnowflakeShare your feedbackRead the latest on our blogGet your own certificationPrivacy NoticeSite Terms© 2024Snowflake, Inc. All Rights Reserved.On this page

Viewing the Sample DatabaseQuerying Tables and Views in the Sample DatabaseUsing the Tutorial SQL ScriptsLanguage: **English**EnglishFrançaisDeutsch日本語한국어Português



