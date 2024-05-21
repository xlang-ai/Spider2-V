from dagster import job
from dagster_airbyte import airbyte_resource, airbyte_sync_op

my_airbyte_resource = airbyte_resource.configured(
    {
        "host": "localhost",
        "port": "8000",
    }
)
mysql_to_json = airbyte_sync_op.configured({"connection_id": "airbyte_connection_uuid"}, name="mysql_to_json")

@job(resource_defs={"airbyte": my_airbyte_resource})
def airbyte_job():
    mysql_to_json()
