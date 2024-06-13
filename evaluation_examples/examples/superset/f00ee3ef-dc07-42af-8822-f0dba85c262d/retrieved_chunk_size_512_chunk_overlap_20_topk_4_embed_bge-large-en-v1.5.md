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
superset.apache.org/docs/using-superset/creating-your-first-dashboard/index.md

Documentation Title:
Creating Your First Dashboard | Superset

Documentation Content:
Customizing column properties​

Now that you've registered your dataset, you can configure column properties
for how the column should be treated in the Explore workflow:

* Is the column temporal? (should it be used for slicing & dicing in time series charts?)
* Should the column be filterable?
* Is the column dimensional?
* If it's a datetime column, how should Superset parse
the datetime format? (using the ISO-8601 string pattern)

!### Superset semantic layer​

Superset has a thin semantic layer that adds many quality of life improvements for analysts.
The Superset semantic layer can store 2 types of computed data:

- Virtual metrics: you can write SQL queries that aggregate values
from multiple column (e.g. `SUM(recovered) / SUM(confirmed)`) and make them
available as columns for (e.g. `recovery_rate`) visualization in Explore.
Aggregate functions are allowed and encouraged for metrics.
!You can also certify metrics if you'd like for your team in this view.

- Virtual calculated columns: you can write SQL queries that
customize the appearance and behavior
of a specific column (e.g. `CAST(recovery_rate) as float`).
Aggregate functions aren't allowed in calculated columns.
!### Creating charts in Explore view​

Superset has 2 main interfaces for exploring data:

* **Explore**: no-code viz builder. Select your dataset, select the chart,
customize the appearance, and publish.
* **SQL Lab**: SQL IDE for cleaning, joining, and preparing data for Explore workflow

We'll focus on the Explore view for creating charts right now.
To start the Explore workflow from the **Datasets**tab, start by clicking the name
of the dataset that will be powering your chart.

!You're now presented with a powerful workflow for exploring data and iterating on charts.

* The **Dataset**view on the left-hand side has a list of columns and metrics,
scoped to the current dataset you selected.
* The **Data**preview below the chart area also gives you helpful data context.
* Using the **Data**tab and **Customize**tabs, you can change the visualization type,
select the temporal column, select the metric to group by, and customize
the aesthetics of the chart.



Documentation Source:
superset.apache.org/docs/configuration/sql-templating/index.md

Documentation Title:
SQL Templating | Superset

Documentation Content:
Once you have the ID you can query it as if it were a table:

SELECT \* FROM {{ dataset(42) }} LIMIT 10If you want to select the metric definitions as well, in addition to the columns, you need to pass an additional keyword argument:

SELECT \* FROM {{ dataset(42, include\_metrics=True) }} LIMIT 10Since metrics are aggregations, the resulting SQL expression will be grouped by all non-metric columns. You can specify a subset of columns to group by instead:

SELECT \* FROM {{ dataset(42, include\_metrics=True, columns=["ds", "category"]) }} LIMIT 10**Metrics**The `{{ metric('metric_key', dataset_id) }}`macro can be used to retrieve the metric SQL syntax from a dataset. This can be useful for different purposes:

* Override the metric label in the chart level
* Combine multiple metrics in a calculation
* Retrieve a metric syntax in SQL lab
* Re-use metrics across datasets

This macro avoids copy/paste, allowing users to centralize the metric definition in the dataset layer.

The `dataset_id`parameter is optional, and if not provided Superset will use the current dataset from context (for example, when using this macro in the Chart Builder, by default the `macro_key`will be searched in the dataset powering the chart).
The parameter can be used in SQL Lab, or when fetching a metric from another dataset.

Edit this pagePreviousAsync Queries via CeleryNextTimezonesJinja TemplatesAvailable MacrosWe use  !Copyright © 2024,
 The Apache Software Foundation,
 Licensed under the Apache License.

Apache Superset, Apache, Superset, the Superset logo, and the Apache feather logo are either registered trademarks or trademarks of The Apache Software Foundation. All other products or name brands are trademarks of their respective holders, including The Apache Software Foundation.
 Apache Software Foundationresources!Security| 
 Donate| 
 Thanks| 
 Events| 
 License| 
 Privacy!



