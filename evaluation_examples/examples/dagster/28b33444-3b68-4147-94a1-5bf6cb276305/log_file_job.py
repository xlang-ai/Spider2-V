from dagster import op, job, Config, OpExecutionContext


class FileConfig(Config):
    filename: str


@op
def process_file(context: OpExecutionContext, config: FileConfig) -> None:
    context.log.info(config.filename)
    
@job
def log_file_job() -> None:
    process_file()