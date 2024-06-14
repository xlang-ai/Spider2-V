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



Documentation Source:
superset.apache.org/docs/using-superset/exploring-data/index.md

Documentation Title:
Exploring Data in Superset | Superset

Documentation Content:
Publishing Your Dashboard​

If you have followed all of the steps outlined in the previous section, you should have a dashboard
that looks like the below. If you would like, you can rearrange the elements of the dashboard by
selecting **Edit dashboard**and dragging and dropping.

If you would like to make your dashboard available to other users, simply select Draft next to the
title of your dashboard on the top left to change your dashboard to be in Published state. You can
also favorite this dashboard by selecting the star.

!### Annotations​

Annotations allow you to add additional context to your chart. In this section, we will add an
annotation to the Tutorial Line Chart we made in a previous section. Specifically, we will add the
dates when some flights were cancelled by the UK’s Civil Aviation Authority in response to the
eruption of the Grímsvötn volcano in Iceland (23-25 May 2011).

First, add an annotation layer by navigating to Manage ‣ Annotation Layers. Add a new annotation
layer by selecting the green plus sign to add a new record. Enter the name Volcanic Eruptions and
save. We can use this layer to refer to a number of different annotations.

Next, add an annotation by navigating to Manage ‣ Annotations and then create a new annotation by
selecting the green plus sign. Then, select the Volcanic Eruptions layer, add a short description
Grímsvötn and the eruption dates (23-25 May 2011) before finally saving.

!Then, navigate to the line chart by going to Charts then selecting Tutorial Line Chart from the
list. Next, go to the Annotations and Layers section and select Add Annotation Layer. Within this
dialogue:

* Name the layer as Volcanic Eruptions
* Change the Annotation Layer Type to Event
* Set the Annotation Source as Superset annotation
* Specify the Annotation Layer as Volcanic Eruptions

!Select **Apply**to see your annotation shown on the chart.

!If you wish, you can change how your annotation looks by changing the settings in the Display
configuration section. Otherwise, select **OK**and finally **Save**to save your chart.



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
superset.apache.org/docs/using-superset/exploring-data/index.md

Documentation Title:
Exploring Data in Superset | Superset

Documentation Content:
Otherwise, select **OK**and finally **Save**to save your chart. If you keep
the default selection to overwrite the chart, your annotation will be saved to the chart and also
appear automatically in the Tutorial Dashboard.



