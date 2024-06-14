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
docs.astronomer.io/learn/connections.md

Documentation Title:
Manage connections in Apache Airflow | Astronomer Documentation

Documentation Content:
!As you update the **Connection Type**field, notice how the other available fields change. Each connection type requires different kinds of information. Specific connection types are only available in the dropdown list when the relevant provider is installed in your Airflow environment.

You don't have to specify every field for most connections. However, the values marked as required in the Airflow UI can be misleading. For example, to set up a connection to a PostgreSQL database, you need to reference the PostgreSQL provider documentationto learn that the connection requires a `Host`, a user name as `login`, and a password in the `password`field.

!Any parameters that don't have specific fields in the connection form can be defined in the **Extra**field as a JSON dictionary. For example, you can add the `sslmode`or a client `sslkey`in the **Extra**field of your PostgreSQL connection.

You can test some connection types from the Airflow UI with the **Test**button if you enable `test_connection`in the Airflow config. After running a connection test, a message shows either a success confirmation or an error message. When using the **Test**button, the connection to your external tool is made from the webserver component of Airflow. See also Testing connections in the Airflow documentation.

Define connections with environment variables​
----------------------------------------------

Connections can also be defined using environment variables. If you use the Astro CLI, you can use the `.env`file for local development or specify environment variables in your project's Dockerfile.

**Note**: If you are synchronizing your project to a remote repository, don't save sensitive information in your Dockerfile. In this case, using either a secrets backend, Airflow connections defined in the UI, or `.env`locally are preferred to avoid exposing secrets in plain text.

The environment variable used for the connection must be formatted as `AIRFLOW_CONN_YOURCONNID`and can be provided as a Uniform Resource Identifier (URI) or in JSON.

URIis a format designed to contain all necessary connection information in one string, starting with the connection type, followed by login, password, and host. In many cases a specific port, schema, and additional parameters must be added.



