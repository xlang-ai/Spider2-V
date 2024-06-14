Documentation Source:
airbyte.com/docs.airbyte.com/using-airbyte/core-concepts/sync-schedules.md

Documentation Title:
Sync Schedules | Airbyte Documentation

Documentation Content:
Skip to main content!!About AirbyteTutorialsSupportCloud StatusTry Airbyte CloudSearch* Airbyte Connectors
Connector CatalogBuild a ConnectorConnector Support Levels* Using Airbyte
Getting Started* Configuring Connections
	Sync SchedulesNamespacesSync ModesTyping and DedupingSchema Change ManagementTransformations
Managing Syncs* Managing Airbyte
Deploy AirbyteSelf-Managed EnterpriseUpgrading AirbyteConfiguring AirbyteAccess ManagementAirbyte at ScaleSecurityIntegrating with AirbyteAccount Management* Developer Guides
API documentationTerraform DocumentationUsing PyAirbyteUnderstand AirbyteContribute to AirbyteLicenses* Community
Getting SupportCode of Conduct* Product Updates
RoadmapRelease Notes
Configuring ConnectionsSync Schedules
On this pageSync Schedules
==============

AvailableCloud AvailableSelf-Managed Community (OSS)AvailableSelf-Managed EnterpriseFor each connection, you can select between three options that allow a sync to run. The three options for `Schedule Type`are:

* Scheduled (e.g. every 24 hours, every 2 hours)
* Cron
* Manual

Sync Considerations​
--------------------

* Only one sync per connection can run at a time.
* If a sync is scheduled to run before the previous sync finishes, the scheduled sync will start after the completion of the previous sync.
* Syncs can run at most every 60 minutes in Airbyte Cloud. Reach out to Salesif you require replication more frequently than once per hour.

noteFor Scheduled or cron scheduled syncs, Airbyte guarantees syncs will initiate with a schedule accuracy of +/- 30 minutes.

Scheduled syncs​
----------------

You can choose between the following scheduled options:

* Every 24 hours (most common)
* Every 12 hours
* Every 8 hours
* Every 6 hours
* Every 3 hours
* Every 2 hours
* Every 1 hour

When a scheduled connection is first created, a sync is executed immediately after creation. After that, a sync is run once the time since the last sync (whether it was triggered manually or due to a schedule) has exceeded the schedule interval. For example:

* **October 1st, 2pm**, a user sets up a connection to sync data every 24 hours.



Documentation Source:
airbyte.com/docs.airbyte.com/using-airbyte/core-concepts/sync-schedules.md

Documentation Title:
Sync Schedules | Airbyte Documentation

Documentation Content:
* **October 1st, 2:01pm**: sync job runs
* **October 2nd, 2:01pm:**24 hours have passed since the last sync, so a sync is triggered.
* **October 2nd, 5pm**: The user manually triggers a sync from the UI
* **October 3rd, 2:01pm:**since the last sync was less than 24 hours ago, no sync is run
* **October 3rd, 5:01pm:**It has been more than 24 hours since the last sync, so a sync is run

Cron Syncs​
-----------

If you prefer more precision in scheduling your sync, you can also use CRON scheduling to set a specific time of day or month.

Airbyte uses the CRON scheduler from Quartz. We recommend reading their documentationto understand the required formatting. You can also refer to these examples:



| Cron string | Sync Timing |
| --- | --- |
| 0 0 \* \* \* ? | Every hour, at 0 minutes past the hour |
| --- | --- |
| 0 0 15 \* \* ? | At 15:00 every day |
| 0 0 15 \* \* MON,TUE | At 15:00, only on Monday and Tuesday |
| 0 0 0,2,4,6 \* \* ? | At 12:00 AM, 02:00 AM, 04:00 AM and 06:00 AM every day |
| 0 0 \_/15 \_ \* ? | At 0 minutes past the hour, every 15 hours |

When setting up the cron expression, you will also be asked to choose a time zone the sync will run in.

Manual Syncs​
-------------

When the connection is set to replicate with `Manual`frequency, the sync will not automatically run.

It can be triggered by clicking the "Sync Now" button at any time through the UI or be triggered through the API.

Edit this pagePreviousConfiguring ConnectionsNextNamespacesSync ConsiderationsScheduled syncsCron SyncsManual Syncs
Was this page helpful?YesNo



Documentation Source:
airbyte.com/docs.airbyte.com/integrations/sources/faker.md

Documentation Title:
Faker | Airbyte Documentation

Documentation Content:
| Feature | Supported?(Yes/No) | Notes |
| --- | --- | --- |
| Full Refresh Sync | Yes |
| --- | --- |
| Incremental Sync | Yes |
| Namespaces | No |

Of note, if you choose `Incremental Sync`, state will be maintained between syncs, and once you hit
`count`records, no new records will be added.

You can choose a specific `seed`(integer) as an option for this connector which will guarantee that
the same fake records are generated each time. Otherwise, random data will be created on each
subsequent sync.



Documentation Source:
airbyte.com/tutorials/how-to-use-airflow-and-airbyte-together.md

Documentation Title:
A step-by-step guide to setting up and configuring Airbyte and Airflow to work together | Airbyte

Documentation Content:
By default the path that you specify will be located inside **/tmp/airbyte\_local**. In this tutorial I set the destination to **/json\_from\_faker**, which means that the data will be copied to**/tmp/airbyte\_local/json\_from\_faker**on the localhost where Airbyte is running. After specifying the Destination Path, click on Set up destination. 

!

Configure the Local JSON destination

‍

This will take you to a page to set up the connection. Set the replication frequency to **Manual**(since we will use Airflow to trigger Airbyte syncs rather than using Airbyte’s scheduler) and then click on **Set up connection**as highlighted in the image below.

!

Specify connection settings

‍

Trigger a sync from the **Sample Data (faker)**source to the **Local JSON**output by clicking on **Sync now**as highlighted in the image below.

!

Manually trigger a sync from the UI

‍

The sync should take a few seconds, at which point you should see that the sync has succeed as shown below.

!

After the sync has completed

‍

You can now confirm if some sample data has been copied to the expected location. As previously mentioned, for this example the JSON data can be seen in **/tmp/airbyte\_local\_json\_from\_faker**. Because there were three streams generated, the following three JSON files should be available: 

`_airbyte_raw_products.jsonl 
_airbyte_raw_users.jsonl
_airbyte_raw_purchases.jsonl`You have now created a simple example connection in Airbyte which can be manually triggered. A manually triggered connection is ideal for situations where you wish to use an external orchestrator. 

In the next section you will see how to trigger a manual sync on this connection by hitting a REST endpoint directly. After that, you will see how Airflow can be used to hit that same endpoint to trigger synchronizations. 

Test the API endpoints with cURL
--------------------------------

Before using the REST endpoint from within Airflow, it is useful to verify that it is working as expected.



