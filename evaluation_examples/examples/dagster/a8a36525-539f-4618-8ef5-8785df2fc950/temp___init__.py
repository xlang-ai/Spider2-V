from dagster import Definitions, load_assets_from_modules
from dagster_duckdb import DuckDBResource

from . import assets

all_assets = load_assets_from_modules([assets])

defs = Definitions(
    assets=all_assets,
    resources={
        "duckdb": DuckDBResource(
            database="iris_db.duckdb"
        )
    }
)
