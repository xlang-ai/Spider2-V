Documentation Source:
release-1-7-2.dagster.dagster-docs.io/concepts/io-management/io-managers.md

Documentation Title:
I/O managers | Dagster

Documentation Content:
Rather than update the I/O manager of the first asset to be able to load as a Pandas DataFrame and a NumPy array, you can write a new loader for the new asset.

In this example, we store `upstream_asset`as a Pandas DataFrame, and we write a new I/O manager to load is as a NumPy array in `downstream_asset`

`classPandasAssetIOManager(ConfigurableIOManager):defhandle_output(self,context:OutputContext,obj):file_path =self._get_path(context)store_pandas_dataframe(name=file_path,table=obj)def_get_path(self,context):returnos.path.join("storage",f"{context.asset_key.path[-1]}.csv",)defload_input(self,context:InputContext)->pd.DataFrame:file_path =self._get_path(context)returnload_pandas_dataframe(name=file_path)classNumpyAssetIOManager(PandasAssetIOManager):defload_input(self,context:InputContext)->np.ndarray:file_path =self._get_path(context)returnload_numpy_array(name=file_path)@asset(io_manager_key="pandas_manager")defupstream_asset()->pd.DataFrame:returnpd.DataFrame([1,2,3])@asset(ins={"upstream":AssetIn(key_prefix="public",input_manager_key="numpy_manager")})defdownstream_asset(upstream:np.ndarray)->tuple:returnupstream.shape


defs =Definitions(assets=[upstream_asset,downstream_asset],resources={"pandas_manager":PandasAssetIOManager(),"numpy_manager":NumpyAssetIOManager(),},)`Testing an I/O manager#
-----------------------

The easiest way to test an I/O manager is to construct an `OutputContext`or `InputContext`and pass it to the `handle_output`or `load_input`method of the I/O manager. The `build_output_context`and `build_input_context`functions allow for easy construction of these contexts.

Here's an example for a simple I/O manager that stores outputs in an in-memory dictionary that's keyed on the step and name of the output.



Documentation Source:
release-1-7-2.dagster.dagster-docs.io/concepts/io-management/io-managers-legacy.md

Documentation Title:
IO Managers (Legacy) | Dagster

Documentation Content:
In this example, we store `upstream_asset`as a Pandas DataFrame, and we write a new IO manager to load is as a NumPy array in `downstream_asset`

`classPandasAssetIOManager(IOManager):defhandle_output(self,context,obj):file_path =self._get_path(context)store_pandas_dataframe(name=file_path,table=obj)def_get_path(self,context):returnos.path.join("storage",f"{context.asset_key.path[-1]}.csv",)defload_input(self,context):file_path =self._get_path(context)returnload_pandas_dataframe(name=file_path)@io_managerdefpandas_asset_io_manager():returnPandasAssetIOManager()classNumpyAssetIOManager(PandasAssetIOManager):defload_input(self,context):file_path =self._get_path(context)returnload_numpy_array(name=file_path)@io_managerdefnumpy_asset_io_manager():returnNumpyAssetIOManager()@asset(io_manager_key="pandas_manager")defupstream_asset():returnpd.DataFrame([1,2,3])@asset(ins={"upstream":AssetIn(key_prefix="public",input_manager_key="numpy_manager")})defdownstream_asset(upstream):returnupstream.shape


defs =Definitions(assets=[upstream_asset,downstream_asset],resources={"pandas_manager":pandas_asset_io_manager,"numpy_manager":numpy_asset_io_manager,},)`Testing an IO manager#
----------------------

The easiest way to test an IO manager is to construct an `OutputContext`or `InputContext`and pass it to the `handle_output`or `load_input`method of the IO manager. The `build_output_context`and `build_input_context`functions allow for easy construction of these contexts.

Here's an example for a simple IO manager that stores outputs in an in-memory dictionary that's keyed on the step and name of the output.

`fromdagster importIOManager,build_input_context,build_output_context,io_manager



Documentation Source:
release-1-7-2.dagster.dagster-docs.io/concepts/partitions-schedules-sensors/partitioning-assets.md

Documentation Title:
Partitioning assets | Dagster

Documentation Content:
Partitioned assets with partitioned I/O managers

**Heads up!**Familiarity withI/O managersis required for this section.Asset functions can write data out to files, but they can also delegate the writing operation to an I/O manager. Dagster's built-in I/O managerssupport handling partitioned assets, but you can also write your own I/O managerif you want additional customization.

For example, the following demonstrates how to define an asset that relies on an I/O manager to store its output:

`importpandas aspd

fromdagster importAssetExecutionContext,DailyPartitionsDefinition,asset


@asset(partitions_def=DailyPartitionsDefinition(start_date="2022-01-01"))defmy_daily_partitioned_asset(context:AssetExecutionContext)->pd.DataFrame:partition_date_str =context.partition_key
 returnpd.read_csv(f"coolweatherwebsite.com/weather_obs&date={partition_date_str}")`If using the default I/O manager, materializing partition `2022-07-23`of this asset would store the output `DataFrame`in a pickle file at a path like `my_daily_partitioned_asset/2022-07-23`.

Relevant APIs#
--------------



Documentation Source:
release-1-7-2.dagster.dagster-docs.io/concepts/io-management/io-managers.md

Documentation Title:
I/O managers | Dagster

Documentation Content:
A custom I/O manager that stores Pandas DataFrames in tables

If your ops produce Pandas DataFrames that populate tables in a data warehouse, you might write something like the following. This I/O manager uses the name assigned to the output as the name of the table to write the output to.

`fromdagster importConfigurableIOManager,io_manager


classDataframeTableIOManager(ConfigurableIOManager):defhandle_output(self,context:OutputContext,obj):# name is the name given to the Out that we're storing fortable_name =context.name
 write_dataframe_to_table(name=table_name,dataframe=obj)defload_input(self,context:InputContext):# upstream_output.name is the name given to the Out that we're loading forifcontext.upstream_output:table_name =context.upstream_output.name
 returnread_dataframe_from_table(name=table_name)@job(resource_defs={"io_manager":DataframeTableIOManager()})defmy_job():op_2(op_1())`### Custom filesystem-based I/O manager#

Dagster provides a feature-rich base class for filesystem-based I/O managers: `UPathIOManager`. It's compatible with both local and remote filesystems (like S3 or GCS) by using `universal-pathlib`and `fsspec`. The full list of supported filesystems can be found here. The `UPathIOManager`also has other important features:

* handles partitioned assets
* handles loading a single upstream partition
* handles loading multiple upstream partitions (with respect to `PartitionMapping`)
* the `get_metadata`method can be customized to add additional metadata to the output
* the `allow_missing_partitions`metadata value can be set to `True`to skip missing partitions (the default behavior is to raise an error)

The default I/O manager inherits from the `UPathIOManager`and therefore has these features too.

The `UPathIOManager`already implements the `load_input`and `handle_output`methods. Instead, if you want to write a custom `UPathIOManager`the `UPathIOManager.dump_to_path`and `UPathIOManager.load_from_path`for a given `universal_pathlib.UPath`should to be implemented.



