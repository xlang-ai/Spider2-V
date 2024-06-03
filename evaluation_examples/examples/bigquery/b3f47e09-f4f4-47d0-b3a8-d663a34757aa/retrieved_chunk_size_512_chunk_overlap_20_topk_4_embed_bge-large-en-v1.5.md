Documentation Source:
cloud.google.com/bigquery/docs/inference-tutorial-resnet.md

Documentation Title:
Tutorial: Run inference on an object table by using a classification model  |  BigQuery  |  Google Cloud

Documentation Content:
listingsMonitor BI EngineMonitor data qualityMonitor Data Transfer ServiceMonitor materialized viewsMonitor reservationsDashboards, charts and alertsAudit workloadsIntroductionAudit policy tagsView Data Policy audit logsData Transfer Service audit logsAnalytics Hub audit loggingBigQuery audit logs referenceMigrate audit logsBigLake API audit logsOptimize resourcesControl costsEstimate and control query costsCustom cost controlsOptimize with recommendationsView cluster and partition recommendationsApply cluster and partition recommendationsManage materialized view recommendationsOrganize with labelsIntroductionAdd labelsView labelsUpdate labelsFilter using labelsDelete labelsManage data qualityMonitor data quality with scansData Catalog overviewWork with Data CatalogGovernIntroductionControl access to resourcesIntroductionControl access to resources with IAMControl access with authorizationAuthorized datasetsAuthorized routinesAuthorized viewsControl access with VPC service controlsControl table and dataset access with tagsControl access with conditionsControl column and row accessControl access to table columnsIntroduction to column-level access controlRestrict access with column-level access controlImpact on writesManage policy tagsManage policy tags across locationsBest practices for using policy tagsControl access to table rowsIntroduction to row-level securityWork with row-level securityUse row-level security with other BigQuery featuresBest practices for row-level securityProtect sensitive dataMask data in table columnsIntroduction to data maskingMask column dataAnonymize data with differential privacyUse differential privacyExtend differential privacyRestrict data access using analysis rulesUse Sensitive Data ProtectionManage encryptionEncryption at restCustomer-managed encryption keysColumn-level encryption with Cloud KMSAEAD encryptionDevelopIntroductionBigQuery code samplesBigQuery API basicsBigQuery APIs and libraries overviewAuthenticationIntroductionGet startedAuthenticate as an end userAuthenticate with JSON Web TokensRun jobs programmaticallyPaginate with BigQuery APIAPI performance tipsBatch requestsChoose a Python libraryBigQuery DataFramesIntroductionUse BigQuery DataFramesUse ODBC and JDBC driversAI solutions, generative AI, and ML
 Application development
 Application hosting
 Compute
 Data analytics and pipelines
 Databases
 Distributed, hybrid, and multicloud
 Industry solutions
 Networking
 Observability and monitoring
 Security
 Storage
 Access and resources management
 Cloud SDK, languages, frameworks,



Documentation Source:
cloud.google.com/bigquery/docs/reference/standard-sql/window-function-calls.md

Documentation Title:
Window function calls  |  BigQuery  |  Google Cloud

Documentation Content:
* (banana, **apple**, **leek**, **cabbage**, **lettuce**, **kale**) = 54 total purchases
* (**banana**, apple, **leek**, **cabbage**, **lettuce**, **kale**) = 54 total purchases
* (**banana**, **apple**, leek, **cabbage**, **lettuce**, **kale**) = 54 total purchases
* (**banana**, **apple**, **leek**, cabbage, **lettuce**, **kale**) = 54 total purchases
* (**banana**, **apple**, **leek**, **cabbage**, lettuce, **kale**) = 54 total purchases
* (**banana**, **apple**, **leek**, **cabbage**, **lettuce**, kale) = 54 total purchases

`SELECT item, purchases, category, SUM(purchases)
 OVER () AS total_purchases
FROM Produce

/*-------------------------------------------------------*
 | item | purchases | category | total_purchases |
 +-------------------------------------------------------+
 | banana | 2 | fruit | 54 |
 | leek | 2 | vegetable | 54 |
 | apple | 8 | fruit | 54 |
 | cabbage | 9 | vegetable | 54 |
 | lettuce | 10 | vegetable | 54 |
 | kale | 23 | vegetable | 54 |
 *-------------------------------------------------------*/`### Compute a subtotal

This computes a subtotal for each category in the
`Produce`table.



Documentation Source:
cloud.google.com/bigquery/docs/analyze-data-tableau.md

Documentation Title:
Quickstart: Analyze BigQuery data with BI Engine and Tableau  |  BigQuery: Cloud Data Warehouse  |  Google Cloud

Documentation Content:
Insights table schemaProduct Inventory table schemaProduct Targeting table schemaProducts table schemaRegional Inventories table schemaTop Brands table schemaTop Products table schemaGoogle PlaySchedule transfersTransfer report transformationOracleSchedule transfersSalesforceSchedule transfersSalesforce Marketing CloudSchedule transfersSearch Ads 360Schedule transfersTransfer report transformationMigration guideServiceNowSchedule transfersYouTube channelSchedule transfersTransfer report transformationYouTube content ownerSchedule transfersTransfer report transformationBatch load dataIntroductionLoad Avro dataLoad Parquet dataLoad ORC dataLoad CSV dataLoad JSON dataLoad externally partitioned dataLoad data from a Datastore exportLoad data from a Firestore exportLoad data using the Storage Write APILoad data into partitioned tablesWrite and read data with the Storage APIRead data with the Storage Read APIWrite data with the Storage Write APIIntroductionStream data with the Storage Write APIBatch load data with the Storage Write APIBest practicesStream updates with change data captureUse the legacy streaming APILoad data from other Google servicesLoad data using third-party appsLoad data using cross-cloud operationsTransform dataIntroductionTransform with DMLTransform data in partitioned tablesWork with change historyExport dataExport to fileExport to Cloud StorageExport to BigtableExport as Protobuf columnsAnalyzeIntroductionQuery BigQuery dataRun a queryAnalyze with a data canvasWrite queries with GeminiWrite query resultsGenerate profile insightsGenerate data insightsQuery data with SQLIntroductionArraysJSON dataSketchesMulti-statement queriesRecursive CTEsTable samplingTime seriesTransactionsSaved queriesIntroductionCreate saved queriesUse cached resultsRun parameterized queriesQuery with wildcard tablesAccess historical dataSchedule queriesTroubleshoot queriesOptimize queriesIntroductionUse the query plan explanationGet query performance insightsOptimize query computationUse history-based optimizationsOptimize storageUse BI EngineUse nested and repeated dataOptimize functionsQuery external data sourcesManage open source metadataUse external tables and datasetsAmazon S3 dataQuery Amazon S3 dataExport query results to Amazon S3Query Apache Iceberg dataQuery open table formats with manifestsAzure Blob Storage dataQuery Azure Blob Storage dataExport query results to Azure Blob StorageQuery Cloud Bigtable dataCloud Storage dataQuery Cloud Storage data in BigLake tablesQuery Cloud Storage data in external tablesWork with Salesforce Data Cloud dataQuery Google Drive dataCreate AWS Glue federated datasetsRun federated queriesFederated queriesQuery SAP Datasphere dataQuery Cloud



Documentation Source:
cloud.google.com/bigquery/docs/inference-tutorial-resnet.md

Documentation Title:
Tutorial: Run inference on an object table by using a classification model  |  BigQuery  |  Google Cloud

Documentation Content:
table schemaProducts table schemaRegional Inventories table schemaTop Brands table schemaTop Products table schemaGoogle PlaySchedule transfersTransfer report transformationOracleSchedule transfersSalesforceSchedule transfersSalesforce Marketing CloudSchedule transfersSearch Ads 360Schedule transfersTransfer report transformationMigration guideServiceNowSchedule transfersYouTube channelSchedule transfersTransfer report transformationYouTube content ownerSchedule transfersTransfer report transformationBatch load dataIntroductionLoad Avro dataLoad Parquet dataLoad ORC dataLoad CSV dataLoad JSON dataLoad externally partitioned dataLoad data from a Datastore exportLoad data from a Firestore exportLoad data using the Storage Write APILoad data into partitioned tablesWrite and read data with the Storage APIRead data with the Storage Read APIWrite data with the Storage Write APIIntroductionStream data with the Storage Write APIBatch load data with the Storage Write APIBest practicesStream updates with change data captureUse the legacy streaming APILoad data from other Google servicesLoad data using third-party appsLoad data using cross-cloud operationsTransform dataIntroductionTransform with DMLTransform data in partitioned tablesWork with change historyExport dataExport to fileExport to Cloud StorageExport to BigtableExport as Protobuf columnsAnalyzeIntroductionQuery BigQuery dataRun a queryAnalyze with a data canvasWrite queries with GeminiWrite query resultsGenerate profile insightsGenerate data insightsQuery data with SQLIntroductionArraysJSON dataSketchesMulti-statement queriesRecursive CTEsTable samplingTime seriesTransactionsSaved queriesIntroductionCreate saved queriesUse cached resultsRun parameterized queriesQuery with wildcard tablesAccess historical dataSchedule queriesTroubleshoot queriesOptimize queriesIntroductionUse the query plan explanationGet query performance insightsOptimize query computationUse history-based optimizationsOptimize storageUse BI EngineUse nested and repeated dataOptimize functionsQuery external data sourcesManage open source metadataUse external tables and datasetsAmazon S3 dataQuery Amazon S3 dataExport query results to Amazon S3Query Apache Iceberg dataQuery open table formats with manifestsAzure Blob Storage dataQuery Azure Blob Storage dataExport query results to Azure Blob StorageQuery Cloud Bigtable dataCloud Storage dataQuery Cloud Storage data in BigLake tablesQuery Cloud Storage data in external tablesWork with Salesforce Data Cloud dataQuery Google Drive dataCreate AWS Glue federated datasetsRun federated queriesFederated queriesQuery SAP Datasphere dataQuery Cloud Spanner dataQuery Cloud SQL dataAnalyze unstructured dataRun



