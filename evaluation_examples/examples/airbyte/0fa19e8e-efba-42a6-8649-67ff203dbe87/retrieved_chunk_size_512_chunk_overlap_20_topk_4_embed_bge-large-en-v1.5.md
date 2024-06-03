Documentation Source:
airbyte.com/tutorials/validate-data-replication-postgres-snowflake.md

Documentation Title:
Validate data replication pipelines from Postgres to Snowflake with data-diff | Airbyte

Documentation Content:
First, you’ll want to install the open-source tool. You can do this with the following command:

`pip install data-diff`Since you are using both Postgres and Snowflake, you want to install the drivers for these specific databases:

`pip install 'data-diff[postgresql]'
pip install 'data-diff[snowflake]'`After you’ve installed data-diff, you’ll have to focus on creating your connection strings. These contain key information about the database you are connecting to like the database user, password, host, account, database, schema, warehouse, and role. 

For Snowflake, your connection string will follow the following format:

`"snowflake://[username]:[password]@[account]/[DATABASE]/[SCHEMA]?warehouse=[WAREHOUSE]&role=[ROLE]"`Because the table I replicated into Snowflake is in the `development` database and `customers` schema, I’ll input this information into the string. I’ll also be using `external\_user` for my user, the `validator\_wh` for my warehouse, and the `validator’ role here. These are different from what I used in the loading process since this is a different step in the data pipeline. 

Make sure whatever role you are using has the appropriate permissions to access the table you are comparing! The user you are inputting in the string also has to be assigned the role you specified. 

My final connection string looks like so:

`"snowflake://external_user:[password]@[account]/development/customers?warehouse=validator_wh&role=validator"`For Postgres, the connection string will be formatted like so:

`postgresql://[username]:[password]@localhost:5432/[database]`I’m using the username and password that I typically use to connect to my Postgres database. Unfortunately, this is a personal username and password which is not a best practice. It’s always best to use a user that is created for the use of external tools like data-diff. This helps keep your databases secure and ensures you are always in tight control of access.



Documentation Source:
airbyte.com/tutorials/validate-data-replication-postgres-snowflake.md

Documentation Title:
Validate data replication pipelines from Postgres to Snowflake with data-diff | Airbyte

Documentation Content:
This helps keep your databases secure and ensures you are always in tight control of access.

My final connection string looks like so:

`postgresql://madison:[password]@localhost:5432/development`Now that you’ve built your connection strings, you can use them in the data-diff command, which looks like this:

`data-diff DB1_URI TABLE1_NAME DB2_URI TABLE2_NAME`You will input Snowflake’s connection string as DB1\_URI and Postgres’s as DB2\_URI. 

Although I’m choosing to do Snowflake first and Postges second, the order doesn’t matter. Then be sure to write the appropriate table names for each of the sources that you are comparing. Note that data-diff only allows you to compare two tables at one time rather than all of your tables in a schema. However, you could easily create a Python script using data-diff Python’s SDKthat loops through a list of table names, running the command for every pair of tables specified and outputting the results in a nicely formatted CSV file. 

Let’s start by comparing the `customer\_contacts` table in our customers schemas. Because the source and destination have the same table names, I would put `customer\_contacts` as my Snowflake table and `customer\_contacts` as my Postgres table. 

The command would look like this:

`data-diff \
"snowflake://external_user:[password]@[account]/development/customers?warehouse=validator_wh&role=validator" customer_contacts \
"postgresql://madison:[password]@localhost:5432/development" customer_contacts`Because we are activating Airbyte normalizationand Airbyte creates extra metadata columns (\_airbyte\_ab\_id, \_airbyte\_emitted\_at, \_airbyte\_\_hashid, airbyte\_normalized\_at), on the Snowflake destination, we will have to specify the specific column names that we wish to compare. Otherwise, data-diff would mark all rows as varying due to the differing columns. In order to specify columns to include, we need to use the flag `columns` (or just `c`) in the command.



Documentation Source:
airbyte.com/tutorials/validate-data-replication-postgres-snowflake.md

Documentation Title:
Validate data replication pipelines from Postgres to Snowflake with data-diff | Airbyte

Documentation Content:
Set up a Postgres to Snowflake connection

Now that you’ve created both your source in Postgres and your destination in Snowflake, you can set up a connection between the two to replicate your data from Postgres. Select “connections” on the left panel.

Select your Postgres source you created from the dropdown, then select Snowflake as your destination.

Now you’ll want to give the connection a good name and choose how often it replicates. I’m going to call mine “postgres\_snowflake\_replication” and set it t replicate every 24 hours. 

!I also recommend selecting “mirror source structure” for the “destination namespace”. This will allow you to easily compare the differences between the source table and the destination table. Your data will be replicated to the database “development” and the schema “customers”, with the same table names. If the naming convention were different, it may get confusing down the line. 

!When you choose the streams you wish to activate, be sure that you are selecting “full refresh | overwrite”. This will capture any deletes or updates in your source data table through the replication process. 

Select “Normalized tabular data” and create your connection. Once you set up your connection, you should see your data syncing. 

‍

!When your connection is finished syncing and reads “successful”, you are ready to begin the validation process! 

Validate the replication process with data-diff
-----------------------------------------------

Now that you have your Postgres database replicated to Snowflake, you want to validate that your data looks as expected. Normally you would have to go through a long process of performing different discovery queries on each data source and comparing values. And, unless you looked at every single row and did a row-by-row comparison, you wouldn’t be confident that your data replicated as expected. This is where data-diff comes in. Let’s walk through how to set this up.

First, you’ll want to install the open-source tool.



Documentation Source:
airbyte.com/tutorials/validate-data-replication-postgres-snowflake.md

Documentation Title:
Validate data replication pipelines from Postgres to Snowflake with data-diff | Airbyte

Documentation Content:
Understanding data-diff output

Once you run the command, data-diff will give you the primary key values of the rows in the tables that differ. Each value will have a + or - in front of it. A + signifies that the rows exists in the second table but not the first. A - sign indicates that the row exists in the first table but not the second. Now, you can dig deeper into your validation process and explore *why* these primary keys are in one database and not the other.

!Also, note that one primary key can be present with a + and a - sign in the output. This means that the row *exists* in both tables but has a column value that varies. So not only does data-diff let you know when one table is missing a primary key, but it also lets you know when the column values for the rows with that primary key differ. 

I can see here that the row with a `customer\_contact\_id` of 14339589 is present in Postgres but not Snowflake. I’ll want to look into why this row wasn’t replicated from my source table to my destination. This will involve a deeper dive into your data and understanding its behavior. You may want to look into the following:

* Did my connection stop mid-way through its sync?
* Is there a condition in this particular row that’s now being met?
* Was this row created after the latest sync time?

If the opposite were to occur, where a row is present in Snowflake but not Postgres, you should ask yourself the following questions:

- Was this record deleted in my source table? Is that accurate? Did this happen after the latest sync?
And, if you have a row whose column values vary between the two tables, you should be thinking about these questions:

* Was this row updated after the latest sync time?
* What conditions could cause this value to be one thing in one table and something else in the other?

Data-diff frees up the most time-consuming, tedious task of finding the rows that differ in column values. It also allows you to fix these issues right then and there rather than reloading all of the data.



