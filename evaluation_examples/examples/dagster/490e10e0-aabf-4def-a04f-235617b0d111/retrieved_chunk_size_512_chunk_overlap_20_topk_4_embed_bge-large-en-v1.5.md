Documentation Source:
release-1-7-2.dagster.dagster-docs.io/guides/running-dagster-locally.md

Documentation Title:
Running Dagster locally | Dagster Docs

Documentation Content:
Ask AI!PlatformDagster+NewPricingBlogCommunityDocsSign inJoin us on Slack!Star usTry Dagster+PlatformDagster+PricingBlogCommunityDocsContact SalesSign inTry Dagster+Search the docsPress Ctrl and `K`to searchGetting startedWhat's Dagster?QuickstartInstallationCreating a new projectGetting helpTutorialConceptsDeploymentIntegrationsGuidesAPI ReferenceAbout1.7.2/ 0.23.2 (libs)### You are viewing an unreleased or outdated version of the documentation

View Latest Documentation →Running Dagster locally#
========================

In this guide, we'll walk you through how to run Dagster on your local machine using the `dagster dev`command.

**Looking for installation help?**Refer to the Dagster installation guide.

Understanding the dagster dev command#
--------------------------------------

The `dagster dev`command launches the Dagster webserver/UIand the Dagster daemon, allowing you to start a full deployment of Dagster from the command line.

This command should be run in a Python environment where the `dagster`and `dagster-webserver`packages are installed. **Once started, the process should be kept running.**

Locating your code#
-------------------

Before you can start developing, you need to tell Dagster how to find the Python code containing your assets and jobs. There are a few ways to do this, which are outlined in the tabs below.

**Note**: If using an example Dagster project, or if you used the `dagster`CLI to create a project, you can run the `dagster dev`command in the same folder as the project to load the project code.

From a fileFrom a moduleWithout command line argumentsDagster can load a file directly as a code location. In the following example, we used the `-f`argument to supply the name of the file:

`dagster dev -f my_file.py`This command loads the definitions in `my_file.py`as a code location in the current Python environment.

You can also include multiple files at a time, where each file will be loaded as a code location:

`dagster dev -f my_file.py -f my_second_file.py`Configuration#
--------------

Run and asset storageLocal instance



Documentation Source:
release-1-7-2.dagster.dagster-docs.io/concepts/webserver/ui.md

Documentation Title:
Dagster UI | Dagster

Documentation Content:
Ask AI!PlatformDagster+NewPricingBlogCommunityDocsSign inJoin us on Slack!Star usTry Dagster+PlatformDagster+PricingBlogCommunityDocsContact SalesSign inTry Dagster+Search the docsPress Ctrl and `K`to searchGetting startedWhat's Dagster?QuickstartInstallationCreating a new projectGetting helpTutorialConceptsDeploymentIntegrationsGuidesAPI ReferenceAbout1.7.2/ 0.23.2 (libs)### You are viewing an unreleased or outdated version of the documentation

View Latest Documentation →Dagster UI#
===========

The Dagster UI is a web-based interface for viewing and interacting with Dagster objects.

You can inspect Dagster objects (ex: assets, jobs, schedules), launch runs, view launched runs, and view assets produced by those runs.

Launching the UI#
-----------------

The easiest way to launch the UI from the command line during local development is to run:

`dagster dev`This command launches both the Dagster webserver (which serves the UI) and the Dagster daemon, allowing you to start a full local deployment of Dagster from the command line.

The command will print out the URL you can access the UI from in the browser, usually on port 3000.

When invoked, the UI will fetch definitions - such as assets, jobs, schedules, sensors, and resources - from a `Definitions`object in a Python module or package or the code locations configured in an open source deployment's workspace files. Refer to the Code location documentationfor more info.

You can also launch the webserver by itself from the command line by running:

`dagster-webserver`Note that several Dagster features, like schedules and sensors, require the Dagster daemon to be running in order to function.

Overview#
---------

**Description**: This page, also known as the "factory floor", provides a high-level look at the activity in your Dagster deployment, across all code locations. This includes information about runs, jobs, schedules, sensors, resources, and backfills, all of which can be accessed using the tabs on this page.

**Accessed by**: Clicking **Overview**in the top navigation bar



Documentation Source:
release-1-7-2.dagster.dagster-docs.io/deployment/guides/docker.md

Documentation Title:
Deploying Dagster to Docker | Dagster

Documentation Content:
For example, if you are using the Dagster daemonto run schedules and sensors or manage a queue of runs, you'll likely want a separate container running the `dagster-daemon`service.

This service must have access to your `dagster.yaml`and `workspace.yaml`files, just like the webserver container. You can also configure your code location server (gRPC server) so that your code can be updated and deployed separately in its own container, without needing to redeploy the other Dagster services. To enable this setup, include a container exposing a gRPC server at a port and add that port in your `workspace.yaml`file.

For example, your user code container might have the following Dockerfile:

`FROMpython:3.10-slim# Checkout and install dagster libraries needed to run the gRPC server by exposing# your code location to dagster-webserver and dagster-daemon, and loading the# DagsterInstance.RUNpip install \dagster \dagster-postgres \dagster-docker# Set $DAGSTER_HOME and copy dagster instance thereENVDAGSTER_HOME=/opt/dagster/dagster_homeRUNmkdir -p $DAGSTER_HOMECOPYdagster.yaml $DAGSTER_HOME# Add repository codeWORKDIR/opt/dagster/appCOPYrepo.py /opt/dagster/app# Run dagster gRPC server on port 4000EXPOSE4000# Using CMD rather than ENTRYPOINT allows the command to be overridden in# run launchers or executors to run other commands using this imageCMD["dagster", "api", "grpc", "-h", "0.0.0.0", "-p", "4000", "-f", "repo.py"]`And your code location server might look like:

`load_from:# Each entry here corresponds to a container that exposes a gRPC server.-grpc_server:host:docker_example_user_code
 port:4000location_name:"example_user_code"`When you update your code, you can rebuild and restart your user code container without needing to redeploy other parts of the system. The Dagster UI will automatically notice that a new server has been redeployed and prompt you to refresh.



Documentation Source:
release-1-7-2.dagster.dagster-docs.io/deployment/guides/docker.md

Documentation Title:
Deploying Dagster to Docker | Dagster

Documentation Content:
A minimal skeleton `Dockerfile`that will run the webserver is shown below:

`FROMpython:3.10-slimRUNmkdir -p /opt/dagster/dagster_home /opt/dagster/appRUNpip install dagster-webserver dagster-postgres dagster-aws# Copy your code and workspace to /opt/dagster/appCOPYrepo.py workspace.yaml /opt/dagster/app/ENVDAGSTER_HOME=/opt/dagster/dagster_home/# Copy dagster instance YAML to $DAGSTER_HOMECOPYdagster.yaml /opt/dagster/dagster_home/WORKDIR/opt/dagster/appEXPOSE3000ENTRYPOINT["dagster-webserver", "-h", "0.0.0.0", "-p", "3000"]`You'll also need to include a workspace file (`workspace.yaml`)file in the same directory as the Dockerfile to configure your code location server:

`load_from:# References the file copied into your Dockerfile-python_file:repo.py`As well as a `dagster.yaml`file to configure your Dagster instance:

`storage:postgres:postgres_db:username:env:DAGSTER_PG_USERNAME
 password:env:DAGSTER_PG_PASSWORD
 hostname:env:DAGSTER_PG_HOST
 db_name:env:DAGSTER_PG_DB
 port:5432compute_logs:module:dagster_aws.s3.compute_log_manager
 class:S3ComputeLogManager
 config:bucket:"mycorp-dagster-compute-logs"prefix:"dagster-test-"local_artifact_storage:module:dagster.core.storage.root
 class:LocalArtifactStorage
 config:base_dir:"/opt/dagster/local/"`In cases where you're using environment variables to configure the instance, you should ensure these environment variables are exposed in the container running `dagster-webserver`.

The webserver exposes a health check endpoint at `/server_info`, which returns a JSON response like:

`{"dagster_webserver_version":"0.12.0","dagster_graphql_version":"0.12.0","dagster_version":"0.12.0"}`Multi-container Docker deployment#
----------------------------------

More advanced Dagster deployments will require deploying more than one container.



