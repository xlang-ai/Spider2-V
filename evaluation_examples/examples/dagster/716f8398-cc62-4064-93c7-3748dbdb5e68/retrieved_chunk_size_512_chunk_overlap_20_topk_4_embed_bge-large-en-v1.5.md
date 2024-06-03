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
Rather than update the I/O manager of the first asset to be able to load as a Pandas DataFrame and a NumPy array, you can write a new loader for the new asset.

In this example, we store `upstream_asset`as a Pandas DataFrame, and we write a new I/O manager to load is as a NumPy array in `downstream_asset`

`classPandasAssetIOManager(ConfigurableIOManager):defhandle_output(self,context:OutputContext,obj):file_path =self._get_path(context)store_pandas_dataframe(name=file_path,table=obj)def_get_path(self,context):returnos.path.join("storage",f"{context.asset_key.path[-1]}.csv",)defload_input(self,context:InputContext)->pd.DataFrame:file_path =self._get_path(context)returnload_pandas_dataframe(name=file_path)classNumpyAssetIOManager(PandasAssetIOManager):defload_input(self,context:InputContext)->np.ndarray:file_path =self._get_path(context)returnload_numpy_array(name=file_path)@asset(io_manager_key="pandas_manager")defupstream_asset()->pd.DataFrame:returnpd.DataFrame([1,2,3])@asset(ins={"upstream":AssetIn(key_prefix="public",input_manager_key="numpy_manager")})defdownstream_asset(upstream:np.ndarray)->tuple:returnupstream.shape


defs =Definitions(assets=[upstream_asset,downstream_asset],resources={"pandas_manager":PandasAssetIOManager(),"numpy_manager":NumpyAssetIOManager(),},)`Testing an I/O manager#
-----------------------

The easiest way to test an I/O manager is to construct an `OutputContext`or `InputContext`and pass it to the `handle_output`or `load_input`method of the I/O manager. The `build_output_context`and `build_input_context`functions allow for easy construction of these contexts.

Here's an example for a simple I/O manager that stores outputs in an in-memory dictionary that's keyed on the step and name of the output.



Documentation Source:
release-1-7-2.dagster.dagster-docs.io/concepts/io-management/io-managers.md

Documentation Title:
I/O managers | Dagster

Documentation Content:
@assetdefupstream_asset():return[1,2,3]@assetdefdownstream_asset(upstream_asset):returnupstream_asset +[4]resources_by_env ={"prod":{"io_manager":S3PickleIOManager(s3_resource=S3Resource(),s3_bucket="my-bucket")},"local":{"io_manager":FilesystemIOManager()},}defs =Definitions(assets=[upstream_asset,downstream_asset],resources=resources_by_env[os.getenv("ENV","local")],)`### Asset input I/O managers#

In some cases you may need to load the input to an asset with different logic than that specified by the upstream asset's I/O manager.

To set an I/O manager for a particular input, use the `input_manager_key`argument on `AssetIn`.

In this example,`first_asset`and `second_asset`will be stored using the default I/O manager, but will be loaded as inputs to `third_asset`using the logic defined in the `PandasSeriesIOManager`(in this case loading as Pandas Series rather than Python lists).

`@assetdeffirst_asset()->List[int]:return[1,2,3]@assetdefsecond_asset()->List[int]:return[4,5,6]@asset(ins={"first_asset":AssetIn(input_manager_key="pandas_series"),"second_asset":AssetIn(input_manager_key="pandas_series"),})defthird_asset(first_asset:pd.Series,second_asset:pd.Series)->pd.Series:returnpd.concat([first_asset,second_asset,pd.Series([7,8])])defs =Definitions(assets=[first_asset,second_asset,third_asset],resources={"pandas_series":PandasSeriesIOManager(),},)`Using I/O managers with non-asset jobs#
---------------------------------------



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



