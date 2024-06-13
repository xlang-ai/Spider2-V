Documentation Source:
release-1-7-2.dagster.dagster-docs.io/concepts/partitions-schedules-sensors/partitioning-assets.md

Documentation Title:
Partitioning assets | Dagster

Documentation Content:
If the asset is stored in a database, then each partition will typically correspond to a range of values in a table that fall within a particular window.

The following example demonstrates creating an asset that has a partition for each day since October 1st, 2023. Materializing partition `2023-11-13`of this asset would result in fetching data from the URL `https://api.nasa.gov/planetary/apod?date=2023-11-13`and storing it at the path `nasa/2023-11-13.csv`. Note that `api_key=DEMO_KEY`is used but has a limited number of calls:

`importos
importurllib.request



Documentation Source:
release-1-7-2.dagster.dagster-docs.io/concepts/partitions-schedules-sensors/partitioning-assets.md

Documentation Title:
Partitioning assets | Dagster

Documentation Content:
Create a new 'nasa' directory if neededdir_name ="nasa"ifnotos.path.exists(dir_name):os.makedirs(dir_name)fromdagster importAssetExecutionContext,DailyPartitionsDefinition,asset


@asset(partitions_def=DailyPartitionsDefinition(start_date="2023-10-01"))defmy_daily_partitioned_asset(context:AssetExecutionContext)->None:partition_date_str =context.partition_key

 url =f"https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&date={partition_date_str}"target_location =f"nasa/{partition_date_str}.csv"urllib.request.urlretrieve(url,target_location)`In the following sections, we'll demonstrate a few additional ways to partition assets:

* **Multi-dimensionally partitioning assets**, for when you want assets to be partitioned by multiple dimensions
* **Dynamically partitioning assets**, for when you don't know the partition set before defining assets



Documentation Source:
release-1-7-2.dagster.dagster-docs.io/_apidocs/execution.md

Documentation Title:
Dagster Docs

Documentation Content:
```
partitions_def=DailyPartitionsDefinition("2023-08-20")@asset(partitions_def=partitions_def)defan_asset(context:AssetExecutionContext):context.log.info(context.asset_partition_keys_for_output())# running a backfill of the 2023-08-21 through 2023-08-25 partitions of this asset will log:#   ["2023-08-21", "2023-08-22", "2023-08-23", "2023-08-24", "2023-08-25"]@multi_asset(outs={"first_asset":AssetOut(key=["my_assets","first_asset"]),"second_asset":AssetOut(key=["my_assets","second_asset"])}partitions_def=partitions_def,)defa_multi_asset(context:AssetExecutionContext):context.log.info(context.asset_partition_keys_for_output("first_asset"))context.log.info(context.asset_partition_keys_for_output("second_asset"))# running a backfill of the 2023-08-21 through 2023-08-25 partitions of this asset will log:#   ["2023-08-21", "2023-08-22", "2023-08-23", "2023-08-24", "2023-08-25"]#   ["2023-08-21", "2023-08-22", "2023-08-23", "2023-08-24", "2023-08-25"]@asset(partitions_def=partitions_def,ins={"self_dependent_asset":AssetIn(partition_mapping=TimeWindowPartitionMapping(start_offset=-1,end_offset=-1))})defself_dependent_asset(context:AssetExecutionContext,self_dependent_asset):context.log.info(context.asset_partition_keys_for_output())# running a backfill of the 2023-08-21 through 2023-08-25 partitions of this asset will log:#   ["2023-08-21", "2023-08-22", "2023-08-23", "2023-08-24", "2023-08-25"]
```
asset\_partitions\_def\_for\_input(input\_name)[source]¶The PartitionsDefinition on the upstream asset corresponding to this input.



Documentation Source:
release-1-7-2.dagster.dagster-docs.io/_apidocs/execution.md

Documentation Title:
Dagster Docs

Documentation Content:
```
partitions_def=DailyPartitionsDefinition("2023-08-20")@asset(partitions_def=partitions_def)defupstream_asset():...@asset(partitions_def=partitions_def)defan_asset(context:AssetExecutionContext,upstream_asset):context.log.info(context.asset_partition_keys_for_input("upstream_asset"))# running a backfill of the 2023-08-21 through 2023-08-25 partitions of this asset will log:#   ["2023-08-21", "2023-08-22", "2023-08-23", "2023-08-24", "2023-08-25"]@asset(ins={"upstream_asset":AssetIn(partition_mapping=TimeWindowPartitionMapping(start_offset=-1,end_offset=-1))}partitions_def=partitions_def,)defanother_asset(context:AssetExecutionContext,upstream_asset):context.log.info(context.asset_partition_keys_for_input("upstream_asset"))# running a backfill of the 2023-08-21 through 2023-08-25 partitions of this asset will log:#   ["2023-08-20", "2023-08-21", "2023-08-22", "2023-08-23", "2023-08-24"]@asset(partitions_def=partitions_def,ins={"self_dependent_asset":AssetIn(partition_mapping=TimeWindowPartitionMapping(start_offset=-1,end_offset=-1))})defself_dependent_asset(context:AssetExecutionContext,self_dependent_asset):context.log.info(context.asset_partition_keys_for_input("self_dependent_asset"))# running a backfill of the 2023-08-21 through 2023-08-25 partitions of this asset will log:#   ["2023-08-20", "2023-08-21", "2023-08-22", "2023-08-23", "2023-08-24"]
```
asset\_partition\_keys\_for\_output(*output\_name='result'*)[source]¶Returns a list of the partition keys for the given output.



