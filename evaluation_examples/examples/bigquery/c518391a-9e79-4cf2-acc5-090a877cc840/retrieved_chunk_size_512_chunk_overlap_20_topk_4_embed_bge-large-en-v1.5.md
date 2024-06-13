Documentation Source:
cloud.google.com/bigquery/docs/create-machine-learning-model.md

Documentation Title:
Quickstart: Create machine learning models in BigQuery ML  |  Google Cloud

Documentation Content:
SQL

The following GoogleSQL query is used to
create the model you use to predict whether a website visitor will make a
transaction.


```
#standardSQL
CREATE MODEL `bqml_tutorial.sample_model`
OPTIONS(model_type='logistic_reg') AS
SELECT
IF(totals.transactions IS NULL, 0, 1) AS label,
IFNULL(device.operatingSystem, "") AS os,
device.isMobile AS is_mobile,
IFNULL(geoNetwork.country, "") AS country,
IFNULL(totals.pageviews, 0) AS pageviews
FROM
`bigquery-public-data.google_analytics_sample.ga_sessions_*`
WHERE
_TABLE_SUFFIX BETWEEN '20160801' AND '20170630'

```
In addition to creating the model, running a query that contains the `CREATE MODEL`statement trains the model using the data retrieved by your query's `SELECT`statement.

**Query details**The `CREATE MODEL`clause is used to create and train the model named `bqml_tutorial.sample_model`.

The `OPTIONS(model_type='logistic_reg')`clause indicates that you are creating
a logistic regressionmodel.
A logistic regression model tries to split input data into two classes and gives
the probability the data is in one of the classes. Usually, what you are
trying to detect (such as whether an email is spam) is represented by 1 and
everything else is represented by 0. If the logistic regression model outputs
0.9, there is a 90% probability the input is what you are trying to detect
(the email is spam).

This query's `SELECT`statement retrieves the following columns that are used by
the model to predict the probability a customer will complete a transaction:

* `totals.transactions`— The total number of ecommerce transactions
within the session. If the number of transactions is `NULL`, the value in the
`label`column is set to `0`. Otherwise, it is set to `1`. These values
represent the possible outcomes. Creating an alias named `label`is an
alternative to setting the `input_label_cols=`option in the `CREATE MODEL`statement.
* `device.operatingSystem`— The operating system of the visitor's device.



Documentation Source:
cloud.google.com/bigquery/docs/create-machine-learning-model.md

Documentation Title:
Quickstart: Create machine learning models in BigQuery ML  |  Google Cloud

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
 
 Stay organized with collections
 Save and categorize content based on your preferences.
 Create machine learning models in BigQuery ML
=============================================

This tutorial introduces users to BigQuery ML using the Google Cloud console.

BigQuery ML enables users to create and execute machine learning models in
BigQuery by using SQL queries and Python code. The goal is to democratize machine
learning by enabling SQL practitioners to build models using their existing
tools and to increase development speed by eliminating the need for data
movement.

In this tutorial, you use the sample
Google Analytics sample dataset for BigQueryto create a model that predicts whether a website visitor will make a
transaction. For information on the schema of the Analytics dataset, see
BigQuery export schemain the Analytics Help Center.

Objectives
----------

In this tutorial, you use:

* BigQuery ML to create a binary logistic regression model using the
`CREATE MODEL`statement
* The `ML.EVALUATE`function to evaluate the ML model
* The `ML.PREDICT`function to make predictions using the ML model

Costs
-----

This tutorial uses billable components of Google Cloud,
including the following:

* BigQuery
* BigQuery ML

For more information on BigQuery costs, see the
BigQuery pricingpage.

For more information on BigQuery ML costs, see
BigQuery ML pricing.

Before you begin
----------------

- Sign in to your Google Cloud account. If you're new to
 Google Cloud, create an accountto evaluate how our products perform in
 real-world scenarios. New customers also get $300 in free credits to
 run, test, and deploy workloads.
- In the Google Cloud console, on the project selector page,
 select or create a Google Cloud project.



Documentation Source:
cloud.google.com/bigquery/docs/create-machine-learning-model.md

Documentation Title:
Quickstart: Create machine learning models in BigQuery ML  |  Google Cloud

Documentation Content:
a confidence score that the data is in one of the classes.
model = LogisticRegression()
model.fit(features, label)



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



