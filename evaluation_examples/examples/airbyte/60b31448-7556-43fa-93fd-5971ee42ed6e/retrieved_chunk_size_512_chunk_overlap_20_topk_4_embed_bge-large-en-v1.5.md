Documentation Source:
airbyte.com/docs.airbyte.com/integrations/sources/marketo.md

Documentation Title:
Marketo | Airbyte Documentation

Documentation Content:
Step 1.5: Obtain your Endpoint and Identity URLs provided by Marketo​

Follow the Marketo documentation for obtaining your base URL. Specifically, copy your **Endpoint**without "/rest" and keep them handy for use in the Airbyte UI.

We're almost there! Armed with your Endpoint & Identity URLs and your Client ID and Secret, head over to the Airbyte UI to setup Marketo as a source.

Step 2: Set up the Marketo connector in Airbyte​
------------------------------------------------

**For Airbyte Cloud:**1. Log into your Airbyte Cloudaccount.
2. In the left navigation bar, click Sources. In the top-right corner, click **+new source**.
3. On the Set up the source page, enter the name for the Marketo connector and select **Marketo**from the Source type dropdown.
4. Enter the start date, domain URL, client ID and secret
5. Submit the form

**For Airbyte Open Source:**1. Navigate to the Airbyte Open Source dashboard
2. Set the name for your source
3. Enter the start date
4. Enter the domain URL
5. Enter client ID and secret
6. Click **Set up source**

Supported sync modes​
---------------------

The Marketo source connector supports the followingsync modes:

* Full Refresh | Overwrite
* Full Refresh | Append
* Incremental | Append
* Incremental | Deduped

Supported Streams​
------------------

This connector can be used to sync the following tables from Marketo:

* **Activities\_X**where X is an activity type contains information about lead activities of the type X. For example, activities\_send\_email contains information about lead activities related to the activity type `send_email`. See the Marketo docsfor a detailed explanation of what each column means.
* **Activity types**Contains metadata about activity types. See the Marketo docsfor a detailed explanation of columns.
* Campaigns: Contains info about your Marketo campaigns.
* Leads: Contains info about your Marketo leads.

cautionAvailable fields are limited by what is presented in the static schema.

* Lists: Contains info about your Marketo static lists.
* Programs: Contains info about your Marketo programs.



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
airbyte.com/docs.airbyte.com/integrations/sources/sftp.md

Documentation Title:
SFTP | Airbyte Documentation

Documentation Content:
Step 2: Set up the SFTP connector in Airbyte​

1. Log in to your Airbyte Cloudaccount, or navigate to your Airbyte Open Source dashboard.
2. In the left navigation bar, click **Sources**. In the top-right corner, click **+ New source**.
3. Find and select **SFTP**from the list of available sources.**For Airbyte Cloud users**: If you do not see the **SFTP**source listed, please make sure the **Alpha**checkbox at the top of the page is checked.
4. Enter a **Source name**of your choosing.
5. Enter your **Username**, as well as the **Host Address**and **Port**. The default port for SFTP is 22. If your remote server is using a different port, please enter it here.
6. In the **Authentication**section, use the dropdown menu to select **Password Authentication**or **SSH Key Authentication**, then fill in the required credentials. If you are authenticating with a private key, you can upload the file containing the private key (usually named `rsa_id`) using the **Upload file**button.
7. If you wish to configure additional optional settings, please refer to the next section. Otherwise, click **Set up source**and wait for the tests to complete.

Optional fields​
----------------

The **Optional fields**can be used to further configure the SFTP source connector. If you do not wish to set additional configurations, these fields can be left at their default settings.

1. **File Types**: Enter the desired file types to replicate as comma-separated values. Currently, only CSV and JSON are supported. The default value is `csv,json`.
2. **Folder Path**: Enter a folder path to specify the directory on the remote server to be synced. For example, given the file structure:

`Root| - logs| | - 2021| | - 2022|| - files| | - 2021| | - 2022`An input of `/logs/2022`will only replicate data contained within the specified folder, ignoring the `/files`and `/logs/2021`folders. Leaving this field blank will replicate all applicable files in the remote server's designated entry point.



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



