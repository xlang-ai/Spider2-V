Documentation Source:
airbyte.com/tutorials/mysql-change-data-capture-cdc.md

Documentation Title:
MySQL CDC: Build an ELT pipeline from MySQL Database | Airbyte

Documentation Content:
Now, you should select a sync mode. If you want to take full advantage of performing MySQL CDC, you should use *Incremental | Append*mode to only look at the rows that have changed in the source and sync them to the destination. Selecting a *Full Refresh*mode would sync the whole source table, which is most likely not what you want when using CDC. Learn more about sync modes in our documentation.

When using an *Incremental*sync mode, you would generally need to provide a *Cursor field*, but when using CDC, that's not necessary since the changes in the source are detected via the Debezium connector stream.

Once you're ready, save the changes. Then, you can run your first sync by clicking on *Sync now*. You can check your run logs to verify everything is going well. Just wait for the sync to be completed, and that's it! You've replicated data from MySQL using CDC.

Step 6: Verify that the sync worked
-----------------------------------

From the root directory of the Airbyte project, go to *tmp/airbyte\_local/json\_data/*, and you will find a file named *\_airbyte\_raw\_cars.jsonl*where the data from the MySQL database was replicated.

You can check the file's contents in your preferred IDE or run the following command.

`cat _airbyte_raw_cars.jsonl`‍

!‍

Step 7: Test CDC in action by creating and deleting an object from the database
-------------------------------------------------------------------------------

Now, let's test the MySQL CDC setup you have configured. To do that, run the following queries to insert and delete a row from the database.

`INSERT INTO cars VALUES(3, 'tesla');
DELETE FROM cars WHERE NAME = 'tesla';`‍

Launch a sync and, once it finishes, check the local JSON file to verify that CDC has captured the change. The JSON file should now have two new lines, showing the addition and deletion of the row from the database.

‍

!CDC allows you to see that a row was deleted, which would be impossible to detect when using the regular *Incremental*sync mode.



Documentation Source:
airbyte.com/tutorials/mysql-change-data-capture-cdc.md

Documentation Title:
MySQL CDC: Build an ELT pipeline from MySQL Database | Airbyte

Documentation Content:
Should you build or buy your data pipelines?

Download our free guide and discover the best approach for your needs, whether it's building your ELT solution in-house or opting for Airbyte Open Source or Airbyte Cloud.

Download now!Step 3: Configure a MySQL source in Airbyte
-------------------------------------------

To set up a new MySQL Airbyte source, go to Airbyte's UI at localhost:8000, click on sources and add a new source. As the connector type, select *MySQL*. As demonstrated in the subsequent illustrations, fill in the following configuration fields if you used the instructions above to configure your  database in MySQL.

!‍

!‍

Then click on *Set up source*and Airbyte will test the connection. If everything goes well, you should see a successful message.

Step 4: Configure a local JSON destination in Airbyte
-----------------------------------------------------

Now, you’ll configure a local JSON destination in Airbyte. Take into account that I use local JSON as a destination for demonstration purposes – as it’s the easiest to set up. For your actual applications, you can select any destination from our ever-growing catalog. 

Go to destinations and add a new one. As demonstrated in the following diagram, select *Local JSON*as the destination type and fill in with the following details.

‍

!Then click on *Set up source*and let Airbyte test the destination.

Step 5: Create an Airbyte connection
------------------------------------

Go to connections and create a new connection. Then, select the existing MySQL source you have just created and then do the same for the Local JSON destination. Once you're done, you can set up the connection as follows.

!As you can see, I set the replication frequency to *manual* so I can trigger synchronization on demand. You can change the replication frequency, later on, to sync **as frequently as every 5 minutes**.

Then, it's time to configure the streams, which in this case are the tables in your database. For now, you only have the *cars*table. If you expand it, you can see the columns it has.

Now, you should select a sync mode.



Documentation Source:
airbyte.com/tutorials/incremental-data-synchronization.md

Documentation Title:
Incremental data synchronization between Postgres databases | Airbyte

Documentation Content:
* Learn **when****incremental synchronization**may be a good choice.
* Learn**what a cursor**is, and why it is required for incremental synchronization.
* Learn **why a primary key**is required for deduplication.
* Create an **Airbyte source**connector to read data from a source database.
* Create an **Airbyte destination**connector to write data into a destination database.
* Explore incremental database replication using the **Incremental Sync - Append** sync mode**.**
* Explore incremental database replication using the **Incremental Sync - Deduped History** sync mode.
* Inspect **raw JSON data**that is replicated into a destination database.
* Inspect the **normalized data**that is created from raw JSON.
* Review the **SQL code**that Airbyte uses for normalizing JSON data.
* See how **inserts**, **updates**, and **deletes**on the source database are reflected in the destination.



Documentation Source:
airbyte.com/docs.airbyte.com/integrations/sources/mysql/mysql-troubleshooting.md

Documentation Title:
Troubleshooting MySQL Sources | Airbyte Documentation

Documentation Content:
Follow the instructions in Airbyte documentationto
run SQL queries on Airbyte database.

If you have connections with MySQL Source using *Standard*replication method, run this SQL:

`updatepublic.actor setconfiguration =jsonb_set(configuration,'{replication_method}','{"method": "STANDARD"}',true)WHEREactor_definition_id ='435bb9a5-7887-4809-aa58-28c27df0d7ad'AND(configuration->>'replication_method'='STANDARD');`If you have connections with MySQL Source using *Logical Replication (CDC)*method, run this SQL:

`updatepublic.actor setconfiguration =jsonb_set(configuration,'{replication_method}','{"method": "CDC"}',true)WHEREactor_definition_id ='435bb9a5-7887-4809-aa58-28c27df0d7ad'AND(configuration->>'replication_method'='CDC');`Edit this pagePreviousMySQLNextN8nGeneral LimitationsCDC Requirements* Troubleshooting
	Common Config ErrorsUnder CDC incremental mode, there are still full refresh syncsEventDataDeserializationException errors during initial snapshot(Advanced) Enable GTIDs(Advanced) Setting up initial CDC waiting time(Advanced) Set up server timezone
Upgrading from 0.6.8 and older versions to 0.6.9 and later versions
Was this page helpful?YesNo



