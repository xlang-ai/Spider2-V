Documentation Source:
release-1-7-2.dagster.dagster-docs.io/tutorial/scheduling-your-pipeline.md

Documentation Title:
Tutorial, part five: Scheduling your pipeline | Dagster Docs

Documentation Content:
Confirm that your job was defined by:

1. Going to the UI
2. Reloading your project through the **Reload Definitions**button in the asset graph or on the **Deployments**page
3. Navigating to **Overview > Jobs**
4. Clicking on the job
5. Seeing your assets selected for the job

!### About definitions#

Up until this point, you defined assets using the `@asset`decorator. Dagster definitions are entities that Dagster learns about by importing your code. Just now, you used a different kind of definition: a job definition.

Managing one type of definition, such as assets, is easy. However, it can quickly become unruly as your project grows to have a variety of definitions (ex. schedules, jobs, sensors). To combine definitions and have them aware of each other, Dagster provides a utility called the `Definitions`object.

Step 2: Scheduling the materializations#
----------------------------------------

After defining a job, it can be attached to a schedule. A schedule's responsibility is to start a run of the assigned job at a specified time. Schedules are added with the `ScheduleDefinition`class.

To regularly update the assets, add the new `ScheduleDefinition`import, create a new schedule for the `hackernews_job`, and add the schedule to the code location. The code below is how your `__init__.py`should look after making these changes:

`fromdagster import(AssetSelection,Definitions,ScheduleDefinition,define_asset_job,load_assets_from_modules,)from.importassets

all_assets =load_assets_from_modules([assets])# Define a job that will materialize the assetshackernews_job =define_asset_job("hackernews_job",selection=AssetSelection.all())# Addition: a ScheduleDefinition the job it should run and a cron schedule of how frequently to run ithackernews_schedule =ScheduleDefinition(job=hackernews_job,cron_schedule="0 * * * *",# every hour)defs =Definitions(assets=all_assets,schedules=[hackernews_schedule],)`Go to the UI, click **Overview > Schedules tab**, and observe your new schedule with the attached job.



Documentation Source:
release-1-7-2.dagster.dagster-docs.io/tutorial/scheduling-your-pipeline.md

Documentation Title:
Tutorial, part five: Scheduling your pipeline | Dagster Docs

Documentation Content:
Ask AI!PlatformDagster+NewPricingBlogCommunityDocsSign inJoin us on Slack!Star usTry Dagster+PlatformDagster+PricingBlogCommunityDocsContact SalesSign inTry Dagster+Search the docsPress Ctrl and `K`to searchGetting startedWhat's Dagster?QuickstartInstallationCreating a new projectGetting helpTutorialConceptsDeploymentIntegrationsGuidesAPI ReferenceAbout1.7.2/ 0.23.2 (libs)### You are viewing an unreleased or outdated version of the documentation

View Latest Documentation →Tutorial, part five: Scheduling your pipeline#
==============================================

Now that you've written an entire pipeline in Dagster, you will need to run it regularly to keep your assets up to date.

By the end of this part of the tutorial, you'll be able to:

* Structure your project with code locations and jobs
* Refresh your assets periodically with schedules

Step 1: Defining what assets to update#
---------------------------------------

A *job*lets you target a selection of assets to materialize them together as a single action. Assets can belong to multiple jobs.

Your Dagster repository has a file called `tutorial/__init__.py`that is used as a top-level definition for your project. Update the code in this file to add the job using the `define_asset_job`function:

`fromdagster import(AssetSelection,Definitions,define_asset_job,load_assets_from_modules,)from.importassets

all_assets =load_assets_from_modules([assets])# Addition: define a job that will materialize the assetshackernews_job =define_asset_job("hackernews_job",selection=AssetSelection.all())defs =Definitions(assets=all_assets,jobs=[hackernews_job],# Addition: add the job to Definitions object (see below))`Dagster's `AssetSelection`module lets you choose which assets to attach to a job. In the example above, `AssetSelection.all`selects all assets.

Once you have a job, you can execute it on a schedule, by clicking a button in the Dagster UI, the CLI, or via Dagster's GraphQL endpoints. Confirm that your job was defined by:

1. Going to the UI
2.



Documentation Source:
release-1-7-2.dagster.dagster-docs.io/tutorial/scheduling-your-pipeline.md

Documentation Title:
Tutorial, part five: Scheduling your pipeline | Dagster Docs

Documentation Content:
!To test the change, click the schedule's name to view its details. Click the **Test Schedule**button on the top right corner of the page to trigger the schedule immediately.

!Schedules are just one way to start jobs. Jobs can also be run by using the CLI, a Python function, or the UI. Refer to theJobs documentationto learn more.### Other ways to automate your pipelines#

You've used a schedule to update your data on a regular cadence. However, there are other ways to trigger jobs. For example, sensors can trigger a job after routinely polling a source. Check out the Automation guideto learn more.

Next steps#
-----------

By now, you've:

* Grouped your objects with a code location
* Defined a sequence of materializations with a job
* Run the job on a schedule

In the next section, you'll learn how to build more robustness, reusability, and flexibility when connecting to external servicesby using resources.

On This Page- Tutorial, part five: Scheduling your pipeline
	1. Step 1: Defining what assets to updateAbout definitions
	2. Step 2: Scheduling the materializationsOther ways to automate your pipelines
	Next steps
Edit Page on GitHubShare FeedbackStar



Documentation Source:
release-1-7-2.dagster.dagster-docs.io/concepts/assets/asset-checks/define-execute-asset-checks.md

Documentation Title:
Defining and executing asset checks | Dagster Docs

Documentation Content:
Via sensors and schedules

To define jobs that execute sets of assets and checks, you can use `define_asset_job`and then trigger the jobs via sensorsor schedules. By default, checks are included with the assets they check. You can also define jobs that include only checks, or only assets.

`fromdagster import(AssetSelection,Definitions,ScheduleDefinition,asset,asset_check,define_asset_job,)@assetdefmy_asset():...@asset_check(asset=my_asset)defcheck_1():...@asset_check(asset=my_asset)defcheck_2():...# includes my_asset and both checksmy_job =define_asset_job("my_job",selection=AssetSelection.assets(my_asset))# includes only my_assetmy_asset_only_job =define_asset_job("my_asset_only_job",selection=AssetSelection.assets(my_asset).without_checks(),)# includes check_1 and check_2, but not my_assetchecks_only_job =define_asset_job("checks_only_job",selection=AssetSelection.checks_for_assets(my_asset))# includes only check_1check_1_job =define_asset_job("check_1_job",selection=AssetSelection.checks(check_1))# schedule my_job to run every day at midnightbasic_schedule =ScheduleDefinition(job=my_job,cron_schedule="0 0 * * *")defs =Definitions(assets=[my_asset],asset_checks=[check_1,check_2],jobs=[my_job,my_asset_only_job,checks_only_job,check_1_job],schedules=[basic_schedule],)`Testing checks#
---------------

Refer to the Asset checks sectionof the Testingdocumentation for more information.

APIs in this guide#
-------------------



