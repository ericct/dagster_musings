from dagster import (
    AssetSelection,
    Definitions,
    ScheduleDefinition,
    define_asset_job,
    load_assets_from_modules,
    FilesystemIOManager,  
)

from dagster_duckdb_pandas import DuckDBPandasIOManager # Adding IO Manager from library

from . import assets

all_assets = load_assets_from_modules([assets])

hackernews_job = define_asset_job("hackernews_job", selection=AssetSelection.all())

hackernews_schedule = ScheduleDefinition(
    job=hackernews_job,
    cron_schedule="0 * * * *",  # every hour
)

file_io_manager = FilesystemIOManager(
    base_dir="data",  
)

database_io_manager = DuckDBPandasIOManager(database="analytics.hackernews.duckdb") # instantiate IO Manager

defs = Definitions(
    assets=all_assets,
    schedules=[hackernews_schedule],
    resources={
        "io_manager": file_io_manager,
        "database_io_manager": database_io_manager,  # Define the I/O manager here (to be referenced in asset definitions)
    },
)