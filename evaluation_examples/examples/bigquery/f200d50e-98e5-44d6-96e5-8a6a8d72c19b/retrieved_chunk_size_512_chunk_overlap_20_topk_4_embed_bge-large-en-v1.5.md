Documentation Source:
cloud.google.com/bigquery/docs/data-canvas.md

Documentation Title:
Analyze with data canvas  |  BigQuery  |  Google Cloud

Documentation Content:
Example 3

**Prompt 1**
```
Find data about USA names
```
**Potential result**BigQuery data canvas generates a list of tables. For this example, we are going to
select the `bigquery-public-data.usa_names.usa_1910_current`table.

Click **Query**to query the data. Enter a prompt to query the data.

**Potential result**BigQuery data canvas generates the following query:


```
SELECT
  state,
  gender,
  year,
  name,
  number
FROM
  `bigquery-public-data.usa_names.usa_1910_current`

```
BigQuery data canvas generates the results of the query. We are going to ask an
additional query to filter this data. Click **Query these results**.

**Prompt 2**
```
Get me the top 10 most popular names in 1980
```
**Potential result**BigQuery data canvas generates the following query:



Documentation Source:
cloud.google.com/bigquery/docs/logistic-regression-prediction.md

Documentation Title:
Build and use a classification model on census data  |  BigQuery  |  Google Cloud

Documentation Content:
data from BigQuery, but you could also use the `census_model` object



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



