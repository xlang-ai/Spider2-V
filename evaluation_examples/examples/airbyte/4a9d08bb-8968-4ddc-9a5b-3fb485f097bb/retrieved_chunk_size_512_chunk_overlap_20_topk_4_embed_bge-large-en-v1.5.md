Documentation Source:
airbyte.com/tutorials/build-a-github-activity-dashboard-for-your-project.md

Documentation Title:
Build a GitHub Activity Dashboard for your Project | Airbyte | Airbyte

Documentation Content:
Setting up Airbyte

You can skip this step if you already have Airbyte on your machine.

To set up Airbyte on your machine, make sure you have Docker and Docker compose set-up, as well as git. Then, open a terminal, and go to a location you want to download Airbyte in and run:

`git clone https://github.com/airbytehq/airbyte.git`‍

You will need to go into the cloned airbyte repo by running cd airbyte and then you run:

`docker-compose up`Or if you are on the newest version of the Docker CLI you can run:

`docker compose up`The above command will create and start the Airbyte containers. After it's done, you can access Airbyte athttp://localhost:8000/(you can go ahead and set up your preference, then leave the Airbyte web app open as we will come back to it shortly)



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
airbyte.com/docs.airbyte.com/integrations/sources/github.md

Documentation Title:
GitHub | Airbyte Documentation

Documentation Content:
Step 1: Set up GitHub​

Create a GitHub Account.

**Airbyte Open Source additional setup steps**Log into GitHuband then generate a personal access token. To load balance your API quota consumption across multiple API tokens, input multiple tokens separated with `,`.



Documentation Source:
airbyte.com/docs.airbyte.com/integrations/sources/github.md

Documentation Title:
GitHub | Airbyte Documentation

Documentation Content:
Step 2: Set up the GitHub connector in Airbyte​

**For Airbyte Cloud:**1. Log into your Airbyte Cloudaccount.
2. In the left navigation bar, click **Sources**.
3. On the source selection page, select **GitHub**from the list of Sources.
4. Add a name for your GitHub connector.
5. To authenticate:
**For Airbyte Cloud:****Authenticate your GitHub account**to authorize your GitHub account. Airbyte will authenticate the GitHub account you are already logged in to. Please make sure you are logged into the right account.

**For Airbyte Open Source:**Authenticate with **Personal Access Token**. To generate a personal access token, log into GitHuband then generate a personal access token. Enter your GitHub personal access token. To load balance your API quota consumption across multiple API tokens, input multiple tokens separated with `,`.



