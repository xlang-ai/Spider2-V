Documentation Source:
release-1-7-2.dagster.dagster-docs.io/integrations/dbt/using-dbt-with-dagster/upstream-assets.md

Documentation Title:
Using Dagster with dbt, part 3: Define assets upstream of your dbt models

Documentation Content:
You'll:

Install the Pandas and DuckDB Python librariesDefine an upstream Dagster assetIn the dbt project, replace a seed with a sourceMaterialize the assets using the Dagster UI
Step 1: Install the Pandas and DuckDB Python libraries#
-------------------------------------------------------

The Dagster asset that you write will fetch data using Pandasand write it out to your DuckDB warehouse using DuckDB's Python API. To use these, you'll need to install them:

`pip installpandas duckdb pyarrow`Step 2: Define an upstream Dagster asset#
-----------------------------------------

To fetch the data the dbt models require, we'll write a Dagster asset for `raw_customers`. We'll put this asset in our `assets.py`file, inside the `jaffle_dagster`directory. This is the file that contains the code that defines our dbt models, which we reviewed at the end of the last section. Copy and paste this code to overwrite the existing contents of that file:

`importos

importduckdb
importpandas aspd
fromdagster importAssetExecutionContext,asset
fromdagster_dbt importDbtCliResource,dbt_assets

from.constants importdbt_manifest_path,dbt_project_dir

duckdb_database_path =dbt_project_dir.joinpath("tutorial.duckdb")@asset(compute_kind="python")defraw_customers(context:AssetExecutionContext)->None:data =pd.read_csv("https://docs.dagster.io/assets/customers.csv")connection =duckdb.connect(os.fspath(duckdb_database_path))connection.execute("create schema if not exists jaffle_shop")connection.execute("create or replace table jaffle_shop.raw_customers as select * from data")# Log some metadata about the table we just wrote.



Documentation Source:
release-1-7-2.dagster.dagster-docs.io/integrations/dbt/using-dbt-with-dagster/load-dbt-models.md

Documentation Title:
Using Dagster with dbt, part 2: Load dbt models as Dagster assets

Documentation Content:
The following code, in your project's `assets.py`, does this:

`fromdagster importAssetExecutionContext
fromdagster_dbt importDbtCliResource,dbt_assets

from.constants importdbt_manifest_path


@dbt_assets(manifest=dbt_manifest_path)defjaffle_shop_dbt_assets(context:AssetExecutionContext,dbt:DbtCliResource):yieldfromdbt.cli(["build"],context=context).stream()`This code might look a bit fancy, because it uses a decorator. Here's a breakdown of what's going on:

* It creates a variable named `jaffle_shop_dbt_assets`that holds an object that represents a set of Dagster assets.
* These Dagster assets reflect the dbt models described in the manifest file. The manifest file is passed in using the `manifest`argument.
* The decorated function defines what should happen when you materialize one of these Dagster assets, e.g. by clicking the **Materialize**button in the UI or materializing it automatically by putting it on a schedule. In this case, it will invoke the `dbt build`command on the selected assets. The `context`parameter that's provided along with `dbt build`carries the selection.

If you later want to customize how your dbt models are translated into Dagster assets, you'll do so by editing its definition in `assets.py`.

What's next?#
-------------

At this point, you've loaded your dbt models into Dagster as assets, viewed them in Dagster's asset graph UI, and materialized them. Next, you'll learn how to add upstream Dagster assets.

On This Page- Using dbt with Dagster, part two: Load dbt models as Dagster assets
	Step 1: Create a Dagster project that wraps your dbt projectStep 2: Inspect your Dagster project in Dagster's UIStep 3: Build your dbt models in DagsterStep 4: Understand the Python code in your Dagster projectWhat's next?
Edit Page on GitHubShare FeedbackStar



Documentation Source:
release-1-7-2.dagster.dagster-docs.io/integrations/dbt/using-dbt-with-dagster/upstream-assets.md

Documentation Title:
Using Dagster with dbt, part 3: Define assets upstream of your dbt models

Documentation Content:
It will show up in the UI.context.add_output_metadata({"num_rows":data.shape[0]})@dbt_assets(manifest=dbt_manifest_path)defjaffle_shop_dbt_assets(context:AssetExecutionContext,dbt:DbtCliResource):yieldfromdbt.cli(["build"],context=context).stream()`Let's review the changes we made:

At the top, we added imports for `pandas`and `duckdb`, which we use for fetching data into a `DataFrame`and writing it to DuckDB.

We added a `duckdb_database_path`variable, which holds the location of our DuckDB database. Remember that DuckDB databases are just regular files on the local filesystem. The path is the same path that we used when we configured our `profiles.yml`file. This variable is used in the implementations of the `raw_customers`asset.

We added a definition for the `raw_customers`table by writing a function named `raw_customers`and decorating it with the `@asset`decorator. We labeled it with `compute_kind="python"`to indicate in the Dagster UI that this is an asset defined in Python. The implementation inside the function fetches data from the internet and writes it to a table in our DuckDB database. Similar to how running a dbt model executes a select statement, materializing this asset will execute this Python code.


Finally, let's update the `assets`argument of our `Definitions`object, in `definitions.py`, to include the new asset we just defined:

`importos

fromdagster importDefinitions
fromdagster_dbt importDbtCliResource

from.assets importjaffle_shop_dbt_assets,raw_customers
from.constants importdbt_project_dir
from.schedules importschedules

defs =Definitions(assets=[raw_customers,jaffle_shop_dbt_assets],schedules=schedules,resources={"dbt":DbtCliResource(project_dir=os.fspath(dbt_project_dir)),},)`Step 3: In the dbt project, replace a seed with a source#
---------------------------------------------------------

1.



Documentation Source:
release-1-7-2.dagster.dagster-docs.io/integrations/dbt/using-dbt-with-dagster/downstream-assets.md

Documentation Title:
Using Dagster with dbt, part 4: Add a downstream asset

Documentation Content:
To add the `order_count_chart`asset:

1. Replace the imports section with the following:

`importos

importduckdb
importpandas aspd
importplotly.express aspx
fromdagster importMetadataValue,AssetExecutionContext,asset
fromdagster_dbt importDbtCliResource,dbt_assets,get_asset_key_for_model

from.constants importdbt_manifest_path,dbt_project_dir`This adds an import for plotly, as well as `get_asset_key_for_model`and `MetadataValue`, which we'll use in our asset.
2. After your definition of `jaffle_shop_dbt_assets`, add the definition for the `order_count_chart`asset:

`@asset(compute_kind="python",deps=get_asset_key_for_model([jaffle_shop_dbt_assets],"customers"),)deforder_count_chart(context:AssetExecutionContext):# read the contents of the customers table into a Pandas DataFrameconnection =duckdb.connect(os.fspath(duckdb_database_path))customers =connection.sql("select * from customers").df()# create a plot of number of orders by customer and write it out to an HTML filefig =px.histogram(customers,x="number_of_orders")fig.update_layout(bargap=0.2)save_chart_path =duckdb_database_path.parent.joinpath("order_count_chart.html")fig.write_html(save_chart_path,auto_open=True)# tell Dagster about the location of the HTML file,# so it's easy to access from the Dagster UIcontext.add_output_metadata({"plot_url":MetadataValue.url("file://"+os.fspath(save_chart_path))})`This asset definition looks similar the asset we defined in the previous section. In this case, instead of fetching data from an external source and writing it to DuckDB, it reads data from DuckDB, and then uses it to make a plot.

The line `deps=get_asset_key_for_model([jaffle_shop_dbt_assets], "customers")`tells Dagster that this asset is downstream of the `customers`dbt model. This dependency will be displayed as such in Dagster's UI.



