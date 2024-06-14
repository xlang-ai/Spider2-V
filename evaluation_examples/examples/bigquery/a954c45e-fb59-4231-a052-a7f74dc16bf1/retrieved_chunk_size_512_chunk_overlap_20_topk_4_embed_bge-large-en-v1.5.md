Documentation Source:
cloud.google.com/bigquery/docs/geospatial-get-started.md

Documentation Title:
Get started with geospatial analytics  |  BigQuery  |  Google Cloud

Documentation Content:
Run the query

To run the query by using the Google Cloud console:

1. Go to the BigQuery page in the Google Cloud console.

Go to the BigQuery page
2. Enter the following GoogleSQL query in the **Query editor**text area.


```
-- Finds Citi Bike stations with > 30 bikes
SELECT
  ST_GeogPoint(longitude, latitude)  AS WKT,
  num_bikes_available
FROM
  `bigquery-public-data.new_york.citibike_stations`
WHERE num_bikes_available > 30

```
3. Click **Run**.

The query takes a moment to complete. After the query runs, your results
appear in the **Query results**pane.

!

Visualize the query results in Geo Viz
--------------------------------------

Next, you visualize your results using BigQuery Geo Viz: a
web tool for visualization of geospatial data in BigQuery using
Google Maps APIs.



Documentation Source:
cloud.google.com/bigquery/docs/geospatial-get-started.md

Documentation Title:
Get started with geospatial analytics  |  BigQuery  |  Google Cloud

Documentation Content:
Run a GoogleSQL query on geospatial data

After you authenticate and grant access, the next step is to run the query in
Geo Viz.

To run the query:

For step one, **Select data**, enter your project ID in the **Project ID**field.

2. In the query window, enter the following GoogleSQL query.


```
-- Finds Citi Bike stations with > 30 bikes
SELECT
  ST_GeogPoint(longitude, latitude)  AS WKT,
  num_bikes_available
FROM
  `bigquery-public-data.new_york.citibike_stations`
WHERE num_bikes_available > 30

```
Click **Run**.

4. When the query completes, click **Show results**. You can also click step two
**Define columns**.

!
5. This moves you to step two. In step two, for **Geometry column**, choose
**WKT**. This plots the points corresponding to the bike stations on your
map.

!



Documentation Source:
cloud.google.com/bigquery/docs/export-file.md

Documentation Title:
Export query results to a file  |  BigQuery  |  Google Cloud

Documentation Content:
Console

1. In the Google Cloud console, open the BigQuery page.

Go to BigQuery
Enter a valid SQL query in the **Query editor**text area.

Click **Run**.

4. When the results are returned, click **Save Results**.

!
Select **CSV (Google Drive)**or **JSON (Google Drive)**. When you save
results to Google Drive, you cannot choose the location. Results are
always saved to the root "My Drive" location.

6. It may take a few minutes to save the results to Google Drive. When
the results are saved, you receive a dialog message that includes the
filename —
`bq-results-[TIMESTAMP]-[RANDOM_CHARACTERS].[CSV or JSON]`.

!
In the dialog message, click **Open**to open the file, or navigate to
Google Drive and click **My Drive**.

Save query results to Google Sheets
-----------------------------------

Saving query results to Google Sheets is not supported by the bq command-line tool or
the API.

You might get an error when you try to open the BigQuery results
from Google Sheets. This error is due to the Drive SDK API
being unable to access Google Workspace. To resolve the issue,
you must enable your user account to
access Google Sheetswith the Drive SDK API.

To save query results to Google Sheets, use the Google Cloud console:



Documentation Source:
cloud.google.com/bigquery/docs/kmeans-tutorial.md

Documentation Title:
Create a k-means model to cluster London bicycle hires dataset  |  BigQuery  |  Google Cloud

Documentation Content:
For more information about these functions, see
Geography
functions. For more
information about geospatial analytics, see Introduction to
geospatial analytics.

**Run the query**The following query compiles your training data, and is also used in the
`CREATE MODEL`statement later in this tutorial.

To run the query:

- Go to the **BigQuery**page.
Go to BigQuery1. In the editor pane, run the following SQL statement:


```
WITH
  hs AS (
  SELECT
    h.start_station_name AS station_name,
    IF
    (EXTRACT(DAYOFWEEK
      FROM
        h.start_date) = 1
      OR EXTRACT(DAYOFWEEK
      FROM
        h.start_date) = 7,
      "weekend",
      "weekday") AS isweekday,
    h.duration,
    ST_DISTANCE(ST_GEOGPOINT(s.longitude,
        s.latitude),
      ST_GEOGPOINT(-0.1,
        51.5))/1000 AS distance_from_city_center
  FROM
    `bigquery-public-data.london_bicycles.cycle_hire` AS h
  JOIN
    `bigquery-public-data.london_bicycles.cycle_stations` AS s
  ON
    h.start_station_id = s.id
  WHERE
    h.start_date BETWEEN CAST('2015-01-01 00:00:00' AS TIMESTAMP)
    AND CAST('2016-01-01 00:00:00' AS TIMESTAMP) ),
  stationstats AS (
  SELECT
    station_name,
    isweekday,
    AVG(duration) AS duration,
    COUNT(duration) AS num_trips,
    MAX(distance_from_city_center) AS distance_from_city_center
  FROM
    hs
  GROUP BY
    station_name, isweekday )
SELECT
  *
FROM
  stationstats
ORDER BY
  distance_from_city_center ASC


```
When the query is complete, click the **Results**tab below the query text
area. The results tab shows the columns you queried that are used to train
your model: `station_name`, `duration`, `num_trips`, `distance_from_city_center`.
The results should look like the following.



