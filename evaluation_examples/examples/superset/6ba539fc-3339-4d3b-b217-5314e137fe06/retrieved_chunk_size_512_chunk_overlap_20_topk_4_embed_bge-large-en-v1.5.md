Documentation Source:
superset.apache.org/docs/using-superset/exploring-data/index.md

Documentation Title:
Exploring Data in Superset | Superset

Documentation Content:
Enabling Data Upload Functionality​

You may need to enable the functionality to upload a CSV or Excel file to your database. The following section
explains how to enable this functionality for the examples database.

In the top menu, select **Data ‣ Databases**. Find the **examples**database in the list and
select the **Edit**button.

!In the resulting modal window, switch to the **Extra**tab and
tick the checkbox for **Allow Data Upload**. End by clicking the **Save**button.

!### Loading CSV Data​

Download the CSV dataset to your computer from
GitHub.
In the Superset menu, select **Data ‣ Upload a CSV**.

!Then, enter the **Table Name**as *tutorial\_flights*and select the CSV file from your computer.

!Next enter the text *Travel Date*into the **Parse Dates**field.

!Leaving all the other options in their default settings, select **Save**at the bottom of the page.



Documentation Source:
superset.apache.org/docs/configuration/databases/index.md

Documentation Title:
Connecting to Databases | Superset

Documentation Content:
Enabling the meta database​

To enable the Superset meta database, first you need to set the `ENABLE_SUPERSET_META_DB`feature flag to true. Then, add a new database of type "Superset meta database" with the SQLAlchemy URI "superset://".

If you enable DML in the meta database users will be able to run DML queries on underlying databases **as long as DML is also enabled in them**. This allows users to run queries that move data across databases.

Second, you might want to change the value of `SUPERSET_META_DB_LIMIT`. The default value is 1000, and defines how many are read from each database before any aggregations and joins are executed. You can also set this value `None`if you only have small tables.

Additionally, you might want to restrict the databases to with the meta database has access to. This can be done in the database configuration, under "Advanced" -> "Other" -> "ENGINE PARAMETERS" and adding:

{"allowed\_dbs":["Google Sheets","examples"]}Edit this pagePreviousConfiguring SupersetNextAlerts and Reports* Installing Database Drivers
	Supported Databases and DependenciesInstalling Drivers in Docker ImagesDatabase-specific Instructions
* Connecting through the UIExtra Database Settings
* Misc.Querying across databases
We use  !Copyright © 2024,
 The Apache Software Foundation,
 Licensed under the Apache License.

Apache Superset, Apache, Superset, the Superset logo, and the Apache feather logo are either registered trademarks or trademarks of The Apache Software Foundation. All other products or name brands are trademarks of their respective holders, including The Apache Software Foundation.
 Apache Software Foundationresources!Security| 
 Donate| 
 Thanks| 
 Events| 
 License| 
 Privacy!



Documentation Source:
superset.apache.org/docs/configuration/databases/index.md

Documentation Title:
Connecting to Databases | Superset

Documentation Content:
{region}/{database}?role={role}&warehouse={warehouse}`
| SQLite | No additional library needed |`sqlite://path/to/file.db?check_same_thread=false`
|SQL Server`pip install pymssql``mssql+pymssql://`
|Teradata`pip install teradatasqlalchemy``teradatasql://{user}:{password}@{host}`
|TimescaleDB`pip install psycopg2``postgresql://:@:/`
|Trino`pip install trino``trino://{username}:{password}@{hostname}:{port}/{catalog}`
|Vertica`pip install sqlalchemy-vertica-python``vertica+vertica_python://:@/`
|YugabyteDB`pip install psycopg2``postgresql://:@/`

Note that many other databases are supported, the main criteria being the existence of a functional
SQLAlchemy dialect and Python driver. Searching for the keyword "sqlalchemy + (database name)"
should help get you to the right place.

If your database or data engine isn't on the list but a SQL interface
exists, please file an issue on the
Superset GitHub repo, so we can work on documenting and
supporting it.

If you'd like to build a database connector for Superset integration,
read the following tutorial.



Documentation Source:
superset.apache.org/docs/using-superset/creating-your-first-dashboard/index.md

Documentation Title:
Creating Your First Dashboard | Superset

Documentation Content:
Connecting to a new database​

Superset itself doesn't have a storage layer to store your data but instead pairs with
your existing SQL-speaking database or data store.

First things first, we need to add the connection credentials to your database to be able
to query and visualize data from it. If you're using Superset locally via
Docker compose, you can
skip this step because a Postgres database, named **examples**, is included and
pre-configured in Superset for you.

Under the **+**menu in the top right, select Data, and then the *Connect Database*option:

!Then select your database type in the resulting modal:

!Once you've selected a database, you can configure a number of advanced options in this window,
or for the purposes of this walkthrough, you can click the link below all these fields:

!Once you've clicked that link you only need to specify two things (the database name and SQLAlchemy URI):

!As noted in the text below the form, you should refer to the SQLAlchemy documentation on
creating new connection URIsfor your target database.

Click the **Test Connection**button to confirm things work end to end. If the connection looks good, save the configuration
by clicking the **Connect**button in the bottom right corner of the modal window:

Congratulations, you've just added a new data source in Superset!



