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
`create table "postgres".public."table_one"
 as (
 
with __dbt__cte__table_one_ab1 as (

-- SQL model to parse JSON blob stored in a single column and extract into separated field columns as described by the JSON Schema
-- depends_on: "postgres".public._airbyte_raw_table_one
select
 jsonb_extract_path_text(_airbyte_data, 'id') as "id",
 jsonb_extract_path_text(_airbyte_data, 'name') as "name",
 jsonb_extract_path_text(_airbyte_data, 'updated_at') as updated_at,
 _airbyte_ab_id,
 _airbyte_emitted_at,
 now() as _airbyte_normalized_at
from "postgres".public._airbyte_raw_table_one as table_alias
-- table_one
where 1 = 1
),`‍

The next part of the SQL casts each field to the appropriate type as follows:

`__dbt__cte__table_one_ab2 as (

-- SQL model to cast each column to its adequate SQL type converted from the JSON schema type
-- depends_on: __dbt__cte__table_one_ab1
select
 cast("id" as 
 bigint
) as "id",
 cast("name" as text) as "name",
 cast(nullif(updated_at, '') as 
 timestamp
) as updated_at,
 _airbyte_ab_id,
 _airbyte_emitted_at,
 now() as _airbyte_normalized_at
from __dbt__cte__table_one_ab1
-- table_one
where 1 = 1

),`‍

The next part of the SQL adds an md5 hash.  

`__dbt__cte__table_one_ab3 as (

-- SQL model to build a hash column based on the values of this record
-- depends_on: __dbt__cte__table_one_ab2
select
 md5(cast(coalesce(cast("id" as text), '') || '-' || coalesce(cast("name" as text), '') || '-' || coalesce(cast(updated_at as text), '') as text)) as _airbyte_table_one_hashid,
 tmp.



Documentation Source:
airbyte.com/blog/synchronize-data-from-mongodb-to-postgresql-in-minutes.md

Documentation Title:
Synchronize Data from MongoDB to PostgreSQL in Minutes! | Airbyte

Documentation Content:
20k+ subscribers!Support centerAccess our knowledge base!CommunityJoin our 15,000+ data  community!Community Reward ProgramLeave your mark in the OSS community!Events & community callsLive events by the Airbyte team#### Our Social Platform

!Community forumGitHub Discussions for questions, ideas!Slack15,000+  share tips and get support!YoutubeLearn more about Airbyte and data engineering!Discourse (read-only)Previous forum (still lots of knowledge)ConnectorsPricingStarTalk to SalesTry it  freeCommunityVideoSynchronize Data from MongoDB to PostgreSQL in Minutes!
=======================================================

!Chris Sean•!•February 28, 2023•12 min watch!!!Limitless data movement with free Alpha and Beta connectorsIntroducing: our Free Connector Program ->The data movement infrastructure for the modern data teams.Try a 14-day free trial !### About the Author

!### About the Author

Table of contents
-----------------

Example H2Example H3Example H4Example H5Example H6Example H2Example H3Example H4Example H5Example H6Join our newsletter to get all the insights on the data stack
-------------------------------------------------------------

Related posts
-------------

VideoAre Building Custom ETL Pipelines Outdated?Chris Sean•April 28, 2023•8 min readArticleInk-credible Data People: Airbyte OSS Contributor Vincent KocKaren Bajza-Terlouw•March 1, 2023•6 min ArticleInk-credible Data People: Airbyte Blog Guest Author Madison MaeKaren Bajza-Terlouw•January 30, 2023•5 minArticleInk-credible Data People: Airbyte OSS Maintainer Yiyang LiKaren Bajza-Terlouw•December 6, 2022•5 min!Airbyte is an open-source data integration engine that helps you consolidate your data in your data warehouses, lakes and databases.!!!!



