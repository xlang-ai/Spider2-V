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
release-1-7-2.dagster.dagster-docs.io/tutorial/building-an-asset-graph.md

Documentation Title:
Tutorial, part four: Building an asset graph | Dagster Docs

Documentation Content:
... Keep the `topstory_ids` asset from the previous section@asset(deps=[topstory_ids]) this asset is dependent on topstory_idsdeftopstories()->None:withopen("data/topstory_ids.json","r")asf:topstory_ids =json.load(f)results =[]foritem_id intopstory_ids:item =requests.get(f"https://hacker-news.firebaseio.com/v0/item/{item_id}.json").json()results.append(item)iflen(results)%20==0:print(f"Got {len(results)}items so far.")df =pd.DataFrame(results)df.to_csv("data/topstories.csv")`Dependencies between assets are defined using the `deps`parameter of the `@asset`decorator. In this case, `topstory_ids`(the list of IDs) is a dependency of `topstories`(the CSV file).

In your browser, navigate back to Dagster's Global Asset Lineage (`localhost:3000/asset-groups`), and click on the **Reload Definitions**button on the top-right region of the page. This will tell Dagster to re-scan your code for new assets and other definitions without stopping Dagster. You can also use the Command + Option + R (Mac) or Control + Alt (Windows) + R keyboard shortcut to perform the same action.

After reloading your definitions, look at the asset graph to see the relationship between your assets.



Documentation Source:
release-1-7-2.dagster.dagster-docs.io/getting-started/quickstart.md

Documentation Title:
Quickstart | Dagster Docs

Documentation Content:
!Congratulations! You have successfully materialized two Dagster assets:

!But wait - there's more. Because the `hackernews_top_stories`asset returned some `metadata`, you can view the metadata right in the UI:

1. Click the asset
2. In the sidebar, click the **Show Markdown**link in the **Materialization in Last Run**section. This opens a preview of the pipeline result, allowing you to view the top 10 HackerNews stories:

!Understanding the Code#
-----------------------

The Quickstart project defines two **Assets**using the `@asset`decorator:

* `hackernews_top_story_ids`retrieves the top stories from the Hacker News API and saves them as a JSON file.
* `hackernews_top_stories`asset builds upon the first asset, retrieving data for each story as a CSV file, and returns a `MaterializeResult`with a markdown preview of the top stories.

`importjson

importpandas aspd
importrequests

fromdagster import(MaterializeResult,MetadataValue,asset,)from.configurations importHNStoriesConfig



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



