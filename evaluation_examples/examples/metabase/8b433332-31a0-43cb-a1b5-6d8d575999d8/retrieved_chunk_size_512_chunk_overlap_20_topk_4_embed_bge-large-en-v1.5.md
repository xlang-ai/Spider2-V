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
www.metabase.com/learn/index.md

Documentation Title:
Learn Metabase

Documentation Content:
This guide will help you pick the right visualization for the job.
	2. Guide to line chartsWhat we talk about when we talk about line charts: time series, trend lines, alerts, and more.
	3. Master the bar chart visualizationCreate a bar chart and customize it with visualization settings.
	4. Visualize your data as a histogramLearn when to use a histogram, and how Metabase makes it easy to create histograms.
	5. Visualizing data with mapsHow to use pin maps, region maps, and grid maps to visualize data in Metabase.
	6. Almost everything you can do with the table visualizationLearn how to set up conditional formatting, mini bar charts, value formatting, and more.
	7. Creating pivot tablesLearn how to create pivot tables using different databases in Metabase.
	8. Funnel chartsUse funnel charts to show progression through steps.Explore this topic
 !!
7. TopicBuilding dashboards
-------------------How to build interactive dashboards.

8 articles
 !
	1. BI dashboard best practicesLearn how to make great business intelligence dashboards.
	2. Linking filters in dashboardsLink filters in dashboards to limit the choices available in one filter based on the current selection of another filter.
	3. Custom destinations: choose what happens when people click on charts in your dashboardYou can set up dashboard cards to send people to dashboards, saved questions, and URLs, and use values from the card to update filters at the destination, or parameterize links to external sites.
	4. Cross-filtering: using a chart to update a dashboard filterWith just a few clicks, you can configure any chart or table to update a dashboard filter.
	5. Adding filters to dashboards with SQL questionsHow to add filter widgets to dashboards and connect them to Field Filter variables in a SQL question.
	6. Build a record lookup tool with MetabaseHow to use Metabase to build an internal lookup tool to quickly find details about your customers, orders, or other data.
	7. Why you should regularly edit your dashboardsEditing dashboards is more than just maintaining your tools; it helps keep you focused on the right priorities.
	8.



Documentation Source:
www.metabase.com/learn/visualization/chart-guide.md

Documentation Title:
Which chart should you use?

Documentation Content:
Tables

Often you’ll want to see a lot of measures at once, list their exact values, and be able to sort those measures. Maybe you simply want to add or remove a few columns, or add a couple of filters to make it easy for people to look up certain values. And that’s what tables are for. Tables in Metabase are one of the most versatile visualization types, so check out our article on Everything you can do with the table visualization.

!If you additionally want to summarize groupings of rows (like seeing the annual subtotal in a grouping of quarterly results), or switch up the columns and rows, you’ll want to use a pivot table. Check out How to create a pivot table to summarize your data.



