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
www.metabase.com/docs/v0.49/questions/sharing/visualizations/scatterplot-or-bubble-chart.md

Documentation Title:
Scatterplots and bubble charts

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
Scatterplots and bubble charts
==============================

**Scatterplots**are useful for visualizing the correlation between two variables, like comparing the age of your users vs. how many dollars they’ve spent on your products. To use a scatterplot, you’ll need to ask a question that results in two numeric columns, like `Count of Orders grouped by Customer Age`. Alternatively, you can use a raw data table and select the two numeric fields you want to use in the chart options.

If you have a third numeric field, you can also create a **bubble chart**. Select the Scatter visualization, then open up the chart settings and select a field in the **bubble size**dropdown. This field will be used to determine the size of each bubble on your chart. For example, you could use a field that contains the total dollar amount for each x-y pair — i.e. larger bubbles for larger total dollar amounts spent on orders.

Scatterplots and bubble charts also have similar chart options as line, bar, and area charts, including the option to display trend or goal lines.

!Read docs for other versions of Metabase.
 

Did this article help you?
 

Yes
 No
 Send
 Thanks for your feedback!

Want to improve these docs? Propose a change.##### Subscribe to our newsletter

Stay in touch with updates and news from Metabase. No spam, ever.



Documentation Source:
www.metabase.com/docs/v0.49/questions/sharing/visualizations/pie-or-donut-chart.md

Documentation Title:
Pie or donut charts

Documentation Content:
UpcomingMetabase for advanced usersRegister Now!×Product
 Use Cases!Self-service Analytics
 Business intelligence for everyone!Embedded Analytics
 Create seamless in-product analyticsMetabase Plans!Starter and Open Source
 Self-service BI in 5 minutes!Pro
 Advanced tools and controls!Enterprise
 White-glove treatmentPlatform!Data Sources!Security!Cloud!Professional Services
 NewWatch a 5-minute demoto see how to set up and publish a dashboard

!Features
 !Query builder
 Get answers in a few clicks!Drill-through
 Pull threads in your data!Usage analytics
 NewSee who did what, when!Analytics dashboards
 Share insights with anyone, anywhere!SQL editor
 For advanced data users!Sandboxing
 Set boundaries around your data!Models
 A starting point for questions!Permissions
 Keep your data secure and private!CSV upload
 Go beyond VLOOKUPNewMetabase 49:New tools for dashboard creators, data sharers, and more
 

DocumentationResources
 !Learn
 Guides on working with data!Blog
 News, updates, and ideas!Events
 Join a live event or watch on demand!Customers
 Real companies, real data, real stories!Discussion
 Share and connect with other users!Metabase Experts
 Find an expert partner!Community Stories
 Practical advice from our community!Startup Guide to Financial Modeling
 NewModeling financial data with Metabase!Community Data Stack Report
 NewSee how others work with dataRecent Blog Posts!Set up a basic pipeline for log analysisEmbed a Metabase dashboard in ZendeskKeeping tabs on embedded analyticsPricingLog inGet startedProductUse Cases!Self-service Analytics
 Business intelligence for everyone!Embedded Analytics
 Create seamless in-product analyticsMetabase Plans!Starter and Open Source!Pro!EnterprisePlatform!Data Sources!Security!Cloud!Professional Services
 NewFeatures!Query builder
 Get answers in a few clicks!Drill-through
 Pull threads in your data!Collections and verified items
 Keep things organized!Usage analytics
 NewSee who did what, when!Analytics dashboards
 Share insights with anyone,



