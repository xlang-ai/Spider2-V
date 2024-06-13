from dagster import Definitions, load_assets_from_modules
from .parquet_io_manager import ParquetIOManager

from . import assets

all_assets = load_assets_from_modules([assets])

defs = Definitions(
    assets=all_assets,
    resources={
        "parquet": ParquetIOManager(),
    }
)
