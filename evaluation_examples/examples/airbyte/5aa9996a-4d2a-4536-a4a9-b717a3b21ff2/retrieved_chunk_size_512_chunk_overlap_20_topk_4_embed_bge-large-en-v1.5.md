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
airbyte.com/blog/manage-and-orchestrate-airbyte-connections-using-python.md

Documentation Title:
You Can Now Manage and Orchestrate Airbyte Connections Using Python | Airbyte

Documentation Content:
Getting your Airbyte API Key

To interact with Airbyte programmatically, you’ll need an API key for authentication. Here's how to get it:

* Navigate to the Airbyte Developer Portaland enter your credentials to login.
* Once logged in, look for the option to create a new API key. The portal will guide you through the steps to generate this key.
* After obtaining your API key, make sure to store it safely. We recommend using your favorite secrets manager for this purpose. You'll need this key later.



Documentation Source:
airbyte.com/docs.airbyte.com/using-airbyte/getting-started/set-up-a-connection.md

Documentation Title:
Set up a Connection | Airbyte Documentation

Documentation Content:
Skip to main content!!About AirbyteTutorialsSupportCloud StatusTry Airbyte CloudSearch* Airbyte Connectors
Connector CatalogBuild a ConnectorConnector Support Levels* Using Airbyte
* Getting Started
	Core ConceptsAdd a SourceAdd a DestinationSet up a Connection
Configuring ConnectionsManaging Syncs* Managing Airbyte
Deploy AirbyteSelf-Managed EnterpriseUpgrading AirbyteConfiguring AirbyteAccess ManagementAirbyte at ScaleSecurityIntegrating with AirbyteAccount Management* Developer Guides
API documentationTerraform DocumentationUsing PyAirbyteUnderstand AirbyteContribute to AirbyteLicenses* Community
Getting SupportCode of Conduct* Product Updates
RoadmapRelease Notes
Getting StartedSet up a Connection
On this pageSet up a Connection
===================

AvailableCloud AvailableSelf-Managed Community (OSS)AvailableSelf-Managed EnterpriseNow that you've learned how to set up your first sourceand destination, it's time to finish the setup by creating your very first connection!

On the left side of your main Airbyte dashboard, select **Connections**. You will be prompted to choose which source and destination to use for this connection. For this example, we'll use the **Google Sheets**source and the destination you previously set up, either **Local JSON**or **Google Sheets**.

Configure the connection​
-------------------------

Once you've chosen your source and destination you can configure the connection. You'll first be asked a few questions about how your data should sync, these correlate to our sync modes which you can read more about on this page.

Most users select "Mirror Source", which will simply copy the data from the source to the destination where you'll see one row in the destination for each row in the source. If you prefer to Append Historical Changes or take a Full Snapshot with each sync, you can optionally select those options, but keep in mind those will create duplicate records in your destination. The sync mode we choose for all the enabled streams will reflect your selection here.

Next, you can toggle which streams you want to replicate. Our test data consists of three streams, which we've enabled and set to `Incremental - Append + Deduped`sync mode.

!Your sync mode is already determined by your selection above, but you can change the sync mode for an individual stream.



Documentation Source:
airbyte.com/blog/manage-and-orchestrate-airbyte-connections-using-python.md

Documentation Title:
You Can Now Manage and Orchestrate Airbyte Connections Using Python | Airbyte

Documentation Content:
Familiarity with Airbyte

If you're already an Airbyte user, you’ll find this post particularly useful, as it builds on what you might already know about the platform. And if you’re somewhat new to Airbyte or just need a quick overview, there’s a helpful tutorialto get you started on setting up your first connection.



