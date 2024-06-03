Documentation Source:
cloud.google.com/bigquery/docs/bigquery-web-ui.md

Documentation Title:
Explore the Google Cloud console  |  BigQuery

Documentation Content:
Close a tab

To close all tabs except for one, follow these steps:

Next to the tab name, click
arrow\_drop\_down**Open menu**.

Select
cancel**Close other tabs**.


View personal and project history
---------------------------------

You can view job histories in the footer of the details pane:

!To view details of your own jobs, click **Personal history**.

To view details of recent jobs in your project, click **Project history**.


To see the details of a job or to open the query in an editor, do the following:

In the **Actions**column for a job or query, click
more\_vert**Actions**.

Select **Show job details**or **Open query in editor**.


The job histories include all load, export, copy, and query jobs that you
submitted in the past six months (up to 1,000 entries). The limit of 1,000 jobs
is cumulative across all job types.

Keyboard shortcuts
------------------

To view shortcuts in the Google Cloud console, click
keyboard**SQL workspace shortcuts**.
The following keyboard shortcuts are supported in the Google Cloud console:



Documentation Source:
cloud.google.com/bigquery/docs/managing-jobs.md

Documentation Title:
Managing jobs  |  BigQuery  |  Google Cloud

Documentation Content:
Console

To repeat a query job, do the following:

1. Go to the **BigQuery**page.

Go to BigQuery
To list all your jobs, click **Personal history**. To list all
 jobs in a project, click **Project history**.

Click a query job to open the job details.

To repeat a query, click **Open as new query**.

Click **Run**.


To repeat a load job, do the following:

1. Go to the **BigQuery**page.

Go to BigQuery
To list all your jobs, click **Personal history**. To list all
 jobs in a project, click **Project history**.

Click a load job to open the job details.

To repeat a job, click **Repeat load job**.


**Note:**You cannot repeat an export job or a copy job using the Google Cloud console.### bq

Issue your command again and BigQuery automatically
generates a job with a new job ID.



Documentation Source:
cloud.google.com/bigquery/docs/managing-jobs.md

Documentation Title:
Managing jobs  |  BigQuery  |  Google Cloud

Documentation Content:
`from google.cloud import bigquery


def get_job(
 client: bigquery.Client,
 location: str = "us",
 job_id: str = "abcd-efgh-ijkl-mnop",
) -> None:
 job = client.get_job(job_id, location=location)

 # All job classes have "location" and "job_id" string properties.
 # Use these properties for job operations such as "cancel_job" and
 # "delete_job".
 print(f"{job.location}:{job.job_id}")
 print(f"Type: {job.job_type}")
 print(f"State: {job.state}")
 print(f"Created: {job.created.isoformat()}")`If you need more information to troubleshoot a job, see the `INFORMATION_SCHEMA.JOBS*`viewsand Logs.

List jobs in a project
----------------------

BigQuery saves a six-month job history for all the jobs of a project.

You can view the job history in the following ways:

* Using the Google Cloud console.
* Using the `bq ls`command.
* Calling the `jobs.list`API method.
* Using the client libraries.

The job history includes jobs that are in the `RUNNING`state and jobs that are
`DONE`(indicated by reporting the state as `SUCCESS`or `FAILURE`).



Documentation Source:
cloud.google.com/bigquery/docs/managing-jobs.md

Documentation Title:
Managing jobs  |  BigQuery  |  Google Cloud

Documentation Content:
Console

1. Go to the **BigQuery**page.

Go to BigQuery
2. Select the type of job history you want to view:


	* To display information of your recent jobs, click **Personal
	history**.
	* To display information of recent jobs in your project, click
	**Project history**.
3. To view job details, click a job.

**Note:**The duration of a job is calculated by subtracting start
time (instead of creation time) from end time.



