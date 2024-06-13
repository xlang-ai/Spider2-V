import pandas as pd
from dagster_duckdb import DuckDBResource

from dagster import Definitions, asset

@asset
def iris_dataset(duckdb: DuckDBResource) -> None:
    iris_df = pd.read_csv(
        "https://docs.dagster.io/assets/iris.csv",
        names=[
            "sepal_length",
            "sepal_width",
            "petal_length",
            "petal_width",
            "species"
        ]
    )

    with duckdb.get_connection() as conn:
        conn.execute("CREATE TABLE iris_dataset AS SELECT * FROM iris_df")
