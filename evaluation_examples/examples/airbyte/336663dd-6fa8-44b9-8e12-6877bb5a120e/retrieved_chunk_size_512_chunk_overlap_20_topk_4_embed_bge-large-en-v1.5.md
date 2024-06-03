Documentation Source:
airbyte.com/tutorials/orchestrate-data-ingestion-and-transformation-pipelines.md

Documentation Title:
Orchestrate data ingestion and transformation pipelines with Dagster | Airbyte

Documentation Content:
Set up a Slack source

Our second source is the public Dagster Slack, where we’ll ingest the messages sent to one of our public channels.

If you’re following along, you can just read from whatever Slack channels you have access to, and if you don’t have easy access to a Slack API token, feel free to skip this entirely and replace the `slack\_github\_analytics.py` file in the Dagster code you cloned with `github\_analytics.py`.

Once again, full instructions for setting up this source and generating a token can be found in the Airbyte docs, but your configuration should end up looking like this:

!Just like with the Github connection, we set a start date of 2022-01-01. Once this source is created, we can hook it up to our LocalPostgres destination:

!Orchestrate Airbyte data ingestion pipelines with Dagster
---------------------------------------------------------

Now that we have some Airbyte connections to work with, we can get back to Dagster.

In the first few lines of slack\_github\_analytics.py, you’ll see the following code:

`from dagster_airbyte import airbyte_resource, airbyte_sync_op



Documentation Source:
airbyte.com/tutorials/orchestrate-data-ingestion-and-transformation-pipelines.md

Documentation Title:
Orchestrate data ingestion and transformation pipelines with Dagster | Airbyte

Documentation Content:
You can easily install Airbyte with Docker Compose and access the UI locally at http://localhost:8000:

`$ git clone https://github.com/airbytehq/airbyte.git$ cd airbyte$ docker-compose up`### Should you build or buy your data pipelines?

Download our free guide and discover the best approach for your needs, whether it's building your ELT solution in-house or opting for Airbyte Open Source or Airbyte Cloud.

Download now!Ingest data from Slack and Github to Postgres
---------------------------------------------

If you already have some Airbyte connections set up for other purposes, feel free to use those instead! All you need for this demo to work is the Airbyte connection ids. However, if you’re starting from scratch, or just want to follow along, read on.



Documentation Source:
airbyte.com/tutorials/orchestrate-data-ingestion-and-transformation-pipelines.md

Documentation Title:
Orchestrate data ingestion and transformation pipelines with Dagster | Airbyte

Documentation Content:
…

sync_github = airbyte_sync_op.configured(
 {"connection_id": ""}, name="sync_github"
)
sync_slack = airbyte_sync_op.configured(
 {"connection_id": ""}, name="sync_slack"
)`Here, we define the first two operations (or “ops”, in Dagster) of our job. Dagster’s Airbyte integrationoffers a pre-built op that will, when configured with a particular connection id, kick off a sync of that connection and wait until it completes. We also give these ops names (“sync\_github” and “sync\_slack”) to help people looking at this job understand what they’re doing.

This is where you can substitute in the relevant connection ids for the connections you set up in the previous steps. A quick way to find the id for a given connection is to click on it in the Airbyte UI, and grab the last section of the URL, i.e.:

!Once you’ve entered the correct values in for the `connection\_id` fields, the code is ready to be executed! However, before that happens, let’s quickly explain what’s happening in the rest of the code.

Orchestrate dbt transformations with Dagster
--------------------------------------------

Directly after the Airbyte ops, you’ll see the following code:

`transform_slack_github = dbt_run_op.alias(name="transform_slack_github")`‍

Here, we’re once again using a pre-built op imported from one of Dagster’s integration libraries. In this case, the op will run a dbt project that is configured to combine and transform the Slack and Github data together into a single table. The dbt project used hereis included in the directory that you originally cloned, so no need to create your own, but feel free to modify / play around with it!

Strictly speaking, this line of code isn’t necessary (we could just directly include `dbt\_run\_op` in the job below), but this allows us to give the generic op a more specific name.

Orchestrate Python transformations with Dagster
-----------------------------------------------

Finally, we have a few custom Python ops.



Documentation Source:
airbyte.com/tutorials/orchestrate-data-ingestion-and-transformation-pipelines.md

Documentation Title:
Orchestrate data ingestion and transformation pipelines with Dagster | Airbyte

Documentation Content:
Dagster has deep integrations with both Airbyte and dbt, which go beyond just kicking off runs in these external environments, giving visibility into the tables that are produced using these tools.

This recipe will demonstrate how you can combine the flexibility of Python with the power of modern data stack tools, and view all the important metadata across these different domains.

Set up Dagster
--------------

First, we’ll want to get Dagster running on our local machine. Dagster is completely open source and free to use, with no need to create an account. Dagster comes with a UI tool, Dagit, which can be used to view and run your jobs. Dagster allows you to write Python code to define data pipelines as a series of interdependent steps. To get you started, the source code used for this demo is available on Github:

`git clone https://github.com/OwenKephart/airbyte_demo.git`‍

Once you have the code, you can install all the required dependencies (including Dagster and Dagit) using pip.

`cd airbyte_demopip install -e .`‍

To make sure that everything is working properly, navigate to the directory you just cloned, and run:

`dagit -f airbyte_demo/slack_github_analytics.py`This will spin up a local Dagit instance in your browser, which should look something like:

!This contains a single data pipeline (called a “job” in Dagster), which is named “slack\_github\_analytics”. Already, you get a rich set of information about the steps in this job, the types of their inputs and outputs, and how they connect to each other.

However, if you try running this job right now, you’ll quickly hit an error, as we haven’t actually set up the Airbyte connections that this job is meant to update, so let’s do that now.

Set up Airbyte
--------------

You can run Airbyte to configure data replication jobs from applications like Github and Slack to databases like Postgres.



