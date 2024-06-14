Documentation Source:
release-1-7-2.dagster.dagster-docs.io/integrations/duckdb/using-duckdb-with-dagster.md

Documentation Title:
Using Dagster with DuckDB | Dagster Docs

Documentation Content:
Completed code example

When finished, your code should look like the following:

`importpandas aspd
fromdagster_duckdb_pandas importDuckDBPandasIOManager

fromdagster importDefinitions,SourceAsset,asset

iris_harvest_data =SourceAsset(key="iris_harvest_data")@assetdefiris_dataset()->pd.DataFrame:returnpd.read_csv("https://docs.dagster.io/assets/iris.csv",names=["sepal_length_cm","sepal_width_cm","petal_length_cm","petal_width_cm","species",],)@assetdefiris_setosa(iris_dataset:pd.DataFrame)->pd.DataFrame:returniris_dataset[iris_dataset["species"]=="Iris-setosa"]defs =Definitions(assets=[iris_dataset,iris_harvest_data,iris_setosa],resources={"io_manager":DuckDBPandasIOManager(database="path/to/my_duckdb_database.duckdb",schema="IRIS",)},)`Related#
--------

For more DuckDB features, refer to the DuckDB reference.

For more information on Software-defined Assets, refer to the tutorialor the Assets documentation.

For more information on I/O managers, refer to the I/O manager documentation.

On This Page- Using Dagster with DuckDB
	Prerequisites2. Option 1: Using the DuckDB resource
		Step 1: Configure the DuckDB resource2. Step 2: Create tables in DuckDB
			Create DuckDB tables in DagsterMaking Dagster aware of existing tables
		Step 3: Define downstream assetsCompleted code example
	3. Option 2: Using the DuckDB I/O manager
		Step 1: Configure the DuckDB I/O manager2. Step 2: Create tables in DuckDB
			Store a Dagster asset as a table in DuckDBMake an existing table available in Dagster
		Step 3: Load DuckDB tables in downstream assetsCompleted code example
	Related
Edit Page on GitHubShare FeedbackStar



Documentation Source:
release-1-7-2.dagster.dagster-docs.io/integrations/duckdb/using-duckdb-with-dagster.md

Documentation Title:
Using Dagster with DuckDB | Dagster Docs

Documentation Content:
this example uses the iris_dataset asset from Step 1@asset(deps=[iris_dataset])defiris_setosa(duckdb:DuckDBResource)->None:withduckdb.get_connection()asconn:conn.execute("CREATE TABLE iris.iris_setosa AS SELECT * FROM iris.iris_dataset WHERE"" species = 'Iris-setosa'")`In this asset, you're creating second table that only contains the data for the *Iris Setosa*species. This asset has a dependency on the `iris_dataset`asset. To define this dependency, you provide the `iris_dataset`asset as the `deps`parameter to the `iris_setosa`asset. You can then run the SQL query to create the table of *Iris Setosa*data.



Documentation Source:
release-1-7-2.dagster.dagster-docs.io/integrations/duckdb/using-duckdb-with-dagster.md

Documentation Title:
Using Dagster with DuckDB | Dagster Docs

Documentation Content:
Completed code example

When finished, your code should look like the following:

`importpandas aspd
fromdagster_duckdb importDuckDBResource

fromdagster importDefinitions,SourceAsset,asset

iris_harvest_data =SourceAsset(key="iris_harvest_data")@assetdefiris_dataset(duckdb:DuckDBResource)->None:iris_df =pd.read_csv("https://docs.dagster.io/assets/iris.csv",names=["sepal_length_cm","sepal_width_cm","petal_length_cm","petal_width_cm","species",],)withduckdb.get_connection()asconn:conn.execute("CREATE TABLE iris.iris_dataset AS SELECT * FROM iris_df")@asset(deps=[iris_dataset])defiris_setosa(duckdb:DuckDBResource)->None:withduckdb.get_connection()asconn:conn.execute("CREATE TABLE iris.iris_setosa AS SELECT * FROM iris.iris_dataset WHERE"" species = 'Iris-setosa'")defs =Definitions(assets=[iris_dataset],resources={"duckdb":DuckDBResource(database="path/to/my_duckdb_database.duckdb",)},)`Option 2: Using the DuckDB I/O manager#
---------------------------------------

You may want to use an I/O manager to handle storing DataFrames as tables in DuckDB and loading DuckDB tables as DataFrames in downstream assets. You may want to use an I/O manager if:

* You want your data to be loaded in memory so that you can interact with it using Python.
* You'd like to have Dagster manage how you store the data and load it as an input in downstream assets.

Using an I/O manager is not required, and you can reference When to use I/O managersto learn more.

This section of the guide focuses on storing and loading Pandas DataFrames in DuckDB, but Dagster also supports using PySpark and Polars DataFrames with DuckDB. The concepts from this guide apply to working with PySpark and Polars DataFrames, and you can learn more about setting up and using the DuckDB I/O manager with PySpark and Polars DataFrames in the reference guide.



Documentation Source:
release-1-7-2.dagster.dagster-docs.io/integrations/duckdb/using-duckdb-with-dagster.md

Documentation Title:
Using Dagster with DuckDB | Dagster Docs

Documentation Content:
this example uses the iris_dataset asset from Step 2@assetdefiris_setosa(iris_dataset:pd.DataFrame)->pd.DataFrame:returniris_dataset[iris_dataset["species"]=="Iris-setosa"]`In this asset, you're providing the `iris_dataset`asset as a dependency to `iris_setosa`. By supplying `iris_dataset`as a parameter to `iris_setosa`, Dagster knows to use the `DuckDBPandasIOManager`to load this asset into memory as a Pandas DataFrame and pass it as an argument to `iris_setosa`. Next, a DataFrame that only contains the data for the *Iris Setosa*species is created and returned. Then the `DuckDBPandasIOManager`will store the DataFrame as the `IRIS.IRIS_SETOSA`table in DuckDB.



