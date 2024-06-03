Documentation Source:
release-1-7-2.dagster.dagster-docs.io/integrations/dbt/using-dbt-with-dagster/upstream-assets.md

Documentation Title:
Using Dagster with dbt, part 3: Define assets upstream of your dbt models

Documentation Content:
Because we're replacing it with a Dagster asset, we no longer need the dbt seed for `raw_customers`, so we can delete it:

`cd..rmseeds/raw_customers.csv`
2. Instead, we want to tell dbt that `raw_customers`is a table that is defined outside of the dbt project. We can do that by defining it inside a dbt source.

Create a file called `sources.yml`inside the `models/`directory, and put this inside it:

`version:2sources:-name:jaffle_shop
 tables:-name:raw_customers
 meta:dagster:asset_key:["raw_customers"]# This metadata specifies the corresponding Dagster asset for this dbt source.`

This is a standard dbt source definition, with one addition: it includes metadata, under the `meta`property, that specifies the Dagster asset that it corresponds to. When Dagster reads the contents of the dbt project, it reads this metadata and infers the correspondence. For any dbt model that depends on this dbt source, Dagster then knows that the Dagster asset corresponding to the dbt model should depend on the Dagster asset corresponding to the source.

- Then, update the model that depends on the `raw_customers`seed to instead depend on the source. Replace the contents of `model/staging/stg_customers.sql`with this:

`withsource as({#-Usesource instead ofseed:
 #}select*from{{ source('jaffle_shop','raw_customers')}}

),renamed as(selectid ascustomer_id,first_name,last_name

 fromsource

)select*fromrenamed`
Step 4: Materialize the assets using the Dagster UI#
----------------------------------------------------

If the Dagster UI is still running from the previous section, click the "Reload Definitions" button in the upper right corner. If you shut it down, then you can launch it again with the same command from the previous section:

`DAGSTER_DBT_PARSE_PROJECT_ON_LOAD=1dagster dev`Our `raw_customers`model is now defined as a Python asset.



Documentation Source:
release-1-7-2.dagster.dagster-docs.io/integrations/dbt/using-dbt-with-dagster/load-dbt-models.md

Documentation Title:
Using Dagster with dbt, part 2: Load dbt models as Dagster assets

Documentation Content:
To build your dbt project, i.e. materialize your assets, click the **Materialize all**button near the top right corner of the page. This will launch a run to materialize the assets. When finished, the **Materialized**and **Latest Run**attributes in the asset will be populated:

!After the run completes, you can:

* Click the **asset**to open a sidebar containing info about the asset, including its last materialization stats and a link to view the **Asset details**page
* Click the ID of the **Latest Run**in an asset to view the **Run details**page. This page contains detailed info about the run, including timing information, errors, and logs.

Step 4: Understand the Python code in your Dagster project#
-----------------------------------------------------------

You saw how you can create a Dagster project that loads a dbt project. How does this work? Understanding how Dagster loads a dbt project will give you a foundation for customizing how Dagster runs your dbt project, as well as for connecting it to other data assets outside of dbt.

The most important file is the Python file that contains the set of definitions for Dagster to load: `jaffle_shop/definitions.py`. Dagster executes the code in this file to find out what assets it should be aware of, as well as details about those assets. For example, when you ran `dagster dev`in the previous step, Dagster executed the code in this file to determine what assets to display in the UI.

In our `definitions.py`Python file, we import from `assets.py`, which contains the code to model our dbt models as Dagster assets. To return a Dagster asset for each dbt model, the code in this `assets.py`file needs to know what dbt models you have. It finds out what models you have by reading a file called a `manifest.json`, which is a file that dbt can generate for any dbt project and contains information about every model, seed, snapshot, test, etc. in the project.



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
release-1-7-2.dagster.dagster-docs.io/integrations/dbt/using-dbt-with-dagster/load-dbt-models.md

Documentation Title:
Using Dagster with dbt, part 2: Load dbt models as Dagster assets

Documentation Content:
It's most common to put your Dagster project at the root of your git repository. Therefore, in this case, because the `dbt_project.yml`was at the root of the `jaffle_shop`git repository, we created our Dagster project there.

**Note**: The `dagster-dbt project scaffold`command creates the Dagster project in whatever directory you run it from. If that's a different directory from where your `dbt_project.yml`lives, then you'll need to provide a value for the `--dbt-project-dir`option so that Dagster knows where to look for your dbt project.

Step 2: Inspect your Dagster project in Dagster's UI#
-----------------------------------------------------

Now that you have a Dagster project, you can run Dagster's UI to take a look at it.

1. Change directories to the Dagster project directory:

`cdjaffle_dagster/`
2. To start Dagster's UI, run the following:

`DAGSTER_DBT_PARSE_PROJECT_ON_LOAD=1dagster dev`Which will result in output similar to:

`Serving dagster-webserver on http://127.0.0.1:3000 inprocess 70635`**Note:**`DAGSTER_DBT_PARSE_PROJECT_ON_LOAD`is an environment variable. If using Microsoft PowerShell, set it before running `dagster dev`using this syntax:

`$env:DAGSTER_DBT_PARSE_PROJECT_ON_LOAD = "1";dagster dev`
In your browser, navigate to http://127.0.0.1:3000. The page will display the assets:


!Step 3: Build your dbt models in Dagster#
-----------------------------------------

You can do more than view your dbt models in Dagster – you can also run them. In Dagster, running a dbt model corresponds to *materializing*an asset. Materializing an asset means running some computation to update its contents in persistent storage. In this tutorial, that persistent storage is our local DuckDB database.

To build your dbt project, i.e.



