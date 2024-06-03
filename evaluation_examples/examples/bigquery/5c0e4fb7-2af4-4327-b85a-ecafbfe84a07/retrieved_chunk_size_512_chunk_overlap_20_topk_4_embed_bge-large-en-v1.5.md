Documentation Source:
cloud.google.com/bigquery/docs/logistic-regression-prediction.md

Documentation Title:
Build and use a classification model on census data  |  BigQuery  |  Google Cloud

Documentation Content:
SQL

1. In the Google Cloud console, go to the **BigQuery**page.

Go to BigQuery
2. In the query editor, run the following GoogleSQL query:


```
SELECT
age,
workclass,
marital_status,
education_num,
occupation,
hours_per_week,
income_bracket,
functional_weight
FROM
`bigquery-public-data.ml_datasets.census_adult_income`
LIMIT
100;

```
3. The results look similar to the following:

!



Documentation Source:
cloud.google.com/bigquery/docs/logistic-regression-prediction.md

Documentation Title:
Build and use a classification model on census data  |  BigQuery  |  Google Cloud

Documentation Content:
!
4. On the **Create dataset**page, do the following:


	For **Dataset ID**, enter `census`.
	
	* For **Location type**, select **Multi-region**, and then select **US (multiple regions in United States)**.
	
	The public datasets are stored in the
	`US`multi-region. For
	simplicity, store your dataset in the same location.
	Leave the remaining default settings as they are, and click **Create dataset**.

Examine the data
----------------

Examine the dataset and identify which columns to use as
training data for the logistic regression model. Select 100 rows from the
`census_adult_income`table:



Documentation Source:
cloud.google.com/bigquery/docs/logistic-regression-prediction.md

Documentation Title:
Build and use a classification model on census data  |  BigQuery  |  Google Cloud

Documentation Content:
languages, frameworks, and tools
 Costs and usage management
 Infrastructure as code
 Migration
 Google Cloud Home
 Free Trial and Free Tier
 Architecture Center
 Blog
 Contact Sales
 Google Cloud Developer Center
 Google Developer Center
 Google Cloud Marketplace (in console)
 Google Cloud Marketplace Documentation
 Google Cloud Skills Boost
 Google Cloud Solution Center
 Google Cloud Support
 Google Cloud Tech Youtube Channel
 HomeBigQueryDocumentationGuides
Send feedback
 
 Build and use a classification model on census data
===================================================

Stay organized with collections
 Save and categorize content based on your preferences.
 In this tutorial, you use a binary
logistic regression modelin BigQuery ML to predict the income range of individuals based on their
demographic data. A binary logistic regression model predicts whether a
value falls into one of two categories, in this case whether an individual's
annual income falls above or below $50,000.

This tutorial uses the
`bigquery-public-data.ml_datasets.census_adult_income`dataset. This dataset contains the demographic and income information of US
residents from 2000 and 2010.

Objectives
----------

In this tutorial you will perform the following tasks:

* Create a logistic regression model.
* Evaluate the model.
* Make predictions by using the model.
* Explain the results produced by the model.
Costs
-----

This tutorial uses billable components of Google Cloud, including the following:

* BigQuery
* BigQuery ML

For more information on BigQuery costs, see the
BigQuery pricingpage.

For more information on BigQuery ML costs, see
BigQuery ML pricing.

Before you begin
----------------

1. In the Google Cloud console, on the project selector page,
 select or create a Google Cloud project.

**Note**: If you don't plan to keep the
 resources that you create in this procedure, create a project instead of
 selecting an existing project. After you finish these steps, you can
 delete the project, removing all resources associated with the project.Go to project selector
Make sure that billing is enabled for your Google Cloud project.
 

3. Enable the BigQuery API.



Documentation Source:
cloud.google.com/bigquery/docs/logistic-regression-prediction.md

Documentation Title:
Build and use a classification model on census data  |  BigQuery  |  Google Cloud

Documentation Content:
```
CREATE OR REPLACE MODEL
`census.census_model`
OPTIONS
( model_type='LOGISTIC_REG',
  auto_class_weights=TRUE,
  data_split_method='NO_SPLIT',
  input_label_cols=['income_bracket'],
  max_iterations=15) AS
SELECT * EXCEPT(dataframe)
FROM
`census.input_data`
WHERE
dataframe = 'training'

```
In the **Explorer**pane, expand the `census`dataset and then the **Models**folder.

Click the **census\_model**model to open the information pane.

Click the **Schema**tab. The model schema lists the attributes
that BigQuery ML used to perform logistic regression. The schema
should look similar to the following:


!### BigQuery DataFrames

Use the
`fit`method to train the model and the
`to_gbq`method to save it to your dataset.

Before trying this sample, follow the BigQuery DataFrames
 setup instructions in the BigQuery quickstart
 using BigQuery DataFrames.
 For more information, see the
 BigQuery DataFrames reference documentation.

To authenticate to BigQuery, set up Application Default Credentials.
 For more information, see Set 
 up authentication for a local development environment.
 

`import bigframes.ml.linear_model



