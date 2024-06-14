Documentation Source:
airbyte.com/tutorials/incremental-data-synchronization.md

Documentation Title:
Incremental data synchronization between Postgres databases | Airbyte

Documentation Content:
Create a connection between the source and destination

In this section you will create a connection that will be used for demonstrating the functionality of database replication with **Incremental Sync | Append****.** This new connection will make use of the connectors that you have just created. 

Create a new connection by clicking on *Connections*and then on*+ New connection*as shown below (Note that this button may appear in the top right corner if you already have some connections instantiated):

!‍

Then select the *Incremental-source* source as follows:

!‍

Select the*Incremental-destination* as follows:

!‍

You will see a set up page as shown below. Set the name of the connection to *incremental-sync-demo*, and configure it as shown below:

!‍

There are a few areas that are annotated in the above configuration:

1. Define the name which will identify this connection - in this case I have called it *incremental-sync-demo*.
2. Select the*incremental append* replication mode for the table called *table\_one*.
3. Select *updated\_at*as the cursor for the *table\_one*table.

After you click on *Set up connection***,**the initial sync will start. Once it completes you should see the following status in the *Sync History*:

!‍

Make a note of the*job ID* and the*attempt ID* which in this case are 149 and 0 respectively, as can be seen in the path to the*logs.log* (/tmp/workspace/149/0/logs.log) in the screenshot above. You will need these values to find the SQL code used for the first*incremental append* sync.



Documentation Source:
airbyte.com/tutorials/validate-data-replication-postgres-snowflake.md

Documentation Title:
Validate data replication pipelines from Postgres to Snowflake with data-diff | Airbyte

Documentation Content:
Set up your Postgres source

On Airbyte Cloudor Airbyte Open Source, click “new connection”. This will bring you to a screen where you can select your data source. Choose “Postgres” as your source type.

!Now you will be brought to a screen where you need to enter some specific information about your Postgres database. This includes host, port, database name, and a list of the schemas you wish to sync. 

I kept the default port and added my database named `development`, `customers` schema, and the login information for my Airbyte user. It is best practice to create users specific to the toolsyou are connecting to your database.

!### Set up your Snowflake destination

Now let’s set up our Snowflake destinationwhere we will be replicating our Postgres data to. Start by clicking on “new destination” in the top right corner. Then select “Snowflake” as your destination type.

‍

!This is where you will input the information for the Snowflake database that you are copying your Postgres data. Make sure you enter the right location information! 

I also recommend setting up a role that is specific for loading data in your destination as well. This will help keep your environment secure and all you to closely monitor different metrics on the replication process.



Documentation Source:
airbyte.com/tutorials/incremental-change-data-capture-cdc-replication.md

Documentation Title:
Airbyte's incremental Change Data Capture (CDC) replication | Airbyte

Documentation Content:
Instantiate a Postgres source connector

Create a new data source by clicking *+ New source*as follows. 


> ℹ️ If you already have some connectors defined, then *+ New source*may appear in the top right corner of the window.

!Then select *Postgres*as the source as follows:

!Define a source connector called *cdc-source*as follows, and be sure to select *Logical Replication (CDC)*as demonstrated below”:

!After selecting Logical Replication (CDC), enter the parameters that will be used for CDC replication as shown below.

!Then click on the *Set up source*button to create the source connector,



Documentation Source:
airbyte.com/tutorials/incremental-change-data-capture-cdc-replication.md

Documentation Title:
Airbyte's incremental Change Data Capture (CDC) replication | Airbyte

Documentation Content:
Instantiate a Postgres destination connector

Select Postgres as the destination as follows:

!Create a destination called *cdc-destination*as follows:

!And click on the *Set up destination*button to create the destination connector. 

Set up the CDC connection with incremental dedupe synchronization
-----------------------------------------------------------------

The orchestration for CDC syncing is similar to non-CDC database sources – in other words, CDC replication works in conjunction with the various Sync modesthat Airbyte supports. In this tutorial I will demonstrate CDC replication only with the incremental dedupe synchronization mode.


> ℹ️ The steps presented in this section could also be used for testing other sync modes.

Define a new connection that will be used for incremental CDC replication as follows: 

!
> ℹ️  In the definition of a CDC replication connection, notice that a *cursor field*is not required (as opposed to “standard” incremental replication). Furthermore, the *primary key*is automatically determined from the source table, and is therefore not selected.

Once you click on *Set up connection*, Airbyte will start a sync operation from the source to the destination. Once the sync has completed, you should see  a response similar to the following:

!‍

View the destination database
-----------------------------

Open a Postgres shell to the destination as follows:

`docker exec -it airbyte-destination psql --username=postgres`You can then view the names of the tables in the destination with the following command:

`\dt;`Which should respond with the following.



