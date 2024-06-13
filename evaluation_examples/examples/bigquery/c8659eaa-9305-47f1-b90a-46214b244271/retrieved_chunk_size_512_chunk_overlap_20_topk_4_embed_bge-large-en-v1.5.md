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
cloud.google.com/bigquery/docs/kmeans-tutorial.md

Documentation Title:
Create a k-means model to cluster London bicycle hires dataset  |  BigQuery  |  Google Cloud

Documentation Content:
data as a DataFrame.
h = bpd.read_gbq(
 "bigquery-public-data.london_bicycles.cycle_hire",
 col_order=["start_station_name", "start_station_id", "start_date", "duration"],
).rename(
 columns={
 "start_station_name": "station_name",
 "start_station_id": "station_id",
 }
)

s = bpd.read_gbq(
 # Use ST_GEOPOINT and ST_DISTANCE to analyze geographical
 # data. These functions determine spatial relationships between
 # geographical features.
 """
 SELECT
 id,
 ST_DISTANCE(
 ST_GEOGPOINT(s.longitude, s.latitude),
 ST_GEOGPOINT(-0.1, 51.5)
 ) / 1000 AS distance_from_city_center
 FROM
 `bigquery-public-data.london_bicycles.cycle_stations` s
 """
)



Documentation Source:
cloud.google.com/bigquery/docs/kmeans-tutorial.md

Documentation Title:
Create a k-means model to cluster London bicycle hires dataset  |  BigQuery  |  Google Cloud

Documentation Content:
Expected output results: >>> stationstats.head(3)



