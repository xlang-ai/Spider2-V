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
Otherwise, select **OK**and finally **Save**to save your chart. If you keep
the default selection to overwrite the chart, your annotation will be saved to the chart and also
appear automatically in the Tutorial Dashboard.



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



