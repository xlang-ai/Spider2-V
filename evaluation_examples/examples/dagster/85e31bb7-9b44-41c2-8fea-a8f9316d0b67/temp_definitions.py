import os

from dagster import Definitions
from dagster_dbt import DbtCliResource

from .assets import jaffle_shop_dbt_assets, customers
from .constants import dbt_project_dir
from .schedules import schedules

defs = Definitions(
    assets=[jaffle_shop_dbt_assets, customers],
    schedules=schedules,
    resources={
        "dbt": DbtCliResource(project_dir=os.fspath(dbt_project_dir)),
    },
)