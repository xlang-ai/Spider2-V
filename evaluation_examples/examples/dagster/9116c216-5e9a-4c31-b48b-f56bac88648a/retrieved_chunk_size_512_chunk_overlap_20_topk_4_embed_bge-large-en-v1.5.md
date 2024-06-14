Documentation Source:
release-1-7-2.dagster.dagster-docs.io/guides/dagster/ml-pipeline.md

Documentation Title:
Building machine learning pipelines with Dagster | Dagster Docs

Documentation Content:
Training the model

At this point, we have `X_train`, `y_train`, `X_test`, and `y_test`ready to go for our model. To train our model, we can use any number of models from libraries like sklearn, TensorFlow, and PyTorch.

In our example, we will train an XGBoost modelto predict a numerical value.

`importxgboost asxg
fromsklearn.metrics importmean_absolute_error


@assetdefxgboost_comments_model(transformed_training_data):transformed_X_train,transformed_y_train =transformed_training_data
 # Train XGBoost model, which is a highly efficient and flexible modelxgb_r =xg.XGBRegressor(objective="reg:squarederror",eval_metric=mean_absolute_error,n_estimators=20)xgb_r.fit(transformed_X_train,transformed_y_train)returnxgb_r


@assetdefcomments_model_test_set_r_squared(transformed_test_data,xgboost_comments_model):transformed_X_test,transformed_y_test =transformed_test_data
 # Use the test set data to get a score of the XGBoost modelscore =xgboost_comments_model.score(transformed_X_test,transformed_y_test)returnscore`### Evaluating our results#

In our model assets, we evaluated each of the models on the test data and in this case, got the scorederived from comparing the predicted to actual results. Next, to predict the results, we'll create another asset that runs inference on the model more frequently than the model is re-trained.



Documentation Source:
release-1-7-2.dagster.dagster-docs.io/guides/dagster/ml-pipeline.md

Documentation Title:
Building machine learning pipelines with Dagster | Dagster Docs

Documentation Content:
@multi_asset(outs={"training_data":AssetOut(),"test_data":AssetOut()})deftraining_test_data(hackernews_stories):X =hackernews_stories.title
 y =hackernews_stories.descendants
 # Split the dataset to reserve 20% of records as the test setX_train,X_test,y_train,y_test =train_test_split(X,y,test_size=0.2)return(X_train,y_train),(X_test,y_test)`Next, we will take both the training and test data subsets and tokenize the titlese.g. take the words and turn them into columns with the frequency of terms for each record to create featuresfor the data. To do this, we will be using the training set to fit the tokenizer. In this case, we are using TfidfVectorizerand then transforming both the training and test set based on that tokenizer.

`fromsklearn.feature_extraction.text importTfidfVectorizer
importnumpy asnp


@multi_asset(outs={"tfidf_vectorizer":AssetOut(),"transformed_training_data":AssetOut()})deftransformed_train_data(training_data):X_train,y_train =training_data
 # Initiate and fit the tokenizer on the training data and transform the training datasetvectorizer =TfidfVectorizer()transformed_X_train =vectorizer.fit_transform(X_train)transformed_X_train =transformed_X_train.toarray()y_train =y_train.fillna(0)transformed_y_train =np.array(y_train)returnvectorizer,(transformed_X_train,transformed_y_train)@assetdeftransformed_test_data(test_data,tfidf_vectorizer):X_test,y_test =test_data
 # Use the fitted tokenizer to transform the test datasettransformed_X_test =tfidf_vectorizer.transform(X_test)transformed_y_test =np.array(y_test)y_test =y_test.fillna(0)transformed_y_test =np.array(y_test)returntransformed_X_test,transformed_y_test`We also transformed the dataframes into NumPy arrays and removed `nan`values to prepare the data for training.



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



