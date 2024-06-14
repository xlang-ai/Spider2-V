Documentation Source:
docs.astronomer.io/astro/view-logs.md

Documentation Title:
View Deployment logs | Astronomer Documentation

Documentation Content:
View task logs in the Airflow UI​

- Access the Airflow UI.
* To access the Airflow UI for a Deployment, open the Deployment in the Astro UI and click **Open Airflow**.
* To access the Airflow UI in a local environment, open a browser and go to `http://localhost:8080`.
1. Click a DAG.
2. Click **Graph**.
3. Click a task run.
4. Click **Instance Details**.
5. Click **Log**.

See also​
---------

Export task logs and metrics to DatadogExport task logs to AWS CloudwatchWas this page helpful?
----------------------

YesNoSign up for Developer Updates
-----------------------------

Get a summary of new Astro features once a month.

SubmitYou can unsubscribe at any time. By proceeding you agree to our Privacy Policy, our Website Termsand to receive emails from Astronomer.

Edit this pagePreviousDeployment API keys (Deprecated)NextDAGs* Airflow Component Logs
	Airflow component log levelsView Airflow component logs in the Astro UIView Airflow component logs locally
* Airflow task logs
	Airflow task log levelsView task logs on the Astro UIView task logs in the Airflow UI
See alsoLegal·Privacy·Security·Cookie Preferences!!© Astronomer 2023. Various trademarks held by their respective owners.



Documentation Source:
docs.astronomer.io/astro/migrate-gcc.md

Documentation Title:
Migrate to Astro from Google Cloud Composer | Astronomer Documentation

Documentation Content:
After the migration is complete, the status **Migrated ✅**appears.


Refer to the Configurationdetailed instructions on using the operator.

Log in to Astro. In the Astro UI, open the Deployment you're migrating to.

Click **Open Airflow**to open the Airflow UI for the Deployment. Copy the URL for the home page. It should look similar to `https://.astronomer.run//home`.

Create a Deployment API token for the Deployment. The token should minimally have permissions to update the Deployment and deploy code. Copy this token. See Create and manage Deployment API tokensfor additional setup steps.

4. Add the following DAG to your source Airflow environment:

`fromairflow.models.dag importDAGfromastronomer.starship.operators importAstroMigrationOperatorfromdatetime importdatetimewithDAG(dag_id="astronomer_migration_dag",start_date=datetime(1970,1,1),schedule_interval=None,)asdag:AstroMigrationOperator(task_id='export_meta',deployment_url='{{ dag_run.conf["deployment_url"] }}',token='{{ dag_run.conf["astro_token"] }}',)`
Deploy this DAG to your source Airflow environment.

Once the DAG is available in the Airflow UI, click **Trigger DAG**, then click **Trigger DAG w/ config**.

7. In **Configuration JSON**, add the following configuration:

`{"deployment_url":"","astro_token":""}`
8. Replace the following placeholder values:


	* ``: The Deployment URL you copied in Step 2.
	* ``: The token you copied in Step 3.
Click **Trigger**. After the DAG successfully runs, all connections, variables, and environment variables that are available from the Airflow UI are migrated to Astronomer.

Step 5: Create an Astro project​
--------------------------------

1. Create a new directory for your Astro project:

mkdir
2. Open the directory:

cd
3. Run the following Astro CLI command to initialize an Astro project in the directory:

astro dev initThis command generates a set of files that will build into a Docker image that you can both run on your local machine and deploy to Astro.
4.



Documentation Source:
docs.astronomer.io/astro/cli/astro-deployment-service-account.md

Documentation Title:
astro deployment service-account | Astronomer Documentation

Documentation Content:
Skip to main content!!**Docs**DocsFind what you're looking forLearn About AstronomerGet Started FreeHomeAstroAstro CLISoftwareLearnTry AstroOverviewInstall the CLIQuickstartDevelop your projectRun Airflow locallyTest your DAGsRelease notesRelease and lifecycle policyAdvanced* Command reference
	astro completionastro configastro contextastro deploy+ astro deployment
		astro deployment airflow upgradeastro deployment airflow-variableastro deployment connectionastro deployment createastro deployment deleteastro deployment hibernateastro deployment inspectastro deployment listastro deployment logsastro deployment poolastro deployment runtime upgradeastro deployment service-accountastro deployment teamastro deployment tokenastro deployment updateastro deployment userastro deployment variableastro deployment wake-upastro deployment worker-queue
	astro devastro loginastro logoutastro organizationastro registryastro runastro teamastro user createastro versionastro workspace
Support Knowledge BaseOffice HoursWebinarsAstro StatusCommand referenceastro deploymentastro deployment service-account
astro deployment service-account
================================

infoThis command is available only if you're authenticated to an Astronomer Software installation.

Manage Deployment-level service accounts, which you can use to configure a CI/CD pipeline or otherwise interact with the Astronomer Houston API.

Usage​
------

This command includes three subcommands: `create`, `delete`, and `list`

`# Creates a Deployment-level service accountastro deployment service-account create --deployment-id=--label=# Deletes a Deployment-level service accountastro deployment service-account delete # Shows the name, ID, and API key for each service account in a specific Deployment.astro deployment service-account list`Options​
--------



Documentation Source:
docs.astronomer.io/astro/authorize-deployments-to-your-cloud.md

Documentation Title:
Authorize an Astro Deployment to cloud resources using workload identity | Astronomer Documentation

Documentation Content:
Step 3: Create an Airflow connection​

1. In the Astro UI, click **Environment**in the main menu to open the **Connections**page.
2. Click **+ Connection**to add a new connection for your Workspace.
3. Search for **Azure**, then select the **Managed identity**option.
4. Configure your Airflow connection with the information you copied in the previous steps.
5. Link the connection to the Deployment(s) where you configured your managed identity.

Any DAG that uses your connection will now be authorized to Azure through your managed identity.

See also​
---------

Manage Airflow connections and variablesDeploy code to AstroWas this page helpful?
----------------------

YesNoSign up for Developer Updates
-----------------------------

Get a summary of new Astro features once a month.

SubmitYou can unsubscribe at any time. By proceeding you agree to our Privacy Policy, our Website Termsand to receive emails from Astronomer.

Edit this pagePreviousCustom Deployment rolesNextTransfer a DeploymentPrerequisitesWhat is workload identity?SetupSee alsoLegal·Privacy·Security·Cookie Preferences!!© Astronomer 2023. Various trademarks held by their respective owners.



