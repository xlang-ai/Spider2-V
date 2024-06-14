Documentation Source:
cloud.google.com/bigquery/docs/working-with-connections.md

Documentation Title:
Manage connections  |  BigQuery  |  Google Cloud

Documentation Content:
Java

Before trying this sample, follow the Javasetup instructions in the
 BigQuery quickstart using
 client libraries.
 
 
 
 For more information, see the
 BigQuery JavaAPI
 reference documentation.
 
 

To authenticate to BigQuery, set up Application Default Credentials.
 For more information, see
 
 Set up authentication for client libraries.
 
 

`import com.google.cloud.bigquery.connection.v1.ListConnectionsRequest;
import com.google.cloud.bigquery.connection.v1.LocationName;
import com.google.cloud.bigqueryconnection.v1.ConnectionServiceClient;
import java.io.IOException;

// Sample to get list of connections
public class ListConnections {

 public static void main(String[] args) throws IOException {
 // TODO(developer): Replace these variables before running the sample.
 String projectId = "MY_PROJECT_ID";
 String location = "MY_LOCATION";
 listConnections(projectId, location);
 }

 static void listConnections(String projectId, String location) throws IOException {
 try (ConnectionServiceClient client = ConnectionServiceClient.create()) {
 LocationName parent = LocationName.of(projectId, location);
 int pageSize = 10;
 ListConnectionsRequest request =
 ListConnectionsRequest.newBuilder()
 .setParent(parent.toString())
 .setPageSize(pageSize)
 .build();
 client
 .listConnections(request)
 .iterateAll()
 .forEach(con -> System.out.println("Connection Id :" + con.getName()));
 }
 }
}`View connection details
-----------------------

After you create a connection, you can get information about the
connection's configuration. The configuration includes the values you
supplied when you created the transfer.

Select one of the following options:



Documentation Source:
cloud.google.com/bigquery/docs/connect-to-sql.md

Documentation Title:
Connect to Cloud SQL  |  BigQuery  |  Google Cloud

Documentation Content:
Java

Before trying this sample, follow the Javasetup instructions in the
 BigQuery quickstart using
 client libraries.
 
 
 
 For more information, see the
 BigQuery JavaAPI
 reference documentation.
 
 

To authenticate to BigQuery, set up Application Default Credentials.
 For more information, see
 
 Set up authentication for client libraries.
 
 

`import com.google.api.resourcenames.ResourceName;
import com.google.cloud.bigquery.connection.v1.ConnectionName;
import com.google.cloud.bigqueryconnection.v1.ConnectionServiceClient;
import com.google.iam.v1.Binding;
import com.google.iam.v1.Policy;
import com.google.iam.v1.SetIamPolicyRequest;
import java.io.IOException;

// Sample to share connections
public class ShareConnection {

 public static void main(String[] args) throws IOException {
 // TODO(developer): Replace these variables before running the sample.
 String projectId = "MY_PROJECT_ID";
 String location = "MY_LOCATION";
 String connectionId = "MY_CONNECTION_ID";
 shareConnection(projectId, location, connectionId);
 }

 static void shareConnection(String projectId, String location, String connectionId)
 throws IOException {
 try (ConnectionServiceClient client = ConnectionServiceClient.create()) {
 ResourceName resource = ConnectionName.of(projectId, location, connectionId);
 Binding binding =
 Binding.newBuilder()
 .addMembers("group:example-analyst-group@google.com")
 .setRole("roles/bigquery.connectionUser")
 .build();
 Policy policy = Policy.newBuilder().addBindings(binding).build();
 SetIamPolicyRequest request =
 SetIamPolicyRequest.newBuilder()
 .setResource(resource.toString())
 .setPolicy(policy)
 .build();
 client.setIamPolicy(request);
 System.out.println("Connection shared successfully");
 }
 }
}`What's next
-----------

* Learn about different connection types.
* Learn about managing connections.
* Learn about federated queries.
* Learn how to query Cloud SQL data.
Send feedback
 
 Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-05-13 UTC.

* ### Why Google



Documentation Source:
cloud.google.com/bigquery/docs/create-cloud-resource-connection.md

Documentation Title:
Create and set up a Cloud resource connection  |  BigQuery  |  Google Cloud

Documentation Content:
bq

1. In a command-line environment, create a connection:


```
bq mk --connection --location=REGION--project_id=PROJECT_ID\
    --connection_type=CLOUD_RESOURCE CONNECTION_ID
```
The `--project_id`parameter overrides the default project.

Replace the following:


	* REGION: your
	connection region
	* PROJECT\_ID: your Google Cloud project ID
	* CONNECTION\_ID: an ID for your
	connectionWhen you create a connection resource, BigQuery creates a
unique system service account and associates it with the connection.

**Troubleshooting**: If you get the following connection error,
update the Google Cloud SDK:


```
Flags parsing error: flag --connection_type=CLOUD_RESOURCE: value should be one of...

```
2. Retrieve and copy the service account ID for use in a later
step:


```
bq show --connection PROJECT_ID.REGION.CONNECTION_ID
```
The output is similar to the following:


```
name                          properties
1234.REGION.CONNECTION_ID{"serviceAccountId": "connection-1234-9u56h9@gcp-sa-bigquery-condel.iam.gserviceaccount.com"}

```



Documentation Source:
cloud.google.com/bigquery/docs/working-with-connections.md

Documentation Title:
Manage connections  |  BigQuery  |  Google Cloud

Documentation Content:
Java

Before trying this sample, follow the Javasetup instructions in the
 BigQuery quickstart using
 client libraries.
 
 
 
 For more information, see the
 BigQuery JavaAPI
 reference documentation.
 
 

To authenticate to BigQuery, set up Application Default Credentials.
 For more information, see
 
 Set up authentication for client libraries.
 
 

`import com.google.cloud.bigquery.connection.v1.Connection;
import com.google.cloud.bigquery.connection.v1.ConnectionName;
import com.google.cloud.bigquery.connection.v1.UpdateConnectionRequest;
import com.google.cloud.bigqueryconnection.v1.ConnectionServiceClient;
import com.google.protobuf.FieldMask;
import com.google.protobuf.util.FieldMaskUtil;
import java.io.IOException;

// Sample to update connection
public class UpdateConnection {

 public static void main(String[] args) throws IOException {
 // TODO(developer): Replace these variables before running the sample.
 String projectId = "MY_PROJECT_ID";
 String location = "MY_LOCATION";
 String connectionId = "MY_CONNECTION_ID";
 String description = "MY_DESCRIPTION";
 Connection connection = Connection.newBuilder().setDescription(description).build();
 updateConnection(projectId, location, connectionId, connection);
 }

 static void updateConnection(
 String projectId, String location, String connectionId, Connection connection)
 throws IOException {
 try (ConnectionServiceClient client = ConnectionServiceClient.create()) {
 ConnectionName name = ConnectionName.of(projectId, location, connectionId);
 FieldMask updateMask = FieldMaskUtil.fromString("description");
 UpdateConnectionRequest request =
 UpdateConnectionRequest.newBuilder()
 .setName(name.toString())
 .setConnection(connection)
 .setUpdateMask(updateMask)
 .build();
 Connection response = client.updateConnection(request);
 System.out.println("Connection updated successfully :" + response.getDescription());
 }
 }
}`Delete a connection
-------------------

Select one of the following options:



