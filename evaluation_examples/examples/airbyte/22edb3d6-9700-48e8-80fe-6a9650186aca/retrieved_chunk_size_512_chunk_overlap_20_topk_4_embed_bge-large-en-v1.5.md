Documentation Source:
airbyte.com/docs.airbyte.com/integrations/destinations/sftp-json.md

Documentation Title:
SFTP JSON | Airbyte Documentation

Documentation Content:
Example:​

If `destination_path`is set to `/myfolder/files`and `filename`is set to `mydata`, the resulting file will be `/myfolder/files/mydata.jsonl`.

These files can then be accessed by creating an SFTP connection to the server and navigating to the `destination_path`.

Changelog​
----------



| Version | Date | Pull Request | Subject |
| --- | --- | --- | --- |
| 0.1.0 | 2022-11-24 |4924 🎉 New Destination: SFTP JSON |

Edit this pagePreviousSelectDBNextSnowflake Cortex Destination* OverviewSync Overview
* Getting StartedExample:
Changelog
Was this page helpful?YesNo



Documentation Source:
airbyte.com/docs.airbyte.com/integrations/destinations/local-json.md

Documentation Title:
Local JSON | Airbyte Documentation

Documentation Content:
Sync Overview​



Documentation Source:
airbyte.com/docs.airbyte.com/integrations/destinations/local-json.md

Documentation Title:
Local JSON | Airbyte Documentation

Documentation Content:
Performance considerations​

This integration will be constrained by the speed at which your filesystem accepts writes.

Getting Started​
----------------

The `destination_path`will always start with `/local`whether it is specified by the user or not. Any directory nesting within local will be mapped onto the local mount.

By default, the `LOCAL_ROOT`env variable in the `.env`file is set `/tmp/airbyte_local`.

The local mount is mounted by Docker onto `LOCAL_ROOT`. This means the `/local`is substituted by `/tmp/airbyte_local`by default.

cautionPlease make sure that Docker Desktop has access to `/tmp`(and `/private`on a MacOS, as /tmp has a symlink that points to /private. It will not work otherwise). You allow it with "File sharing" in `Settings -> Resources -> File sharing -> add the one or two above folder`and hit the "Apply & restart" button.



Documentation Source:
airbyte.com/docs.airbyte.com/using-airbyte/getting-started/add-a-destination.md

Documentation Title:
Add a Destination | Airbyte Documentation

Documentation Content:
The left half of the page contains a set of fields that you will have to fill out. In the **Destination name**field, you can enter a name of your choosing to help you identify this instance of the connector. By default, this will be set to the name of the destination (i.e., `Google Sheets`).

Authenticate into your Google account by clicking "Sign in with Google" and granting permissions to Airbyte. Because this is a simple Google Sheets destination, there is only one more required field, **Spreadsheet Link**. This is the path to your spreadsheet that can be copied directly from your browser.

As an example, we'll be setting up a simple JSON file that will be saved on our local system as the destination. Select **Local JSON**from the list of destinations. This will take you to the destination setup page.

The left half of the page contains a set of fields that you will have to fill out. In the **Destination name**field, you can enter a name of your choosing to help you identify this instance of the connector. By default, this will be set to the name of the destination (i.e., `Local JSON`).

Because this is a simple JSON file, there is only one more required field, **Destination Path**. This is the path in your local filesystem where the JSON file containing your data will be saved. In our example, if we set the path to `/my_first_destination`, the file will be saved in `/tmp/airbyte_local/my_first_destination`.

Each destination will have its own set of required fields to configure during setup. You can refer to your destination's provided setup guide on the right side of the page for specific details on the nature of each field.

tipSome destinations will also have an **Optional Fields**tab located beneath the required fields. You can open this tab to view and configure any additional optional parameters that exist for the source. These fields generally grant you more fine-grained control over your data replication, but you can safely ignore them.

Once you've filled out the required fields, select **Set up destination**. A connection check will run to verify that a successful connection can be established. Now you're ready to set up your first connection!



