Documentation Source:
airbyte.com/tutorials/incremental-data-synchronization.md

Documentation Title:
Incremental data synchronization between Postgres databases | Airbyte

Documentation Content:
Look at its contents by executing the following:

`SELECT * FROM _airbyte_raw_table_one;`‍

Which should respond with a table that looks as follows:

`_airbyte_ab_id | _airbyte_data | _airbyte_emitted_at 
--------------------------------------+-----------------------------------------------------------------------------+----------------------------
 2abc7493-bfc8-4493-ab62-de6ffe094a2d | {"id": 1, "name": "Eg1 IncApp", "updated_at": "2022-09-01T11:01:41.666004"} | 2022-09-01 11:12:03.301+00
 06e67da7-9c6a-46b6-a2e5-e1d102e16c7e | {"id": 2, "name": "Eg2a IncAp", "updated_at": "2022-09-01T11:02:05.017416"} | 2022-09-01 11:12:03.301+00
(2 rows)`‍

In addition to the field containing the source data there are two additional fields in the raw table:

* *\_airbyte\_emitted\_at*which tells you what time airbyte sent the record to the destination.
* *\_airbyte\_ab\_id*is a UUID value added by the destination connector to each record before it is sent to the destination. This is a UUID (not a hash) and therefore it changes for each row after each sync, even if the data has not been modified.



Documentation Source:
airbyte.com/tutorials/postgres-to-bigquery.md

Documentation Title:
How to Connect & Load Data from Postgres to BigQuery?

Documentation Content:
Airbyte allows both manual and automatic scheduling for your data refreshes.
5. **Select the data to sync:**Choose the specific Postgres objects you want to import data from towards BigQuery. You can sync all data or select specific tables and fields.
6. **Select the sync mode for your streams:**Choose between full refreshes or incremental syncs (with deduplication if you want), and this for all streams or at the stream level. Incremental is only available for streams that have a primary cursor.
7. **Test your connection:**Click the 'Test Connection' button to make sure that your setup works. If the connection test is successful, save your configuration.
8. **Start the sync:**If the test passes, click 'Set Up Connection'. Airbyte will start moving data from Postgres to BigQuery according to your settings.

Remember, Airbyte keeps your data in sync at the frequency you determine, ensuring your BigQuery data warehouse is always up-to-date with your Postgres data.

Use Cases to transfer your Postgres data to BigQuery
----------------------------------------------------

Integrating data from Postgres to BigQuery provides several benefits. Here are a few use cases:

1. **Advanced Analytics:**BigQuery’s powerful data processing capabilities enable you to perform complex queries and data analysis on your Postgres data, extracting insights that wouldn't be possible within Postgres alone.
2. **Data Consolidation:**If you're using multiple other sources along with Postgres, syncing to BigQuery allows you to centralize your data for a holistic view of your operations, and to set up a change data capture process so you never have any discrepancies in your data again.
3. **Historical Data Analysis:**Postgres has limits on historical data. Syncing data to BigQuery allows for long-term data retention and analysis of historical trends over time.
4. **Data Security and Compliance:**BigQuery provides robust data security features. Syncing Postgres data to BigQuery ensures your data is secured and allows for advanced data governance and compliance management.
5. **Scalability:**BigQuery can handle large volumes of data without affecting performance, providing an ideal solution for growing businesses with expanding Postgres data.
6.



Documentation Source:
airbyte.com/tutorials/postgres-replication.md

Documentation Title:
Postgres Replication: Data Transfer Efficiency | Airbyte

Documentation Content:
Should you build or buy your data pipelines?

Download our free guide and discover the best approach for your needs, whether it's building your ELT solution in-house or opting for Airbyte Open Source or Airbyte Cloud.

Download now!Step 3: Create an Airbyte connection
------------------------------------

Go to connections and create a new connection. Then, select the existing Postgres source you have just created and then do the same for the destination. Once you’re done, you can set up the connection as follows.

* **Replication Frequency:**I recommend setting it to “manual” if you’re testing. When you’re ready, you can change to any frequency that makes sense to your use case.
* **Destination Namespace:**I selected a mirror source structure, so the schema and tables are the same as the source.
* **Destination Stream Prefix:**I added the prefix *tutorial\_*so my table will be created as *tutorial\_users.*

Then, it’s time to configure the streams, which in this case are the tables in our database. If we expand the tables, we can see the columns they have. We can also see they’re part of the *public*namespace or schema. The destination schema will be also *public*.

!Now, you should select a sync mode. I chose **Full refresh | Overwrite**to sync the *cities*table and **Incremental | Append** for the *users*table since it has an *id*column (primary key) suitable for the incremental cursor field. The most important thing to note is that you can have different sync modes for each table! Learn more about sync modes in our documentation. 

Once you’re ready, save the changes. Then, you can run your first sync by clicking on “Sync now.” You can check your run logs to verify everything is going well. Just wait for the sync to be completed, and that’s it! You’ve synchronized two Postgres databases.

!Step 4: Verify that the sync worked
-----------------------------------

Now, let's verify that this worked.



Documentation Source:
airbyte.com/tutorials/incremental-data-synchronization.md

Documentation Title:
Incremental data synchronization between Postgres databases | Airbyte

Documentation Content:
`SELECT * FROM _airbyte_raw_table_two;`‍

Which should respond with a table that looks as follows:

`_airbyte_ab_id | _airbyte_data | _airbyte_emitted_at 
--------------------------------------+-----------------------------------------------------------------------------+----------------------------
 3bd474b8-0329-4bce-bde7-aee7c5d30cc8 | {"id": 1, "name": "Eg1 DD+Hst", "updated_at": "2022-09-01T16:18:07.569818"} | 2022-09-01 16:52:44.103+00
 4282344a-62c3-4634-a91a-e6dafb9b253a | {"id": 2, "name": "Eg2a DD+Hs", "updated_at": "2022-09-01T16:30:13.939030"} | 2022-09-01 16:52:44.103+00
 89377204-7801-49c8-a779-91da45a86cc3 | {"id": 2, "name": "Eg2b DD+Hs", "updated_at": "2022-09-01T17:02:14.841419"} | 2022-09-01 17:02:39.894+00
(3 rows)`### Update: View the normalized tables in the destination

View the history table called *table\_two\_scd*by executing the following:

`SELECT * FROM table_two_scd;`‍

Which looks as follows.



