Documentation Source:
cloud.google.com/bigquery/docs/logistic-regression-prediction.md

Documentation Title:
Build and use a classification model on census data  |  BigQuery  |  Google Cloud

Documentation Content:
SQL

To prepare your sample data, create a viewto
contain the training data. This view is used by the `CREATE MODEL`statement
later in this tutorial.

Run the query that prepares the sample data:

1. In the Google Cloud console, go to the **BigQuery**page.

Go to BigQuery
2. In the query editor, run the following query:


```
CREATE OR REPLACE VIEW
`census.input_data` AS
SELECT
age,
workclass,
marital_status,
education_num,
occupation,
hours_per_week,
income_bracket,
CASE
  WHEN MOD(functional_weight, 10) < 8 THEN 'training'
  WHEN MOD(functional_weight, 10) = 8 THEN 'evaluation'
  WHEN MOD(functional_weight, 10) = 9 THEN 'prediction'
END AS dataframe
FROM
`bigquery-public-data.ml_datasets.census_adult_income`

```
In the **Explorer**pane, expand the `census`dataset and locate the
`input_data`view.

Click the view name to open the information pane. The view schema appears in
the **Schema**tab.



Documentation Source:
cloud.google.com/bigquery/docs/working-with-time-series.md

Documentation Title:
Work with time series data  |  BigQuery  |  Google Cloud

Documentation Content:
environmental_data_hourly
GROUP BY zip_code, time
ORDER BY zip_code, time;

/*---------------------+----------+-----------------+-----------------+
 | time | zip_code | temperature_min | temperature_max |
 +---------------------+----------+-----------------+-----------------+
 | 2020-09-08 00:00:00 | 60606 | 60 | 66 |
 | 2020-09-08 03:00:00 | 60606 | 57 | 59 |
 | 2020-09-08 06:00:00 | 60606 | 55 | 56 |
 | 2020-09-08 09:00:00 | 60606 | 55 | 56 |
 | 2020-09-08 12:00:00 | 60606 | 56 | 59 |
 | 2020-09-08 15:00:00 | 60606 | 63 | 68 |
 | 2020-09-08 18:00:00 | 60606 | 67 | 69 |
 | 2020-09-08 21:00:00 | 60606 | 63 | 67 |
 | 2020-09-08 00:00:00 | 94105 | 71 | 74 |
 | 2020-09-08 03:00:00 | 94105 | 66 | 69 |
 | 2020-09-08 06:00:00 | 94105 | 64 | 65 |
 | 2020-09-08 09:00:00 | 94105 | 62 | 63 |
 | 2020-09-08 12:00:00 | 94105 | 61 | 62 |
 | 2020-09-08 15:00:00 | 94105 | 62 | 63 |
 | 2020-09-08 18:00:00 | 94105 | 64 | 69 |
 | 2020-09-08 21:00:00 | 94105 | 72 | 76 |
 +---------------------+----------+-----------------+-----------------*/`### Get a 3-hour average with custom alignment

When you perform time series aggregation,



Documentation Source:
cloud.google.com/bigquery/docs/reference/standard-sql/window-function-calls.md

Documentation Title:
Window function calls  |  BigQuery  |  Google Cloud

Documentation Content:
The
`Produce`table is referenced.

* fruit
	+ (banana, **apple**) = apple is most popular
	+ (**banana**, apple) = apple is most popular
* vegetable
	+ (leek, **cabbage**, **lettuce**, **kale**) = kale is most popular
	+ (**leek**, cabbage, **lettuce**, **kale**) = kale is most popular
	+ (**leek**, **cabbage**, lettuce, **kale**) = kale is most popular
	+ (**leek**, **cabbage**, **lettuce**, kale) = kale is most popular

`SELECT item, purchases, category, LAST_VALUE(item)
 OVER (
 PARTITION BY category
 ORDER BY purchases
 ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
 ) AS most_popular
FROM Produce

/*----------------------------------------------------*
 | item | purchases | category | most_popular |
 +----------------------------------------------------+
 | banana | 2 | fruit | apple |
 | apple | 8 | fruit | apple |
 | leek | 2 | vegetable | kale |
 | cabbage | 9 | vegetable | kale |
 | lettuce | 10 | vegetable | kale |
 | kale | 23 | vegetable | kale |
 *----------------------------------------------------*/`### Get the last value in a range

This example gets the most popular item in a specific window frame, using
the `Produce`table. The window frame analyzes up to three
rows at a time. Take a close look at the `most_popular`column for vegetables.
Instead of getting the most popular item in a specific category, it gets the
most popular item in a specific range in that category.



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



