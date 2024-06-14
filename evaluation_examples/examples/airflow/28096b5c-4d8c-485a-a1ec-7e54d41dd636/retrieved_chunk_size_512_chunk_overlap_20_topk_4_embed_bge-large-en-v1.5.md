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
docs.astronomer.io/astro/cli/run-airflow-locally.md

Documentation Title:
Run your Astro project in a local Airflow environment with the CLI | Astronomer Documentation

Documentation Content:
cURL​

curl-XGET localhost:8080/api/v1/--user"admin:admin"### Python​

`importrequestsresponse =requests.get(url="http://localhost:8080/api/v1/",auth=("admin","admin"))`Hard reset your local environment​
----------------------------------

In most cases, restarting your local projectis sufficient for testing and making changes to your project. However, it is sometimes necessary to kill your Docker containers and metadata database for testing purposes. To do so, run the following command:

astro dev killThis command forces your running containers to stop and deletes all data associated with your local Postgres metadata database, including Airflow connections, logs, and task history.

Override the Astro CLI Docker Compose file​
-------------------------------------------

The Astro CLI uses a default set of Docker Composeconfigurations to define and run local Airflow components. For advanced testing cases, you might need to override these default configurations. For example, you might need to:

* Add extra containers to mimic services that your Airflow environment needs to interact with locally, such as an SFTP server.
* Change the volumes mounted to any of your local containers.

infoThe Astro CLI does not support overrides to environment variables that are required globally. For the list of environment variables that Astro enforces, see Global environment variables. To learn more about environment variables, read Environment variables.

1. Reference the Astro CLI's default Docker Compose file(`composeyml.yml`) and determine one or more configurations to override.
2. Add a `docker-compose.override.yml`file at the top level of your Astro project.
3. Specify your new configuration values in `docker-compose.override.yml`file using the same format as in `composeyml.yml`.

For example, to add another volume mount for a directory named `custom_dependencies`, add the following to your `docker-compose.override.yml`file:

`version:"3.1"services:scheduler:volumes:-/home/astronomer_project/custom_dependencies:/usr/local/airflow/custom_dependencies:ro`Make sure to specify `version: "3.1"`and follow the format of the source code file linked above.



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



Documentation Source:
docs.astronomer.io/astro/cli/authenticate-to-clouds.md

Documentation Title:
Authenticate to cloud services with user credentials | Astronomer Documentation

Documentation Content:
Configure your Astro project​

The Astro CLI runs Airflow in a Docker-based environment. To give Airflow access to your credential file, mount it as a Docker volume.

1. In your Astro project, create a file named `docker-compose.override.yml`to your project with the following configuration:


	* Mac
	* Linux
	* Windows`version:"3.1"services:scheduler:volumes:-/Users//.config/gcloud/application_default_credentials.json:/usr/local/airflow/gcloud/application_default_credentials.json:rwwebserver:volumes:-/Users//.config/gcloud/application_default_credentials.json:/usr/local/airflow/gcloud/application_default_credentials.json:rwtriggerer:volumes:-/Users//.config/gcloud/application_default_credentials.json:/usr/local/airflow/gcloud/application_default_credentials.json:rw``version:"3.1"services:scheduler:volumes:-/home//.config/gcloud/application_default_credentials.json:/usr/local/airflow/gcloud/application_default_credentials.json:rwwebserver:volumes:-/home//.config/gcloud/application_default_credentials.json:/usr/local/airflow/gcloud/application_default_credentials.json:rwtriggerer:volumes:-/home//.config/gcloud/application_default_credentials.json:/usr/local/airflow/gcloud/application_default_credentials.json:rw``version:"3.1"services:scheduler:volumes:-/c/Users//AppData/Roaming/gcloud/application_default_credentials.json:/usr/local/airflow/gcloud/application_default_credentials.json:rwwebserver:volumes:-/c/Users//AppData/Roaming/gcloud/application_default_credentials.json:/usr/local/airflow/gcloud/application_default_credentials.json:rwtriggerer:volumes:-/c/Users//AppData/Roaming/gcloud/application_default_credentials.json:/usr/local/airflow/gcloud/application_default_credentials.json:rw`
2. In your Astro project's `.env`file, add the following environment variable. Ensure that this volume path is the same as the one you configured in `docker-compose.override.yml`.

GOOGLE\_APPLICATION\_CREDENTIALS=/usr/local/airflow/gcloud/application\_default\_credentials.json

When you run Airflow locally, all GCP connections without defined credentials automatically fall back to your user credentials when connecting to GCP.



