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



Documentation Source:
superset.apache.org/docs/using-superset/exploring-data/index.md

Documentation Title:
Exploring Data in Superset | Superset

Documentation Content:
Pivot Table​

In this section, we will extend our analysis using a more complex visualization, Pivot Table. By the
end of this section, you will have created a table that shows the monthly spend on flights for the
first six months, by department, by travel class.

Create a new chart by selecting **+ ‣ Chart**from the top right corner. Choose
tutorial\_flights again as a datasource, then click on the visualization type to get to the
visualization menu. Select the **Pivot Table**visualization (you can filter by entering text in the
search box) and then **Create New Chart**.

!In the **Time**section, keep the Time Column as Travel Date (this is selected automatically as we
only have one time column in our dataset). Then select Time Grain to be month as having daily data
would be too granular to see patterns from. Then select the time range to be the first six months of
2011 by click on Last week in the Time Range section, then in Custom selecting a Start / end of 1st
January 2011 and 30th June 2011 respectively by either entering directly the dates or using the
calendar widget (by selecting the month name and then the year, you can move more quickly to far
away dates).

!Next, within the **Query**section, remove the default COUNT(\*) and add Cost, keeping the default
SUM aggregate. Note that Apache Superset will indicate the type of the metric by the symbol on the
left hand column of the list (ABC for string, # for number, a clock face for time, etc.).

In **Group by**select **Time**: this will automatically use the Time Column and Time Grain
selections we defined in the Time section.

Within **Columns**, select first Department and then Travel Class. All set – let’s **Run Query**to
see some data!

!You should see months in the rows and Department and Travel Class in the columns. Publish this chart
to your existing Tutorial Dashboard you created earlier.



Documentation Source:
superset.apache.org/docs/using-superset/exploring-data/index.md

Documentation Title:
Exploring Data in Superset | Superset

Documentation Content:
Table Visualization​

You should now see *tutorial\_flights*as a dataset in the **Datasets**tab. Click on the entry to
launch an Explore workflow using this dataset.

In this section, we'll create a table visualization
to show the number of flights and cost per travel class.

By default, Apache Superset only shows the last week of data. In our example, we want to visualize all
of the data in the dataset. Click the **Time ‣ Time Range**section and change
the **Range Type**to **No Filter**.

!Click **Apply**to save.

Now, we want to specify the rows in our table by using the **Group by**option. Since in this
example, we want to understand different Travel Classes, we select **Travel Class**in this menu.

Next, we can specify the metrics we would like to see in our table with the **Metrics**option.

* `COUNT(*)`, which represents the number of rows in the table
(in this case, quantity of flights in each Travel Class)
* `SUM(Cost)`, which represents the total cost spent by each Travel Class

!Finally, select **Run Query**to see the results of the table.

!To save the visualization, click on **Save**in the top left of the screen. In the following modal,

* Select the **Save as**option and enter the chart name as Tutorial Table (you will be able to find it again through the
**Charts**screen, accessible in the top menu).
* Select **Add To Dashboard**and enter
Tutorial Dashboard. Finally, select **Save & Go To Dashboard**.

!### Dashboard Basics​

Next, we are going to explore the dashboard interface. If you’ve followed the previous section, you
should already have the dashboard open. Otherwise, you can navigate to the dashboard by selecting
Dashboards on the top menu, then Tutorial dashboard from the list of dashboards.

On this dashboard you should see the table you created in the previous section. Select **Edit
dashboard**and then hover over the table. By selecting the bottom right hand corner of the table
(the cursor will change too), you can resize it by dragging and dropping.

!Finally, save your changes by selecting Save changes in the top right.



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



