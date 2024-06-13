Documentation Source:
release-1-7-2.dagster.dagster-docs.io/guides/dagster/intro-to-ops-jobs/single-op-job.md

Documentation Title:
Intro to ops and jobs, part one: Write a single-op job | Dagster Docs

Documentation Content:
Ask AI!PlatformDagster+NewPricingBlogCommunityDocsSign inJoin us on Slack!Star usTry Dagster+PlatformDagster+PricingBlogCommunityDocsContact SalesSign inTry Dagster+Search the docsPress Ctrl and `K`to searchGetting startedWhat's Dagster?QuickstartInstallationCreating a new projectGetting helpTutorialConceptsDeploymentIntegrationsGuidesAPI ReferenceAbout1.7.2/ 0.23.2 (libs)### You are viewing an unreleased or outdated version of the documentation

View Latest Documentation →Intro to ops and jobs, part one: Write a single-op job#
=======================================================

You can find the code for this example on GithubIn this guide, we'll touch on Dagster opsand jobs. Opsare individual units of computation that we wire together to form jobs.

In this part, you'll:

Write your first opWrite your first jobExecute the job
Step 1: Write your first op#
----------------------------

Let's write our first Dagster op and save it as `hello.py`.

Typically, you'll define ops by annotating ordinary Python functions with the `@op`decorator.

Our first op finds the sizes of all the files in our current directory and logs them.

`importos
fromdagster importjob,op,get_dagster_logger


@opdefget_file_sizes():files =[f forf inos.listdir(".")ifos.path.isfile(f)]forf infiles:get_dagster_logger().info(f"Size of {f}is {os.path.getsize(f)}")`In this simple case, our op takes no arguments, and also returns no outputs. Don't worry, we'll soon encounter ops that are more dynamic.

Step 2: Write your first job#
-----------------------------

To execute our op, we'll embed it in an equally simple job. A job is a set of ops arranged into a DAGof computation. You'll typically define jobs by annotating ordinary Python functions with the `@job`decorator.

`@jobdeffile_sizes_job():get_file_sizes()`Here you'll see that we call `get_file_sizes()`.



Documentation Source:
release-1-7-2.dagster.dagster-docs.io/guides/dagster/intro-to-ops-jobs/connecting-ops.md

Documentation Title:
Intro to ops and jobs, part two: Connecting ops in jobs | Dagster Docs

Documentation Content:
`importos

fromdagster importget_dagster_logger,job,op


@opdefget_file_sizes():files =[f forf inos.listdir(".")ifos.path.isfile(f)]return{f:os.path.getsize(f)forf infiles}@opdefreport_total_size(file_sizes):total_size =sum(file_sizes.values())# In real life, we'd send an email or Slack message instead of just logging:get_dagster_logger().info(f"Total size: {total_size}")@jobdefserial():report_total_size(get_file_sizes())`You'll see that we've modified our existing `get_file_sizes`op to return an output, in this case a dictionary that maps file names to their sizes.

We've defined our new op, `report_total_size`, to take an input, `file_sizes`.

We can use inputs and outputs to connect ops to each other. Here we tell Dagster that:

* `get_file_sizes`doesn't depend on the output of any other op.
* `report_total_size`depends on the output of `get_file_sizes`.

Let's visualize this job in the Dagster UI:

`dagster dev -f serial_job.py`Navigate to http://127.0.0.1:3000:

!Step 2: Use op outputs as op inputs#
------------------------------------

Ops don't need to be wired together serially. The output of one op can be consumed by any number of other ops, and the outputs of several different ops can be consumed by a single op.

`importos

fromdagster importget_dagster_logger,job,op



Documentation Source:
release-1-7-2.dagster.dagster-docs.io/guides/dagster/intro-to-ops-jobs/connecting-ops.md

Documentation Title:
Intro to ops and jobs, part two: Connecting ops in jobs | Dagster Docs

Documentation Content:
Dagster models these dataflow dependencies with inputs and outputs.

In this part, you'll:

* Expand the `serial`job from part oneto encompass multiple ops
Use the output of one op as the input to another op
Step 1: Expand the serial job#
------------------------------

We'll expand the job we worked with in the first section of the tutorial into two ops that:

* Get the sizes of all the files in our directory
* Report the sum of the file sizes. In a more realistic setting, we'd send an email or Slack message. For simplicity, we just emit a log message.

This will allow us to re-run the code that reports the summed size without re-running the code that crawls the filesystem. If we spot a bug in our reporting code, or if we decide we want to change how we report it, we won't need to re-crawl the filesystem.

`importos

fromdagster importget_dagster_logger,job,op



Documentation Source:
release-1-7-2.dagster.dagster-docs.io/guides/dagster/intro-to-ops-jobs/single-op-job.md

Documentation Title:
Intro to ops and jobs, part one: Write a single-op job | Dagster Docs

Documentation Content:
This call doesn't actually execute the op. Within the bodies of functions decorated with `@job`, we use function calls to indicate the dependency structure of the op making up the job. Here, we indicate that the execution of `get_file_sizes`doesn't depend on any other ops by calling it with no arguments.

Step 3: Execute your first job#
-------------------------------

Assuming you’ve saved this job as `hello.py`, you can execute it via any of three different mechanisms:

Dagster UIDagster CLIPython API### Dagster UI#

To visualize your job (which only has one op) in the UI, just run the following. Make sure you're in the directory in which you've saved the job file:

`dagster dev -f hello.py`You'll see output like:

`Serving dagster-webserver on http://127.0.0.1:3000 inprocess 70635`You should be able to navigate to http://127.0.0.1:3000in your web browser and view your job. It isn't very interesting yet, because it only has one op.

!Click on the **Launchpad**tab and you'll see the view below.

!The large upper left pane is empty here, but, in jobs with parameters, this is where you'll be able to edit job configuration on the fly.

Click the **Launch Run**button on the bottom right to execute this job directly from the UI. A new window should open, and you'll see a much more structured view of the stream of Dagster events start to appear in the left-hand pane.

If you have pop-up blocking enabled, you may need to tell your browser to allow pop-ups from 127.0.0.1—or, just navigate to the **Runs**tab to see this, and every run of your job.

!In this view, you can filter and search through the logs corresponding to your job run.

What's next?#
-------------

At this point, you should have an executed job that contains a single op. The next step is to connect a series of ops in a job.



