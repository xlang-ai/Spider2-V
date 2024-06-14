Documentation Source:
cloud.google.com/bigquery/docs/connected-sheets.md

Documentation Title:
Using Connected Sheets  |  BigQuery  |  Google Cloud

Documentation Content:
Enable the BigQuery API.
 
 
 
 

Enable the API

When you finish this topic, you can avoid continued billing by deleting the
resources you created. See Cleaning upfor more detail.

Open BigQuery datasets from Connected Sheets
--------------------------------------------

The following example uses a public dataset to show you how to connect to
BigQuery from Google Sheets.

Create or open a Google Sheets spreadsheet.

2. Click **Data**, click **Data connectors**, and then click **Connect to
BigQuery**.

**Note:**If you do not see the **Data connectors**option, see
Before you begin.
Click **Get connected**.

Select a Google Cloud project that has billing enabled.

Click **Public datasets**.

In the search box, type **chicago**and then select the
**chicago\_taxi\_trips**dataset.

7. Select the **taxi\_trips**table and then click **Connect**.

!Your spreadsheet should look similar to the following:

!

Start using the spreadsheet. You can create pivot tables, formulas, and charts
using familiar Google Sheets techniques.

Although the spreadsheet shows a preview of only 500 rows, any pivot tables,
formulas, and charts use the entire set of data. The maximum number of rows for
results returned for pivot tables is 50,000. You can also extract the data to a
sheet. The maximum number of rows for results returned for data extracts is
50,000. For more information, see the
Connected Sheets tutorial.

Open tables in Connected Sheets
-------------------------------

To open tables in Connected Sheets from the
Google Cloud console, use one of the following methods:

* Use the **Explorer**pane:


	In the **Explorer**pane, expand the dataset that contains the table
	that you want to open in Google Sheets.
	
	2. Next to the table name, click
	more\_vert**View actions**,
	and then select **Open with >Connected Sheets**:
	
	!
* Use the table toolbar:



Documentation Source:
cloud.google.com/bigquery/docs/connected-sheets.md

Documentation Title:
Using Connected Sheets  |  BigQuery  |  Google Cloud

Documentation Content:
```
# Allows egress to Sheets through the Connected Sheets feature
- egressTo:
    operations:
    - serviceName: 'bigquery.googleapis.com'
      methodSelectors:
      - permission: 'bigquery.vpcsc.importData'
    resources:
    - projects/628550087766 # Sheets-owned Google Cloud project
  egressFrom:
    identityType: ANY_USER_ACCOUNT

```
**Note:**Scheduled refreshes of Connected Sheets don't propagate any
end-user context such as IP address or device information.
VPC Service Controls perimeters that use end-user context to restrict access
cause scheduled refreshes to fail.Before you begin
----------------

First, make sure that you meet the requirements for accessing BigQuery
data in Sheets, as described in the "What you need" section of
the Google Workspace topic
Get started with BigQuery data in Google Sheets.

If you do not yet have a Google Cloud project that is set up for billing, follow
these steps:

- Sign in to your Google Cloud account. If you're new to
 Google Cloud, create an accountto evaluate how our products perform in
 real-world scenarios. New customers also get $300 in free credits to
 run, test, and deploy workloads.
- In the Google Cloud console, on the project selector page,
 select or create a Google Cloud project.

**Note**: If you don't plan to keep the
 resources that you create in this procedure, create a project instead of
 selecting an existing project. After you finish these steps, you can
 delete the project, removing all resources associated with the project.Go to project selector
Make sure that billing is enabled for your Google Cloud project.
 

- In the Google Cloud console, on the project selector page,
 select or create a Google Cloud project.

**Note**: If you don't plan to keep the
 resources that you create in this procedure, create a project instead of
 selecting an existing project. After you finish these steps, you can
 delete the project, removing all resources associated with the project.Go to project selector
Make sure that billing is enabled for your Google Cloud project.
 

2. BigQuery is automatically enabled in new projects.
 To activate BigQuery in a preexisting project, go to



Documentation Source:
cloud.google.com/bigquery/docs/analyze-data-tableau.md

Documentation Title:
Quickstart: Analyze BigQuery data with BI Engine and Tableau  |  BigQuery: Cloud Data Warehouse  |  Google Cloud

Documentation Content:
Required permissions

To get the permissions that you need to execute queries, run jobs, and view data,
 
 ask your administrator to grant you the
 
 
 BigQuery Admin(`roles/bigquery.admin`) IAM role.
 

 
 
 For more information about granting roles, see Manage access.
 
 

You might also be able to get
 the required permissions through custom
 rolesor other predefined
 roles.
 

Additional permissions might be needed if you have are using a custom OAuth
client in Tableau to connect to BigQuery. For more information,
see Troubleshooting Errors.

Create a BigQuery dataset
-------------------------

The first step is to create a BigQuery dataset to store your
BI Engine-managed table. To create your dataset, follow these
steps:

1. In the Google Cloud console, go to the BigQuery page.

Go to BigQuery
In the navigation panel, in the **Explorer**panel, click your project
name.

In the details panel, click more\_vert**View actions**, and then click **Create dataset**.

4. On the **Create dataset**page, do the following:


	* For **Dataset ID**, enter `biengine_tutorial`.
	For **Data location**, choose **us (multiple regions in United
	States)**, the multi-region
	locationwhere public datasets
	are stored.
	
	* For this tutorial, you can select **Enable table expiration**, and then
	specify the number of days before the table expires.
	
	!
Leave all of the other default settings in place and click **Create dataset**.


Create a table by copying data from a public dataset
----------------------------------------------------

This tutorial uses a dataset available through the
Google Cloud Public Dataset Program. Public datasets
are datasets that BigQuery hosts for you to access and integrate
into your applications.

In this section, you create a table by copying data from the
San Francisco 311 service requestsdataset. You can explore the dataset by using the
Google Cloud console.



Documentation Source:
cloud.google.com/bigquery/docs/bi-engine-looker-studio.md

Documentation Title:
Quickstart using Looker Studio  |  BigQuery  |  Google Cloud

Documentation Content:
Creating your data source

To create your data source:

Open Looker Studio.

2. On the **Reports**page, in the **Start a new report section**, click the
**Blank Report**template. This creates a new untitled report.

!
If prompted, complete the **Marketing Preferences**and the **Account and
Privacy**settings and then click **Save**. You may need to click the **Blank**template again after saving your settings.

4. In the **Add a data source**window, click **Create new data source**.

!
In the **Google Connectors**section, hover over **BigQuery**and then click **Select**.

For **Authorization**, click **Authorize**. This allows Looker Studio
access to your Google Cloud project.

In the **Request for permission**dialog, click **Allow**to give
Looker Studio the ability to view data in BigQuery. You may
not receive this prompt if you previously used Looker Studio.

Leave **My Projects**selected and in the **Project**pane, click the name of
your project.

In the **Dataset**pane, click **biengine\_tutorial**.

In the **Table**pane, click **311\_service\_requests\_copy**.

In the upper right corner of the window, click **Connect**. Once Looker Studio
connects to the BigQuery data source, the table's fields are
displayed. You can use this page to adjust the field properties or to create new
calculated fields.

In the upper right corner, click **Add to report**.

When prompted, click **Add to report**.

In the **Request for permission**dialog, click **Allow**to give
Looker Studio the ability to view and manage files in Google Drive.
You may not receive this prompt if you previously used Looker Studio.



