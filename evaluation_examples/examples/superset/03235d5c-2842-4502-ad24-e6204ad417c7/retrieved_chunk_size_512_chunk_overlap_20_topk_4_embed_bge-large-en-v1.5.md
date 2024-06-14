Documentation Source:
superset.apache.org/docs/configuration/databases/index.md

Documentation Title:
Connecting to Databases | Superset

Documentation Content:
YugabyteDB​

YugabyteDBis a distributed SQL database built on top of PostgreSQL.

Note that, if you're using docker compose, the
Postgres connector library psycopg2comes out of the box with Superset.

The connection string looks like:

postgresql://{username}:{password}@{host}:{port}/{database}Connecting through the UI​
--------------------------

Here is the documentation on how to leverage the new DB Connection UI. This will provide admins the ability to enhance the UX for users who want to connect to new databases.

!There are now 3 steps when connecting to a database in the new UI:

Step 1: First the admin must inform superset what engine they want to connect to. This page is powered by the `/available`endpoint which pulls on the engines currently installed in your environment, so that only supported databases are shown.

Step 2: Next, the admin is prompted to enter database specific parameters. Depending on whether there is a dynamic form available for that specific engine, the admin will either see the new custom form or the legacy SQLAlchemy form. We currently have built dynamic forms for (Redshift, MySQL, Postgres, and BigQuery). The new form prompts the user for the parameters needed to connect (for example, username, password, host, port, etc.) and provides immediate feedback on errors.

Step 3: Finally, once the admin has connected to their DB using the dynamic form they have the opportunity to update any optional advanced settings.

We hope this feature will help eliminate a huge bottleneck for users to get into the application and start crafting datasets.



Documentation Source:
superset.apache.org/docs/using-superset/creating-your-first-dashboard/index.md

Documentation Title:
Creating Your First Dashboard | Superset

Documentation Content:
Connecting to a new database​

Superset itself doesn't have a storage layer to store your data but instead pairs with
your existing SQL-speaking database or data store.

First things first, we need to add the connection credentials to your database to be able
to query and visualize data from it. If you're using Superset locally via
Docker compose, you can
skip this step because a Postgres database, named **examples**, is included and
pre-configured in Superset for you.

Under the **+**menu in the top right, select Data, and then the *Connect Database*option:

!Then select your database type in the resulting modal:

!Once you've selected a database, you can configure a number of advanced options in this window,
or for the purposes of this walkthrough, you can click the link below all these fields:

!Once you've clicked that link you only need to specify two things (the database name and SQLAlchemy URI):

!As noted in the text below the form, you should refer to the SQLAlchemy documentation on
creating new connection URIsfor your target database.

Click the **Test Connection**button to confirm things work end to end. If the connection looks good, save the configuration
by clicking the **Connect**button in the bottom right corner of the modal window:

Congratulations, you've just added a new data source in Superset!



Documentation Source:
superset.apache.org/docs/installation/docker-compose/index.md

Documentation Title:
Docker Compose | Superset

Documentation Content:
By default, postgresql only allows incoming connections from
`localhost`and under Docker, unless you use `--network=host`, `localhost`will refer to different
endpoints on the host machine and in a docker container respectively. Allowing postgresql to accept
connections from the Docker involves making one-line changes to the files `postgresql.conf`and
`pg_hba.conf`; you can find helpful links tailored to your OS / PG version on the web easily for
this task. For Docker it suffices to only whitelist IPs `172.0.0.0/8`instead of `*`, but in any
case you are *warned*that doing this in a production database *may*have disastrous consequences as
you are opening your database to the public internet. 2. Instead of `localhost`, try using
`host.docker.internal`(Mac users, Ubuntu) or `172.18.0.1`(Linux users) as the hostname when
attempting to connect to the database. This is a Docker internal detail -- what is happening is
that, in Mac systems, Docker Desktop creates a dns entry for the hostname `host.docker.internal`which resolves to the correct address for the host machine, whereas in Linux this is not the case
(at least by default). If neither of these 2 hostnames work then you may want to find the exact
hostname you want to use, for that you can do `ifconfig`or `ip addr show`and look at the IP
address of `docker0`interface that must have been created by Docker for you. Alternately if you
don't even see the `docker0`interface try (if needed with sudo) `docker network inspect bridge`and
see if there is an entry for `"Gateway"`and note the IP address.
Edit this pagePreviousPyPINextUpgrading SupersetRequirements1. Clone Superset's GitHub repository* 2. Launch Superset Through Docker Compose
	Option #1 - for an interactive development environmentOption #2 - build a set of immutable images from the local branchOption #3 - boot up an official release
* docker-compose tips & configurationConfiguring Further
3. Log in to Superset4.



Documentation Source:
superset.apache.org/docs/configuration/databases/index.md

Documentation Title:
Connecting to Databases | Superset

Documentation Content:
{region}/{database}?role={role}&warehouse={warehouse}`
| SQLite | No additional library needed |`sqlite://path/to/file.db?check_same_thread=false`
|SQL Server`pip install pymssql``mssql+pymssql://`
|Teradata`pip install teradatasqlalchemy``teradatasql://{user}:{password}@{host}`
|TimescaleDB`pip install psycopg2``postgresql://:@:/`
|Trino`pip install trino``trino://{username}:{password}@{hostname}:{port}/{catalog}`
|Vertica`pip install sqlalchemy-vertica-python``vertica+vertica_python://:@/`
|YugabyteDB`pip install psycopg2``postgresql://:@/`

Note that many other databases are supported, the main criteria being the existence of a functional
SQLAlchemy dialect and Python driver. Searching for the keyword "sqlalchemy + (database name)"
should help get you to the right place.

If your database or data engine isn't on the list but a SQL interface
exists, please file an issue on the
Superset GitHub repo, so we can work on documenting and
supporting it.

If you'd like to build a database connector for Superset integration,
read the following tutorial.



