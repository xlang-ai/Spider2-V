Documentation Source:
airbyte.com/tutorials/postgres-replication.md

Documentation Title:
Postgres Replication: Data Transfer Efficiency | Airbyte

Documentation Content:
Prerequisites
-------------

* Having Dockerand Docker Composeinstalled.
* Deploying Airbyte.
Step 1: Set up your source Postgres database (optional)
-------------------------------------------------------

If you don’t have a readily available Postgres database to sync, here are some quick instructions. Run the following commands in a new terminal window to start backgrounded source and destination databases:

`docker run --rm --name airbyte-source -e POSTGRES_PASSWORD=password -p 2000:5432 -d postgres
docker run --rm --name airbyte-destination -e POSTGRES_PASSWORD=password -p 3000:5432 -d postgres`Add two tables with a few rows to the source database:

`docker exec -it airbyte-source psql -U postgres -c "CREATE TABLE users(id SERIAL PRIMARY KEY, col1 VARCHAR(200));"
docker exec -it airbyte-source psql -U postgres -c "INSERT INTO public.users(col1) VALUES('record1');"
docker exec -it airbyte-source psql -U postgres -c "INSERT INTO public.users(col1) VALUES('record2');"
docker exec -it airbyte-source psql -U postgres -c "INSERT INTO public.users(col1) VALUES('record3');"

docker exec -it airbyte-source psql -U postgres -c "CREATE TABLE cities(city_code VARCHAR(8), city VARCHAR(200));"
docker exec -it airbyte-source psql -U postgres -c "INSERT INTO public.cities(city_code, city) VALUES('BCN', 'Barcelona');"
docker exec -it airbyte-source psql -U postgres -c "INSERT INTO public.cities(city_code, city) VALUES('MAD', 'Madrid');" 
docker exec -it airbyte-source psql -U postgres -c "INSERT INTO public.cities(city_code, city) VALUES('VAL', 'Valencia');"`You now have a Postgres database ready to be replicated.

Alternatively, you can use a local Postgres database on your computer: use *host.docker.internal*(if you are on Mac) as the host instead of *localhost*when setting up the source and destination.



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
Insert a new record on the source

If you don’t have a terminal open on the Postgres source database, open one as follows: 

`docker exec -it airbyte-source /bin/bash
psql --username=postgres`‍

Add a new record to the source Postgres database as follows:

`INSERT INTO full_refresh_demo(id, name) VALUES(3, 'Alex M');`‍

And view the source table by executing: 

`SELECT * FROM full_refresh_demo;`‍

The source table should look as follows:

`id | name 
----+--------
 1 | Mary X
 2 | John D
 3 | Alex M
(3 rows)`Execute a new sync by clicking on **Sync Now**in the connection pane and wait for the sync to complete. 

‍

!‍

Once complete, you should see that three records have been emitted. Also take note of the **job ID**and **attempt ID**, which are 104 and 0 for this run.



Documentation Source:
airbyte.com/tutorials/full-data-synchronization.md

Documentation Title:
Explore Airbyte's full refresh data synchronization | Airbyte

Documentation Content:
Open a Postgres terminal in the destination container

‍

Now that the first sync has completed you can take a look at the Postgres destination to see how the replicated data looks. Execute the following command to open a shell to the destination Postgres database:

`docker exec -it airbyte-destination /bin/bashpsql --username=postgres
psql --username=postgres`### Look at the data in the Postgres destination

You can view the tables in the destination Postgres database by executing the following command from the Postgres shell that you have just opened . 

`\dt;`‍

Which should respond with the following: 

`List of relations
 Schema | Name | Type | Owner 
--------+------------------------------------------+-------+----------
 public | _airbyte_raw_overwrite_full_refresh_demo | table | postgres
 public | overwrite_full_refresh_demo | table | postgres
(2 rows)`‍


> ℹ️  Notice that there are two tables. As discussed earlier, Airbyte converts each source record into a JSON blob that contains all of your data, and writes it into the **\_airbyte\_raw\_overwrite\_full\_refresh\_demo**table. This is then normalized into a separate table.



