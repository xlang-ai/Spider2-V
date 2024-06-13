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
this example uses the iris_dataset asset from Step 2@assetdefiris_setosa(iris_dataset:pd.DataFrame)->pd.DataFrame:returniris_dataset[iris_dataset["species"]=="Iris-setosa"]`In this asset, you're providing the `iris_dataset`asset as a dependency to `iris_setosa`. By supplying `iris_dataset`as a parameter to `iris_setosa`, Dagster knows to use the `DuckDBPandasIOManager`to load this asset into memory as a Pandas DataFrame and pass it as an argument to `iris_setosa`. Next, a DataFrame that only contains the data for the *Iris Setosa*species is created and returned. Then the `DuckDBPandasIOManager`will store the DataFrame as the `IRIS.IRIS_SETOSA`table in DuckDB.



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
@assetdefiris_dataset()->pd.DataFrame:returnpd.read_csv("https://docs.dagster.io/assets/iris.csv",names=["sepal_length_cm","sepal_width_cm","petal_length_cm","petal_width_cm","species",],)`In this example, you're defining an asset that fetches the Iris dataset as a Pandas DataFrame, renames the columns, then returns the DataFrame. The type signature of the function tells the I/O manager what data type it is working with, so it is important to include the return type `pd.DataFrame`.

When Dagster materializes the `iris_dataset`asset using the configuration from Step 1: Configure the DuckDB I/O manager, the DuckDB I/O manager will create the table `IRIS.IRIS_DATASET`if it does not exist and replace the contents of the table with the value returned from the `iris_dataset`asset.



