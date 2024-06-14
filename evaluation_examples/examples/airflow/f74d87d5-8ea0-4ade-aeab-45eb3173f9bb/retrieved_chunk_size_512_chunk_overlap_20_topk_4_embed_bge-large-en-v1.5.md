Documentation Source:
docs.astronomer.io/astro/first-dag-cli.md

Documentation Title:
Run your first DAG with the Astro CLI | Astronomer Documentation

Documentation Content:
You deploy DAGs to a Deployment, and you can have one or more Deployments within a Workspace.

Log in to the Astro UI.

On the **Deployments**page, click **+ Deployment**.

In the **Name**field, enter a name for your Deployment. You can leave the other fields at their default values. This creates a basic Deployment on a standard Astronomer-hosted cluster. You can delete the Deployment after you finish testing your example DAG runs.

4. Click **Create Deployment**.

A confirmation message appears indicating that the Deployment status is **Creating**until all underlying components in the Deployment are healthy. During this time, the Airflow UI is unavailable and you can't deploy code or modify Deployment settings. When the Deployment is ready, the status changes to **Healthy**.

For more information about possible Deployment health statuses, see Deployment health. Or, to learn more about how to customize your Deployment settings, see Deployment settings.

Step 3: Create an Astro project​
--------------------------------

An *Astro project*contains the set of files necessary to run Airflow, including dedicated folders for your DAG files, plugins, and dependencies. All new Astro projects contain two example DAGs. In this tutorial, you'll be deploying these example DAGs to your Deployment on Astro.

Open your terminal or IDE.

2. Create a new folder for your Astro project:

mkdir
3. Open the folder:

cd
4.



Documentation Source:
docs.astronomer.io/astro/first-dag-github-actions.md

Documentation Title:
Run your first DAG with GitHub Actions | Astronomer Documentation

Documentation Content:
This automatically deploys the example DAGs in your Astro project to your Deployment.

Step 4: View your DAG run results​
----------------------------------

Open your Deployment in the Astro UI and click **DAGs**in the left sidebar, then click **S3**. From this page, you can see that the `s3`DAG has run exactly once.

!The **DAGs**page of the Astro UI includes the most commonly used information and actions from the Airflow UI in one place. If you prefer to view your DAG run in the Airflow UI, click **Open Airflow**in the upper right corner of the page.

Congratulations! You deployed and ran your first DAG on Astro with GitHub Actions.

Next Steps​
-----------

* Develop your Astro project.
* Read more about Developing CI/CD workflows.
* Install the CLIto test DAGs or run Airflow locally.
* Write your First DAG.
Was this page helpful?
----------------------

YesNoSign up for Developer Updates
-----------------------------

Get a summary of new Astro features once a month.

SubmitYou can unsubscribe at any time. By proceeding you agree to our Privacy Policy, our Website Termsand to receive emails from Astronomer.

Edit this pagePreviousRun your first DAGNextWith Astro CLIPrerequisitesStep 1: Create a DeploymentStep 2: Fork the example project repositoryStep 3: Set up the GitHub Actions WorkflowStep 4: View your DAG run resultsNext StepsLegal·Privacy·Security·Cookie Preferences!!© Astronomer 2023. Various trademarks held by their respective owners.



Documentation Source:
docs.astronomer.io/learn/get-started-with-airflow.md

Documentation Title:
Get started with Apache Airflow, Part 1: Write and run your first DAG | Astronomer Documentation

Documentation Content:
Edit this pagePreviousQuickstartNextPart 1: Write your first DAGTime to completeAssumed knowledgePrerequisitesStep 1: Create an Astro projectStep 2: Start AirflowStep 3: Log in to the Airflow UIStep 4: Trigger a DAG runStep 5: Explore the Airflow UIStep 6: Write a new DAGStep 7: Run the new DAGStep 8: View task logsNext stepsSee alsoLegal·Privacy·Security·Cookie Preferences!!© Astronomer 2023. Various trademarks held by their respective owners.



Documentation Source:
docs.astronomer.io/astro/first-dag-cli.md

Documentation Title:
Run your first DAG with the Astro CLI | Astronomer Documentation

Documentation Content:
This prevents your example DAG from running automatically and consuming your Deployment resources.


Step 6: View your DAG status in the Astro UI​
---------------------------------------------

The Astro UI shows you information about the health of your Deployment, including analytics and logs for your DAG runs.

Go back to your Deployment page in the Astro UI. Because you ran your example DAG, your Deployment information page now has data about your Deployment and DAG runs. The following example shows an example of what you might find in the **Overview**page for your Deployment.

!When you're done exploring, you can delete your Deployment from the **More Options**menu on your **Deployments**page.

Next Steps​
-----------

Now that you've created and run your first DAG on Astro, the next step is to add your own DAGs, build out the rest of your Astro project, and start testing real data. See:

* Develop a project.
* Install Dockerto use the full capabilities of the Astro CLI, such as the ability to run Airflow locally and deploy the rest of your Astro project to Astro, including Python packages.
* Write your First DAG.
* Deploy code to Astro.
Was this page helpful?
----------------------

YesNoSign up for Developer Updates
-----------------------------

Get a summary of new Astro features once a month.

SubmitYou can unsubscribe at any time. By proceeding you agree to our Privacy Policy, our Website Termsand to receive emails from Astronomer.

Edit this pagePreviousWith GitHub ActionsNextLog in to AstroPrerequisitesStep 1: Install the Astro CLIStep 2: Create a DeploymentStep 3: Create an Astro projectStep 4: Deploy example DAGs to your Astro DeploymentStep 5: Trigger your DAG on AstroStep 6: View your DAG status in the Astro UINext StepsLegal·Privacy·Security·Cookie Preferences!!© Astronomer 2023. Various trademarks held by their respective owners.



