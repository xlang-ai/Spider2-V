import pandas as pd
from dagster_pipes import PipesContext, open_dagster_pipes


def main():
    orders_df = pd.read_csv("orders_data.csv")
    total_orders = len(orders_df)
    # get the Dagster Pipes context
    context = PipesContext.get()
    # send structured metadata back to Dagster
    context.report_asset_materialization(metadata={"total_orders": total_orders})
    # report data quality check result back to Dagster
    context.report_asset_check(
        passed=orders_df[["Item_ID"]].notnull().all().bool(),
        check_name="no_null_check",
    )


if __name__ == "__main__":
    # connect to Dagster Pipes
    with open_dagster_pipes():
        main()
