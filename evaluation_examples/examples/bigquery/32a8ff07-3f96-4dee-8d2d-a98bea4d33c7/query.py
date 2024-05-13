import os
import pandas as pd
from google.cloud import bigquery

def query_data():
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "bigquery_credential.json"
    client = bigquery.Client()
    query = """
SELECT
    city, AVG(value) as avg_aqi, latitude, longitude
FROM
    `bigquery-public-data.openaq.global_air_quality`
WHERE
    pollutant = 'pm25'
    AND (city = 'Beijing' OR city = 'Shanghai')
    AND EXTRACT(YEAR FROM timestamp) BETWEEN 2017 AND 2021
GROUP BY
    city, latitude, longitude
ORDER BY
    AVG(value) DESC
    """
    query_job = client.query(query)

if __name__ == "__main__":
    query_data()
