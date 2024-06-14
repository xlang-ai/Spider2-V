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
www.metabase.com/docs/v0.49/questions/sharing/visualizing-results.md

Documentation Title:
Visualizing data

Documentation Content:
!Tables
------

The Tableoption is good for looking at tabular data (duh), or for lists of things like users or orders.

!Pivot tables
------------

Pivot tablesallow you swap rows and columns, group data, and include subtotals in your table. You can group one or more metrics by one or more dimensions.

!Line charts
-----------

Line chartsare best for displaying the trend of a number over time, especially when you have lots of x-axis values. For more, check out our Guide to line chartsand Time series analysistutorials.

!Bar charts
----------

Bar chartsare great for displaying a number grouped by a category (e.g., the number of users you have by country).

!Area charts
-----------

Area chartsare useful when comparing the proportions of two metrics over time. Both bar and area charts can be stacked.

!Combo charts
------------

Combo chartslet you combine bars and lines (or areas) on the same chart.

!Histograms
----------

If you have a bar chart like Count of Users by Age, where the x-axis is a number, you’ll get a special kind of bar chart called a histogramwhere each bar represents a range of values (called a “bin”).

!Row charts
----------

Row chartsare good for visualizing data grouped by a column that has a lot of possible values, like a Vendor or Product Title field.

!Waterfall charts
----------------

Waterfall chartsare a kind of bar chart useful for visualizing results that contain both positive and negative values.

!Scatterplots and bubble charts
------------------------------

Scatterplotsare useful for visualizing the correlation between two variables, like comparing the age of your people using your app vs. how many dollars they’ve spent on your products.

!Pie chart or donut charts
-------------------------

A pie chart or donut chartcan be used when breaking out a metric by a single dimension, especially when the number of possible breakouts is small, like users by gender.

!Funnel charts
-------------

Funnelsare commonly used in e-commerce or sales to visualize how many customers are present within each step of a checkout flow or sales cycle. At their most general, funnels show you values broken out by steps, and the percent decrease between each successive step.



Documentation Source:
www.metabase.com/docs/v0.49/questions/sharing/visualizations/pie-or-donut-chart.md

Documentation Title:
Pie or donut charts

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
Pie or donut charts
===================

A **pie or donut chart**can be used when breaking out a metric by a single dimension, especially when the number of possible breakouts is small, like users by gender. If you have more than a few breakouts, like users per country, it’s usually better to use a bar chart so that your users can more easily compare the relative sizes of each bar.

The options for pie charts let you choose which field to use as your measurement, and which one to use for the dimension (i.e. the pie slices). You can also customize the color of each slice, the pie chart’s legend, whether or not to show each slice’s percent of the whole in the legend, and the minimum size a slice needs to be in order for Metabase to display it.

!Read docs for other versions of Metabase.
 

Did this article help you?
 

Yes
 No
 Send
 Thanks for your feedback!

Want to improve these docs? Propose a change.##### Subscribe to our newsletter

Stay in touch with updates and news from Metabase. No spam, ever.



Documentation Source:
www.metabase.com/docs/v0.49/troubleshooting-guide/visualization.md

Documentation Title:
Troubleshooting question and dashboard visualizations

Documentation Content:
when!Analytics dashboards
 Share insights with anyone, anywhere!SQL editor
 For advanced data users!Sandboxing
 Set boundaries around your data!Models
 A starting point for questions!Permissions
 Keep your data secure and private!CSV upload
 Go beyond VLOOKUPDocumentationResources!Learn!Blog!Events!Customers!Discussion!Partners!Community Stories!Startup Guide to Financial Modeling
 New!Community Data Stack Report
 NewPricingLog inv0.49Troubleshooting Guide
Troubleshooting question and dashboard visualizations
=====================================================

To start, check if your current browser settings are compatible with Metabase:

1. Clear your browser cache, and refresh your page.
2. Disable all extensions and plugins. Load the page again.
3. Give it one last shot—try opening your page in a private/incognito session, or a different browser.

Formatting dashboard cards
--------------------------

1. Make sure that you’re making and saving changes from the card’s settings(*not*the original question’s settings).
2. Reset your card’s visualization settings.

**Explanation**The visualization settings on a card are independent of the settings on the original question. When you first create a question, your selected visualization type is saved along with the query. When you add that question to a dashboard, the dashboard will display the same visualization as the original question by default. You can override the original visualization type by using the card’s visualization settings.

Visualizing SQL questions
-------------------------

Go to your SQL question and change the visualization typeto a table. Then, check if any of the following situations apply to the raw query results:

* Aggregations (counts, sums, etc.) are wrong.
* Results have duplicated rows.
* Results are missing rows.

**Explanation**If your question or dashboard card is powered by a handwritten SQL queryrather than the query builder, your visualization is going to be more sensitive to changes in the underlying data (for example, renamed fields, or the sudden appearance of a wild null value). To learn more, read about Common reasons for unexpected query results.

If you’re having problems with things like SQL syntax errors or SQL variables, see Troubleshooting SQL questionsfor more help.

Related problems
----------------

* My dates and times are wrong.



