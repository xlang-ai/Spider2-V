Documentation Source:
airbyte.com/docs.airbyte.com/integrations/sources/faker.md

Documentation Title:
Faker | Airbyte Documentation

Documentation Content:
Output schema​

This source will generate an "e-commerce-like" dataset with users, products, and purchases. Here's
what is produced at a Postgres destination connected to this source:

`CREATETABLE"public"."users"("address"jsonb,"occupation"text,"gender"text,"academic_degree"text,"weight"int8,"created_at"timestamptz,"language"text,"telephone"text,"title"text,"updated_at"timestamptz,"nationality"text,"blood_type"text,"name"text,"id"float8,"age"int8,"email"text,"height"text,-- "_airbyte_ab_id" varchar,-- "_airbyte_emitted_at" timestamptz,-- "_airbyte_normalized_at" timestamptz,-- "_airbyte_users_hashid" text);CREATETABLE"public"."users_address"("_airbyte_users_hashid"text,"country_code"text,"province"text,"city"text,"street_number"text,"state"text,"postal_code"text,"street_name"text,-- "_airbyte_ab_id" varchar,-- "_airbyte_emitted_at" timestamptz,-- "_airbyte_normalized_at" timestamptz,-- "_airbyte_address_hashid" text);CREATETABLE"public"."products"("id"float8,"make"text,"year"float8,"model"text,"price"float8,"created_at"timestamptz,-- "_airbyte_ab_id" varchar,-- "_airbyte_emitted_at" timestamptz,-- "_airbyte_normalized_at" timestamptz,-- "_airbyte_dev_products_hashid" text,);CREATETABLE"public"."purchases"("id"float8,"user_id"float8,"product_id"float8,"purchased_at"timestamptz,"added_to_cart_at"timestamptz,"returned_at"timestamptz,-- "_airbyte_ab_id" varchar,-- "_airbyte_emitted_at" timestamptz,-- "_airbyte_normalized_at" timestamptz,-- "_airbyte_dev_purchases_hashid" text,);`### Features​



Documentation Source:
airbyte.com/tutorials/configure-airbyte-with-python-dagster.md

Documentation Title:
Configure Airbyte Connections with Python (Dagster) | Airbyte

Documentation Content:
The AirbyteConnectionsets configure both together as a connection in Airbyte.

These features open instrumental use cases for **data integration as code**. Imagine you need to provision Airbyte, have multi-tenancy requirements for teams or customers, or read from a dynamic API (imagine the Notion API where the content is nested into the databases and constantly evolves). Based on these configs, you can automatically apply new sync based on the latest status. Everything is versioned, which leads to changes with confidence.

*How does it work*So much for when to use it. Let's explore now how it all works.

Dagster offers the interfaces that we can define our Airbyte connections with Python and a command line tool called dagster-airbytethat allows two functions to check or apply the defined connections to the Airbyte instance.

As the name suggests, checking is verifying against the current live Airbyte instance vs. your pythonic configurations. Apply will delete an existing source, destination, and connection and re-apply based on your updated configs.

📝 Below, I will skip the step on setting up Airbyte and Postgres database; You can find that in the ReadMeor Postgres Replication Tutorial.

*Configure Airbyte Connections in Python*For my demo, I am scraping a GitHub repo that is evolving.

**Define Airbyte Instance**First, I define the airbyte instance in my dagster python code:

`airbyte_instance = airbyte_resource.configured(
 {
 "host": "localhost",
 "port": "8000",
 "username": "airbyte",
 "password": {"env": "AIRBYTE_PASSWORD"},
 }
)`➡️ Make sure you set the environment variable AIRBYTE\_PASSWORD on your laptop. The default password is password. As well as createa token AIRBYTE\_PERSONAL\_GITHUB\_TOKEN for fetching the stargazers from the public repositories in the below code.



Documentation Source:
airbyte.com/docs.airbyte.com/integrations/sources/postgres/cloud-sql-postgres.md

Documentation Title:
Cloud SQL for PostgreSQL | Airbyte Documentation

Documentation Content:
Step 1: Create a dedicated read-only Postgres user​

These steps create a dedicated read-only user for replicating data. Alternatively, you can use an existing Postgres user in your database. To create a user, first connect to your database. If you are getting started, you can use Cloud Shell to connect directly from the UI.

The following commands will create a new user:

CREATE USER  PASSWORD 'your\_password\_here';Now, provide this user with read-only access to relevant schemas and tables. Re-run this command for each schema you expect to replicate data from (e.g. `public`):

`GRANT USAGE ON SCHEMA  TO ;GRANT SELECT ON ALL TABLES IN SCHEMA  TO ;ALTER DEFAULT PRIVILEGES IN SCHEMA  GRANT SELECT ON TABLES TO ;`#### Step 2: Create a new Postgres source in Airbyte UI​

From your Airbyte Cloudor Airbyte Open Source account, select `Sources`from the left navigation bar, search for `Postgres`, then create a new Postgres source.

!To fill out the required information:

1. Enter the hostname, port number, and name for your Postgres database.
2. You may optionally opt to list each of the schemas you want to sync. These are case-sensitive, and multiple schemas may be entered. By default, `public`is the only selected schema.
3. Enter the username and password you created in Step 1.
4. Select an SSL mode. You will most frequently choose `require`or `verify-ca`. Both of these always require encryption. `verify-ca`also requires certificates from your Postgres database. See here to learn about other SSL modes and SSH tunneling.
5. Select `Standard (xmin)`from available replication methods. This uses the xmin system columnto reliably replicate data from your database.
6. If your database is particularly large (> 500 GB), you will benefit from configuring your Postgres source using logical replication (CDC).



Documentation Source:
airbyte.com/docs.airbyte.com/integrations/sources/faker.md

Documentation Title:
Faker | Airbyte Documentation

Documentation Content:
Config fields reference

FieldTypeProperty name›Countintegercount›Seedintegerseed›Records Per Stream Sliceintegerrecords\_per\_slice›Always Updatedbooleanalways\_updated›ParallelismintegerparallelismChangelog​
----------



| Version | Date | Pull Request | Subject |
| --- | --- | --- | --- |
| 6.1.0 | 2024-04-08 |36898 Update car prices and years |
| --- | --- | --- |
| 6.0.3 | 2024-03-15 |36167 Make 'count' an optional config parameter. |
| 6.0.2 | 2024-02-12 |35174 Manage dependencies with Poetry. |
| 6.0.1 | 2024-02-12 |35172 Base image migration: remove Dockerfile and use the python-connector-base image |
| 6.0.0 | 2024-01-30 |34644 Declare 'id' columns as primary keys.



