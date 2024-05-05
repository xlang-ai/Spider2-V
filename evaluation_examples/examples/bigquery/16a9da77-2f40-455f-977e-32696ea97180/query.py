import os
import pandas as pd
from google.cloud import bigquery

def query_data():
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 
    client = bigquery.Client()
    
    query = """
    FROM `bigquery-public-data.austin_bikeshare.

    """


if __name__ == "__main__":
    query_data()