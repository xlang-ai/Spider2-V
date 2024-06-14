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
docs.astronomer.io/learn/get-started-with-airflow.md

Documentation Title:
Get started with Apache Airflow, Part 1: Write and run your first DAG | Astronomer Documentation

Documentation Content:
1. Create a new directory for your Astro project:

mkdir
2. Open the directory:

cd
3. Run the following Astro CLI command to initialize an Astro project in the directory:

astro dev init

The Astro project is built to run Airflow with Docker. Dockeris a service to run software in virtualized containers within a machine. When you run Airflow on your machine with the Astro CLI, Docker creates a container for each Airflow component that is required to run DAGs. For this tutorial, you don't need an in-depth knowledge of Docker. All you need to know is that Airflow runs on the compute resources of your machine, and that all necessary files for running Airflow are included in your Astro project.

The default Astro project structure includes a collection of folders and files that you can use to run and customize Airflow. For this tutorial, you only need to know the following files and folders:

* `/dags`: A directory of DAG files. Each Astro project includes an example DAG called `example_astronauts`. For more information on DAGs, see Introduction to Airflow DAGs.
* `Dockerfile`: This is where you specify your version of Astro Runtime, which is a runtime software based on Apache Airflow that is built and maintained by Astronomer. The CLI generates new Astro projects with the latest version of Runtime, which is equivalent to the latest version of Airflow. For advanced use cases, you can also configure this file with Docker-based commands to run locally at build time.

Step 2: Start Airflow​
----------------------

Now that you have an Astro project ready, the next step is to actually start Airflow on your machine. In your terminal, open your Astro project directory and run the following command:

astro dev startStarting Airflow for the first time can take 1 to 3 minutes. Once your local environment is ready, the CLI automatically opens a new tab or window in your default web browser to the Airflow UI at `https://localhost:8080`.

infoIf port 8080 or 5432 are in use on your machine, Airflow won't be able to start.



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
docs.astronomer.io/astro/cli/get-started-cli.md

Documentation Title:
Get started with Airflow using the Astro CLI | Astronomer Documentation

Documentation Content:
Skip to main content!!**Docs**DocsFind what you're looking forLearn About AstronomerGet Started FreeHomeAstroAstro CLISoftwareLearnTry AstroOverviewInstall the CLIQuickstartDevelop your projectRun Airflow locallyTest your DAGsRelease notesRelease and lifecycle policyAdvancedCommand referenceSupport Knowledge BaseOffice HoursWebinarsAstro StatusQuickstartOn this pageGet started with Airflow using the Astro CLI
============================================

One of the Astro CLI's main features is its ability to run Airflow on your local machine. After you install the Astro CLI and Docker Desktop, follow this quickstart to build an Airflow project and run it in a local Airflow environment using just a few commands. At the end of the tutorial, you'll have all of the files and components you need to develop and test Airflow DAGs locally.

Prerequisites​
--------------

* The Astro CLI
* Docker Desktop(v18.09 or higher).

Step 1: Create an Astro project​
--------------------------------

An *Astro project*contains the set of files necessary to run Airflow, including dedicated folders for your DAG files, plugins, and dependencies. All new Astro projects contain two example DAGs. This set of files builds a Docker image that you can both run on your local machine with Airflow and deploy to Astro.

astro dev initThis command generates all of the project files you need to run Airflow locally, including example DAGs that you can run out of the box. See Create an Astro projectfor more information about the default project structure.

Step 2: Run Airflow locally​
----------------------------

Running your project locally allows you to test your DAGs before you deploy them to a production environment. While this step is not required for deploying and running your code on Astro, Astronomer recommends always using the Astro CLI to test locally before deploying.

1. To start running your project in a local Airflow environment, run the following command from your project directory:

astro dev startThis command builds your project and spins up 4 Docker containers on your machine, each for a different Airflow component:



