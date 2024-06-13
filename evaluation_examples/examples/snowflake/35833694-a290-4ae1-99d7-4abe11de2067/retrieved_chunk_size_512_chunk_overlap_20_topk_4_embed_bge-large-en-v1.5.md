Documentation Source:
docs.snowflake.com/en/user-guide/ui-snowsight-quick-tour.md

Documentation Title:
Snowsight quick tour | Snowflake Documentation

Documentation Content:
!For more details, see:

Getting started with worksheetsManaging and using worksheets in SnowsightQuerying data using worksheetsWriting Snowpark Code in Python WorksheetsVisualize query results with charts and dashboards¶
---------------------------------------------------

When you run a query in Snowsight, you can choose to view your results as a chart. You can also create a collection of charts
as a Dashboard, allowing you to review your data more easily. Dashboards provide flexible collections of charts arranged as tiles.
Dashboard charts start with SQL to generate results and associated charts. You can share these charts with others, modify the charts,
and display them as dashboard tiles.

!To learn more about charts, see Visualizing worksheet data. To learn more about dashboards,
see Visualizing data with dashboards

Explore and manage your database objects¶
-----------------------------------------

You can explore and manage your database objects in Snowsight as follows:

Explore databases and objects, including tables, functions, views, and more using the database object explorer.

Create objects like databases, tables, file formats, and more.

Search within the object explorer to browse database objects across your account.

Preview the contents of database objects like tables, and view the files uploaded to a stage.

Load files to an existing table, or create a table from a file so that you can start working with data in Snowflake faster.


!To learn more, see:

Explore and manage database objects in SnowsightLoading data using the web interfaceStaging files using SnowsightShare and publish data products¶
--------------------------------

Collaborate with users in other Snowflake accounts by sharing data and application packages with them, or publishing those data products
on the Snowflake Marketplace. When you share or publish data products with a listing, you can use auto-fulfillment to easily provide your data
products in other Snowflake regions.

As a consumer of data, you can access datasets and application packages shared with your account or published on the Snowflake Marketplace,
helping you derive real time data insights without needing to set up a data pipeline or write any code.



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
docs.snowflake.com/en/user-guide/querying-time-series-data.md

Documentation Title:
Analyzing time-series data | Snowflake Documentation

Documentation Content:
000 |     35.4139 | 31.6798333 || DEVICE2   | 2024-03-15 00:01:02.000 |     33.5019 | 32.1353500 || DEVICE2   | 2024-03-15 00:01:03.000 |     25.5342 | 30.8151200 || DEVICE2   | 2024-03-15 00:01:04.000 |     27.6066 | 30.2803666 || DEVICE2   | 2024-03-15 00:01:05.000 |     35.6839 | 31.0523000 || DEVICE2   | 2024-03-15 00:01:06.000 |     25.1949 | 30.1941571 || DEVICE2   | 2024-03-15 00:01:07.000 |     33.4865 | 30.9174142 || DEVICE2   | 2024-03-15 00:01:08.000 |     34.0321 | 30.7200142 || DEVICE2   | 2024-03-15 00:01:09.000 |     31.4201 | 30.4226142 || DEVICE2   | 2024-03-15 00:01:10.000 |     27.5301 | 30.7077428 |+-----------+-------------------------+-------------+------------+
```
Note

If you run this example yourself, your output will not match exactly because the sensor\_data\_tstable is loaded
with randomly generated values.

You can use Snowsight to visualize the results of queries like this one, and get a
better sense of the smoothing effect of calculations with sliding window frames.
In the query worksheet, click the Chartbutton next to Results.

For example, the yellow line in the bar chart shows a much smoother trend for average
temperature versus the blue line for the raw temperature.

!Other window functions, such as the
LEADand LAGranking functions,
are also commonly used in time-series analysis.



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



