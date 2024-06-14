Documentation Source:
release-1-7-2.dagster.dagster-docs.io/getting-started/create-new-project.md

Documentation Title:
Creating a new Dagster project | Dagster Docs

Documentation Content:
Ask AI!PlatformDagster+NewPricingBlogCommunityDocsSign inJoin us on Slack!Star usTry Dagster+PlatformDagster+PricingBlogCommunityDocsContact SalesSign inTry Dagster+Search the docsPress Ctrl and `K`to searchGetting startedWhat's Dagster?QuickstartInstallationCreating a new projectGetting helpTutorialConceptsDeploymentIntegrationsGuidesAPI ReferenceAbout1.7.2/ 0.23.2 (libs)### You are viewing an unreleased or outdated version of the documentation

View Latest Documentation →Creating a new Dagster project#
===============================

The easiest way to start building a Dagster project is by using the `dagster project`CLI. This CLI tool helps generate files and folder structures that enable you to quickly get started with Dagster.

Step 1: Bootstrap a new project#
--------------------------------

If you don't already have Dagster installed, verify you meet theinstallation requirementsbefore continuing.You can scaffold a new project using the default project skeleton, or start with one of the official Dagster examples.

To learn more about the default files in a Dagster project, refer to the Dagster project file reference.

Default project skeletonOfficial example### Using the default project skeleton#

To get started, run:

`pip installdagster
dagster project scaffold --name my-dagster-project`The `dagster project scaffold`command generates a folder structure with a single Dagster code location and other files, such as `pyproject.toml`and `setup.py`. This takes care of setting things up with an empty project, enabling you to quickly get started.

Step 2: Install project dependencies#
-------------------------------------

The newly generated `my-dagster-project`directory is a fully functioning Python packageand can be installed with `pip`.

To install it as a package and its Python dependencies, run:

`pip install-e ".



Documentation Source:
release-1-7-2.dagster.dagster-docs.io/_apidocs/cli.md

Documentation Title:
Dagster Docs

Documentation Content:
```
dagsterproject[OPTIONS]COMMAND[ARGS]...

```
Commands

from-exampleDownload one of the official Dagster examples to the current directory. This CLI enables you to quickly bootstrap your project with an officially maintained example.

list-examplesList the examples that available to bootstrap with.

scaffoldCreate a folder structure with a single Dagster code location and other files such as pyproject.toml. This CLI enables you to quickly start building a new Dagster project with everything set up.

scaffold-code-locationCreate a folder structure with a single Dagster code location, in the current directory. This CLI helps you to scaffold a new Dagster code location within a folder structure that includes multiple Dagster code locations.

scaffold-repository(DEPRECATED; Use dagster project scaffold-code-locationinstead) Create a folder structure with a single Dagster repository, in the current directory. This CLI helps you to scaffold a new Dagster repository within a folder structure that includes multiple Dagster repositories

dagster-graphql¶
----------------

Run a GraphQL query against the dagster interface to a specified repository or pipeline/job.

Can only use ONE of –workspace/-w, –python-file/-f, –module-name/-m, –grpc-port, –grpc-socket.

Examples:

dagster-graphql

dagster-graphql -y path/to/workspace.yaml

dagster-graphql -f path/to/file.py -a define\_repo

dagster-graphql -m some\_module -a define\_repo

dagster-graphql -f path/to/file.py -a define\_pipeline

dagster-graphql -m some\_module -a define\_pipeline



```
dagster-graphql[OPTIONS]
```
Options

--version¶Show the version and exit.

-t,--text¶GraphQL document to execute passed as a string

-f,--file¶GraphQL document to execute passed as a file

-p,--predefined¶GraphQL document to execute, from a predefined set provided by dagster-graphql.

Options:launchPipelineExecution

-v,--variables¶A JSON encoded string containing the variables for GraphQL execution.

-r,--remote¶A URL for a remote instance running dagster-webserver to send the GraphQL request to.

-o,--output¶A file path to store the GraphQL response to.



Documentation Source:
release-1-7-2.dagster.dagster-docs.io/_apidocs/libraries/dagster-dbt.md

Documentation Title:
Dagster Docs

Documentation Content:
scaffold¶

This command will initialize a new Dagster project and create directories and files that
load assets from an existing dbt project.


```
dagster-dbtprojectscaffold[OPTIONS]
```
Options

--project-name¶**Required**The name of the Dagster project to initialize for your dbt project.

--dbt-project-dir¶The path of your dbt project directory. This path must contain a dbt\_project.yml file. By default, this command will assume that the current working directory contains a dbt project, but you can set a different directory by setting this option.

dbt Core¶
---------

Here, we provide interfaces to manage dbt projects invoked by the local dbt command line interface
(dbt CLI).



Documentation Source:
release-1-7-2.dagster.dagster-docs.io/getting-started/create-new-project.md

Documentation Title:
Creating a new Dagster project | Dagster Docs

Documentation Content:
To install it as a package and its Python dependencies, run:

`pip install-e ".[dev]"`Using the `--editable`(`-e`) flag instructs`pip`to install your code location as a Python package in"editable mode"so that as you develop, local code changes are automatically applied.Step 3: Start the Dagster UI#
-----------------------------

To start the Dagster UI, run:

`dagster dev`**Note**: This command also starts the Dagster daemon. Refer to the Running Dagster locally guidefor more info.

Use your browser to open http://localhost:3000to view the project.

Step 4: Development#
--------------------

Adding new Python dependenciesEnvironment variables and secretsUnit testing



