Documentation Source:
airbyte.com/tutorials/full-data-synchronization.md

Documentation Title:
Explore Airbyte's full refresh data synchronization | Airbyte

Documentation Content:
Create a full refresh overwrite connection

Create a new connection that will be used for verifying the functionality of **full refresh | overwrite**synchronization. Select the **Postgres-source**source, which you previously defined, as the source for this connection.

!‍

And select **Postgres-destination,**which you previously defined, as the destination for this connection.

!‍

You will see a set up page as shown below. Set the name of the connection to **full-refresh-overwrite**, and the destination stream prefix as **overwrite\_**as shown below.

‍

!‍

After you set up the connection, you should see that a first sync has automatically started.  Once it completes, you should see a message indicating that two records have been emitted as follows:

!.



Documentation Source:
airbyte.com/tutorials/full-data-synchronization.md

Documentation Title:
Explore Airbyte's full refresh data synchronization | Airbyte

Documentation Content:
Create a full refresh append connection

Set up a new connection that will demonstrate **full refresh | append**functionality, using the connectors that you created earlier in this tutorial.

First, select **Postgres-source**as the source for this connection.

!‍

Then select **Postgres-destination** as the destination for this connection.

!‍

Then create a new connection and name it **full-refresh-append**, set the prefix to **append**\_ ,and select **full refresh | append**as the sync mode, as shown below.

!A sync should automatically start after you create the connection. Wait for the sync to complete, and you should see a message like the following: 

‍

!### Open a Postgres terminal on the destination

If you don’t already have a shell open to your Postgres destination, execute the following commands:

`docker exec -it airbyte-destination /bin/bash
psql --username=postgres`‍

You can view the tables in the destination Postgres database by executing the following command from the Postgres shell that you have just opened . 

`\dt;`‍

Which should respond with the following: 

`List of relations
 Schema | Name | Type | Owner 
--------+------------------------------------------+-------+----------
 public | _airbyte_raw_append_full_refresh_demo | table | postgres
 public | _airbyte_raw_overwrite_full_refresh_demo | table | postgres
 public | append_full_refresh_demo | table | postgres
 public | overwrite_full_refresh_demo | table | postgres
(4 rows)`‍

Two new tables have been created, **\_airbyte\_raw\_append\_full\_refresh\_demo**and **append\_full\_refresh\_demo**. 

You can look at the raw data as follows:

`SELECT * FROM  _airbyte_raw_append_full_refresh_demo;`‍

Which should respond with a table that looks very similar to the raw table that you saw created with **full refresh | overwrite**replication, as follows: 

`_airbyte_ab_id | _airbyte_data | _airbyte_emitted_at 
--------------------------------------+-----------------------------+----------------------------
 972a8d74-d840-4c43-826e-b0a1042c1681 | {"id": 1,



Documentation Source:
airbyte.com/tutorials/full-data-synchronization.md

Documentation Title:
Explore Airbyte's full refresh data synchronization | Airbyte

Documentation Content:
788+00 | 2022-07-27 15:53:49.016524+00 | 85aefb77a6bc2acc426eedf5a822b8b3
(2 rows)`‍

Looking at the **\_airbyte\_emitted\_at**timestamp and the **\_airbyte\_normalized\_at**timestamp confirms that every record has been overwritten and re-normalized. In other words, even if no data was modified in the Postgres source, the entire table is copied and overwritten in the destination. 

Database synchronization with full refresh append
-------------------------------------------------

In this section you will create an Airbyte connectionthat reads data from the Postgres source and drives it into the Postgres destination using the **full refresh | append**replication mode. In this mode, as with the **full refresh | overwrite**replication mode, all data in the source database is sent to the destination database, regardless of whether it has been synced before or not. However, in the **append**variant, new syncs will take all data from the most recent sync and append it to the raw destination table. If normalization is enabled, then records that have recently been appended to the raw table will be normalized and appended to the normalized table. This is easiest to see for yourself via a hands-on example, as presented below.



Documentation Source:
airbyte.com/tutorials/full-data-synchronization.md

Documentation Title:
Explore Airbyte's full refresh data synchronization | Airbyte

Documentation Content:
Update a record on the source

Update a record on the **full\_refresh\_demo**table on the source Postgres database, and view the source table by running the following commands:

`UPDATE full_refresh_demo SET name='New Jane' WHERE id=3;
SELECT * FROM full_refresh_demo;`‍

And the source **full\_refresh\_demo**table should now look as follows: 

`id | name 
----+----------
 1 | Mary X
 2 | John D
 3 | New Jane
(3 rows)`‍

As before, execute a new sync by clicking on **Sync Now**in the connection pane and wait for it to complete. The UI will indicate that 3 records have been emitted as follows:

‍

!‍

Have a look at the **\_airbyte\_raw\_overwrite\_full\_refresh\_demo**table in the destination Postgres database with the following command:

`SELECT * FROM _airbyte_raw_overwrite_full_refresh_demo;`‍

Which should respond with a table similar to the following

`_airbyte_ab_id | _airbyte_data | _airbyte_emitted_at 
--------------------------------------+-------------------------------+----------------------------
 9d647452-21cd-4e6b-b9e6-1021b4eea06f | {"id": 1, "name": "Mary X"} | 2022-07-27 14:38:26.594+00
 d0c7d8a6-ed0e-4280-a768-08dfc424abda | {"id": 2, "name": "John D"} | 2022-07-27 14:38:26.594+00
 23472df3-9ac7-48fb-8675-84b240367dc4 | {"id": 3, "name": "New Jane"} | 2022-07-27 14:38:26.594+00
(3 rows)`‍

Once again, by comparing the value of **\_airbyte\_emitted\_at**to the prior values (shown earlier in this tutorial), you can see that every record has been overwritten, not just the record that was updated.



