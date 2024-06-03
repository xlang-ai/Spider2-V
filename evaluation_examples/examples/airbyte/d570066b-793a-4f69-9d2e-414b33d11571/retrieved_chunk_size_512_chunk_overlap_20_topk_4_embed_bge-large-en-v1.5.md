Documentation Source:
airbyte.com/quickstart/airbyte-dbt-and-airflow-stack-with-bigquery.md

Documentation Title:
E-commerce Analytics Stack with Airbyte, dbt, Airflow (ADA) and BigQuery | Airbyte

Documentation Content:
3.2. Setting Up Airbyte Connectors Using the UI

Start by launching the Airbyte UI by going to http://localhost:8000/in your browser. Then:

**1. Create a source**:

1. Go to the "Sources" tab and click on "+ New source".
2. Search for “faker” using the search bar and select "Sample Data (Faker)".
3. Adjust the count and optional fields as needed for your use case. You can also leave as is.
4. Click on "Set up source".

**2. Create a destination**:

1. Go to the "Destinations" tab and click on "+ New destination".
2. Search for “bigquery” using the search bar and select BigQuery.
3. Enter the connection details as needed.
4. For simplicity, you can use "Standard Inserts" as the loading method.
5. In the Service Account Key JSON field, enter the contents of the JSON file. Yes, the full JSON.
6. Click on Set up destination.

**3. Create a connection**:

1. Go to the "Connections" tab and click on "+ New connection".
2. Select the source and destination you just created.
3. Enter the connection details as needed.
4. Click on "Set up connection".

That’s it! Your connection is set up and ready to go! 🎉 

4. Setting Up the dbt Project
-----------------------------

dbt (data build tool)allows you to transform your data by writing, documenting, and executing SQL workflows. Setting up the dbt project requires specifying connection details for your data platform, in this case, BigQuery. Here’s a step-by-step guide to help you set this up:



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
airbyte.com/tutorials/building-an-e-commerce-data-pipeline-a-hands-on-guide-to-using-airbyte-dbt-dagster-and-bigquery.md

Documentation Title:
How to build E-commerce Data Pipeline with Airbyte? | Airbyte

Documentation Content:
3. Create a connection:

* Go to the Connections tab and click on "+ New connection".
* Select the source and destination you just created.
* Enter the connection details as needed.
* For this project, leave the “replication frequency” as “Manual”, since we will orchestrate the syncs with Dagster.
* Click on "Set up connection".

That’s it! Your connection is set up and ready to go! 🎉

‍

!

Establish a connector between Faker and BigQuery

4. Setting Up the dbt Project
-----------------------------

dbt (data build tool)allows you to transform your data by writing, documenting, and executing SQL workflows. Setting up the dbt project requires specifying connection details for your data platform, in this case, BigQuery.



Documentation Source:
airbyte.com/docs.airbyte.com/integrations/sources/faker.md

Documentation Title:
Faker | Airbyte Documentation

Documentation Content:
| Feature | Supported?(Yes/No) | Notes |
| --- | --- | --- |
| Full Refresh Sync | Yes |
| --- | --- |
| Incremental Sync | Yes |
| Namespaces | No |

Of note, if you choose `Incremental Sync`, state will be maintained between syncs, and once you hit
`count`records, no new records will be added.

You can choose a specific `seed`(integer) as an option for this connector which will guarantee that
the same fake records are generated each time. Otherwise, random data will be created on each
subsequent sync.



