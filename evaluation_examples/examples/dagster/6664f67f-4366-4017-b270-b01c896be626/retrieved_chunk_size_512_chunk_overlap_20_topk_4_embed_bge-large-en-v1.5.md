Documentation Source:
release-1-7-2.dagster.dagster-docs.io/guides/dagster-pipes/subprocess/reference.md

Documentation Title:
Dagster Pipes subprocess reference | Dagster Docs

Documentation Content:
defmain():orders_df =pd.DataFrame({"order_id":[1,2],"item_id":[432,878]})total_orders =len(orders_df)# get the Dagster Pipes contextcontext =PipesContext.get()# get all extras provided by Dagster assetprint(context.extras)# get the value of an extraprint(context.get_extra("foo"))# get env varprint(os.environ["MY_ENV_VAR_IN_SUBPROCESS"])if__name__ =="__main__":# connect to Dagster Pipeswithopen_dagster_pipes():main()`Working with @asset\_check#
---------------------------

Sometimes, you may not want to materialize an asset, but instead want to report a data quality check result. When your asset has data quality checks defined in `@asset_check`:

External code in external\_code.pyDagster code in dagster\_code.pyFrom the external code, you can report to Dagster that an asset check has been performed via `PipesContext.report_asset_check`. Note that `asset_key`in this case is required, and must match the asset key defined in `@asset_check`:

`importpandas aspd
fromdagster_pipes importPipesContext,open_dagster_pipes



Documentation Source:
release-1-7-2.dagster.dagster-docs.io/guides/dagster-pipes/subprocess/modify-external-code.md

Documentation Title:
Using Dagster Pipes, Part two: Modify external code | Dagster Docs

Documentation Content:
defmain():orders_df =pd.DataFrame({"order_id":[1,2],"item_id":[432,878]})total_orders =len(orders_df)# get the Dagster Pipes contextcontext =PipesContext.get()# send structured metadata back to Dagstercontext.report_asset_materialization(metadata={"total_orders":total_orders})# report data quality check result back to Dagstercontext.report_asset_check(passed=orders_df[["item_id"]].notnull().all().bool(),check_name="no_empty_order_check",)if__name__ =="__main__":# connect to Dagster Pipeswithopen_dagster_pipes():main()`When Dagster executes the code, you’ll see an asset check event with the check result in the UI:

!This check result will also be displayed on the **Checks**tab of the **Asset Details**page in the UI:

!Finished code#
--------------

At this point, your two files should look like the following:

External code in external\_code.pyDagster code in dagster\_code.py`importpandas aspd
fromdagster_pipes importPipesContext,open_dagster_pipes



Documentation Source:
release-1-7-2.dagster.dagster-docs.io/guides/dagster-pipes/subprocess/modify-external-code.md

Documentation Title:
Using Dagster Pipes, Part two: Modify external code | Dagster Docs

Documentation Content:
Report asset materialization

Similar to reporting materialization metadata within the Dagster process, you can also report asset materialization back to Dagster from the external process.

In this example, we’re passing a piece of metadata named `total_orders`to the `metadata`parameter of the `PipesContext.report_asset_materialization`. This payload will be sent from the external process back to Dagster:

`importpandas aspd
fromdagster_pipes importPipesContext,open_dagster_pipes


defmain():orders_df =pd.DataFrame({"order_id":[1,2],"item_id":[432,878]})total_orders =len(orders_df)# get the Dagster Pipes contextcontext =PipesContext.get()# send structured metadata back to Dagstercontext.report_asset_materialization(metadata={"total_orders":total_orders})if__name__ =="__main__":# connect to Dagster Pipeswithopen_dagster_pipes():main()`Then, `total_orders`will show up in the UI as structured metadata:

!This metadata will also be displayed on the **Events**tab of the **Asset Details**page in the UI:

!### Report asset checks#

Dagster allows you to define and execute data quality checks on assets. Refer to the Asset Checksdocumentation for more information.

If your asset has data quality checks defined, you can report to Dagster that an asset check has been performed via `PipesContext.report_asset_check`:

Report from the external codeDefine the asset in the Dagster code`importpandas aspd
fromdagster_pipes importPipesContext,open_dagster_pipes



Documentation Source:
release-1-7-2.dagster.dagster-docs.io/guides/dagster-pipes/subprocess/modify-external-code.md

Documentation Title:
Using Dagster Pipes, Part two: Modify external code | Dagster Docs

Documentation Content:
defmain():orders_df =pd.DataFrame({"order_id":[1,2],"item_id":[432,878]})total_orders =len(orders_df)# get the Dagster Pipes contextcontext =PipesContext.get()# send structured metadata back to Dagstercontext.report_asset_materialization(metadata={"total_orders":total_orders})# report data quality check result back to Dagstercontext.report_asset_check(passed=orders_df[["item_id"]].notnull().all().bool(),check_name="no_empty_order_check",)if__name__ =="__main__":# connect to Dagster Pipeswithopen_dagster_pipes():main()`What's next?#
-------------

In this tutorial, you learned how to get access to Dagster Pipes context, report log messages events from the external process, and send structured events back to Dagster.

What's next? From here, you can:

* Learn about other capabilities of executing external code in subprocess via Dagster Pipes in the Subprocess reference
* Learn how to customize your own Dagster Pipes protocols
On This Page- Using Dagster Pipes, part 2: Modify external code & send information to Dagster
	Step 1: Make Dagster context available in external codeStep 2: Send log messages to Dagster3. Step 3: Send structured metadata to Dagster
		Report asset materializationReport asset checks
	Finished codeWhat's next?
Edit Page on GitHubShare FeedbackStar



