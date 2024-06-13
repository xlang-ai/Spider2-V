Documentation Source:
www.metabase.com/learn/visualization/line-charts.md

Documentation Title:
Guide to line charts

Documentation Content:
Trend lines and goal lines

You can add a trend linefrom the display settings of a time series chart. You’ll see the toggle if you’ve chosen exactly one time field from **Summarize**> **Group by**. In the example below, we’ve chosen the grouping field “Created At: Month”:

!You can also add a goal line to plot a horizontal line at your goal value. Goal lines are especially useful when paired with alerts. For example, if you’re monitoring sales, and you only want to get notified if a metric dips below a certain threshold, you can add a goal line to specify that threshold and get an email or have a Slack message sent when the line goes under it.



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
www.metabase.com/learn/visualization/bar-charts.md

Documentation Title:
Master the bar chart visualization

Documentation Content:
Add a goal line

This specifies where you want the values to be. Metabase can alertyou when the values exceed (or drop below) that goal. For example, you can add a goal line at 5500 and name it ‘Arbitrary Sales Goal’.



