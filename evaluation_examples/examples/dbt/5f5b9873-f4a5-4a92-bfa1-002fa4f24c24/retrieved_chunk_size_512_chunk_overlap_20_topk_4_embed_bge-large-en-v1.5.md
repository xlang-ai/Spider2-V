Documentation Source:
cloud.google.com/bigquery/docs/samples/bigqueryconnection-create-connection.md

Documentation Title:
Create a Cloud SQL connection  |  BigQuery  |  Google Cloud

Documentation Content:
def main() -> None:
 # TODO(developer): Set all variables for your Cloud SQL for MySQL connection.
 project_id = "your-project-id" # set project_id
 location = "US" # set location
 # See: https://cloud.google.com/bigquery/docs/locations for a list of
 # available locations.
 database = "my-database" # set database name
 username = "my-username" # set database username
 password = "my-password" # set database password
 cloud_sql_conn_name = "" # set the name of your connection
 transport = "grpc" # Set the transport to either "grpc" or "rest"
 connection_id = "my-sample-connection"

 cloud_sql_credential = bq_connection.CloudSqlCredential(
 {
 "username": username,
 "password": password,
 }
 )
 cloud_sql_properties = bq_connection.CloudSqlProperties(
 {
 "type_": bq_connection.CloudSqlProperties.DatabaseType.MYSQL,
 "database": database,
 "instance_id": cloud_sql_conn_name,
 "credential": cloud_sql_credential,
 }
 )
 create_mysql_connection(
 connection_id, project_id, location, cloud_sql_properties, transport
 )



Documentation Source:
cloud.google.com/bigquery/docs/samples/bigqueryconnection-create-connection.md

Documentation Title:
Create a Cloud SQL connection  |  BigQuery  |  Google Cloud

Documentation Content:
def create_mysql_connection(
 connection_id: str,
 project_id: str,
 location: str,
 cloud_sql_properties: bq_connection.CloudSqlProperties,
 transport: str,
) -> None:
 connection = bq_connection.types.Connection({"cloud_sql": cloud_sql_properties})
 client = bq_connection.ConnectionServiceClient(transport=transport)
 parent = client.common_location_path(project_id, location)
 request = bq_connection.CreateConnectionRequest(
 {
 "parent": parent,
 "connection": connection,
 # connection_id is optional, but can be useful to identify
 # connections by name. If not supplied, one is randomly
 # generated.
 "connection_id": connection_id,
 }
 )
 response = client.create_connection(request)
 print(f"Created connection successfully: {response.name}")`What's next
-----------

To search and filter code samples for other Google Cloud products, see the
 Google Cloud sample browser.
 

Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.

* ### Why Google


	Choosing Google CloudTrust and securityOpen cloudMulticloudGlobal infrastructureCustomers and case studiesAnalyst reportsWhitepapersBlog
* ### Products and pricing


	Google Cloud pricingGoogle Workspace pricingSee all products
* ### Solutions


	Infrastructure modernizationDatabasesApplication modernizationSmart analyticsArtificial IntelligenceSecurityProductivity & work transformationIndustry solutionsDevOps solutionsSmall business solutionsSee all solutions
* ### Resources


	Google Cloud documentationGoogle Cloud quickstartsGoogle Cloud MarketplaceLearn about cloud computingSupportCode samplesCloud Architecture CenterTrainingCertificationsGoogle for DevelopersGoogle Cloud for StartupsSystem statusRelease Notes
* ### Engage


	Contact salesFind a PartnerBecome a PartnerEventsPodcastsDeveloper CenterPress CornerGoogle Cloud on YouTubeGoogle Cloud Tech on YouTubeFollow on XJoin User ResearchWe're hiring. Join Google Cloud!Google Cloud Community

About GooglePrivacySite termsGoogle Cloud termsManage cookiesOur third decade of climate action: join us* Sign up for the Google Cloud newsletterSubscribe
EnglishDeutschEspañol – América LatinaFrançaisIndonesiaItalianoPortuguês – Brasil中文 – 简体日本語한국어



Documentation Source:
cloud.google.com/bigquery/docs/samples/bigqueryconnection-quickstart.md

Documentation Title:
List connections  |  BigQuery  |  Google Cloud

Documentation Content:
For more information, see the
 BigQuery PythonAPI
 reference documentation.
 
 

To authenticate to BigQuery, set up Application Default Credentials.
 For more information, see
 
 Set up authentication for client libraries.
 
 

`from google.cloud import bigquery_connection_v1 as bq_connection


def main(
 project_id: str = "your-project-id", location: str = "US", transport: str = "grpc"
) -> None:
 """Prints details and summary information about connections for a given admin project and location"""
 client = bq_connection.ConnectionServiceClient(transport=transport)
 print(f"List of connections in project {project_id} in location {location}")
 req = bq_connection.ListConnectionsRequest(
 parent=client.common_location_path(project_id, location)
 )
 for connection in client.list_connections(request=req):
 print(f"\tConnection {connection.friendly_name} ({connection.name})")`What's next
-----------

To search and filter code samples for other Google Cloud products, see the
 Google Cloud sample browser.
 

Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 4.0 License, and code samples are licensed under the Apache 2.0 License. For details, see the Google Developers Site Policies. Java is a registered trademark of Oracle and/or its affiliates.

* ### Why Google


	Choosing Google CloudTrust and securityOpen cloudMulticloudGlobal infrastructureCustomers and case studiesAnalyst reportsWhitepapersBlog
* ### Products and pricing


	Google Cloud pricingGoogle Workspace pricingSee all products
* ### Solutions


	Infrastructure modernizationDatabasesApplication modernizationSmart analyticsArtificial IntelligenceSecurityProductivity & work transformationIndustry solutionsDevOps solutionsSmall business solutionsSee all solutions
* ### Resources


	Google Cloud documentationGoogle Cloud quickstartsGoogle Cloud MarketplaceLearn about cloud computingSupportCode samplesCloud Architecture CenterTrainingCertificationsGoogle for DevelopersGoogle Cloud for StartupsSystem statusRelease Notes
* ### Engage



Documentation Source:
cloud.google.com/bigquery/docs/reference/bigqueryconnection/rpc/google.cloud.bigquery.connection-2.md

Documentation Title:
Package google.cloud.bigquery.connection.v1beta1  |  BigQuery  |  Google Cloud

Documentation Content:
Fields ||`instance_id` `string`Cloud SQL instance ID in the form `project:location:instance`. |
| --- |
|`database` `string`Database name. |
|`type` DatabaseTypeType of the Cloud SQL database. |
|`credential` CloudSqlCredentialInput only. Cloud SQL credential. |
|`service_account_id` `string`Output only. The account ID of the service used for the purpose of this connection.When the connection is used in the context of an operation in BigQuery, this service account will serve as the identity being used for connecting to the CloudSQL instance specified in this connection. |

DatabaseType
------------

Supported Cloud SQL database types.



 Enums ||`DATABASE_TYPE_UNSPECIFIED` Unspecified database type. |
| --- |
|`POSTGRES` Cloud SQL for PostgreSQL. |
|`MYSQL` Cloud SQL for MySQL. |

Connection
----------

Configuration parameters to establish connection with an external data source, except the credential attributes.



 Fields ||`name` `string`The resource name of the connection in the form of: `projects/{project_id}/locations/{location_id}/connections/{connection_id}` |
| --- |
|`friendly_name` `string`User provided display name for the connection. |
|`description` `string`User provided description. |
|`creation_time` `int64`Output only. The creation timestamp of the connection. |
|`last_modified_time` `int64`Output only. The last update timestamp of the connection. |
|`has_credential` `bool`Output only. True, if credential is configured for this connection. |
 Union field `properties`. Properties specific to the underlying data source. `properties`can be only one of the following: ||`cloud_sql` CloudSqlPropertiesCloud SQL properties. |

ConnectionCredential
--------------------

Credential to use with a connection.



 Fields | Union field `credential`. Credential specific to the underlying data source. `credential`can be only one of the following: ||`cloud_sql` CloudSqlCredentialCredential for Cloud SQL database. |

CreateConnectionRequest
-----------------------

The request for ConnectionService.CreateConnection.



