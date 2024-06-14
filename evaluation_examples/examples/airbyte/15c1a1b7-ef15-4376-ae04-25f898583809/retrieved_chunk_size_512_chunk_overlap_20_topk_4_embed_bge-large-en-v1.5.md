Documentation Source:
airbyte.com/tutorials/build-a-slack-activity-dashboard-with-apache-superset.md

Documentation Title:
How to Build a Slack Activity Dashboard with Apache Superset | Airbyte | Airbyte

Documentation Content:
Setting Up a Postgres Database in Superset

To do this, on the top menu in your Superset dashboard, hover on the Data dropdown and click on **Databases.**

‍

!‍

In the page that opens up, click on the **+ Database** button in the top right corner.

‍

!‍

Then, you will be presented with a modal to add your Database Name and the connection URI.

‍

!‍

Let’s call our Database **slack\_db,**and then add the following URI as the connection URI:

`postgresql://postgres:password@docker.for.mac.localhost:2000/postgres`‍

**If you are on a Windows Machine, yours will be:**`postgresql://postgres:password@docker.for.win.localhost:2000/postgres`‍

Note: We are using **docker.for.[mac|win].localhost**in order to access the localhost of your machine, because using just *localhost*will point to the Docker container network and not your machine’s network.

Your Superset UI should look like this:

‍

!‍

We will need to enable some settings on this connection. Click on the **SQL LAB SETTINGS**and check the following boxes:

‍

!‍

Afterwards, click on the **ADD** button,and you will see your database on the data page of Superset.

‍

!‍



Documentation Source:
airbyte.com/docs.airbyte.com/integrations/sources/postgres/cloud-sql-postgres.md

Documentation Title:
Cloud SQL for PostgreSQL | Airbyte Documentation

Documentation Content:
Step 1: Create a dedicated read-only Postgres user​

These steps create a dedicated read-only user for replicating data. Alternatively, you can use an existing Postgres user in your database. To create a user, first connect to your database. If you are getting started, you can use Cloud Shell to connect directly from the UI.

The following commands will create a new user:

CREATE USER  PASSWORD 'your\_password\_here';Now, provide this user with read-only access to relevant schemas and tables. Re-run this command for each schema you expect to replicate data from (e.g. `public`):

`GRANT USAGE ON SCHEMA  TO ;GRANT SELECT ON ALL TABLES IN SCHEMA  TO ;ALTER DEFAULT PRIVILEGES IN SCHEMA  GRANT SELECT ON TABLES TO ;`#### Step 2: Create a new Postgres source in Airbyte UI​

From your Airbyte Cloudor Airbyte Open Source account, select `Sources`from the left navigation bar, search for `Postgres`, then create a new Postgres source.

!To fill out the required information:

1. Enter the hostname, port number, and name for your Postgres database.
2. You may optionally opt to list each of the schemas you want to sync. These are case-sensitive, and multiple schemas may be entered. By default, `public`is the only selected schema.
3. Enter the username and password you created in Step 1.
4. Select an SSL mode. You will most frequently choose `require`or `verify-ca`. Both of these always require encryption. `verify-ca`also requires certificates from your Postgres database. See here to learn about other SSL modes and SSH tunneling.
5. Select `Standard (xmin)`from available replication methods. This uses the xmin system columnto reliably replicate data from your database.
6. If your database is particularly large (> 500 GB), you will benefit from configuring your Postgres source using logical replication (CDC).



Documentation Source:
airbyte.com/tutorials/build-a-github-activity-dashboard-for-your-project.md

Documentation Title:
Build a GitHub Activity Dashboard for your Project | Airbyte | Airbyte

Documentation Content:
Creating the Airbyte connection

Back in the Airbyte web app in your browser, click on the *new source*button in the top right corner of the app to go to the page to add a new Airbyte source.

Enter the name **github-source**as the source name and click the drop down and select Github connector as source type. After selecting the GitHub source type, you will be presented with two text boxes.The first is to enter a repository you want. In this box, type in **airbytehq/airbyte**, and then, in the second box, you will need to provide a GitHub access token which you can obtain fromhere.

Make sure you grant the token the repo and write:discussion permissions. After you've filled all fields, hit the set up source button.

!If the setup was successful, you will be taken to the destination screen where you will add a new destination.

Click the *add destination*button, and, in the drop down that follows, click *add new destination*. Then, you will see a page to add the destination name. Type in the name we gave the Postgres container we created earlier (github-destination), and then choose Postgres as the destination type.

After, you will be presented with some text boxes to enter the database connection details. Enter the values for the Postgres container we created earlier:

* host - localhost
* post - 3003
* schema - public (leave default)
* database - postgres
* Password - password
* username - postgres

Then click on the basic normalization toggle button to check it on as we want Airbyte to normalize the data coming in from GitHub. Overall the UI should look like this:

!Then click on the Set up destination button. If your credentials are all good for the database, the postgres destination would have been set, and now you will need to make the connection from the source (GitHub) to the destination (Postgres).

You should check the boxes that are checked in the screenshot below, and then choose how often Airbyte will attempt to replicate data to be every hour in the Sync frequency drop down. Then, click on the *Set up connection*button.



Documentation Source:
airbyte.com/tutorials/postgres-to-bigquery.md

Documentation Title:
How to Connect & Load Data from Postgres to BigQuery?

Documentation Content:
Step 2: Set up BigQuery as a destination connector
--------------------------------------------------

!1. First, navigate to the Airbyte dashboard and select the "Destinations" tab on the left-hand side of the screen. 

2. Scroll down until you find the "BigQuery" destination connector and click on it. 

3. Click the "Create Destination" button to begin setting up your BigQuery destination. 

4. Enter your Google Cloud Platform project ID and service account credentials in the appropriate fields. 

5. Next, select the dataset you want to use for your destination and enter the table prefix you want to use. 

6. Choose the schema mapping for your data, which will determine how your data is organized in BigQuery. 

7. Finally, review your settings and click the "Create Destination" button to complete the setup process. 

8. Once your destination is created, you can begin configuring your source connectors to start syncing data to BigQuery. 

9. To do this, navigate to the "Sources" tab on the left-hand side of the screen and select the source connector you want to use. 

10. Follow the prompts to enter your source credentials and configure your sync settings. 

11. When you reach the "Destination" step, select your BigQuery destination from the dropdown menu and choose the dataset and table prefix you want to use. 

12. Review your settings and click the "Create Connection" button to start syncing data from your source to your BigQuery destination.

Step 3: Set up a connection to sync your Postgres data to BigQuery
------------------------------------------------------------------

!Once you've successfully connected Postgres as a data source and BigQuery as a destination in Airbyte, you can set up a data pipeline between them with the following steps:

1. **Create a new connection:**On the Airbyte dashboard, navigate to the 'Connections' tab and click the '+ New Connection' button.
2. **Choose your source:**Select Postgres from the dropdown list of your configured sources.
3. **Select your destination:**Choose BigQuery from the dropdown list of your configured destinations.
4. **Configure your sync:**Define the frequency of your data syncs based on your business needs. Airbyte allows both manual and automatic scheduling for your data refreshes.



