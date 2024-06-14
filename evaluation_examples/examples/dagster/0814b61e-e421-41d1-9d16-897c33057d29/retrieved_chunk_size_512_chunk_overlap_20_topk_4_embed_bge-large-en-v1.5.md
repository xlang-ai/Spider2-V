Documentation Source:
release-1-7-2.dagster.dagster-docs.io/tutorial/writing-your-first-asset.md

Documentation Title:
Tutorial, part three: Writing your first asset | Dagster Docs

Documentation Content:
Exploring the Dagster UI

Using Dagster's UI, you can explore your data assets, manually launch runs, and observe what's happening during pipeline runs.

As a reminder, to launch the UI, set your terminal's current directory to `/tutorial`and run the following command:

`dagster dev`Navigate to `localhost:3000`in your browser to see the Dagster UI.

You should see a screen that looks similar to below. If you do not see it, go the top navigation bar, click on **Assets**, then go the top-right region and click on **View global asset lineage**. You can also navigate directly to this page by going to `localhost:3000/asset-groups`. As more assets are built, this graph will show your entire data platform in one place. This page can also be referred to as the **Global Asset Lineage**.

!Observe that Dagster has detected your `topstory_ids`asset, but it says that the asset has never been *“materialized”*.

Step 2: Materialize your asset#
-------------------------------

To **materialize**a Software-defined asset means to create or update it. Dagster materializes assets by executing the asset's function or triggering an integration.

To manually materialize an asset in the UI, click the **Materialize**button in the upper right corner of the screen. This will create a Dagster run that will materialize your assets.

To follow the progress of the materialization and monitor the logs, each run has a dedicated page. To find the page:

Click on the **Runs**tab in the upper navigation bar

Click the value in the **Run ID**column on the table of the Runs page

3. The top section displays the progress, and the bottom section live updates with the logs

!

Next steps#
-----------

You've written the first step in your data pipeline! In the next section, you'll learn how to add more assets to your pipeline. You'll also learn how to add information and metadata to your assets.

On This Page- Tutorial, part three: Writing your first asset
	1.



Documentation Source:
release-1-7-2.dagster.dagster-docs.io/concepts/assets/software-defined-assets.md

Documentation Title:
Software-defined assets | Dagster

Documentation Content:
Viewing assets in the UI

Viewing all assetsDetails for an assetDependency graph
Asset catalog (all assets)Asset detailsDependency graph#### Asset catalog#

To view a list of all your assets, click **Assets**in the top navigation. This opens the **Asset catalog**:

!### Materializing assets in the UI#

In the UI, you can launch runs that materialize assets by:

* Navigating to the **Asset details**pagefor the asset and clicking the **Materialize**button in the upper right corner.
* Navigating to the graph view of the **Asset catalog**pageand clicking the **Materialize**button in the upper right corner. You can also click on individual assets to collect a subset to materialize.

Building jobs that materialize assets#
--------------------------------------

Jobs that target assets can materialize a fixed selection of assets each time they run and be placed on schedules and sensors. Refer to the Asset jobs documentationfor more info and examples.

Grouping assets#
----------------

To help keep your assets tidy, you can organize them into groups. Grouping assets by project, concept, and so on simplifies keeping track of them in the UI. Each asset is assigned to a single group, which by default is called "default".

Assigning assets to groupsViewing asset groups in the UI



Documentation Source:
release-1-7-2.dagster.dagster-docs.io/tutorial/building-an-asset-graph.md

Documentation Title:
Tutorial, part four: Building an asset graph | Dagster Docs

Documentation Content:
Add the imports above to the top of `assets.py`@asset(deps=[topstory_ids])deftopstories(context:AssetExecutionContext)->MaterializeResult:withopen("data/topstory_ids.json","r")asf:topstory_ids =json.load(f)results =[]foritem_id intopstory_ids:item =requests.get(f"https://hacker-news.firebaseio.com/v0/item/{item_id}.json").json()results.append(item)iflen(results)%20==0:context.log.info(f"Got {len(results)}items so far.")df =pd.DataFrame(results)df.to_csv("data/topstories.csv")returnMaterializeResult(metadata={"num_records":len(df), Metadata can be any key-value pair"preview":MetadataValue.md(df.head().to_markdown()), The `MetadataValue` class has useful static methods to build Metadata})`Reload the definitions and re-materialize your assets. The metadata can then be seen in the following places:

* In the **Asset graph**page, click on an asset and its metadata will be shown in the right sidebar:

!
* In the **Asset Catalog's**page for the `topstories`asset:

!



Documentation Source:
release-1-7-2.dagster.dagster-docs.io/concepts/metadata-tags/asset-metadata.md

Documentation Title:
Defining asset metadata | Dagster Docs

Documentation Content:
@asset(deps=[topstory_ids])deftopstories(context:AssetExecutionContext)->MaterializeResult:withopen("data/topstory_ids.json","r")asf:topstory_ids =json.load(f)results =[]foritem_id intopstory_ids:item =requests.get(f"https://hacker-news.firebaseio.com/v0/item/{item_id}.json").json()results.append(item)iflen(results)%20==0:context.log.info(f"Got {len(results)}items so far.")df =pd.DataFrame(results)df.to_csv("data/topstories.csv")returnMaterializeResult(metadata={"num_records":len(df),# Metadata can be any key-value pair"preview":MetadataValue.md(df.head().to_markdown()),# The `MetadataValue` class has useful static methods to build Metadata})`Viewing asset metadata in the Dagster UI#
-----------------------------------------

Metadata attached to assets shows up in a few places in the Dagster UI.

Global asset lineageAsset detailsDagster+ Insights### Global asset lineage#

In the **Global asset lineage**page, click on an asset to open the asset details in the sidepanel:

!If materialization metadata is numeric, it will display as a plot in the **Metadata plots**section of the sidepanel.

APIs in this guide#
-------------------



| Name | Description |
| --- | --- |
|`@asset` A decorator used to define assets. |
| --- |
|`MaterializeResult` An object representing a successful materialization of an asset. |
|`MetadataValue` Utility class to wrap metadata values passed into Dagster events, which allows them to be displayed in the Dagster UI and other tooling. |

Related#
--------

Software-defined AssetsMetadata & tagsTagsDagster UIIntegrating asset metadata with Dagster+ InsightsOn This Page- Asset metadata
	How it works2. Attaching definition metadata
		Arbitrary metadata using the metadata parameterAsset owners
	Attaching materialization metadata4. Viewing asset metadata in the Dagster UI
		Global asset lineageAsset detailsDagster+ Insights
	APIs in this guideRelated
Edit Page on GitHubShare FeedbackStar



