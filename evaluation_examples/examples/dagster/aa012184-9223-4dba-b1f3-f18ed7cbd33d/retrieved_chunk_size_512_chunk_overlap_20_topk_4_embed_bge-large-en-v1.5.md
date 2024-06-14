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
@opdefget_file_sizes():files =[f forf inos.listdir(".")ifos.path.isfile(f)]return{f:os.path.getsize(f)forf infiles}@opdefget_total_size(file_sizes):returnsum(file_sizes.values())@opdefget_largest_size(file_sizes):returnmax(file_sizes.values())@opdefreport_file_stats(total_size,largest_size):# In real life, we'd send an email or Slack message instead of just logging:get_dagster_logger().info(f"Total size: {total_size}, largest size: {largest_size}")@jobdefdiamond():file_sizes =get_file_sizes()report_file_stats(total_size=get_total_size(file_sizes),largest_size=get_largest_size(file_sizes),)`First, we introduce the intermediate variable `file_sizes`into our job definition to represent the output of the `get_file_sizes`op. Then we make both `get_total_size`and `get_largest_size`consume this output. Their outputs are in turn both consumed by `report_file_stats`.

Let's visualize this job in the UI:

`dagster dev -f complex_job.py`Which looks like:

!When you execute this example from the UI, you'll see that `get_file_sizes`executes first, followed by `get_total_size`and `get_largest_size`executing in parallel, since they don't depend on each other's outputs. Finally, `report_file_stats`executes last, only after `get_total_size`and `get_largest_size`have both executed (because `report_file_stats`depends on both of their outputs).

What's next?#
-------------

At this point, you've connected a series of ops in a job and learned how to use op output as input to another op. The next step is to test your ops and jobs.

On This Page- Intro to ops and jobs, part two: Connecting ops in jobs
	Step 1: Expand the serial jobStep 2: Use op outputs as op inputsWhat's next?
Edit Page on GitHubShare FeedbackStar



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



