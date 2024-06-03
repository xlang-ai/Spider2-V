Documentation Source:
airbyte.com/tutorials/build-a-github-activity-dashboard-for-your-project.md

Documentation Title:
Build a GitHub Activity Dashboard for your Project | Airbyte | Airbyte

Documentation Content:
Then, click on the *Set up connection*button.

!You will be taken to the source page, click on the source and you will see the status of your sync. The sync should take a while to complete.

When done, you will see the status change from running to Succeeded. Also, the byte count will be referring to the byte of data Airbyte has pulled from GitHub into your Postgres database.

!‍

That wasn’t a lot of work, was it? You can pat yourself in the back as you just synced data from GitHub to a Postgres database.

Let's move on to connecting that database to Metabase, so we can start creating our dashboard.

Step 2: Connecting the PostgreSQL database to Metabase
------------------------------------------------------



Documentation Source:
airbyte.com/tutorials/build-a-github-activity-dashboard-for-your-project.md

Documentation Title:
Build a GitHub Activity Dashboard for your Project | Airbyte | Airbyte

Documentation Content:
Setting Up a Postgres Database in Metabase

In order to set up our database, we will click on the cog(settings) icon on the menu bar of the Metabase app and choose the admin option to be taken to the admin view where we can add a database:

!‍

Click on the add a database button and you will be presented with a form where you should select PostgreSQL as your database of choice and then fill out the connection parameters which will be the one for the PostgreSQL database we created to hold the data from GitHub

Fill out the details to match the credentials of the PostgreSQL database we created earlier.

‍

!‍

Afterwards, hit save when you are done entering the database credentials and your database would have been fully loaded onto Metabase ready for us to start creating our dashboard.



Documentation Source:
airbyte.com/tutorials/build-a-github-activity-dashboard-for-your-project.md

Documentation Title:
Build a GitHub Activity Dashboard for your Project | Airbyte | Airbyte

Documentation Content:
Evolution of the number of new issues from non-team members

*Table: Issues*!‍

Wrapping up.
------------

In this article, we have worked through getting data from a GitHub repo using the GitHub Airbyte connector and storing that data in a PostgreSQL database. We then set up Metabase and asked questions to visualize the data. Here is the finished GitHub dashboard with our visualizations on Metabase:

!‍



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



