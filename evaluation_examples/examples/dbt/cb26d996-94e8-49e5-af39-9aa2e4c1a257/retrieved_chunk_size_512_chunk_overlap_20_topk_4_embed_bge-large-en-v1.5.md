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
docs.getdbt.com/docs/deploy/source-freshness.md

Documentation Title:
Source freshness | dbt Developer Hub

Documentation Content:
| Options | Outcomes |
| --- | --- |
|**Select checkbox**  The **Run source freshness**checkbox in your **Execution Settings**will run `dbt source freshness`as the first step in your job and won't break subsequent steps if it fails. If you wanted your job dedicated *exclusively*to running freshness checks, you still need to include at least one placeholder step, such as `dbt compile`. |
| --- |
|**Add as a run step** Add the `dbt source freshness`command to a job anywhere in your list of run steps. However, if your source data is out of date —this step will "fail", and subsequent steps will not run. dbt Cloud will trigger email notifications (if configured) based on the end state of this step. You can create a new job to snapshot source freshness. If you *do not*want your models to run if your source data is out of date, then it could be a good idea to run `dbt source freshness`as the first step in your job. Otherwise, we recommend adding `dbt source freshness`as the last step in the job, or creating a separate job just for this task. |

!Adding a step to snapshot source freshness### Source freshness snapshot frequency​

It's important that your freshness jobs run frequently enough to snapshot data latency in accordance with your SLAs. You can imagine that if you have a 1 hour SLA on a particular dataset, snapshotting the freshness of that tableonce daily would not be appropriate. As a good rule of thumb, you should run your source freshness jobs with at least double the frequency of your lowest SLA. Here's an example table of some reasonable snapshot frequencies given typical SLAs:



Documentation Source:
docs.getdbt.com/guides/snowflake.md

Documentation Title:
Quickstart for dbt Cloud and Snowflake | dbt Developer Hub

Documentation Content:
FAQs​

As I create more models, how should I keep my project organized? What should I name my models?Build models on top of sources​
-------------------------------

Sources make it possible to name and describe the data loaded into your warehouse by your extract and load tools. By declaring these tables as sources in dbt, you can:

* select from source tables in your models using the `{{ source() }}`function, helping define the lineage of your data
* test your assumptions about your source data
* calculate the freshness of your source data
Create a new YML file `models/sources.yml`.

2. Declare the sources by copying the following into the file and clicking **Save**.

models/sources.yml`version:2sources:-name:jaffle_shopdescription:This is a replica of the Postgres database used by our appdatabase:rawschema:jaffle_shoptables:-name:customersdescription:One record per customer.-name:ordersdescription:One record per order. Includes cancelled and deleted orders.`
3. Edit the `models/stg_customers.sql`file to select from the `customers`table in the `jaffle_shop`source.

models/stg\_customers.sql`selectid ascustomer_id,first_name,last_namefrom{{ source('jaffle_shop','customers')}}`
4. Edit the `models/stg_orders.sql`file to select from the `orders`table in the `jaffle_shop`source.

models/stg\_orders.sql`selectid asorder_id,user_id ascustomer_id,order_date,statusfrom{{ source('jaffle_shop','orders')}}`
5. Execute `dbt run`. 

The results of your `dbt run`will be exactly the same as the previous step. Your `stg_customers`and `stg_orders`models will still query from the same raw data source in Snowflake. By using `source`, you can
test and document your raw data and also understand the lineage of your sources.
Add tests to your models​
-------------------------

Adding teststo a project helps validate that your models are working correctly.

To add tests to your project:

Create a new YAML file in the `models`directory, named `models/schema.yml`

2.



