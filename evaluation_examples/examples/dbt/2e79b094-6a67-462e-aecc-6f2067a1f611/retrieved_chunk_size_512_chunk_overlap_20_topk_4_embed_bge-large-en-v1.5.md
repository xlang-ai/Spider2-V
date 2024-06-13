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
models/changed\_orders.sqlselect\*from{{ ref('orders\_snapshot')}}- Schedule the `snapshot`command to run regularly — snapshots are only useful if you run them frequently.
Detecting row changes​
----------------------

Snapshot "strategies" define how dbt knows if a row has changed. There are two strategies built-in to dbt — `timestamp`and `check`.



Documentation Source:
docs.getdbt.com/docs/build/snapshots.md

Documentation Title:
Add snapshots to your DAG | dbt Developer Hub

Documentation Content:
Timestamp strategy (recommended)​

The `timestamp`strategy uses an `updated_at`field to determine if a row has changed. If the configured `updated_at`column for a row is more recent than the last time the snapshot ran, then dbt will invalidate the old record and record the new one. If the timestamps are unchanged, then dbt will not take any action.

The `timestamp`strategy requires the following configurations:



| Config | Description | Example |
| --- | --- | --- |
| updated\_at | A column which represents when the source row was last updated |`updated_at`

**Example usage:**snapshots/orders\_snapshot\_timestamp.sql`{%snapshotorders_snapshot_timestamp %}{{config(target_schema='snapshots',strategy='timestamp',unique_key='id',updated_at='updated_at',)}}select*from{{ source('jaffle_shop','orders')}}{%endsnapshot %}`### Check strategy​

The `check`strategy is useful for tables which do not have a reliable `updated_at`column. This strategy works by comparing a list of columns between their current and historical values. If any of these columns have changed, then dbt will invalidate the old record and record the new one. If the column values are identical, then dbt will not take any action.

The `check`strategy requires the following configurations:



Documentation Source:
docs.getdbt.com/docs/build/snapshots.md

Documentation Title:
Add snapshots to your DAG | dbt Developer Hub

Documentation Content:
What are snapshots?​

Analysts often need to "look back in time" at previous data states in their mutable tables. While some source data systems are built in a way that makes accessing historical data possible, this is not always the case. dbt provides a mechanism, **snapshots**, which records changes to a mutable tableover time.

Snapshots implement type-2 Slowly Changing Dimensionsover mutable source tables. These Slowly Changing Dimensions (or SCDs) identify how a row in a table changes over time. Imagine you have an `orders`table where the `status`field can be overwritten as the order is processed.



| id | status | updated\_at |
| --- | --- | --- |
| 1 | pending | 2019-01-01 |

Now, imagine that the order goes from "pending" to "shipped". That same record will now look like:



| id | status | updated\_at |
| --- | --- | --- |
| 1 | shipped | 2019-01-02 |

This order is now in the "shipped" state, but we've lost the information about when the order was last in the "pending" state. This makes it difficult (or impossible) to analyze how long it took for an order to ship. dbt can "snapshot" these changes to help you understand how values in a row change over time. Here's an example of a snapshot table for the previous example:



| id | status | updated\_at | dbt\_valid\_from | dbt\_valid\_to |
| --- | --- | --- | --- | --- |
| 1 | pending | 2019-01-01 | 2019-01-01 | 2019-01-02 |
| --- | --- | --- | --- | --- |
| 1 | shipped | 2019-01-02 | 2019-01-02 |`null`

In dbt, snapshots are `select`statements, defined within a snapshot block in a `.sql`file (typically in your `snapshots`directory). You'll also need to configure your snapshot to tell dbt how to detect record changes.



