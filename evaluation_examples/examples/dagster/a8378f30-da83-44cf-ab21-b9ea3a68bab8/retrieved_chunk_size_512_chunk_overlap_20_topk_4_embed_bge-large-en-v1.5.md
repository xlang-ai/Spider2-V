Documentation Source:
release-1-7-2.dagster.dagster-docs.io/tutorial/building-an-asset-graph.md

Documentation Title:
Tutorial, part four: Building an asset graph | Dagster Docs

Documentation Content:
Below is the finished code for a `most_frequent_words`asset. Copy and paste the code into `assets.py`:

`@asset(deps=[topstories])defmost_frequent_words()->None:stopwords =["a","the","an","of","to","in","for","and","with","on","is"]topstories =pd.read_csv("data/topstories.csv")# loop through the titles and count the frequency of each wordword_counts ={}forraw_title intopstories["title"]:title =raw_title.lower()forword intitle.split():cleaned_word =word.strip(".,-!?:;()[]'\"-")ifcleaned_word notinstopwords andlen(cleaned_word)>0:word_counts[cleaned_word]=word_counts.get(cleaned_word,0)+1# Get the top 25 most frequent wordstop_words ={pair[0]:pair[1]forpair insorted(word_counts.items(),key=lambdax:x[1],reverse=True)[:25]}withopen("data/most_frequent_words.json","w")asf:json.dump(top_words,f)`Step 3: Educating users with metadata#
--------------------------------------

Up until now, you've annotated your asset functions with `None`, meaning the asset doesn't return anything. In this section, you'll learn about the `MaterializeResult`object, which lets you record metadata about your asset.

Software-defined Assets can be enriched with different types of metadata. Anything can be used as metadata for an asset. Common details to add are:

* Statistics about the data, such as row counts or other data profiling
* Test results or assertions about the data
* Images or tabular previews of the asset
* Information about who owns the asset, where it's stored, and links to external documentation

The following code adds a row count and a preview of the `topstories`asset. Update your code for the `topstories`asset to match the changes below. The `None`type annotation is replaced with `MaterializeResult`from the `dagster`module, which allows you to add metadata to the materialization of your asset.



Documentation Source:
release-1-7-2.dagster.dagster-docs.io/getting-started/quickstart.md

Documentation Title:
Quickstart | Dagster Docs

Documentation Content:
@assetdefhackernews_top_story_ids(config:HNStoriesConfig):"""Get top stories from the HackerNews top stories endpoint."""top_story_ids =requests.get("https://hacker-news.firebaseio.com/v0/topstories.json").json()withopen(config.hn_top_story_ids_path,"w")asf:json.dump(top_story_ids[:config.top_stories_limit],f)@asset(deps=[hackernews_top_story_ids])defhackernews_top_stories(config:HNStoriesConfig)->MaterializeResult:"""Get items based on story ids from the HackerNews items endpoint."""withopen(config.hn_top_story_ids_path,"r")asf:hackernews_top_story_ids =json.load(f)results =[]foritem_id inhackernews_top_story_ids:item =requests.get(f"https://hacker-news.firebaseio.com/v0/item/{item_id}.json").json()results.append(item)df =pd.DataFrame(results)df.to_csv(config.hn_top_stories_path)returnMaterializeResult(metadata={"num_records":len(df),"preview":MetadataValue.md(str(df[["title","by","url"]].to_markdown())),})`Next steps#
-----------

Congratulations on successfully running your first Dagster pipeline! In this example, we used assets, which are a cornerstone of Dagster projects. They empower data engineers to:

* Think in the same terms as stakeholders
* Answer questions about data quality and lineage
* Work with the modern data stack (dbt, Airbyte/Fivetran, Spark)
* Create declarative freshness policies instead of task-driven cron schedules

Dagster also offers ops and jobs, but we recommend starting with assets.

To create your own project, consider the following options:

* Scaffold a new project using our new project guide.
* Begin with an official example, like the dbt & Dagster project, and explore all examples on GitHub.
On This Page- Quickstart
	
		Option 1: Running LocallyOption 2: Using GitHub CodespacesNavigating the User InterfaceUnderstanding the CodeNext steps
Edit Page on GitHubShare FeedbackStar



Documentation Source:
release-1-7-2.dagster.dagster-docs.io/guides/dagster/ml-pipeline.md

Documentation Title:
Building machine learning pipelines with Dagster | Dagster Docs

Documentation Content:
This will be a supervised model since we have the number of comments for all the previous stories.

The assets graph will look like this at the end of this guide (click to expand):

!### Ingesting data#

First, we will create an asset that retrieves the most recent Hacker News records.

`importrequests
fromdagster importasset
importpandas aspd


@assetdefhackernews_stories():# Get the max ID number from hacker newslatest_item =requests.get("https://hacker-news.firebaseio.com/v0/maxitem.json").json()# Get items based on story ids from the HackerNews items endpointresults =[]scope =range(latest_item -1000,latest_item)foritem_id inscope:item =requests.get(f"https://hacker-news.firebaseio.com/v0/item/{item_id}.json").json()results.append(item)# Store the results in a dataframe and filter on stories with valid titlesdf =pd.DataFrame(results)iflen(df)>0:df =df[df.type=="story"]df =df[~df.title.isna()]returndf`### Transforming data#

Now that we have a dataframe with all valid stories, we want to transform that data into something our machine learning model will be able to use.

The first step is taking the dataframe and splitting it into a training and test set. In some of your models, you also might choose to have an additional split for a validation set. The reason we split the data is so that we can have a test and/or a validation dataset that is independent of the training set. We can then use that dataset to see how well our model did.

`fromsklearn.model_selection importtrain_test_split
fromdagster importmulti_asset,AssetOut



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



