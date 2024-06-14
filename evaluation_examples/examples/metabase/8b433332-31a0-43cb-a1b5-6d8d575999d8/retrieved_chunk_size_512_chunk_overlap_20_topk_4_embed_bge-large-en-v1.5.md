Documentation Source:
www.metabase.com/learn/visualization/bar-charts.md

Documentation Title:
Master the bar chart visualization

Documentation Content:
Create a bar chart and customize it with visualization settings.

Create a bar chart* Bar chart settings
	Data+ Display settings
		Add a goal lineShow valuesAdd a trend lineStacking options
	+ Axes
		LabelShow lines and marksScale
* Stacked bar charts
	Don’t stackStackStack-100%
Further reading
We’ll walk through creating a bar chartand editing that bar chart’s settings, then talk about stacked bar chartsand when we might want to use them.

Create a bar chart
------------------

You can follow along using Metabase’s Sample Database. Select **+ New**> **Question**> **Raw data**> **Sample database**. Choose the Sample Database’s `Orders`table as your data. Next, summarize the count of rows and group by Product -> Category.

!Click **Visualize**, and Metabase will present the data as a bar chart:

!Bar chart settings
------------------

To customize the chart, click on the **gear**icon at the bottom left of the chart to open the settings sidebar, within the settings, you’ll find the following tabs:

DataDisplayAxes
Data
----

Here we can format and style our bar chart by clicking the `...`under Y-axis.
To change bar colors, click the color swatch and choose from the palette.

Customize your chart in the **Formatting tab**by adjusting numbers, separators, decimals, and scale. You can also add Prefix/Suffix as needed. In the **Style tab**, select colors, modify labels, choose a chart type (line, area, or bar), and position the Y-axis according to your chart preferences.

!Display settings
----------------

In the Settings > Display section, you can customize your chart in several ways:



Documentation Source:
www.metabase.com/learn/visualization/bar-charts.md

Documentation Title:
Master the bar chart visualization

Documentation Content:
when!Analytics dashboards
 Share insights with anyone, anywhere!SQL editor
 For advanced data users!Sandboxing
 Set boundaries around your data!Models
 A starting point for questions!Permissions
 Keep your data secure and private!CSV upload
 Go beyond VLOOKUPDocumentationResources!Learn!Blog!Events!Customers!Discussion!Partners!Community Stories!Startup Guide to Financial Modeling
 New!Community Data Stack Report
 NewPricingLog in1. !Getting Started
	Getting started with MetabaseSharing your work with othersExploring data with Metabase's data browserNext steps: advanced Metabase features for data analystsBeyond BI: other problems you can solve with MetabaseA tour of Metabase
2. !Data fundamentals
	A guide to the data landscapeA short overview of databasesData types and metadataDatabase table relationshipsMeasures and dimensionsData normalizationTypes of databasesData warehouse vs data lake vs data martData cubes
3. !Asking questions
	Create interactive chartsCustom expressions in the notebook editorJoins in MetabaseMulti-level aggregationSearching your tables and questionsCleaning and formatting text
4. !Working with SQL
	Best practices for writing SQL queriesCreate filter widgets for charts using SQL variablesField Filters: create smart filter widgets for SQL questionsWorking with dates in SQLSQL snippets: reuse and share SQL codeSimplify complex queries with Common Table Expressions (CTEs)SQL Snippets vs. Saved Questions vs. ViewsCombining tables with joinsSQL join typesSQL trick: ordering bars in a chartHow to calculate customer lifetime value (LTV) with SQL
5. !Debugging SQL
	Debugging SQL syntax errorsDebugging SQL query logicDebugging duplicated data in SQL query resultsDebugging missing data in SQL query results
6. !Visualizing data
	Which chart should you use?Guide to line chartsMaster the bar chart visualizationVisualize your data as a histogramVisualizing data with mapsAlmost everything you can do with the table visualizationCreating pivot tablesFunnel charts
7.



Documentation Source:
www.metabase.com/docs/v0.49/questions/sharing/visualizing-results.md

Documentation Title:
Visualizing data

Documentation Content:
when!Analytics dashboards
 Share insights with anyone, anywhere!SQL editor
 For advanced data users!Sandboxing
 Set boundaries around your data!Models
 A starting point for questions!Permissions
 Keep your data secure and private!CSV upload
 Go beyond VLOOKUPDocumentationResources!Learn!Blog!Events!Customers!Discussion!Partners!Community Stories!Startup Guide to Financial Modeling
 New!Community Data Stack Report
 NewPricingLog inv0.49Questions
Visualizing data
================

While tables are useful for looking up information or finding specific numbers, it’s usually easier to see trends and make sense of data using charts.

To change how the answer to your question is displayed, click on the **Visualization**button in the bottom-left of the screen to open the visualization sidebar.

!If a particular visualization doesn’t really make sense for your answer, that option will appear in the “Other charts” section. You can still select one of these other charts, though you might need to fiddle with the chart options to make the chart work with your data.

Not sure which visualization type to use? Check out Which chart should you use?

Visualization options
---------------------

!Each visualization type has its own advanced options.

To change the settings for a specific chart, for example a row chart, you could either:

* Click on the gear icon in the bottom left of the chart (next to the **Visualization**button, or
* Click on **Visualization**in the bottom left of the chart, then hover over the currently selected chart and click on the **gear**icon that pops up.

Visualization types
-------------------

Metabase ships with a bunch of different visualizations types:

Numbers
-------

The Numbersoption is for displaying a single number, nice and big.

!Trends
------

The Trendvisualization is great for displaying how a single number has changed between two time periods.

!Detail
------

The Detailvisualization shows a single result record (row) in an easy-to-read, two-column display.

!Progress bars
-------------

Progress barsare for comparing a single number to a goal value that you set.

!Gauges
------

Gaugesallow you to show a single number in the context of a set of colored ranges that you can specify.



Documentation Source:
www.metabase.com/docs/v0.49/questions/sharing/visualizations/combo-chart.md

Documentation Title:
Combo charts

Documentation Content:
when!Analytics dashboards
 Share insights with anyone, anywhere!SQL editor
 For advanced data users!Sandboxing
 Set boundaries around your data!Models
 A starting point for questions!Permissions
 Keep your data secure and private!CSV upload
 Go beyond VLOOKUPDocumentationResources!Learn!Blog!Events!Customers!Discussion!Partners!Community Stories!Startup Guide to Financial Modeling
 New!Community Data Stack Report
 NewPricingLog inv0.49Questions
Combo charts
============

Combo charts let you combine bars and lines (or areas) on the same chart.

!Metabase will pick one of your series to display as a line, and another to display as a bar by default. Open up the visualization settings to change which series are lines, bars, or areas, as well as to change per-series settings like colors. Click the down arrow icon on the right of a series to see additional options:

!To use a Combo chart you’ll either need to have two or more metrics selected in the Summarize By section of your question, with one or two grouping columns, like this:

!Or you’ll need a question with a single metric and two grouping columns, like this:

!Read docs for other versions of Metabase.
 

Did this article help you?
 

Yes
 No
 Send
 Thanks for your feedback!

Want to improve these docs? Propose a change.##### Subscribe to our newsletter

Stay in touch with updates and news from Metabase. No spam, ever.



