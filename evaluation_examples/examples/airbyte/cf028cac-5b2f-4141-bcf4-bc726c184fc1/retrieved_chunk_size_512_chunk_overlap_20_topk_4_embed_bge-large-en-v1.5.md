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



Documentation Source:
airbyte.com/docs.airbyte.com/integrations/sources/postgres/postgres-troubleshooting.md

Documentation Title:
Troubleshooting Postgres Sources | Airbyte Documentation

Documentation Content:
CDC Requirements​

* Incremental sync is only supported for tables with primary keys. For tables without primary keys, use Full Refresh sync.
* Data must be in tables and not views. If you require data synchronization from a view, you would need to create a new connection with `Standard`as `Replication Method`.
* The modifications you want to capture must be made using `DELETE`/`INSERT`/`UPDATE`. For example, changes made using `TRUNCATE`/`ALTER`will not appear in logs and therefore in your destination.
* Schema changes are not supported automatically for CDC sources. Reset and resync data if you make a schema change.
* The records produced by `DELETE`statements only contain primary keys. All other data fields are unset.
* Log-based replication only works for master instances of Postgres. CDC cannot be run from a read-replica of your primary database.
* An Airbyte database source using CDC replication can only be used with a single Airbyte destination. This is due to how Postgres CDC is implemented - each destination would recieve only part of the data available in the replication slot.
* Using logical replication increases disk space used on the database server. The additional data is stored until it is consumed.
	+ Set frequent syncs for CDC to ensure that the data doesn't fill up your disk space.
	+ If you stop syncing a CDC-configured Postgres instance with Airbyte, delete the replication slot. Otherwise, it may fill up your disk space.



Documentation Source:
airbyte.com/tutorials/postgresql-change-data-capture-elt.md

Documentation Title:
Build an EL(T) from Postgres CDC (Change Data Capture) | Airbyte

Documentation Content:
* **Name:**Postgres CDC Tutorial (or any name you'd like)
* **Host:** localhost
* **Port:**5432
* **DB Name:**postgres
* **Schemas:**postgres
* **User:**airbyte
* **Password:**password (or any password you assigned to the airbyte user)
* **Connect using SSL:**disabled
* **Replication method:**Logical replication (CDC)
* **Plugin:** pgoutput
* **Replication\_slot:**airbyte\_slot
* **Publication:**pub1

- **SSH Tunnel Method:**No Tunnel
!!Then click on *Set up source*and Airbyte will test the connection. If everything goes well, you should see a successful message.

Step 4: Configure a local JSON destination in Airbyte
-----------------------------------------------------

Go to destinations and add a new one. As demonstrated in the following diagram, select *Local JSON*as the destination type and fill in with the following details.

* **Name:**JSON CDC Tutorial (or any name you would like)
* **Destination\_path:**/cdc\_tutorial (or any path where you'd like to store the Postgres data)

‍

!Then click on *Set up source*and let Airbyte test the destination.

Step 5: Create an Airbyte connection
------------------------------------

Go to connections and create a new connection. Then, select the existing Postgres source you have just created and then do the same for the Local JSON destination. Once you're done, you can set up the connection as follows.

* **Replication Frequency:**I recommend setting it to "manual" if you're testing. You can change to any frequency that makes sense to your use case when you're ready.
* **Destination Namespace:** Mirror source structure
* **Destination Stream Prefix:**You can leave this option blank, as we don't want a prefix at the destination.

!Then, it's time to configure the streams, which in this case are the tables in our database. For now, we only have the *cars*table. If you expand it, you can see the columns it has.

Now, you should select a **sync mode**.



