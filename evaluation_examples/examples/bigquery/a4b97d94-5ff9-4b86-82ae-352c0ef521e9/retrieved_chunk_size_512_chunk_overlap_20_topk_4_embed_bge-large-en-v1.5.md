Documentation Source:
cloud.google.com/bigquery/docs/generate-text.md

Documentation Title:
Generate text by using the ML.GENERATE_TEXT function  |  BigQuery  |  Google Cloud

Documentation Content:
Console

1. Go to the **BigQuery**page.

Go to BigQuery
To create a connection, click add**Add**, and then click **Connections to external data sources**.

In the **Connection type**list, select **Vertex AI remote models,
remote functions and BigLake (Cloud Resource)**.

In the **Connection ID**field, enter a name for your
connection.

Click **Create connection**.

Click **Go to connection**.

In the **Connection info**pane, copy the service account ID for use in a
later step.



Documentation Source:
cloud.google.com/bigquery/docs/generate-text-tutorial.md

Documentation Title:
Generate text by using a remote model and the ML.GENERATE_TEXT function  |  BigQuery  |  Google Cloud

Documentation Content:
Console

1. Go to the **BigQuery**page.

Go to BigQuery
To create a connection, click add**Add**, and then click **Connections to external data sources**.

In the **Connection type**list, select **Vertex AI remote models,
remote functions and BigLake (Cloud Resource)**.

In the **Connection ID**field, enter a name for your
connection.

Click **Create connection**.

Click **Go to connection**.

In the **Connection info**pane, copy the service account ID for use in a
later step.



Documentation Source:
cloud.google.com/bigquery/docs/generate-text-tutorial.md

Documentation Title:
Generate text by using a remote model and the ML.GENERATE_TEXT function  |  BigQuery  |  Google Cloud

Documentation Content:
Terraform

Append the following section into your `main.tf`file.
 


```
## This creates a cloud resource connection.
 ## Note: The cloud resource nested object has only one output only field - serviceAccountId.
 resource "google_bigquery_connection" "connection" {
    connection_id = "CONNECTION_ID"
    project = "PROJECT_ID"
    location = "REGION"
    cloud_resource {}
}        
```
Replace the following:

* CONNECTION\_ID: an ID for your
connection
* PROJECT\_ID: your Google Cloud project ID
* REGION: your
connection region
Grant permissions to the connection's service account
-----------------------------------------------------

To grant the connection's service account an appropriate role to access the
Vertex AI service, follow these steps:

1. Go to the **IAM & Admin**page.

Go to IAM & Admin
Click person\_add**Grant Access**.

In the **New principals**field, enter the service account ID that you
copied earlier.

In the **Select a role**field, choose **Vertex AI**, and then
select **Vertex AI User role**.

Click **Save**.


Create the remote model
-----------------------

Create a remote model that represents a hosted Vertex AI
large language model (LLM):



Documentation Source:
cloud.google.com/bigquery/docs/generate-text-embedding.md

Documentation Title:
Generate text embeddings by using the ML.GENERATE_EMBEDDING function  |  BigQuery  |  Google Cloud

Documentation Content:
Console

1. Go to the **BigQuery**page.

Go to BigQuery
To create a connection, click add**Add**, and then click **Connections to external data sources**.

In the **Connection type**list, select **Vertex AI remote models,
remote functions and BigLake (Cloud Resource)**.

In the **Connection ID**field, enter a name for your
connection.

Click **Create connection**.

Click **Go to connection**.

In the **Connection info**pane, copy the service account ID for use in a
later step.



