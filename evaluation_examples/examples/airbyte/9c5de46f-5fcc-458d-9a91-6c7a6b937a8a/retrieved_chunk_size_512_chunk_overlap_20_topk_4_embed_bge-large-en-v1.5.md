Documentation Source:
airbyte.com/tutorials/building-an-e-commerce-data-pipeline-a-hands-on-guide-to-using-airbyte-dbt-dagster-and-bigquery.md

Documentation Title:
How to build E-commerce Data Pipeline with Airbyte? | Airbyte

Documentation Content:
1. Create a source:

* Go to the Sources tab and click on "+ New source".
* Search for “faker” using the search bar and select "Sample Data (Faker)".
* Adjust the Count and optional fields as needed for your use case. You can also leave as is.
* Click on "Set up source".

!

Look fo Faker source connector

!

Create a Faker source



Documentation Source:
airbyte.com/quickstart/e-commerce-analytics-with-airbyte-dbt-dagster-and-bigquery.md

Documentation Title:
E-commerce Analytics Stack with Airbyte, dbt, Dagster and BigQuery | Airbyte

Documentation Content:
**1. Create a source**:

* Go to the Sources tab and click on "+ New source".
* Search for “faker” using the search bar and select "Sample Data (Faker)".
* Adjust the Count and optional fields as needed for your use case. You can also leave as is.
* Click on "Set up source".



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



