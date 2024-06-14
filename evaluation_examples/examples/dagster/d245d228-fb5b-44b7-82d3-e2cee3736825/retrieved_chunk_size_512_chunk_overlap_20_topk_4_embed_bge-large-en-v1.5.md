Documentation Source:
release-1-7-2.dagster.dagster-docs.io/guides/dagster/testing-assets.md

Documentation Title:
Testing Assets | Dagster Docs

Documentation Content:
To do that, we can put them in a list and then pass it to the `materialize`function. That returns an `ExecuteInProcessResult`object, whose methods let us investigate, in detail, the success or failure of execution, the values produced by the computation, and other events associated with execution.

Update the `test_assets.py`file to include the following code:

`fromdagster importmaterialize
fromtutorial_project.assets import(topstory_ids,topstories,topstories_word_cloud
)# Instead of importing one asset, import them alldeftest_hackernews_assets():assets =[topstory_ids,topstories,topstories_word_cloud]result =materialize(assets)assertresult.success
 df =result.output_for_node("topstories")assertlen(df)==100`Running the tests#
------------------

Use pytest, or your test runner of choice, to run the unit tests. Navigate to the top-level `tutorial_project`directory (the one that contains the `tutorial_project_tests`directory) and run:

`pytest tutorial_project_tests`Wait a few seconds for the tests to run and observe the output in your terminal.

Related#
--------

Dagster is written to make testing easy in a domain where it has historically been very difficult. Refer to the Testingdocumentation to learn more.

On This Page- Testing assets
	PrerequisitesTesting an individual assetTesting a graph of assetsRunning the testsRelated
Edit Page on GitHubShare FeedbackStar



Documentation Source:
release-1-7-2.dagster.dagster-docs.io/concepts/testing.md

Documentation Title:
Testing | Dagster

Documentation Content:
Testing multiple assets together

You may want to test multiple assets together, to more closely mirror actual materialization. This can be done using the `materialize_to_memory`method, which loads the materialized results of assets into memory:

`fromdagster importasset,materialize_to_memory


@assetdefdata_source():returnget_data_from_source()@assetdefstructured_data(data_source):returnextract_structured_data(data_source)# An example unit test using materialize_to_memorydeftest_data_assets():result =materialize_to_memory([data_source,structured_data])assertresult.success
 # Materialized objects can be accessed in terms of the underlying opmaterialized_data =result.output_for_node("structured_data")...`Mock resources can be provided directly using `materialize_to_memory`:

`fromdagster importasset,materialize_to_memory,ConfigurableResource
importmock


classMyServiceResource(ConfigurableResource):...@assetdefasset_requires_service(service:MyServiceResource):...@assetdefother_asset_requires_service(service:MyServiceResource):...deftest_assets_require_service():# Mock objects can be provided directly.result =materialize_to_memory([asset_requires_service,other_asset_requires_service],resources={"service":mock.MagicMock()},)assertresult.success
 ...`Testing asset checks#
---------------------

Functions decorated with `@asset_check`can be directly invoked. For example:

`importpandas aspd

fromdagster importAssetCheckResult,asset_check



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
release-1-7-2.dagster.dagster-docs.io/guides/dagster/testing-assets.md

Documentation Title:
Testing Assets | Dagster Docs

Documentation Content:
Ask AI!PlatformDagster+NewPricingBlogCommunityDocsSign inJoin us on Slack!Star usTry Dagster+PlatformDagster+PricingBlogCommunityDocsContact SalesSign inTry Dagster+Search the docsPress Ctrl and `K`to searchGetting startedWhat's Dagster?QuickstartInstallationCreating a new projectGetting helpTutorialConceptsDeploymentIntegrationsGuidesAPI ReferenceAbout1.7.2/ 0.23.2 (libs)### You are viewing an unreleased or outdated version of the documentation

View Latest Documentation →Testing assets#
===============

Creating testable and verifiable data pipelines is one of the focuses of Dagster. We believe ensuring data quality is critical for managing the complexity of data systems. Here, we'll cover how to write unit tests for individual assets, as well as for graphs of assets together.

Prerequisites#
--------------

This guide builds off of the project written in the tutorial. If you haven't already, you should complete the tutorial before continuing. Other guides may also build off the project created in the tutorial, but for this guide, we'll assume that the Dagster project is the same as the one created in the tutorial.

It also assumes that you have installed a test runner like pytest.

Testing an individual asset#
----------------------------

We'll start by writing a test for the `topstories_word_cloud`asset definition, which is an image of a word cloud of the titles of top stories on Hacker News. To run the function that derives an asset from its upstream dependencies, we can invoke it directly, as if it's a regular Python function.

Add the following code to the `test_assets.py`file in your `tutorial_project_tests`directory:

`importpandas aspd
fromtutorial_project.assets importtopstories_word_cloud

deftest_topstories_word_cloud():df =pd.DataFrame([{"title":"Wow, Dagster is such an awesome and amazing product. I can't wait to use it!"},{"title":"Pied Piper launches new product"},])results =topstories_word_cloud(df)assertresults isnotNone# It returned something`Testing a graph of assets#
--------------------------

We'll also write a test for all the assets together.



