Documentation Source:
airbyte.com/docs.airbyte.com/integrations/destinations/sqlite.md

Documentation Title:
Sqlite | Airbyte Documentation

Documentation Content:
Example:​

* If `destination_path`is set to `/local/sqlite.db`
* the local mount is using the `/tmp/airbyte_local`default
* then all data will be written to `/tmp/airbyte_local/sqlite.db`.

Access Replicated Data Files​
-----------------------------

If your Airbyte instance is running on the same computer that you are navigating with, you can open your browser and enter file:///tmp/airbyte\_localto look at the replicated data locally. If the first approach fails or if your Airbyte instance is running on a remote server, follow the following steps to access the replicated files:

1. Access the scheduler container using `docker exec -it airbyte-server bash`
2. Navigate to the default local mount using `cd /tmp/airbyte_local`
3. Navigate to the replicated file directory you specified when you created the destination, using `cd /{destination_path}`
4. Execute `sqlite3 {filename}`to access the data in a particular database file.

You can also copy the output file to your host machine, the following command will copy the file to the current working directory you are using:

docker cp airbyte-server:/tmp/airbyte\_local/{destination\_path} .Note: If you are running Airbyte on Windows with Docker backed by WSL2, you have to use similar step as above or refer to this linkfor an alternative approach.

Changelog​
----------



| Version | Date | Pull Request | Subject |
| --- | --- | --- | --- |
| 0.1.0 | 2022-07-25 |15018 New SQLite destination |

Edit this pagePreviousSnowflake Migration GuideNextStarburst Galaxy destination user guide* OverviewSync Overview
* Getting StartedExample:
Access Replicated Data FilesChangelog
Was this page helpful?YesNo



Documentation Source:
airbyte.com/docs.airbyte.com/integrations/destinations/sqlite.md

Documentation Title:
Sqlite | Airbyte Documentation

Documentation Content:
To change this location, modify the `LOCAL_ROOT`environment variable for Airbyte.

cautionPlease make sure that Docker Desktop has access to `/tmp`(and `/private`on a MacOS, as /tmp has a symlink that points to /private. It will not work otherwise). You allow it with "File sharing" in `Settings -> Resources -> File sharing -> add the one or two above folder`and hit the "Apply & restart" button.



Documentation Source:
airbyte.com/docs.airbyte.com/integrations/destinations/sqlite.md

Documentation Title:
Sqlite | Airbyte Documentation

Documentation Content:
Performance considerations​

This integration will be constrained by the speed at which your filesystem accepts writes.

Getting Started​
----------------

The `destination_path`will always start with `/local`whether it is specified by the user or not. Any directory nesting within local will be mapped onto the local mount.

By default, the `LOCAL_ROOT`env variable in the `.env`file is set `/tmp/airbyte_local`.

The local mount is mounted by Docker onto `LOCAL_ROOT`. This means the `/local`is substituted by `/tmp/airbyte_local`by default.



Documentation Source:
airbyte.com/docs.airbyte.com/integrations/locating-files-local-destination.md

Documentation Title:
Windows - Browsing Local File Output | Airbyte Documentation

Documentation Content:
Note that there are scenarios where you may not be able to browse to the actual files in which case, use the below method to take a local copy.

Use Docker to Copy your temp folder files​
------------------------------------------

Note that this method does not allow direct access to any files directly, instead it creates local, readable copies.

1. Open and standard CMD shell
2. Type the following (where ``is the path on your Windows host machine to place copies)
`docker cp airbyte-server:/tmp/airbyte_local `
3. This will copy the entire `airbyte_local`folder to your host machine.

Note that if you know the specific filename or wildcard, you can add append it to the source path of the `docker cp`command.

Notes​
------

1. Local JSON and Local CSV files do not persist between Docker restarts. This means that once you turn off your Docker image, your data is lost. This is consistent with the `tmp`nature of the folder.
2. In the root folder of your docker files, it might generate tmp and var folders that only have empty folders inside.
Edit this pageOverviewLocating where your temp folder isUse Docker to Copy your temp folder filesNotes
Was this page helpful?YesNo



