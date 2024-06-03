Documentation Source:
superset.apache.org/docs/using-superset/creating-your-first-dashboard/index.md

Documentation Title:
Creating Your First Dashboard | Superset

Documentation Content:
As you customize your chart using drop-down menus, make sure to click the **Run**button
to get visual feedback.

!In the following screenshot, we craft a grouped Time-series Bar Chart to visualize
our quarterly sales data by product line just by clicking options in drop-down menus.

!### Creating a slice and dashboard​

To save your chart, first click the **Save**button. You can either:

* Save your chart and add it to an existing dashboard
* Save your chart and add it to a new dashboard

In the following screenshot, we save the chart to a new "Superset Duper Sales Dashboard":

!To publish, click **Save and goto Dashboard**.

Behind the scenes, Superset will create a slice and store all the information needed
to create your chart in its thin data layer
(the query, chart type, options selected, name, etc).

!To resize the chart, start by clicking the Edit Dashboard button in the top right corner.

!Then, click and drag the bottom right corner of the chart until the chart layout snaps
into a position you like onto the underlying grid.

!Click **Save**to persist the changes.

Congrats! You’ve successfully linked, analyzed, and visualized data in Superset. There are a wealth
of other table configuration and visualization options, so please start exploring and creating
slices and dashboards of your own

ֿ



Documentation Source:
superset.apache.org/docs/using-superset/exploring-data/index.md

Documentation Title:
Exploring Data in Superset | Superset

Documentation Content:
Line Chart​

In this section, we are going to create a line chart to understand the average price of a ticket by
month across the entire dataset.

In the Time section, as before, keep the Time Column as Travel Date and Time Grain as month but this
time for the Time range select No filter as we want to look at entire dataset.

Within Metrics, remove the default `COUNT(*)`metric and instead add `AVG(Cost)`, to show the mean value.

!Next, select **Run Query**to show the data on the chart.

How does this look? Well, we can see that the average cost goes up in December. However, perhaps it
doesn’t make sense to combine both single and return tickets, but rather show two separate lines for
each ticket type.

Let’s do this by selecting Ticket Single or Return in the Group by box, and the selecting **Run
Query**again. Nice! We can see that on average single tickets are cheaper than returns and that the
big spike in December is caused by return tickets.

Our chart is looking pretty good already, but let’s customize some more by going to the Customize
tab on the left hand pane. Within this pane, try changing the Color Scheme, removing the range
filter by selecting No in the Show Range Filter drop down and adding some labels using X Axis Label
and Y Axis Label.

!Once you’re done, publish the chart in your Tutorial Dashboard.



Documentation Source:
superset.apache.org/docs/using-superset/exploring-data/index.md

Documentation Title:
Exploring Data in Superset | Superset

Documentation Content:
Time Comparison​

In this section, we will compare values in our time series to the value a week before. Start off by
opening the Tutorial Advanced Analytics Base chart, by going to **Charts**in the top menu and then
selecting the visualization name in the list (alternatively, find the chart in the Tutorial
Dashboard and select Explore chart from the menu for that visualization).

Next, in the Time Comparison subsection of **Advanced Analytics**, enter the Time Shift by typing in
“minus 1 week” (note this box accepts input in natural language). Run Query to see the new chart,
which has an additional series with the same values, shifted a week back in time.

!Then, change the **Calculation type**to Absolute difference and select **Run Query**. We can now
see only one series again, this time showing the difference between the two series we saw
previously.

!Save the chart as Tutorial Time Comparison and add it to the Tutorial Dashboard.



Documentation Source:
superset.apache.org/docs/using-superset/exploring-data/index.md

Documentation Title:
Exploring Data in Superset | Superset

Documentation Content:
Resampling the data​

In this section, we’ll resample the data so that rather than having daily data we have weekly data.
As in the previous section, reopen the Tutorial Advanced Analytics Base chart.

Next, in the Python Functions subsection of **Advanced Analytics**, enter 7D, corresponding to seven
days, in the Rule and median as the Method and show the chart by selecting **Run Query**.

!Note that now we have a single data point every 7 days. In our case, the value showed corresponds to
the median value within the seven daily data points. For more information on the meaning of the
various options in this section, refer to the
Pandas documentation.

Lastly, save your chart as Tutorial Resample and add it to the Tutorial Dashboard. Go to the
tutorial dashboard to see the four charts side by side and compare the different outputs.

Edit this pagePreviousCreating Your First DashboardNextIssue Codes- Exploring Data in Superset
	Enabling Data Upload FunctionalityLoading CSV DataTable VisualizationDashboard BasicsPivot TableLine ChartMarkupPublishing Your DashboardAnnotationsAdvanced AnalyticsRolling MeanTime ComparisonResampling the data
We use  !Copyright © 2024,
 The Apache Software Foundation,
 Licensed under the Apache License.

Apache Superset, Apache, Superset, the Superset logo, and the Apache feather logo are either registered trademarks or trademarks of The Apache Software Foundation. All other products or name brands are trademarks of their respective holders, including The Apache Software Foundation.
 Apache Software Foundationresources!Security| 
 Donate| 
 Thanks| 
 Events| 
 License| 
 Privacy!



