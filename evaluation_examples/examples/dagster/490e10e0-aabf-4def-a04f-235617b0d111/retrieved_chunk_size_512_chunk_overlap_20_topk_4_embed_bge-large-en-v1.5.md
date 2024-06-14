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
release-1-7-2.dagster.dagster-docs.io/deployment/dagster-daemon.md

Documentation Title:
Dagster daemon | Dagster

Documentation Content:
Running locally

Running the daemon and webserverRunning only the daemonThe easiest way to run the Dagster daemon locally is to run the `dagster dev`command:

`dagster dev`This command launches both the Dagster webserver/UIand the Dagster daemon, allowing you to start a full local deployment of Dagster from the command line. Refer to the Running Dagster locally guidefor more information about `dagster dev`.



Documentation Source:
release-1-7-2.dagster.dagster-docs.io/deployment/guides/service.md

Documentation Title:
Running Dagster as a Service | Dagster"

Documentation Content:
Ask AI!PlatformDagster+NewPricingBlogCommunityDocsSign inJoin us on Slack!Star usTry Dagster+PlatformDagster+PricingBlogCommunityDocsContact SalesSign inTry Dagster+Search the docsPress Ctrl and `K`to searchGetting startedWhat's Dagster?QuickstartInstallationCreating a new projectGetting helpTutorialConceptsDeploymentIntegrationsGuidesAPI ReferenceAbout1.7.2/ 0.23.2 (libs)### You are viewing an unreleased or outdated version of the documentation

View Latest Documentation →Running Dagster as a Service#
=============================

Running the Dagster webserver#
------------------------------

The core of any deployment of Dagster is the Dagster webserver, a process that serves the Dagster UI and responds to GraphQL queries.

To run the webserver locally, first ensure that you are running a recent Python version. Typically, you'll want to run the webserver inside a virtualenv. Then, you can install the webserver and any additional libraries you might need.

`pip installdagster-webserver`To run the webserver, use a command like the following:

`DAGSTER_HOME=/opt/dagster/dagster_home dagster-webserver -h 0.0.0.0 -p 3000`In this configuration, the webserver will write execution logs to `$DAGSTER_HOME/logs`and listen on *0.0.0.0:3000*.

Running the Dagster daemon#
---------------------------

If you're using schedules, sensors, or backfills, or want to set limits on the number of runs that can be executed at once, you'll want to also run a dagster-daemon serviceas part of your deployment. To run this service locally, run the following command:

`pip installdagster

DAGSTER_HOME=/opt/dagster/dagster_home dagster-daemon run`The `dagster-daemon`process will periodically check your instance for any new runs that should be launched from your run queue or triggered by your running schedules or sensors.



