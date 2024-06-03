Documentation Source:
release-1-7-2.dagster.dagster-docs.io/guides/dagster/managing-ml.md

Documentation Title:
Managing machine learning models with Dagster | Dagster Docs

Documentation Content:
@assetdefsome_data():...@asset(auto_materialize_policy=AutoMaterializePolicy.lazy())defsome_ml_model(some_data):...@asset(auto_materialize_policy=AutoMaterializePolicy.lazy(),freshness_policy=FreshnessPolicy(maximum_lag_minutes=7*24*60),)defpredictions(some_ml_model):...`A more traditional schedule can also be used to update machine learning assets, causing them to be re-materialized or retrained on the latest data. For example, setting up a cron schedule on a daily basis.

This can be useful if you have data that is also being scheduled on a cron schedule and want to add your machine model jobs to run on a schedule as well.

`fromdagster importAssetSelection,define_asset_job,ScheduleDefinition

ml_asset_job =define_asset_job("ml_asset_job",AssetSelection.groups("ml_asset_group"))basic_schedule =ScheduleDefinition(job=ml_asset_job,cron_schedule="0 9 * * *")`### Monitoring#

Integrating your machine learning models into Dagster allows you to see when the model and its data dependencies were refreshed, or when a refresh process has failed. By using Dagster to monitor performance changes and process failures on your ML model, it becomes possible to set up remediation paths, such as automated model retraining, that can help resolve issues like model drift.

In this example, the model is being evaluated against the previous model’s accuracy. If the model’s accuracy has improved, the model is returned for use in downstream steps, such as inference or deploying to production.

`fromsklearn importlinear_model
fromdagster importasset,Output,AssetKey,AssetExecutionContext
importnumpy asnp
fromsklearn.model_selection importtrain_test_split



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
release-1-7-2.dagster.dagster-docs.io/integrations/airflow/from-airflow-to-dagster.md

Documentation Title:
Learning Dagster from Airlfow

Documentation Content:
Once enabled in your `dagster.yaml`file, you can define the retry count for the job.

Step 3: Define the schedule#
----------------------------

In Dagster, schedules can be defined for jobs, which determine the cadence at which a job is triggered to be executed. Below we define a schedule that will run the `tutorial_job`daily:

`schedule =ScheduleDefinition(job=tutorial_job,cron_schedule="@daily")`Step 4: Run Dagster locally#
----------------------------

In order to run our newly defined Dagster job we'll need to add it and the schedule to our project's Definitions.

`defs =Definitions(jobs=[tutorial_job],schedules=[schedule],)`We can now load this file with the UI:

`dagster dev -f .py`Completed code example#
-----------------------

That's it! By now, your code should look like this:

`importtime
fromdatetime importdatetime,timedelta

fromdagster import(Definitions,In,Nothing,OpExecutionContext,RetryPolicy,ScheduleDefinition,job,op,schedule,)@opdefprint_date(context:OpExecutionContext)->datetime:ds =datetime.now()context.log.info(ds)returnds


@op(retry_policy=RetryPolicy(max_retries=3),ins={"start":In(Nothing)})defsleep():time.sleep(5)@opdeftemplated(context:OpExecutionContext,ds:datetime):for_i inrange(5):context.log.info(ds)context.log.info(ds -timedelta(days=7))@job(tags={"dagster/max_retries":1,"dag_name":"example"})deftutorial_job():ds =print_date()sleep(ds)templated(ds)schedule =ScheduleDefinition(job=tutorial_job,cron_schedule="@daily")defs =Definitions(jobs=[tutorial_job],schedules=[schedule],)`On This Page- Learning Dagster from Airflow
	Comparing an Airflow DAG to Dagster2. Step 1: Defining the opsOp-level retries
	3. Step 2: Define the jobJob-level retries
	Step 3: Define the scheduleStep 4: Run Dagster locallyCompleted code example
Edit Page on GitHubShare FeedbackStar



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



