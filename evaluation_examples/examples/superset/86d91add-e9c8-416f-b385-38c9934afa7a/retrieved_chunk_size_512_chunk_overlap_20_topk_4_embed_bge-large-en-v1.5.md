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
Enabling Data Upload Functionality​

You may need to enable the functionality to upload a CSV or Excel file to your database. The following section
explains how to enable this functionality for the examples database.

In the top menu, select **Data ‣ Databases**. Find the **examples**database in the list and
select the **Edit**button.

!In the resulting modal window, switch to the **Extra**tab and
tick the checkbox for **Allow Data Upload**. End by clicking the **Save**button.

!### Loading CSV Data​

Download the CSV dataset to your computer from
GitHub.
In the Superset menu, select **Data ‣ Upload a CSV**.

!Then, enter the **Table Name**as *tutorial\_flights*and select the CSV file from your computer.

!Next enter the text *Travel Date*into the **Parse Dates**field.

!Leaving all the other options in their default settings, select **Save**at the bottom of the page.



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
superset.apache.org/docs/using-superset/creating-your-first-dashboard/index.md

Documentation Title:
Creating Your First Dashboard | Superset

Documentation Content:
Registering a new table​

Now that you’ve configured a data source, you can select specific tables (called **Datasets**in Superset)
that you want exposed in Superset for querying.

Navigate to **Data ‣ Datasets**and select the **+ Dataset**button in the top right corner.

!A modal window should pop up in front of you. Select your **Database**,
**Schema**, and **Table**using the drop downs that appear. In the following example,
we register the **cleaned\_sales\_data**table from the **examples**database.

!To finish, click the **Add**button in the bottom right corner. You should now see your dataset in the list of datasets.



