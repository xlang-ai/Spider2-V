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
Now, you should select a **sync mode**. If you want to take full advantage of using Change Data Capture, you should use *Incremental | Append*mode to only look at the rows that have changed in the source and sync them to the destination. Selecting a *Full Refresh*mode would sync the whole source table, which is most likely not what you want when using CDC. Learn more about sync modes in our documentation.

When using an *Incremental*sync mode, we would generally need to provide a *Cursor field*, but when using CDC, that's not necessary since the changes in the source are detected via the Debezium connector stream.

!Once you're ready, save the changes. Then, you can run your first sync by clicking on *Sync now*. You can check your run logs to verify everything is going well. Just wait for the sync to be completed, and that's it! You've replicated data using Postgres Change Data Capture.

Step 6: Verify that the sync worked
-----------------------------------

From the root directory of the Airbyte project, go to */tmp/airbyte\_local/cdc\_tutorial*, and you will find a file named *\_airbyte\_raw\_cars.jsonl*where the data from the PostgreSQL database was replicated.

You can check the file's contents in your preferred IDE or run the following command.

`cat _airbyte_raw_cars.jsonl`‍

!Step 7: Test CDC in action by creating and deleting an object from the database
-------------------------------------------------------------------------------

Now, let's test the CDC setup we have configured. To do that, run the following queries to insert and delete a row from the database.

`INSERT INTO cars VALUES(3, 'tesla');
DELETE FROM cars WHERE NAME = 'tesla';`Launch a sync and, once it finishes, check the local JSON file to verify that CDC has captured the change. The JSON file should now have two new lines, showing the addition and deletion of the row from the database. 

!We confirm that CDC allows you to see that a row was deleted, which would be impossible to detect when using the regular *Incremental*sync mode.



Documentation Source:
airbyte.com/blog/what-is-data-replication.md

Documentation Title:
What is Data Replication: Examples, Techniques & Challenges | Airbyte

Documentation Content:
Can we replicate data without the CDC?

It is feasible to replicate data between systems without the need for Change Data Capture (CDC). Entire datasets are periodically copied from a source to a target system using traditional replication techniques. CDC is not the only method available; it provides real-time replication by capturing and propagating only the modifications made to the source data. Although it is less efficient in terms of processing and bandwidth, full data replication can still be used in situations where real-time data synchronization is not necessary.

The data movement infrastructure for the modern data teams.Try a 14-day free trial !### About the Author

Thalia Barrera is a data engineer and technical writer at Airbyte. She has over a decade of experience as an engineer in the IT industry. She enjoys crafting technical and training materials for fellow engineers. Drawing on her computer science expertise and client-oriented nature, she loves turning complex topics into easy-to-understand content.

!### About the Author

Table of contents
-----------------

Example H2Example H3Example H4Example H5Example H6Example H2Example H3Example H4Example H5Example H6Join our newsletter to get all the insights on the data stack
-------------------------------------------------------------

Related posts
-------------

ArticleImportant Nodes of the Query Plan Tree in PostgreSQLArun Nanda•May 17, 2024•10 min readArticlePostgreSQL Query Plans for Reading TablesArun Nanda•May 17, 2024•15 min readArticleIntroduction to Using the EXPLAIN Command in PostgreSQLArun Nanda•May 16, 2024•5 min readArticleHow to Read PostgreSQL Query PlansArun Nanda•May 16, 2024•10 min read!Airbyte is an open-source data integration engine that helps you consolidate your data in your data warehouses, lakes and databases.!!!!



Documentation Source:
airbyte.com/tutorials/postgresql-change-data-capture-elt.md

Documentation Title:
Build an EL(T) from Postgres CDC (Change Data Capture) | Airbyte

Documentation Content:
Additionally, you'll require a logical decoding plugin, such as pgoutput or wal2json, which converts the WAL records into a format that can be consumed by downstream applications or systems.
9. **Can CDC in PostgreSQL capture all types of data modifications, including inserts, updates, and deletions?**
10. Yes, CDC in PostgreSQL can capture all types of data modifications, including inserts, updates, and deletions. By monitoring changes at the database level and utilizing logical decoding, PostgreSQL CDC ensures that all modifications to database records are captured and made available for replication or analysis.
11. **How does CDC ensure data consistency and integrity when replicating data from PostgreSQL using a data replication tool?**
12. CDC guarantees data consistency and integrity when replicating PostgreSQL data with Airbyte by continuously monitoring database changes, capturing all modifications (inserts, updates, and deletions), and preserving the order of operations during replication. Airbyte's incremental replication minimizes latency, and its built-in data validation and error handling mechanisms ensure accuracy and reliability.

!### About the Author

Thalia Barrera is a data engineer and technical writer at Airbyte. She has over a decade of experience as an engineer in the IT industry. She enjoys crafting technical and training materials for fellow engineers. Drawing on her computer science expertise and client-oriented nature, she loves turning complex topics into easy-to-understand content.

!!!### About the Author

!!Text LinkJoin our newsletter to get all the insights on the data stack
-------------------------------------------------------------



