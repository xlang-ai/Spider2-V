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
`data-diff \
"snowflake://external_user:[password]@[account]/development/customers?warehouse=validator_wh&role=validator" customer_contacts \
"postgresql://madison'[password]@localhost:5432/development" customer_contacts \
-c customer_contact_id customer_name phone_number email_address updated_at`Another thing to note, if your primary keys are not `id`, then you’ll have to specify another parameter called `key column` in your connection string. This just lets data-diff know which column acts as a primary key, allowing the two tables to be compared using that.

Since the primary key of these tables is `customer\_contact\_id` I would add that to the `key-columns` (or just `k`)  flag in my command. Like this:

`data-diff \
"snowflake://external_user:[password]@[password]/development/customers?warehouse=validator_wh&role=validator" customer_contacts \
"postgresql://madison:[password]@localhost:5432/development" customer_contacts \
-columns customer_contact_id customer_name phone_number email_address updated_at \
-key-columns customer_contact_id`And, lastly, if you ever want to filter the column values that you are comparing, you can specify a `where` (or just `w`) flag in the command. This acts as a where clause for your query, allowing you to filter for certain conditions. This is particularly helpful if you have a fast-changing source and need to validate a new batch of data that has been ingested after a previous validation check. Using this will prevent false positives of rows that have been updated since being ingested when checking for differing rows. We can add this to our command like so:

`data-diff \
"snowflake://external_user:[password]@[account]/development/customers?warehouse=validator_wh&role=validator" customer_contacts \
"postgresql://madison:[password]@localhost:5432/development" customer_contacts \
-columns customer_contact_id customer_name phone_number email_address updated_at \
-key-columns customer_contact_id \
-where “updated_at <= '10-31-2022'"`Now we are ready to run data-diff!



