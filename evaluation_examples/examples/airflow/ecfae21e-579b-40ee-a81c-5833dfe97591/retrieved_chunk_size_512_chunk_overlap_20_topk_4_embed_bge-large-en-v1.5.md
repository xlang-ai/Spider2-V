Documentation Source:
docs.astronomer.io/learn/connections/postgres.md

Documentation Title:
Create a Postgres connection in Airflow | Astronomer Documentation

Documentation Content:
2. Open the **Connectivity & security**tab and copy the **Endpoint**and **Port**.
3. Follow the AWS instructions to create a userand grant a role to the userthat Airflow will use to connect to Postgres. Copy the username and password.
4. (Optional) To use a specific schema, copy the name of the schema. If you skip this, the default schema `public`will be used.

Create your connection​
-----------------------

1. Open your Astro project and add the following line to your `requirements.txt`file:

apache-airflow-providers-postgresThis will install the Postgres provider package, which makes the Postgres connection type available in Airflow.
Run `astro dev restart`to restart your local Airflow environment and apply your changes in `requirements.txt`.

In the Airflow UI for your local Airflow environment, go to **Admin**> **Connections**. Click **+**to add a new connection, then choose **Postgres**as the connection type.

4. Fill out the following connection fields using the information you retrieved from Get connection details:



Documentation Source:
docs.astronomer.io/learn/connections/postgres.md

Documentation Title:
Create a Postgres connection in Airflow | Astronomer Documentation

Documentation Content:
Skip to main content!!**Docs**DocsFind what you're looking forLearn About AstronomerGet Started FreeHomeAstroAstro CLISoftwareLearnTry AstroOverviewGet startedAirflow conceptsAirflow tutorials* Integrations & connections
	Amazon SageMakerApache Kafka/ConfluentAzure Blob StorageAzure Container InstancesAzure Data FactoryMicrosoft Entra Workload IDBigQueryCohereDatabricksdbt Clouddbt CoreDuckDBFivetranGreat ExpectationsJupyter notebookMarquezMLflowMongoDBMicrosoft SQL ServerOpenAIOpenSearchpgvectorPineconePostgresRedshiftSnowflakeSoda CoreWeaviateWeights and Biases
Use casesAirflow glossarySupport Knowledge BaseOffice HoursWebinarsAstro StatusIntegrations & connectionsPostgres
On this pageCreate a Postgres connection in Airflow
=======================================

Postgresis a free and open source relational database system. Integrating Postgres with Airflow allows you to interact with your Postgres database, run queries, ans load or export data from an Airflow DAG.

This guide provides the basic setup for creating a Postgres connection.

Prerequisites​
--------------

* The Astro CLI.
* A locally running Astro project.
* A Postgres database running in the cloud or on-premises.
* Permissionto access your Postgres database from your local Airflow environment.

Get connection details​
-----------------------

A connection from Airflow to Postgres requires the following information:

* Host (also known as the endpoint URL, server name, or instance ID based on your cloud provider)
* Port (default is 5432)
* Username
* Password
* Schema (default is `public`)

The method to retrieve these values will vary based which cloud provider you use to host Microsoft SQL Server. Refer to the following documents to for more information about retrieveing these values:

* AWS: Connect to Postgres running on RDS
* GCP: Connect to Postgres running on Cloud SQL
* Azure: Connect to Postgres running on an Azure database

For example, if you're running Postgres in a Relational Data Store (RDS) in AWS, complete the following steps to retrieve these values:

1. In your AWS console, select your region, then go to the RDS service and select your Postgres database.



Documentation Source:
docs.astronomer.io/learn/connections/postgres.md

Documentation Title:
Create a Postgres connection in Airflow | Astronomer Documentation

Documentation Content:
4. Fill out the following connection fields using the information you retrieved from Get connection details:


	* **Connection Id**: Enter a name for the connection.
	* **Host**: Enter your Postgres server's host/ endpoint URL/ server name/ instance ID.
	* **Schema**: Enter your schema name.
	* **Login**: Enter your username.
	* **Password**: Enter your password.
	* **Port**: Enter your Postgres server's **Port**.
5. Click **Test**. After the connection test succeeds, click **Save**.

!

How it works​
-------------

Airflow uses the psycopg2python library to connect to Postgres through the PostgresHook. You can also directly use the PostgresHook to create your own custom operators.

See also​
---------

Apache Airflow Postgres provider package documentation* Postgres modulesand example DAGsin the Astronomer Registry
Import and export Airflow connections using Astro CLIWas this page helpful?
----------------------

YesNoSign up for Developer Updates
-----------------------------

Get a summary of new Astro features once a month.

SubmitYou can unsubscribe at any time. By proceeding you agree to our Privacy Policy, our Website Termsand to receive emails from Astronomer.

Edit this pagePreviousPineconeNextRedshiftPrerequisitesGet connection detailsCreate your connectionHow it worksSee alsoLegal·Privacy·Security·Cookie Preferences!!© Astronomer 2023. Various trademarks held by their respective owners.



Documentation Source:
docs.astronomer.io/astro/cli/configure-cli.md

Documentation Title:
Configure the Astro CLI | Astronomer Documentation

Documentation Content:
|`docker` `docker`or `podman` |
|`context` The context for your Astro project. | Empty string | Any available context |
|`disable_astro_run` Determines whether to disable `astro run`commands and exclude `astro-run-dag`from any images built by the CLI. |`false` `true`, `false` |
|`disable_env_objects` Determines whether the Astro CLI pulls connections set in the Astro UI to your local environment. When set to `true`, connections are not pulled to the local environment. Set to `false`to import connections from the Astro UI for local development. Can be set globally with the `-g`flag. |`true` `true`, `false` |
|`duplicate_volumes` Determines if the Astro CLI creates duplicate volumes when running Airflow locally. |`true` `true`or `false` |
|`local.registry` The location of your local Docker container running Airflow. |`localhost:5555` Any available port |
|`postgres.user` The username for the Postgres metadata database. |`postgres` Any string |
|`postgres.password` The password for the Postgres metadata database. |`postgres` Any string |
|`postgres.host` The hostname for the Postgres metadata database. |`postgres` Any string |
|`postgres.port` The port for the Postgres metadata database. |`5432` Any available port |
|`postgres.repository` Image repository to pull the Postgres image from |`docker.io/postgres` Any Postgres image in a repository |
|`postgres.tag` The tag for your Postgres image |`12.6` Any valid image tag |
|`project.name` The name of your Astro project. | Empty string | Any string |
|`show_warnings` Determines whether warning messages appear when starting a local Airflow environment. For example, when set to `true`, you'll receive warnings when a new version of Astro Runtime is available and when your Astro project doesn't have any DAGs. |`true` `true`, `false` |
|`skip_parse` Determines whether the CLI parses DAGs before pushing code to a Deployment.



