Documentation Source:
airbyte.com/tutorials/how-to-use-airflow-and-airbyte-together.md

Documentation Title:
A step-by-step guide to setting up and configuring Airbyte and Airflow to work together | Airbyte

Documentation Content:
Get the **connectionId**from the URL shown in your browser as annotated in the following image: 

!

Get the Airbyte connection ID

‍

You can use cURLto verify that Airbyte’s API endpoint is working as expected. Be sure to update the **connectionID**in the following command to reflect the value extracted from the URL above. Execute a call to the REST API as follows:

`curl -u 'airbyte:password' -X POST "http://localhost:8000/api/v1/connections/sync" \
 -H "Accept: application/json"\
 -H "Content-Type: application/json" \
 -d '{"connectionId":"[REPLACE WITH YOUR CONNECTION ID]"}'`The above command should respond with the following, which indicates that a Sync has started:

`{"job":{"id":303,"configType":"sync","configId":"1ab174f8-fa2c-4204-9442-2900be4fd28a","createdAt":1675690032,"updatedAt":1675690032,"status":"running"},"attempts":[{"attempt":{"id":0,"status":"running","createdAt":1675690032,"updatedAt":1675690032},"logs":{"logLines":[]}}]}%`If you look in the UI, you will see that a sync executes each time that you run the cURL command. In my case I have executed the command twice within a minute of each other, and so my UI looks as follows:

!

View the Sync History

Install and Launch Airflow
--------------------------

Now that you have verified that the REST endpoint is functioning as expected, we’ll start working with Airflow, which will trigger that same Airbyte API endpoint to execute a sync. The instructions for this section are based on Running Airflow in Docker, with additional information about how to get the Airbyte providerinstalled.



Documentation Source:
airbyte.com/tutorials/extract-data-from-the-webflow-api.md

Documentation Title:
Build a connector to extract data from the Webflow API | Airbyte

Documentation Content:
Update the configuration file

In order to validate connectivity to the API, the *check*functionality must be supplied with input values for the fields specified in *spec.yaml*– because you are still running Airbyte without the full UI functionality, the input parameters will be passed in via a configuration file for now. In the Webflow source connector directory, the *secrets/config.json*file will look as follows: 

`{
 "site_id": "",
 "api_key": ""
}`‍

You can get your *site\_id*and *api\_key*as instructed in the Webflow source documentation. Next, verify that the configuration conforms to your *spec.yaml*by executing the following command from the Webflow source connector directory:

`python main.py check --config secrets/config.json`‍

Which should respond with the following:

`{"type": "LOG", "log": {"level": "INFO", "message": "Check succeeded"}}
{"type": "CONNECTION_STATUS", "connectionStatus": {"status": "SUCCEEDED"}}`‍

If you look at the default implementation of the *check\_connection*method in your local copy of *source.py*, you will see that it returns *True*, *None*regardless of the status of the connection – in other words, the connection to Webflow hasn’t actually been verified yet.



Documentation Source:
airbyte.com/tutorials/extract-data-from-the-webflow-api.md

Documentation Title:
Build a connector to extract data from the Webflow API | Airbyte

Documentation Content:
Import your connector into a locally running Airbyte UI

If you have not previously done so, you can start Airbyte by switching to the root Airbyte directory (in my case */Users/arm/Documents/airbyte-webflow-source/*) and then run the following: 

`docker compose up`‍

After a few minutes, you will be able to connect to http://localhost:8000in your browser, and should be able to import the new connector into your locally running Airbyte. Go to *Settings → Sources  → + New connector*as shown below.

‍

!‍

From here you should be able to enter in the information about the docker container that you created as shown in the pop-up below, and by then pressing the *Add*button. 

‍

!‍

You should now be able to create a new *connection*(source connector + destination connector) that uses your Webflow source connector, by clicking in the UI as demonstrated below:

‍

!‍

Select the Webflow connector that you created as follows. 

!And from there you will be requested to enter in the *Site id*and *API token*as follows: 

‍

!Once the source has been created you will be asked to select a destination. You may wish to export Webflow data to a local CSV file, backup Webflow data into S3, or extract Webflow data to send into BigQuery, etc. – the list of supported destinationsis long and growing. 

Below I show how to replicate Webflow collections to a local json file.

!‍

This tells Airbyte to output json data to */tmp/airbyte\_local/webflow-blog-test*. You will then be presented with a screen that allows you to configure the connection parameters as follows:

!Notice that there are many stream names available, all of which were **dynamically generated based on the collections that are available in Webflow**. Using the switch on the left side allows you to specify which of these streams you are interested in replicating to your output. For this demonstration, you may leave all settings with their default value, and then click on the *Set up connection*button in the bottom right corner.



Documentation Source:
airbyte.com/docs.airbyte.com/connector-development/connector-builder-ui/tutorial.md

Documentation Title:
Tutorial | Airbyte Documentation

Documentation Content:
Setting up global configuration​

On the "global configuration" page, general settings applying to all streams are configured - the base URL that requests are sent to, as well as configuration for how to authenticate with the API server.

* Set the base URL to `https://api.apilayer.com`
* Select the "API Key" authentication method
* Set the "Header" to `apikey`

The actual API Key you copied from apilayer.com will not be part of the connector itself - instead it will be set as part of the source configuration when configuring a connection based on your connector in a later step.

You can find more information about authentication method on the authentication concept page.



