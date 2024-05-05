import os
from typing import Union

import pandas as pd
from dagster import (
    ConfigurableIOManager,
    InputContext,
    OutputContext,
    _check as check,
)
from dagster._seven.temp_dir import get_system_temp_directory


class ParquetIOManager(ConfigurableIOManager):
    """This IOManager will take in a pandas dataframe and store it in parquet at the
    specified path.

    It stores outputs for different partitions in different filepaths.
    """

    base_path: str = get_system_temp_directory()

    @property
    def _base_path(self):
        return self.base_path

    def handle_output(self, context: OutputContext, obj: pd.DataFrame):
        path = self._get_path(context)
        if "://" not in self._base_path:
            os.makedirs(os.path.dirname(path), exist_ok=True)

        if isinstance(obj, pd.DataFrame):
            row_count = len(obj)
            context.log.info(f"Row count: {row_count}")
            obj.to_parquet(path=path, index=False)
        else:
            raise Exception(f"Outputs of type {type(obj)} not supported.")

        context.add_output_metadata({"row_count": row_count, "path": path})

    def load_input(self, context):
        pass

    def _get_path(self, context: Union[InputContext, OutputContext]):
        key = context.asset_key.path[-1]

        return os.path.join(self._base_path, f"{key}.pq")
