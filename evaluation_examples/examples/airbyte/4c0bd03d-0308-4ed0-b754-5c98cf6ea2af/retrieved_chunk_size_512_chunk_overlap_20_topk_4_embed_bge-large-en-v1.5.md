Documentation Source:
airbyte.com/docs.airbyte.com/cloud/managing-airbyte-cloud/configuring-connections.md

Documentation Title:
Configuring Connections | Airbyte Documentation

Documentation Content:
noteThese settings apply to all streams in the connection.

You can configure the following settings:



| Setting | Description |
| --- | --- |
| Connection Name | A custom name for your connection |
| --- | --- |
|Schedule Type How often data syncs (can be scheduled, cron, API-triggered or manual) |
|Destination Namespace Where the replicated data is written to in the destination |
| Destination Stream Prefix | A prefix added to each table name in the destination |
|Detect and propagate schema changes How Airbyte handles schema changes in the source |
|Connection Data Residency Where data will be processed (Cloud only) |

Modify Streams​
---------------

On the "Schema" tab, you choose which streams to sync and how they are loaded to the destination.

infoA connection's schema consists of one or many streams. Each stream is most commonly associated with a database table or an API endpoint. Within a stream, there can be one or many fields or columns.

To modify streams, click **Connections**and then click the connection you want to change. Click the **Schema**tab to see all the streams Airbyte can sync. To modify an individual stream:

Toggle **Sync**on or off for your selected stream. To select or deselect all streams at once, use "Hide disabled streams" in the table header. To deselect an individual stream, use the toggle in its row.

Click the **Sync mode**dropdown and select the sync mode you want to apply. Depending on the sync mode you select, you may need to choose a cursor or primary key.


infoSource-defined cursors and primary keys are selected automatically and cannot be changed in the table.

Click on a stream to display the stream details panel. You'll see each column we detect from the source.

Column selection is available to protect PII or sensitive data from being synced to the destination. Toggle individual fields to include or exclude them in the sync, or use the toggle in the table header to select all fields at once.



Documentation Source:
airbyte.com/docs.airbyte.com/integrations/sources/jira-migrations.md

Documentation Title:
Jira Migration Guide | Airbyte Documentation

Documentation Content:
To gracefully handle these changes for your existing connections, we highly recommend resetting your data before resuming your data syncs with the new version. The **Issues**, **Board Issues**and **Sprint Issues**streams can be manually reset in the following way:

1. Select **Connections**in the main navbar.
1.1 Select the connection(s) affected by the update.
2. Select the **Schema**tab.
3. Uncheck all streams except the affected ones.
4. Select **Save changes**at the bottom of the page.
5. Select the **Settings**tab.
6. Press the **Clear your data**button.
7. Return to the **Schema**tab.
8. Check all your streams.
9. Select **Sync now**to sync your data

For more information on resetting your data in Airbyte, see this page.

Upgrading to 1.0.0​
-------------------

Note: this change is only breaking if you are using the `Boards Issues`stream in Incremental Sync mode.

This is a breaking change because Stream State for `Boards Issues`will be changed, so please follow the instructions below to migrate to version 1.0.0:

1. Select **Connections**in the main navbar.
1.1 Select the connection(s) affected by the update.
2. Select the **Replication**tab.
2.1 Select **Refresh source schema**.
`note Any detected schema changes will be listed for your review.` 2.2 Select **OK**.
3. Select **Save changes**at the bottom of the page.
3.1 Ensure the **Reset affected streams**option is checked.
`note Depending on destination type you may not be prompted to reset your data`
4. Select **Save connection**.
`note This will reset the data in your destination and initiate a fresh sync.`

For more information on resetting your data in Airbyte, see this page.

Edit this pagePreviousJiraNextK6 Cloud APIUpgrading to 2.0.0Upgrading to 1.0.0
Was this page helpful?YesNo



Documentation Source:
airbyte.com/docs.airbyte.com/cloud/managing-airbyte-cloud/configuring-connections.md

Documentation Title:
Configuring Connections | Airbyte Documentation

Documentation Content:
info* You can only deselect top-level fields. You cannot deselect nested fields.
* The Airbyte platform may read all data from the source (depending on the source), but it will only write data to the destination from fields you selected. Deselecting fields will not prevent the Airbyte platform from reading them.
* When you refresh the schema, newly added fields will be selected by default, even if you have previously deselected fields in that stream.
Click the **X**to close the stream details panel.

Click **Save changes**, or click **Cancel**to discard the changes.

The **Stream configuration changed**dialog displays. This gives you the option to reset streams when you save the changes.


tipWhen editing the stream configuration, Airbyte recommends that you reset streams. A reset will delete data in the destination of the affected streams and then re-sync that data. Skipping a reset is discouraged and might lead to unexpected behavior.

- Click **Save connection**.
Edit this pagePreviousSet up a ConnectionNextSync SchedulesConfigure Connection SettingsModify Streams
Was this page helpful?YesNo



Documentation Source:
airbyte.com/docs.airbyte.com/integrations/sources/faker.md

Documentation Title:
Faker | Airbyte Documentation

Documentation Content:
|
| 5.0.2 | 2024-01-17 |34344 Ensure unique state messages |
| 5.0.1 | 2023-01-08 |34033 Add standard entrypoints for usage with AirbyteLib |
| 5.0.0 | 2023-08-08 |29213 Change all `*id`fields and `products.year`to be integer |
| 4.0.0 | 2023-07-19 |28485 Bump to test publication |
| 3.0.2 | 2023-07-07 |27807 Bump to test publication |
| 3.0.1 | 2023-06-28 |27807 Fix bug with purchase stream updated\_at |
| 3.0.0 | 2023-06-23 |27684 Stream cursor is now `updated_at`& remove `records_per_sync`option |
| 2.1.0 | 2023-05-08 |25903 Add user.address (object) |
| 2.0.3 | 2023-02-20 |23259 bump to test publication |
| 2.0.2 | 2023-02-20 |23259 bump to test publication |
| 2.0.1 | 2023-01-30 |22117 `source-faker`goes beta |
| 2.0.0 | 2022-12-14 | 20492and 20741 | Decouple stream states for better parallelism |
| 1.0.0 | 2022-11-28 |19490 Faker uses the CDK; rename streams to be lower-case (breaking), add determinism to random purchases, and rename |
| 0.2.1 | 2022-10-14 |19197 Emit `AirbyteEstimateTraceMessage` |
| 0.2.0 | 2022-10-14 |18021 Move to mimesis for speed!



