Documentation Source:
docs.astronomer.io/astro/cli/troubleshoot-locally.md

Documentation Title:
Troubleshoot a local Airflow environment | Astronomer Documentation

Documentation Content:
Change the default port assignment​

If port 8080 or 5432 are in use on your machine by other services, the Airflow webserver and metadata database won't be able to start. To run these components on different ports, run the following commands in your Astro project:

`astro config setwebserver.port astro config setpostgres.port `For example, to use 8081 for your webserver port and 5435 for your database port, you would run the following commands:

`astro config setwebserver.port 8081astro config setpostgres.port 5435`Was this page helpful?
----------------------

YesNoSign up for Developer Updates
-----------------------------

Get a summary of new Astro features once a month.

SubmitYou can unsubscribe at any time. By proceeding you agree to our Privacy Policy, our Website Termsand to receive emails from Astronomer.

Edit this pagePreviousUse Airflow connections from AstroNextTest your DAGsTroubleshoot KubernetesPodOperator issuesTroubleshoot dependency errorsNew DAGs aren't visible in the Airflow UIDAGs running slowlyAstro project won't load after running `astro dev start`* Ports are not available for my local Airflow webserver
	Stop all running Docker containersChange the default port assignment
Legal·Privacy·Security·Cookie Preferences!!© Astronomer 2023. Various trademarks held by their respective owners.



Documentation Source:
docs.astronomer.io/astro/cli/local-airflow-overview.md

Documentation Title:
Run Airflow locally | Astronomer Documentation

Documentation Content:
Skip to main content!!**Docs**DocsFind what you're looking forLearn About AstronomerGet Started FreeHomeAstroAstro CLISoftwareLearnTry AstroOverviewInstall the CLIQuickstartDevelop your project* Run Airflow locally
	OverviewBasic setupUse Airflow connections from AstroTroubleshoot a local environment
Test your DAGsRelease notesRelease and lifecycle policyAdvancedCommand referenceSupport Knowledge BaseOffice HoursWebinarsAstro StatusRun Airflow locallyOverview
Run Airflow locally
===================

Running Airflow locally with the Astro CLI lets you preview and debug DAG changes before deploying to production. In a local Airflow environment, you can fix issues with your DAGs without consuming infrastructure resources or waiting on code deploy processes.

To run Airflow locally, the Astro CLI creates and runs containers for core Airflow components. It uses Docker by default to orchestrate these containers, but you can also use Podman. All tasks run locally in the scheduler container using the local executor.

See the following documentation to get started:

Run Airflow locallyTest your DAGsTroubleshoot locallySync Deployment connections from AstroWas this page helpful?
----------------------

YesNoSign up for Developer Updates
-----------------------------

Get a summary of new Astro features once a month.

SubmitYou can unsubscribe at any time. By proceeding you agree to our Privacy Policy, our Website Termsand to receive emails from Astronomer.

Edit this pagePreviousDevelop your projectNextBasic setupLegal·Privacy·Security·Cookie Preferences!!© Astronomer 2023. Various trademarks held by their respective owners.



Documentation Source:
docs.astronomer.io/astro/cli/run-airflow-locally.md

Documentation Title:
Run your Astro project in a local Airflow environment with the CLI | Astronomer Documentation

Documentation Content:
Skip to main content!!**Docs**DocsFind what you're looking forLearn About AstronomerGet Started FreeHomeAstroAstro CLISoftwareLearnTry AstroOverviewInstall the CLIQuickstartDevelop your project* Run Airflow locally
	OverviewBasic setupUse Airflow connections from AstroTroubleshoot a local environment
Test your DAGsRelease notesRelease and lifecycle policyAdvancedCommand referenceSupport Knowledge BaseOffice HoursWebinarsAstro StatusRun Airflow locallyBasic setup
On this pageRun your Astro project in a local Airflow environment with the CLI
==================================================================

Running Airflow locally with the Astro CLI can be an easy way to preview and debug DAG changes quickly before deploying your code to Astro. By locally running your DAGs, you can fix issues with your DAGs without consuming infrastructure resources or waiting on code deploy processes.

This document explains how to use the Astro CLI to start a local Airflow environment on your computer and interact with your Astro project. To learn more about unit testing for your DAGs or testing project dependencies when changing Python or Astro Runtime versions, see Test your project locally.

You can find common issues and resolutions in the troubleshoot a local environmentsection.

Start a local Airflow environment​
----------------------------------

To begin running your project in a local Airflow environment, run:

astro dev startThis command builds your project and spins up 4 containers on your machine, each for a different Airflow component. After the command completes, you can access your project's Airflow UI at `https://localhost:8080/`.

Restart a local Airflow environment​
------------------------------------

Restarting your Airflow environment rebuilds your image and restarts the Docker containers running on your local machine with the new image. Restart your environment to apply changes from specific files in your project, or to troubleshoot issues that occur when your project is running.

To restart your local Airflow environment, run:

astro dev restartAlternatively, you can run `astro dev stop`to stop your Docker containers without restarting your environment, then run `astro dev start`when you want to restart.

Stop a local Airflow environment​
---------------------------------

Run the following command to pause all Docker containers and stop running your local Airflow environment.



Documentation Source:
docs.astronomer.io/astro/cli/develop-project.md

Documentation Title:
Develop your Astro project | Astronomer Documentation

Documentation Content:
3. Reference your utility files in your DAG code.
4. Apply your changes. If you're developing locally, refresh the Airflow UI in your browser.

Utility files in the `/dags`directory will not be parsed by Airflow, so you don't need to specify them in `.airflowignore`to prevent parsing. If you're using DAG-only deployson Astro, changes to this folder are deployed when you run `astro deploy --dags`and do not require rebuilding your Astro project into a Docker image and restarting your Deployment.

Add Airflow connections, pools, variables​
------------------------------------------

Airflow connections connect external applications such as databases and third-party services to Apache Airflow. See Manage connections in Apache Airflowor Apache Airflow documentation.

To add Airflow connections, pools, and variablesto your local Airflow environment, you have the following options:

* Use the Airflow UI. In **Admin**, click **Connections**, **Variables**or **Pools**, and then add your values. These values are stored in the metadata database and are deleted when you run the `astro dev kill`command, which can sometimes be used for troubleshooting.
* Modify the `airflow_settings.yaml`file of your Astro project. This file is included in every Astro project and permanently stores your values in plain-text. To prevent you from committing sensitive credentials or passwords to your version control tool, Astronomer recommends adding this file to `.gitignore`.
* Use the Astro UI to create connections that can be shared across Deployments in a Workspace. These connections are not visible in the Airflow UI. See Create Airflow connections in the Astro UI.
* Use a secret backend, such as AWS Secrets Manager, and access the secret backend locally. See Configure an external secrets backend on Astro.

When you add Airflow objects to the Airflow UI of a local environment or to your `airflow_settings.yaml`file, your values can only be used locally. When you deploy your project to a Deployment on Astro, the values in this file are not included.

Astronomer recommends using the `airflow_settings.yaml`file so that you don’t have to manually redefine these values in the Airflow UI every time you restart your project.



