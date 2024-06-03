Documentation Source:
cloud.google.com/bigquery/docs/external-data-drive.md

Documentation Title:
Create Google Drive external tables  |  BigQuery  |  Google Cloud

Documentation Content:
dataset_id = "your-project.your_dataset"



Documentation Source:
cloud.google.com/bigquery/docs/samples/bigquery-pandas-gbq-to-gbq-simple.md

Documentation Title:
Load a DataFrame to BigQuery with pandas-gbq  |  Google Cloud

Documentation Content:
project_id = "my-project"



Documentation Source:
cloud.google.com/bigquery/docs/samples/bigquery-load-table-clustered.md

Documentation Title:
Clustered table  |  BigQuery  |  Google Cloud

Documentation Content:
/**
 * TODO(developer): Uncomment the following lines before running the sample.
 */
 // const datasetId = "my_dataset";
 // const tableId = "my_table";

 const metadata = {
 sourceFormat: 'CSV',
 skipLeadingRows: 1,
 schema: {
 fields: [
 {name: 'timestamp', type: 'TIMESTAMP'},
 {name: 'origin', type: 'STRING'},
 {name: 'destination', type: 'STRING'},
 {name: 'amount', type: 'NUMERIC'},
 ],
 },
 clustering: {
 fields: ['origin', 'destination'],
 },
 };

 // Load data from a Google Cloud Storage file into the table
 const [job] = await bigquery
 .dataset(datasetId)
 .table(tableId)
 .load(storage.bucket(bucketName).file(filename), metadata);

 // load() waits for the job to finish
 console.log(`Job ${job.id} completed.`);
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



Documentation Source:
cloud.google.com/bigquery/docs/batch-loading-data.md

Documentation Title:
Batch loading data  |  BigQuery  |  Google Cloud

Documentation Content:
The following code demonstrates how to load a local CSV file to a new
BigQuery table. To load a local file of another format, set
the sourceFormatto the appropriate format.`use Google\Cloud\BigQuery\BigQueryClient;
use Google\Cloud\Core\ExponentialBackoff;

/** Uncomment and populate these variables in your code */
// $projectId = 'The Google project ID';
// $datasetId = 'The BigQuery dataset ID';
// $tableId = 'The BigQuery table ID';
// $source = 'The path to the CSV source file to import';

// instantiate the bigquery table service
$bigQuery = new BigQueryClient([
 'projectId' => $projectId,
]);
$dataset = $bigQuery->dataset($datasetId);
$table = $dataset->table($tableId);
// create the import job
$loadConfig = $table->load(fopen($source, 'r'))->sourceFormat('CSV');

$job = $table->runJob($loadConfig);
// poll the job until it is complete
$backoff = new ExponentialBackoff(10);
$backoff->execute(function () use ($job) {
 printf('Waiting for job to complete' . PHP_EOL);
 $job->reload();
 if (!$job->isComplete()) {
 throw new Exception('Job has not yet completed', 500);
 }
});
// check if the job has errors
if (isset($job->info()['status']['errorResult'])) {
 $error = $job->info()['status']['errorResult']['message'];
 printf('Error running job: %s' . PHP_EOL, $error);
} else {
 print('Data imported successfully' . PHP_EOL);
}`### Python

Before trying this sample, follow the Pythonsetup instructions in the
 BigQuery quickstart using
 client libraries.
 
 
 
 For more information, see the
 BigQuery PythonAPI
 reference documentation.
 
 

To authenticate to BigQuery, set up Application Default Credentials.
 For more information, see
 
 Set up authentication for client libraries.
 
 

The following code demonstrates how to load a local CSV file to a new
BigQuery table. To load a local file of another format, set
the LoadJobConfig.source\_format
propertyto the appropriate format.`from google.cloud import bigquery



