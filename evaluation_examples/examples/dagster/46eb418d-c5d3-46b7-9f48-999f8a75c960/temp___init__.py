from dagster import Definitions, load_assets_from_modules

from . import assets, log_file_job
from .directory_sensor import directory_sensor

all_assets = load_assets_from_modules([assets])

defs = Definitions(
    assets=all_assets,
    sensors=[directory_sensor]
)