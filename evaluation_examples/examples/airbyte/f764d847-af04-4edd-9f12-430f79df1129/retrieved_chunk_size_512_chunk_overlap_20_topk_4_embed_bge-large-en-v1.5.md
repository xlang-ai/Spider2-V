Documentation Source:
airbyte.com/docs.airbyte.com/operator-guides/browsing-output-logs.md

Documentation Title:
Browsing logs | Airbyte Documentation

Documentation Content:
You can also access the link to a sync job from the in-app log viewer.

Download the logs​
------------------

To download a copy of the logs locally, select the three grey dots next to a sync and select `Download logs`.

You can also access the download log button from the in-app log viewer.

noteIf a sync was completed across multiple attempts, downloading the logs will union all the logs for all attempts for that job.

Exploring Local Logs​
---------------------

Open SourceonlyThe following documentation only applies to Open Source.### Establish the folder directory​

In the UI, you can discover the Attempt ID within the sync job. Most jobs will complete in the first attempt, so your folder directory will look like `/tmp/workspace/9/0`. If you sync job completes in multiple attempts, you'll need to define which attempt you're interested in, and note this. For example, for the third attempt, it will look like `/tmp/workspace/9/2/`.



Documentation Source:
airbyte.com/docs.airbyte.com/using-airbyte/getting-started/set-up-a-connection.md

Documentation Title:
Set up a Connection | Airbyte Documentation

Documentation Content:
You can also select a cursor or primary key to enable incremental and/or deduplication. For more information on the nature of each sync mode supported by Airbyte, see this page.

You can also select individual fields to sync on this page. Expand the fields available by clicking any stream. This is helpful when you have security concerns or don't want to sync all the data from the source.
!

Click **Next**to complete your stream setup and move to the connection configuration. This is where you'll set up how often your data will sync and where it will live in the destination. For this demo, we'll set the connection to run at 8 AM every day and sync the connection to a custom namespace with a stream prefix.

noteTo ensure your data is synced to the correct place, see our examples for Destination Namespace

Once you've set up all the connection settings, click "Set up connection". You've successfully set up your first data pipeline with Airbyte. Your first sync is about to begin!

Connection Overview​
--------------------

Once you've finished setting up the connection, you will be automatically redirected to a connection overview containing all the tools you need to keep track of your connection.

!Here's a basic overview of the tabs and their use:

1. The **Status**tab shows you an overview of your connector's sync health.
2. The **Job History**tab allows you to check the logs for each sync. If you encounter any errors or unexpected behaviors during a sync, checking the logs is always a good first step to finding the cause and solution.
3. The **Schema**tab allows you to modify the streams you chose during the connection setup.
4. The **Transformation**tab allows you to set up a custom post-sync transformations using dbt.
5. The **Settings**tab contains the connection settings, and the option to delete the connection if you no longer wish to use it.



Documentation Source:
airbyte.com/docs.airbyte.com/operator-guides/browsing-output-logs.md

Documentation Title:
Browsing logs | Airbyte Documentation

Documentation Content:
Skip to main content!!About AirbyteTutorialsSupportCloud StatusTry Airbyte CloudSearch* Airbyte Connectors
Connector CatalogBuild a ConnectorConnector Support Levels* Using Airbyte
Getting StartedConfiguring Connections* Managing Syncs
	Review the connection statusReview the sync historyBrowsing logsClearing your dataModifying connection state
* Managing Airbyte
Deploy AirbyteSelf-Managed EnterpriseUpgrading AirbyteConfiguring AirbyteAccess ManagementAirbyte at ScaleSecurityIntegrating with AirbyteAccount Management* Developer Guides
API documentationTerraform DocumentationUsing PyAirbyteUnderstand AirbyteContribute to AirbyteLicenses* Community
Getting SupportCode of Conduct* Product Updates
RoadmapRelease Notes
Managing SyncsBrowsing logs
On this pageBrowsing logs
=============

AvailableCloud AvailableSelf-Managed Community (OSS)AvailableSelf-Managed EnterpriseAirbyte records the full logs as a part of each sync. These logs can be used to understand the underlying operations Airbyte performs to read data from the source and write to the destination as a part of the Airbyte Protocol. The logs includes many details, including any errors that can be helpful when troubleshooting sync errors.

infoWhen using Airbyte Open Source, you can also access additional logs outside of the UI. This is useful if you need to browse the Docker volumes where extra output files of Airbyte server and workers are stored.

To find the logs for a connection, navigate to a connection's `Job History`tab to see the latest syncs.

View the logs in the UI​
------------------------

To open the logs in the UI, select the three grey dots next to a sync and select `View logs`. This will open our full screen in-app log viewer.

tipIf you are troubleshooting a sync error, you can search for `Error`, `Exception`, or `Fail`to find common errors.

The in-app log viewer will only search for instances of the search term within that attempt. To search across all attempts, download the logs locally.

Link to a sync job​
-------------------

To help others quickly find your job, copy the link to the logs to your clipboard, select the three grey dots next to a sync and select `Copy link to job`.

You can also access the link to a sync job from the in-app log viewer.



Documentation Source:
airbyte.com/blog/manage-and-orchestrate-airbyte-connections-using-python.md

Documentation Title:
You Can Now Manage and Orchestrate Airbyte Connections Using Python | Airbyte

Documentation Content:
Getting Sync Results from Prior Executions

You can use get\_sync\_history() to get a SyncResult object from a previously run job, or get\_sync\_job() if you already know the job ID.

`# Get the last n job results
last_5_sync_results: list[SyncResult] = workspace.get_sync_history(
 connection_id=connection_id,
 limit=5,
)



