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
docs.astronomer.io/learn/managing-airflow-code.md

Documentation Title:
Manage Airflow code | Astronomer Documentation

Documentation Content:
Astronomer uses the following project structure:

`.├── dags # Folder where all your DAGs go│ ├── example-dag.py│ └── redshift_transforms.py├── Dockerfile # For Astronomer's Docker image and runtime overrides├── include # For any scripts that your DAGs might need to access│ └── sql│ └── transforms.sql├── packages.txt # For OS-level packages├── plugins # For any custom or community Airflow plugins│ └── example-plugin.py└── requirements.txt # For any Python packages`To create a project with this structure automatically, install the Astro CLIand initialize a project with `astro dev init`.

If you are not running Airflow with Docker or have different requirements for your organization, your project structure might look different. Choose a structure that works for your organization and keep it consistent so that anyone working with Airflow can easily transition between projects without having to re-learn a new structure.

When to separate projects​
--------------------------

The most common setup for Airflow projects is to keep all code for a given deployment in the same repository. However, there are some circumstances where it makes sense to separate DAGs into multiple projects. In these scenarios, it's best practice to have a separate Airflow deployment for each project. You might implement this project structure for the following reasons:

* Access control: Role-based access control (RBAC) should be managed at the Airflow Deployment level and not at the DAG level. If Team A and Team B should only have access to their own team's DAGs, it would make sense to split them up into two projects and deployments.
* Infrastructure considerations: If you have a set of DAGs that are well suited to the Kubernetes executor and another set that are well suited to the Celery executor, you may want to separate them into two different projects that feed Airflow deployments with different infrastructure. See Configure Deployment resources.
* Dependency management: If DAGs have conflicting Python or OS dependencies, one way of managing this can be separating them into separate projects so they are isolated from one another.

Occasionally, some use cases require DAGs from multiple projects to be deployed to the same Airflow deployment. This is a less common pattern and is not recommended for project organization unless it is specifically required.



Documentation Source:
docs.astronomer.io/learn/airflow-ui.md

Documentation Title:
An introduction to the Airflow UI | Astronomer Documentation

Documentation Content:
Browse tab​
-----------

The **Browse**tab links to multiple pages that provide additional insight into and control over your DAG runs and task instances for all DAGs in one place.

!The DAG runs and task instances pages are the easiest way to view and manipulate these objects in aggregate. If you need to re-run tasks in multiple DAG runs, you can do so from this page by selecting all relevant tasks and clearing their status.

!The DAG Dependencies view shows a graphical representation of any cross-DAGand dataset dependencies in your Airflow environment.

!Other views on the **Browse**tab include:

* **Jobs:**Shows a list of all jobs that have been completed. This includes executed tasks as well as scheduler jobs.
* **Audit Logs:**Shows a list of events that have occurred in your Airflow environment that can be used for auditing purposes.
* **Task Reschedules:**Shows a list of all tasks that have been rescheduled.
* **Triggers:**Shows any triggers that occurred in this Airflow environment. To learn more about triggers and related concepts, you can check out the guide on Deferrable Operators.
* **SLA Misses:**Shows any task instances that have missed their SLAs.

Admin tab​
----------

The **Admin**tab links to pages for content related to Airflow administration that are not specific to any particular DAG. Many of these pages can be used to both view and modify your Airflow environment.

!For example, the **Connections**page shows all Airflow connections stored in your environment. Click `+`to add a new connection. For more information, see Managing your Connections in Apache Airflow.

!Similarly, the XComs page shows a list of all XComs stored in the metadata database and allows you to easily delete them.

!Other pages on the **Admin**tab include:

* **Variables:**View and manage Airflow variables.
* **Configurations:**View the contents of your `airflow.cfg`file. Note that this can be disabled by your Airflow admin for security reasons.
* **Plugins:**View any Airflow pluginsdefined in your environment.
* **Providers:**View all Airflow providersincluded in your Airflow environment with their version number.
* **Pools:**View and manage Airflow pools.



Documentation Source:
docs.astronomer.io/astro/first-dag-github-actions.md

Documentation Title:
Run your first DAG with GitHub Actions | Astronomer Documentation

Documentation Content:
**to open it.

Step 2: Fork the example project repository​
--------------------------------------------

This repository contains an *Astro project*, which is a collection of files required for running Airflow on Astro. An Astro project includes folders for DAG files, plugins, dependencies, and more. Specifically, this Astro project includes an example DAG which, when you run it, retrieves a list of countries from an Astro S3 data store and filters the list through a data transform.

Open the example project repositoryin a new tab or browser window.

**Choose an owner**from your available options.

Keep the selection to **Copy the `main`branch only**.

Click **Create fork**.


Step 3: Set up the GitHub Actions Workflow​
-------------------------------------------

This example repository also includes a pre-configured Astronomer deploy action, which you can use to set up a CI/CD deployment pipeline. In this step, you'll configure the GitHub action to deploy code from your forked repository to Astro and run the workflow.

Open two browser windows: one with the Astro UI, and one with your forked GitHub repository.

In the Astro UI, choose the Deployment where you want to deploy your Astro project.

In GitHub, open your forked repository and click **Actions**.

Click **I understand my workflows, go ahead and enable them.**



