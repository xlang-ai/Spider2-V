Documentation Source:
superset.apache.org/docs/configuration/event-logging/index.md

Documentation Title:
Event Logging | Superset

Documentation Content:
Skip to main content!!DocumentationGetting StartedFAQCommunityResourcesGitHubSlackMailing ListStack OverflowGet StartedSearchIntroductionQuickstartInstallation* Configuration
	Configuring SupersetConnecting to DatabasesAlerts and ReportsCachingAsync Queries via CelerySQL TemplatingTimezonesNetwork and Security SettingsSetup SSH TunnelingEvent LoggingCountry Map ToolsImporting and Exporting Datasources
Using SupersetContributingSecurityFAQAPI
Edit this page on GitHubConfigurationEvent Logging
On this pageLogging
=======

Event Logging​
--------------

Superset by default logs special action events in its internal database (DBEventLogger). These logs can be accessed
on the UI by navigating to **Security > Action Log**. You can freely customize these logs by
implementing your own event log class.
**When custom log class is enabled DBEventLogger is disabled and logs
stop being populated in UI logs view.**To achieve both, custom log class should extend built-in DBEventLogger log class.

Here's an example of a simple JSON-to-stdout class:

`deflog(self,user_id,action,*args,**kwargs):records =kwargs.get('records',list())dashboard_id =kwargs.get('dashboard_id')slice_id =kwargs.get('slice_id')duration_ms =kwargs.get('duration_ms')referrer =kwargs.get('referrer')forrecord inrecords:log =dict(action=action,json=record,dashboard_id=dashboard_id,slice_id=slice_id,duration_ms=duration_ms,referrer=referrer,user_id=user_id)print(json.dumps(log))`End by updating your config to pass in an instance of the logger you want to use:

EVENT\_LOGGER = JSONStdOutEventLogger()StatsD Logging​
---------------

Superset can be configured to log events to StatsDif desired. Most endpoints hit are logged as
well as key events like query start and end in SQL Lab.

To setup StatsD logging, it’s a matter of configuring the logger in your `superset_config.py`.

`fromsuperset.stats_logger importStatsdStatsLoggerSTATS_LOGGER =StatsdStatsLogger(host='localhost',port=8125,prefix='superset')`Note that it’s also possible to implement your own logger by deriving
`superset.stats_logger.BaseStatsLogger`.



Documentation Source:
superset.apache.org/docs/configuration/alerts-reports/index.md

Documentation Title:
Alerts and Reports | Superset

Documentation Content:
Browse to your report from the worker​

The worker may be unable to reach the report. It will use the value of `WEBDRIVER_BASEURL`to browse to the report. If that route is invalid, or presents an authentication challenge that the worker can't pass, the report screenshot will fail.

Check this by attempting to `curl`the URL of a report that you see in the error logs of your worker. For instance, from the worker environment, run `curl http://superset_app:8088/superset/dashboard/1/`. You may get different responses depending on whether the dashboard exists - for example, you may need to change the `1`in that URL. If there's a URL in your logs from a failed report screenshot, that's a good place to start. The goal is to determine a valid value for `WEBDRIVER_BASEURL`and determine if an issue like HTTPS or authentication is redirecting your worker.

In a deployment with authentication measures enabled like HTTPS and Single Sign-On, it may make sense to have the worker navigate directly to the Superset application running in the same location, avoiding the need to sign in. For instance, you could use `WEBDRIVER_BASEURL="http://superset_app:8088"`for a docker compose deployment, and set `"force_https": False,`in your `TALISMAN_CONFIG`.

Scheduling Queries as Reports​
------------------------------

You can optionally allow your users to schedule queries directly in SQL Lab. This is done by adding
extra metadata to saved queries, which are then picked up by an external scheduled (like
Apache Airflow).

To allow scheduled queries, add the following to `SCHEDULED_QUERIES`in your configuration file:

`SCHEDULED_QUERIES ={# This information is collected when the user clicks "Schedule query",# and saved into the `extra` field of saved queries.# See: https://github.com/mozilla-services/react-jsonschema-form'JSONSCHEMA':{'title':'Schedule','description':('In order to schedule a query, you need to specify when it ''should start running, when it should stop running, and how ''often it should run. You can also optionally specify ''dependencies that should be met before the query is ''executed.



Documentation Source:
superset.apache.org/docs/configuration/alerts-reports/index.md

Documentation Title:
Alerts and Reports | Superset

Documentation Content:
Confirm feature flag is enabled and you have sufficient permissions​

If you don't see "Alerts & Reports" under the *Manage*section of the Settings dropdown in the Superset UI, you need to enable the `ALERT_REPORTS`feature flag (see above). Enable another feature flag and check to see that it took effect, to verify that your config file is getting loaded.

Log in as an admin user to ensure you have adequate permissions.



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



