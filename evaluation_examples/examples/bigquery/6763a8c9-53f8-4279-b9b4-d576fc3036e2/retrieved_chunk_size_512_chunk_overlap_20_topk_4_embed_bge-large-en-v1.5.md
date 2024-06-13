Documentation Source:
cloud.google.com/bigquery/docs/samples/bigquery-add-empty-column.md

Documentation Title:
Add an empty column  |  BigQuery  |  Google Cloud

Documentation Content:
table_id = "your-project.your_dataset.your_table_name"

table = client.get_table(table_id) # Make an API request.

original_schema = table.schema
new_schema = original_schema[:] # Creates a copy of the schema.
new_schema.append(bigquery.SchemaField("phone", "STRING"))

table.schema = new_schema
table = client.update_table(table, ["schema"]) # Make an API request.

if len(table.schema) == len(original_schema) + 1 == len(new_schema):
 print("A new column has been added.")
else:
 print("The column has not been added.")`What's next
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
cloud.google.com/bigquery/docs/samples/bigquery-add-empty-column.md

Documentation Title:
Add an empty column  |  BigQuery  |  Google Cloud

Documentation Content:
languages, frameworks, and tools
 Costs and usage management
 Infrastructure as code
 Migration
 Google Cloud Home
 Free Trial and Free Tier
 Architecture Center
 Blog
 Contact Sales
 Google Cloud Developer Center
 Google Developer Center
 Google Cloud Marketplace (in console)
 Google Cloud Marketplace Documentation
 Google Cloud Skills Boost
 Google Cloud Solution Center
 Google Cloud Support
 Google Cloud Tech Youtube Channel
 HomeBigQueryDocumentationSamples
Add an empty column
===================

Stay organized with collections
 Save and categorize content based on your preferences.
 Manually add an empty column.

Explore further
---------------

For detailed documentation that includes this code sample, see the following:
 

Modifying table schemasCode sample
-----------

GoBefore trying this sample, follow the Gosetup instructions in the
 BigQuery quickstart using
 client libraries.
 
 
 
 For more information, see the
 BigQuery GoAPI
 reference documentation.
 
 

To authenticate to BigQuery, set up Application Default Credentials.
 For more information, see
 
 Set up authentication for client libraries.
 
 

`import (
 "context"
 "fmt"

 "cloud.google.com/go/bigquery"
)

// updateTableAddColumn demonstrates modifying the schema of a table to append an additional column.
func updateTableAddColumn(projectID, datasetID, tableID string) error {
 // projectID := "my-project-id"
 // datasetID := "mydataset"
 // tableID := "mytable"
 ctx := context.Background()
 client, err := bigquery.NewClient(ctx, projectID)
 if err != nil {
 return fmt.Errorf("bigquery.NewClient: %w", err)
 }
 defer client.Close()

 tableRef := client.Dataset(datasetID).Table(tableID)
 meta, err := tableRef.Metadata(ctx)
 if err != nil {
 return err
 }
 newSchema := append(meta.Schema,
 &bigquery.FieldSchema{Name: "phone", Type: bigquery.StringFieldType},
 )
 update := bigquery.TableMetadataToUpdate{
 Schema: newSchema,
 }
 if _, err := tableRef.Update(ctx, update, meta.ETag); err != nil {
 return err
 }
 return nil
}`JavaBefore trying this sample, follow the Javasetup instructions in the
 BigQuery quickstart using
 client libraries.



Documentation Source:
cloud.google.com/bigquery/docs/samples/bigquery-add-empty-column.md

Documentation Title:
Add an empty column  |  BigQuery  |  Google Cloud

Documentation Content:
credentials with scopesCreate external table with hive partitioningCreate IAM policyCreate materialized viewCreate table with schemaDelete a datasetDelete a dataset and its contentsDelete a label from a datasetDelete a label from a tableDelete a modelDelete a routineDelete a tableDelete materialized viewDeploy and apply a remote function using BigQuery DataFramesDisable query cacheDownload public table data to DataFrameDownload public table data to DataFrame from the sandboxDownload query results to a GeoPandas GeoDataFrameDownload query results to DataFrameDownload table data to DataFrameDry run queryEnable large resultsExport a modelExport a table to a compressed fileExport a table to a CSV fileExport a table to a JSON fileGenerate text with the BigQuery DataFrames APIGet a modelGet a routineGet dataset labelsGet dataset propertiesGet job propertiesGet table labelsGet table propertiesGet view propertiesGrant view accessImport a local fileInsert GeoJSON dataInsert rows with no IDsInsert WKT dataList by labelList datasetsList jobsList modelsList models using streamingList routinesList tablesLoad a CSV fileLoad a CSV file to replace a tableLoad a CSV file with autodetect schemaLoad a DataFrame to BigQuery with pandas-gbqLoad a JSON fileLoad a JSON file to replace a tableLoad a JSON file with autodetect schemaLoad a Parquet fileLoad a Parquet to replace a tableLoad a table in JSON formatLoad an Avro fileLoad an Avro file to replace a tableLoad an ORC fileLoad an ORC file to replace a tableLoad data from DataFrameLoad data into a column-based time partitioning tableMigration Guide: pandas-gbqMigration Guide: pandas-gbqNamed parametersNamed parameters and provided typesNested repeated schemaPositional parametersPositional parameters and provided typesPreview table dataQuery a clustered tableQuery a column-based time-partitioned tableQuery a tableQuery Bigtable using a permanent tableQuery Bigtable using a temporary tableQuery Cloud Storage with a permanent tableQuery Cloud Storage with a temporary tableQuery materialized viewQuery paginationQuery scriptQuery Sheets with a permanent tableQuery Sheets with a temporary tableQuery with the BigQuery APIRelax a columnRelax a column in a load append jobRelax a column in a query append jobRevoke access to a datasetRun a legacy SQL query with pandas-gbqRun a query and get total rowsRun a query with batch priorityRun



Documentation Source:
cloud.google.com/bigquery/docs/samples/bigquery-add-empty-column.md

Documentation Title:
Add an empty column  |  BigQuery  |  Google Cloud

Documentation Content:
For more information, see the
 BigQuery Node.jsAPI
 reference documentation.
 
 

To authenticate to BigQuery, set up Application Default Credentials.
 For more information, see
 
 Set up authentication for client libraries.
 
 

`// Import the Google Cloud client library and create a client
const {BigQuery} = require('@google-cloud/bigquery');
const bigquery = new BigQuery();

async function addEmptyColumn() {
 // Adds an empty column to the schema.

 /**
 * TODO(developer): Uncomment the following lines before running the sample.
 */
 // const datasetId = 'my_dataset';
 // const tableId = 'my_table';
 const column = {name: 'size', type: 'STRING'};

 // Retrieve current table metadata
 const table = bigquery.dataset(datasetId).table(tableId);
 const [metadata] = await table.getMetadata();

 // Update table schema
 const schema = metadata.schema;
 const new_schema = schema;
 new_schema.fields.push(column);
 metadata.schema = new_schema;

 const [result] = await table.setMetadata(metadata);
 console.log(result.schema.fields);
}`PythonBefore trying this sample, follow the Pythonsetup instructions in the
 BigQuery quickstart using
 client libraries.
 
 
 
 For more information, see the
 BigQuery PythonAPI
 reference documentation.
 
 

To authenticate to BigQuery, set up Application Default Credentials.
 For more information, see
 
 Set up authentication for client libraries.
 
 

`from google.cloud import bigquery



