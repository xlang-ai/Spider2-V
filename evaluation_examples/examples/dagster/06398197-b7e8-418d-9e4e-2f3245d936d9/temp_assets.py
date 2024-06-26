import shutil

from dagster import (
    AssetCheckSpec,
    AssetExecutionContext,
    PipesSubprocessClient,
    asset,
    file_relative_path,
)


@asset(
    check_specs=[AssetCheckSpec(name="no_null_check", asset="subprocess_asset")],
)
def subprocess_asset(
    context: AssetExecutionContext, pipes_subprocess_client: PipesSubprocessClient
):
    cmd = [
        shutil.which("python"),
        file_relative_path(__file__, "external.py"),
    ]
    return pipes_subprocess_client.run(
        command=cmd, context=context
    ).get_materialize_result()


