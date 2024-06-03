Documentation Source:
docs.getdbt.com/docs/build/sources.md

Documentation Title:
Add sources to your DAG | dbt Developer Hub

Documentation Content:
Declaring source freshness​

To configure sources to snapshot freshness information, add a `freshness`block to your source and `loaded_at_field`to your table declaration:

models/.yml`version:2sources:-name:jaffle_shopdatabase:rawfreshness:# default freshnesswarn_after:{count:12,period:hour}error_after:{count:24,period:hour}loaded_at_field:_etl_loaded_attables:-name:ordersfreshness:# make this a little more strictwarn_after:{count:6,period:hour}error_after:{count:12,period:hour}-name:customers # this will use the freshness defined above-name:product_skusfreshness:null# do not check freshness for this table`In the `freshness`block, one or both of `warn_after`and `error_after`can be provided. If neither is provided, then dbt will not calculate freshness snapshots for the tables in this source.

Additionally, the `loaded_at_field`is required to calculate freshness for a table. If a `loaded_at_field`is not provided, then dbt will not calculate freshness for the table.

These configs are applied hierarchically, so `freshness`and `loaded_at_field`values specified for a `source`will flow through to all of the `tables`defined in that source. This is useful when all of the tables in a source have the same `loaded_at_field`, as the config can just be specified once in the top-level source definition.



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
docs.getdbt.com/reference/resource-properties/freshness.md

Documentation Title:
freshness | dbt Developer Hub

Documentation Content:
Complete example​

models/.yml`version:2sources:-name:jaffle_shopdatabase:rawfreshness:# default freshnesswarn_after:{count:12,period:hour}error_after:{count:24,period:hour}loaded_at_field:_etl_loaded_attables:-name:customers # this will use the freshness defined above-name:ordersfreshness:# make this a little more strictwarn_after:{count:6,period:hour}error_after:{count:12,period:hour}# Apply a where clause in the freshness queryfilter:datediff('day',_etl_loaded_at,current_timestamp) < 2-name:product_skusfreshness:# do not check freshness for this table`When running `dbt source freshness`, the following query will be run:

* Compiled SQL
* Jinja SQL

`selectmax(_etl_loaded_at)asmax_loaded_at,convert_timezone('UTC',current_timestamp())assnapshotted_atfromraw.jaffle_shop.orderswheredatediff('day',_etl_loaded_at,current_timestamp)<2``selectmax({{ loaded_at_field }})asmax_loaded_at,{{ current_timestamp()}} assnapshotted_atfrom{{ source }}{%iffilter %}where{{ filter }}{%endif %}`Source code0Edit this pageLast updatedon May 16, 2024PreviousexternalNextidentifierDefinitionloaded\_at\_fieldcountperiodfilter* ExamplesComplete example

Edit this pageTerms of ServicePrivacy PolicySecurityCookie Settings© 2024 dbt Labs, Inc. All Rights Reserved.



Documentation Source:
docs.getdbt.com/reference/commands/source.md

Documentation Title:
About dbt source command | dbt Developer Hub

Documentation Content:
dbt source freshness​

If your dbt project is configured with sources, then the `dbt source freshness`command will query all of your defined source tables, determining the "freshness" of these tables. If the tables are stale (based on the `freshness`config specified for your sources) then dbt will report a warning or error accordingly. If a source tableis in a stale state, then dbt will exit with a nonzero exit code.



