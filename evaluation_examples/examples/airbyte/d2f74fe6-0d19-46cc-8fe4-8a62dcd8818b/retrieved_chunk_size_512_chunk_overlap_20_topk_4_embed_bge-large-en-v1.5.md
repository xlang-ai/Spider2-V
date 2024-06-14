Documentation Source:
airbyte.com/docs.airbyte.com/deploying-airbyte/local-deployment.md

Documentation Title:
Local Deployment | Airbyte Documentation

Documentation Content:
After the first run
users should be able to run the command from the terminal. Airbyte suggests mac users to use `brew`if it is available.

./abctl local install* Your browser should open to the Airbyte Application, if it does not visit http://localhost
* You will be asked for a username and password. By default, that's username `airbyte`and password `password`. You can set these values through command line flags or environment variables. For example, to set the username and password to `foo`and `bar`respectively, you can run the following command:

`./abctl local install --username foo --password bar# Or as Environment VariablesABCTL_LOCAL_INSTALL_PASSWORD=fooABCTL_LOCAL_INSTALL_USERNAME=bar`- Start moving some data!
Troubleshooting​
----------------

If you have any questions about the local setup and deployment process, head over to our Getting Started FAQon our Airbyte Forum that answers the following questions and more:

* How long does it take to set up Airbyte?
* Where can I see my data once I've run a sync?
* Can I set a start time for my sync?

If you encounter any issues, check out Getting Supportdocumentation
for options how to get in touch with the community or us.

Edit this pagePreviousDeploy AirbyteNextDocker ComposeSetup & launch AirbyteTroubleshooting
Was this page helpful?YesNo



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
airbyte.com/tutorials/how-to-use-airflow-and-airbyte-together.md

Documentation Title:
A step-by-step guide to setting up and configuring Airbyte and Airflow to work together | Airbyte

Documentation Content:
The instructions presented in this tutorial were created in February 2023, and the following tools were used:

* Airbyte OSS 0.40.32
* Docker Desktop v4.10.1
* macOS Monterey Version 12.5.1
* MacBook Pro with the Apple M1 Pro Chip
* Airflow v2.5.1 Git Version: .release:2.5.1+49867b660b6231c1319969217bc61917f7cf9829

Install Airbyte
---------------

If you already have a local copy of Airbyte running, then you may skip this section. Otherwise, follow the instructions to deploy Airbyte. 

[Optional] Modify **BASIC\_AUTH\_USERNAME**and **BASIC\_AUTH\_PASSWORD**in the (hidden) **.env**file. For this tutorial I use the following default values: 

`BASIC_AUTH_USERNAME=airbyte
BASIC_AUTH_PASSWORD=password`Once Airbyte is running, in your browser type in localhost:8000, which should prompt you for a username and password as follows:

!

Airbyte OSS login prompt

Create a connection
-------------------

Create a connection that sends data from the **Sample Data (Faker)**source to the **Local JSON**(file system) output. Click on “Create your first connection” as shown below:

!

Create your first connection prompt

‍

You should then see an option to set up a source connection. Select the Faker source from the dropdown as shown below.

!

Select Sample Data (Faker) as a source

‍

After selecting Sample Data as the source, you will see a screen that should look as follows. Click on **Set up source**as shown below. 

!

Configure Sample Data (Faker) as a source

‍

You will then wait a few seconds for the Sample Data source to be verified, at which point you will be prompted to configure the destination that will be used for the connection. Select **Local JSON**as shown below:

!

Select Local JSON as a destination

‍

After selecting Local JSON as the output, you will need to specify where the JSON files should be written.



Documentation Source:
airbyte.com/docs.airbyte.com/deploying-airbyte/docker-compose.md

Documentation Title:
Docker Compose | Airbyte Documentation

Documentation Content:
Setup Guide​

**1. Check out system requirements from Docker documentation.**Follow the steps on the system requirements, and necessarily, download and install the Linux kernel update package.

**2. Install Docker Desktop on Windows.**Install Docker Desktopfrom here.

Make sure to select the options:

*Enable Hyper-V Windows Features*2. *Install required Windows components for WSL 2*when prompted. After installation, it will require to reboot your computer.

**3. You're done!**`git clone --depth=1 https://github.com/airbytehq/airbyte.gitcd airbytebash run-ab-platform.sh`* In your browser, just visit http://localhost:8000
* You will be asked for a username and password. By default, that's username `airbyte`and password `password`. Once you deploy airbyte to your servers, be sure to change these.
* Start moving some data!

Troubleshooting​
----------------

If you have any questions about the local setup and deployment process, head over to our Getting Started FAQon our Airbyte Forum that answers the following questions and more:

* How long does it take to set up Airbyte?
* Where can I see my data once I've run a sync?
* Can I set a start time for my sync?

If you encounter any issues, check out Getting Supportdocumentation
for options how to get in touch with the community or us.

Edit this pagePreviousLocal DeploymentNextDeploy Airbyte on AWS (Amazon EC2)Setup & launch Airbyte* Deploy on WindowsSetup Guide
Troubleshooting
Was this page helpful?YesNo



