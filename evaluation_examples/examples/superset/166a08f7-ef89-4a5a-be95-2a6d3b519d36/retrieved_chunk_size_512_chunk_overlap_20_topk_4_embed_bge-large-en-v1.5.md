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
superset.apache.org/docs/configuration/indexf8a0.md

Documentation Title:
Index of /docs/configuration

Documentation Content:
html/ 2024-04-24 21:23 | - |
|!timezones.htm/ 2024-04-24 21:23 | - |
|!timezones.html/ 2024-04-24 21:23 | - |
|!databases.htm/ 2024-05-01 01:36 | - |
|!databases.html/ 2024-05-01 01:36 | - |
|!alerts-reports/ 2024-05-06 16:58 | - |
|!async-queries-celery/ 2024-05-06 16:58 | - |
|!cache/ 2024-05-06 16:58 | - |
|!configuring-superset/ 2024-05-06 16:58 | - |
|!country-map-tools/ 2024-05-06 16:58 | - |
|!databases/ 2024-05-06 16:58 | - |
|!event-logging/ 2024-05-06 16:58 | - |
|!importing-exporting-datasources/ 2024-05-06 16:58 | - |
|!networking-settings/ 2024-05-06 16:58 | - |
|!setup-ssh-tunneling/ 2024-05-06 16:58 | - |
|!sql-templating/ 2024-05-06 16:58 | - |
|!timezones/ 2024-05-06 16:58 | - |



Documentation Source:
superset.apache.org/docs/configuration/event-logging/index.md

Documentation Title:
Event Logging | Superset

Documentation Content:
Edit this pagePreviousSetup SSH TunnelingNextCountry Map ToolsEvent LoggingStatsD LoggingWe use  !Copyright © 2024,
 The Apache Software Foundation,
 Licensed under the Apache License.

Apache Superset, Apache, Superset, the Superset logo, and the Apache feather logo are either registered trademarks or trademarks of The Apache Software Foundation. All other products or name brands are trademarks of their respective holders, including The Apache Software Foundation.
 Apache Software Foundationresources!Security| 
 Donate| 
 Thanks| 
 Events| 
 License| 
 Privacy!



