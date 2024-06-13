Documentation Source:
superset.apache.org/docs/using-superset/creating-your-first-dashboard/index.md

Documentation Title:
Creating Your First Dashboard | Superset

Documentation Content:
Manage access to Dashboards​

Access to dashboards is managed via owners (users that have edit permissions to the dashboard)

Non-owner users access can be managed two different ways:

1. Dataset permissions - if you add to the relevant role permissions to datasets it automatically grants implicit access to all dashboards that uses those permitted datasets
2. Dashboard roles - if you enable **DASHBOARD\_RBAC**feature flagthen you be able to manage which roles can access the dashboard
	* Granting a role access to a dashboard will bypass dataset level checks. Having dashboard access implicitly grants read access to all the featured charts in the dashboard, and thereby also all the associated datasets.
	* If no roles are specified for a dashboard, regular **Dataset permissions**will apply.

!### Customizing dashboard​

The following URL parameters can be used to modify how the dashboard is rendered:

* `standalone`:
	+ `0`(default): dashboard is displayed normally
	+ `1`: Top Navigation is hidden
	+ `2`: Top Navigation + title is hidden
	+ `3`: Top Navigation + title + top level tabs are hidden
* `show_filters`:
	+ `0`: render dashboard without Filter Bar
	+ `1`(default): render dashboard with Filter Bar if native filters are enabled
* `expand_filters`:
	+ (default): render dashboard with Filter Bar expanded if there are native filters
	+ `0`: render dashboard with Filter Bar collapsed
	+ `1`: render dashboard with Filter Bar expanded

For example, when running the local development build, the following will disable the
Top Nav and remove the Filter Bar:
`http://localhost:8088/superset/dashboard/my-dashboard/?standalone=1&show_filters=0`

Edit this pagePreviousImporting and Exporting DatasourcesNextExploring Data in Superset- Creating Your First Dashboard
	Connecting to a new databaseRegistering a new tableCustomizing column propertiesSuperset semantic layerCreating charts in Explore viewCreating a slice and dashboardManage access to DashboardsCustomizing dashboard
We use  !Copyright © 2024,
 The Apache Software Foundation,
 Licensed under the Apache License.

Apache Superset, Apache, Superset, the Superset logo, and the Apache feather logo are either registered trademarks or trademarks of The Apache Software Foundation.



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
Markup​

In this section, we will add some text to our dashboard. If you’re there already, you can navigate
to the dashboard by selecting Dashboards on the top menu, then Tutorial dashboard from the list of
dashboards. Got into edit mode by selecting **Edit dashboard**.

Within the Insert components pane, drag and drop a Markdown box on the dashboard. Look for the blue
lines which indicate the anchor where the box will go.

!Now, to edit the text, select the box. You can enter text, in markdown format (see
this Markdown Cheatsheetfor
more information about this format). You can toggle between Edit and Preview using the menu on the
top of the box.

!To exit, select any other part of the dashboard. Finally, don’t forget to keep your changes using
**Save changes**.



Documentation Source:
superset.apache.org/docs/creating-charts-dashboards/indexad3f.md

Documentation Title:
Index of /docs/creating-charts-dashboards

Documentation Content:
Index of /docs/creating-charts-dashboards
=========================================



|!NameLast modifiedSizeDescription
|  |
|!Parent Directory - |
|!first-dashboard/ 2024-04-24 21:23 | - |
|!exploring-data/ 2024-04-28 01:04 | - |
|!creating-your-first-dashboard/ 2024-04-28 01:04 | - |



