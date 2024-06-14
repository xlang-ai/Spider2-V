Documentation Source:
www.metabase.com/learn/visualization/line-charts.md

Documentation Title:
Guide to line charts

Documentation Content:
To make the chart more legible, we can summarize the data, so each point on the line chart is an aggregate of rows—“buckets” of records. (It’s much more common to plot unaggregated rows in visualizations like pin maps, or a scatterplot, e.g., to show each product plotted by price and rating.)

As an example of an aggregated metric, let’s plot the sum of order totals for each month. Click on the green **Summarize button**to pull up the **Summarize sidebar**. Metabase defaults to counting the records, but we’re not interested in the number of orders, so we’ll click on `Count`and change it to `Sum of`and select the `Total`column from `Order`.

Next, we’ll want to group our order totals by month. In the **Group by**section, under `Order`, mouse over the `Created At`field click on the `+`button to add the grouping.

!As soon as you add the grouping, Metabase updates the chart:

!This chart is a lot easier to read. And, of course, we can always select a section of the line to filter the results for that time period, and drill through to see those individual, unaggregated records.

!Customizing your line chart
---------------------------

To customize your line chart, you can click on the **Settings**button in the bottom left. There are too many settings to cover here without boring you, so we’ll just give you some highlights.



Documentation Source:
www.metabase.com/learn/visualization/line-charts.md

Documentation Title:
Guide to line charts

Documentation Content:
What we talk about when we talk about line charts: time series, trend lines, alerts, and more.

How to create a line chart* Customizing your line chart
	+ Display tab
		Trend lines and goal linesLine, area, or bar chart?
	Axes tab
* Line chart tips
	Pair a line chart with a trend chartHover over a label to highlight a lineFor time series, filter out any time period still in progress
Further reading
Line charts are good for plotting data captured in a sequence, whether that sequence is the passage of time, or steps in a process or flow. These charts are typically used to plot a time series (also known as a run chart): a set of markers connected by lines, with the x axis showing the passage of time and the y axis plotting the value of a metric at each moment.

How to create a line chart
--------------------------

Let’s take a look at the `Orders`table in the Sample Databasethat ships with Metabase. From the main navigation bar, click on **+ New**> **Question**, which will take you to Metabase’s query builder. Choose **Raw Data**> **Sample Database**, then pick the `Orders`table. Click **Visualize**, then click the **Visualization button**in the bottom right to bring up the **Visualization sidebar**.

!Let’s start with how *not*to create a line chart. If you select **line chart**, Metabase will present you with an empty line chart.

!Metabase can’t read minds (yet), so it doesn’t know which columns from the `Orders`table to use for the x and y axes. To create a line chart, you’ll need to pick a metric for Metabase to plot over time. For example, you could show order totals over time by setting the x axis to `created_at`and the y axis to `total`. Metabase will automatically plot the line chart:

!That’s technically a line chart, but it looks more like the cardiograph of a startled hummingbird, and that’s even after Metabase has truncated the results shown. (If you hover over the gray warning triangle in the upper right, you’ll see that Metabase has only plotted 2,000 rows.)



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



