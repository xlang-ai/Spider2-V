Documentation Source:
docs.astronomer.io/learn/airflow-quickstart.md

Documentation Title:
Airflow Quickstart | Astronomer Documentation

Documentation Content:
Skip to main content!!**Docs**DocsFind what you're looking forLearn About AstronomerGet Started FreeHomeAstroAstro CLISoftwareLearnTry AstroOverview* Get started
	Introduction to AirflowQuickstartTutorials
Airflow conceptsAirflow tutorialsIntegrations & connectionsUse casesAirflow glossarySupport Knowledge BaseOffice HoursWebinarsAstro StatusGet startedQuickstart
On this pageAirflow Quickstart
==================

A great way to explore Airflow features and use cases is using Astronomer's Airflow Quickstart.

This quickstart uses open source tools including Airflow, DuckDB, Streamlit, and the Astro Python SDKto implement an ELT pipeline that creates an interactive dashboard showing global and local temperature changes over time.

!You can run the quickstart without installing anything locally by using GitHub Codespaces, or you can run locally using the Astro CLI.

This project is designed to show what Airflow can do and provide a sandbox for you to explore important Airflow concepts. The repository contains one pre-built pipeline that will create and populate the interactive dashboard with no user code changes, as well as several exercises that will enhance the dashboard when completed. For more instructions on using the quickstart, see the project Readme.

tipIf you are new to Airflow and want more instructions for getting started, check out our step-by-step Get Started with Airflowtutorial.

Concepts covered​
-----------------

The pre-built pipeline and exercises in this quickstart show the implementation of several key Airflow features, which you can learn more about in our Learn resources:

* Datasets: This feature helps make Airflow data-aware and expands Airflow scheduling capabilities. Using datasets, you can schedule DAGs to run only when other tasks that update shared data have completed.
* Dynamic task mapping: This feature allows you to write DAGs that dynamically generate parallel tasks at runtime based on the results of previous tasks or external criteria.
* The Astro Python SDK: This open source package built on top of Airflow provides functions and classes that simplify common ELT operations such as loading files or using SQL or Pandas to transform data.
Was this page helpful?
----------------------

YesNoSign up for Developer Updates
-----------------------------

Get a summary of new Astro features once a month.

SubmitYou can unsubscribe at any time.



Documentation Source:
docs.astronomer.io/learn/airflow-quickstart.md

Documentation Title:
Airflow Quickstart | Astronomer Documentation

Documentation Content:
SubmitYou can unsubscribe at any time. By proceeding you agree to our Privacy Policy, our Website Termsand to receive emails from Astronomer.

Edit this pagePreviousIntroduction to AirflowNextPart 1: Write your first DAGConcepts coveredLegal·Privacy·Security·Cookie Preferences!!© Astronomer 2023. Various trademarks held by their respective owners.



Documentation Source:
docs.astronomer.io/learn/airflow-pgvector.md

Documentation Title:
Orchestrate pgvector operations with Apache Airflow | Astronomer Documentation

Documentation Content:
If it is available, order it and wait for it to arrive. You will likely need a library card to check out the book.
2. Make sure to prepare an adequate amount of tea for your reading session. Astronomer recommends Earl Grey, but you can use any tea you like.
3. Enjoy your book!

Conclusion​
-----------

Congratulations! You used Airflow and pgvector to get a book suggestion! You can now use Airflow to orchestrate pgvector operations in your own machine learning pipelines. Additionally, you remembered the satisfaction and joy of spending hours reading a good book and supported your local library.

Was this page helpful?
----------------------

YesNoSign up for Developer Updates
-----------------------------

Get a summary of new Astro features once a month.

SubmitYou can unsubscribe at any time. By proceeding you agree to our Privacy Policy, our Website Termsand to receive emails from Astronomer.

Edit this pagePreviousOpenSearchNextPineconeWhy use Airflow with pgvector?Time to completeAssumed knowledgePrerequisitesStep 1: Configure your Astro projectStep 2: Add your dataStep 3: Create your DAGStep 4: Run your DAGStep 5: (Optional) Fetch and read the bookConclusionLegal·Privacy·Security·Cookie Preferences!!© Astronomer 2023. Various trademarks held by their respective owners.



Documentation Source:
docs.astronomer.io/software.md

Documentation Title:
Astronomer Software documentation | Astronomer Documentation

Documentation Content:
Skip to main content!!**Docs**DocsFind what you're looking forLearn About AstronomerGet Started FreeHomeAstroAstro CLISoftwareLearnTry AstroSelect Software VersionOverviewGet startedDevelopAdministrationObservabilityAstro RuntimeTroubleshootRelease notesReferenceSupport Knowledge BaseOffice HoursWebinarsAstro StatusOverviewVersion: 0.34Astronomer Software documentation
=================================

Astronomer Software is the best way to run Apache Airflow in your private cloud. Using Astronomer's tooling, you can have fine-tuned control over every aspect of your Airflow experience.

Need a managed Airflow solution?
--------------------------------

Astro is a cloud solution that helps you focus on your data pipelines and spend less time managing Apache Airflow, with capabilities enabling you to build, run, and observe data all in one place.

Try AstroLearn about AstronomerRun Airflow in your private cloud using Astronomer Software​
------------------------------------------------------------

The following diagram shows how you can run Airflow in your private cloud using Astronomer Software:

!Get Started​
------------

Installation guides

Install Astronomer Software on your cloud.

Integrate an auth system

Set up enterprise-grade user authentication on Astronomer Software.

CI/CD and automation

Use the Houston API and CI/CD tools to automate code deploys and changes to your platform.

Astronomer Software features​
-----------------------------

Push-button Deployments

Deploy an Airflow instance with the push of a button.

Role-based access control

Use an extensive RBAC system for configurable and secure user management.

Configurations via Helm

Manage cloud, network, third party provider, and system component configurations using Helm.

Grafana & Kibana integrations

System logging, monitoring, and alerts are available through Grafana and Kibana.

Astronomer Docker images

Run versions of Airflow with extended support lifecycles and additional bug testing.

Most popular software docs​
---------------------------

Release notes

A list of all changes in the latest version of Astronomer Software.

Customize image

Guides and considerations for customizing your Astro project and fine-tuning Airflow.

Create a project

Create all of the necessary files to run Airflow locally or on Astronomer Software.

Was this page helpful?



