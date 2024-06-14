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
release-1-7-2.dagster.dagster-docs.io/tutorial/writing-your-first-asset.md

Documentation Title:
Tutorial, part three: Writing your first asset | Dagster Docs

Documentation Content:
Ingesting data

To get started, you will fetch data from the Hacker News API. Copy and paste the following code into `assets.py`:

`importjson
importos

importrequests

newstories_url ="https://hacker-news.firebaseio.com/v0/topstories.json"top_new_story_ids =requests.get(newstories_url).json()[:100]os.makedirs("data",exist_ok=True)withopen("data/topstory_ids.json","w")asf:json.dump(top_new_story_ids,f)`This code creates a list of integers representing the IDs for the current top stories on Hacker News and stores them in a file called `data/topstory_ids.json`.

Next, you will work towards making this code into a software-defined asset. The first step is turning it into a function:

`importjson
importos

importrequests


deftopstory_ids()->None:# turn it into a functionnewstories_url ="https://hacker-news.firebaseio.com/v0/topstories.json"top_new_story_ids =requests.get(newstories_url).json()[:100]os.makedirs("data",exist_ok=True)withopen("data/topstory_ids.json","w")asf:json.dump(top_new_story_ids,f)`Now, add the `@asset`decorator from the `dagster`library to the function:

`importjson
importos

importrequests
fromdagster importasset # import the `dagster` library@asset# add the asset decorator to tell Dagster this is an assetdeftopstory_ids()->None:newstories_url ="https://hacker-news.firebaseio.com/v0/topstories.json"top_new_story_ids =requests.get(newstories_url).json()[:100]os.makedirs("data",exist_ok=True)withopen("data/topstory_ids.json","w")asf:json.dump(top_new_story_ids,f)`That's all it takes to get started 🎉. Dagster now knows that this is an asset. In future sections, you'll see how you can add metadata, schedule when to refresh the asset, and more.

And now you're done! Time to go into the Dagster UI and see what you've built.



Documentation Source:
release-1-7-2.dagster.dagster-docs.io/guides/dagster/ml-pipeline.md

Documentation Title:
Building machine learning pipelines with Dagster | Dagster Docs

Documentation Content:
`@assetdeflatest_story_comment_predictions(xgboost_comments_model,tfidf_vectorizer):# Get the max ID number from hacker newslatest_item =requests.get("https://hacker-news.firebaseio.com/v0/maxitem.json").json()# Get items based on story ids from the HackerNews items endpointresults =[]scope =range(latest_item -100,latest_item)foritem_id inscope:item =requests.get(f"https://hacker-news.firebaseio.com/v0/item/{item_id}.json").json()results.append(item)df =pd.DataFrame(results)iflen(df)>0:df =df[df.type=="story"]df =df[~df.title.isna()]inference_x =df.title
 # Transform the new story titles using the existing vectorizerinference_x =tfidf_vectorizer.transform(inference_x)returnxgboost_comments_model.predict(inference_x)`Depending on what the objective of your ML model is, you can use this data to set alerts, save model performance history, and trigger retraining.

Where to go from here#
----------------------

* Managing machine learning models with Dagster- This guide reviews ways to manage and maintain your machine learning (ML) models in Dagster
* Dagster is flexible so there could be many 'right' ways to implement your machine learning pipeline and different avenues to explore
* Dagster intergrates with MLflowthat can be used to keep track of your models
* Dagster integrates with Weights & Biasesand an examplewhich demonstrates how to use W\&B's artifacts with Dagster.
On This Page- Building machine learning pipelines with Dagster
	Before you beginBenefits of building machine learning pipelines in Dagster3. Machine learning development
		Ingesting dataTransforming dataTraining the modelEvaluating our results
	Where to go from here
Edit Page on GitHubShare FeedbackStar



