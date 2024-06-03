Documentation Source:
docs.getdbt.com/docs/build/snapshots.md

Documentation Title:
Add snapshots to your DAG | dbt Developer Hub

Documentation Content:
You'll also need to configure your snapshot to tell dbt how to detect record changes.

snapshots/orders\_snapshot.sql`{%snapshotorders_snapshot %}{{config(target_database='analytics',target_schema='snapshots',unique_key='id',strategy='timestamp',updated_at='updated_at',)}}select*from{{ source('jaffle_shop','orders')}}{%endsnapshot %}`Preview or Compile Snapshots in IDEIt is not possible to "preview data" or "compile sql" for snapshots in dbt Cloud. Instead, run the `dbt snapshot`command in the IDE by completing the following steps.

When you run the `dbt snapshot`command:

* **On the first run:**dbt will create the initial snapshot table — this will be the result set of your `select`statement, with additional columns including `dbt_valid_from`and `dbt_valid_to`. All records will have a `dbt_valid_to = null`.
* **On subsequent runs:**dbt will check which records have changed or if any new records have been created:
	+ The `dbt_valid_to`column will be updated for any existing records that have changed
	+ The updated record and any new records will be inserted into the snapshot table. These records will now have `dbt_valid_to = null`

Snapshots can be referenced in downstream models the same way as referencing models — by using the reffunction.

Example​
--------

To add a snapshot to your project:

1. Create a file in your `snapshots`directory with a `.sql`file extension, e.g. `snapshots/orders.sql`
2. Use a `snapshot`block to define the start and end of a snapshot:

snapshots/orders\_snapshot.sql`{%snapshotorders_snapshot %}{%endsnapshot %}`- Write a `select`statement within the snapshot block (tips for writing a good snapshot query are below). This select statement defines the results that you want to snapshot over time. You can use `sources`and `refs`here.
snapshots/orders\_snapshot.sql`{%snapshotorders_snapshot %}select*from{{ source('jaffle_shop','orders')}}{%endsnapshot %}`Check whether the result set of your query includes a reliable timestamp column that indicates when a record was last updated.



Documentation Source:
docs.getdbt.com/docs/build/snapshots.md

Documentation Title:
Add snapshots to your DAG | dbt Developer Hub

Documentation Content:
For our example, the `updated_at`column reliably indicates record changes, so we can use the `timestamp`strategy. If your query result set does not have a reliable timestamp, you'll need to instead use the `check`strategy — more details on this below.

Add configurations to your snapshot using a `config`block (more details below). You can also configure your snapshot from your `dbt_project.yml`file (docs).


snapshots/orders\_snapshot.sql`{%snapshotorders_snapshot %}{{config(target_database='analytics',target_schema='snapshots',unique_key='id',strategy='timestamp',updated_at='updated_at',)}}select*from{{ source('jaffle_shop','orders')}}{%endsnapshot %}`- Run the `dbt snapshot`command— for our example a new table will be created at `analytics.snapshots.orders_snapshot`. You can change the `target_database`configuration, the `target_schema`configuration and the name of the snapshot (as defined in `{% snapshot .. %}`) will change how dbt names this table.
`$ dbt snapshotRunning with dbt=0.16.015:07:36 | Concurrency: 8 threads (target='dev')15:07:36 |15:07:36 | 1 of 1 START snapshot snapshots.orders_snapshot...... [RUN]15:07:36 | 1 of 1 OK snapshot snapshots.orders_snapshot..........[SELECT 3 in 1.82s]15:07:36 |15:07:36 | Finished running 1 snapshots in 0.68s.Completed successfullyDone. PASS=2 ERROR=0 SKIP=0 TOTAL=1`Inspect the results by selecting from the table dbt created. After the first run, you should see the results of your query, plus the snapshot meta fieldsas described below.

Run the `snapshot`command again, and inspect the results. If any records have been updated, the snapshot should reflect this.

Select from the `snapshot`in downstream models using the `ref`function.



Documentation Source:
docs.getdbt.com/docs/build/snapshots.md

Documentation Title:
Add snapshots to your DAG | dbt Developer Hub

Documentation Content:
Snapshot source data.​

Your models should then select from these snapshots, treating them like regular data sources. As much as possible, snapshot your source data in its raw form and use downstream models to clean up the data



Documentation Source:
docs.getdbt.com/faqs/Project/source-has-bad-name.md

Documentation Title:
What if my source is in a poorly named schema or table? | dbt Developer Hub

Documentation Content:
models/.yml`version:2sources:-name:jaffle_shopschema:postgres_backend_public_schemadatabase:rawtables:-name:ordersidentifier:api_orders`In a downstream model:

select\*from{{ source('jaffle\_shop','orders')}}Will get compiled to:

select\*fromraw.postgres\_backend\_public\_schema.api\_orders0Edit this pageLast updatedon May 16, 2024PreviousProfiles stored outside projectNextSource is in a different database to target databaseTerms of ServicePrivacy PolicySecurityCookie Settings© 2024 dbt Labs, Inc. All Rights Reserved.



