Documentation Source:
airbyte.com/tutorials/building-an-e-commerce-data-pipeline-a-hands-on-guide-to-using-airbyte-dbt-dagster-and-bigquery.md

Documentation Title:
How to build E-commerce Data Pipeline with Airbyte? | Airbyte

Documentation Content:
1. Create a source:

* Go to the Sources tab and click on "+ New source".
* Search for “faker” using the search bar and select "Sample Data (Faker)".
* Adjust the Count and optional fields as needed for your use case. You can also leave as is.
* Click on "Set up source".

!

Look fo Faker source connector

!

Create a Faker source



Documentation Source:
airbyte.com/quickstart/e-commerce-analytics-with-airbyte-dbt-dagster-and-bigquery.md

Documentation Title:
E-commerce Analytics Stack with Airbyte, dbt, Dagster and BigQuery | Airbyte

Documentation Content:
**1. Create a source**:

* Go to the Sources tab and click on "+ New source".
* Search for “faker” using the search bar and select "Sample Data (Faker)".
* Adjust the Count and optional fields as needed for your use case. You can also leave as is.
* Click on "Set up source".



Documentation Source:
airbyte.com/quickstart/airbyte-dbt-and-airflow-stack-with-bigquery.md

Documentation Title:
E-commerce Analytics Stack with Airbyte, dbt, Airflow (ADA) and BigQuery | Airbyte

Documentation Content:
3.2. Setting Up Airbyte Connectors Using the UI

Start by launching the Airbyte UI by going to http://localhost:8000/in your browser. Then:

**1. Create a source**:

1. Go to the "Sources" tab and click on "+ New source".
2. Search for “faker” using the search bar and select "Sample Data (Faker)".
3. Adjust the count and optional fields as needed for your use case. You can also leave as is.
4. Click on "Set up source".

**2. Create a destination**:

1. Go to the "Destinations" tab and click on "+ New destination".
2. Search for “bigquery” using the search bar and select BigQuery.
3. Enter the connection details as needed.
4. For simplicity, you can use "Standard Inserts" as the loading method.
5. In the Service Account Key JSON field, enter the contents of the JSON file. Yes, the full JSON.
6. Click on Set up destination.

**3. Create a connection**:

1. Go to the "Connections" tab and click on "+ New connection".
2. Select the source and destination you just created.
3. Enter the connection details as needed.
4. Click on "Set up connection".

That’s it! Your connection is set up and ready to go! 🎉 

4. Setting Up the dbt Project
-----------------------------

dbt (data build tool)allows you to transform your data by writing, documenting, and executing SQL workflows. Setting up the dbt project requires specifying connection details for your data platform, in this case, BigQuery. Here’s a step-by-step guide to help you set this up:



Documentation Source:
airbyte.com/docs.airbyte.com/using-airbyte/getting-started/add-a-source.md

Documentation Title:
Add a Source | Airbyte Documentation

Documentation Content:
Skip to main content!!About AirbyteTutorialsSupportCloud StatusTry Airbyte CloudSearch* Airbyte Connectors
Connector CatalogBuild a ConnectorConnector Support Levels* Using Airbyte
* Getting Started
	Core ConceptsAdd a SourceAdd a DestinationSet up a Connection
Configuring ConnectionsManaging Syncs* Managing Airbyte
Deploy AirbyteSelf-Managed EnterpriseUpgrading AirbyteConfiguring AirbyteAccess ManagementAirbyte at ScaleSecurityIntegrating with AirbyteAccount Management* Developer Guides
API documentationTerraform DocumentationUsing PyAirbyteUnderstand AirbyteContribute to AirbyteLicenses* Community
Getting SupportCode of Conduct* Product Updates
RoadmapRelease Notes
Getting StartedAdd a Source
Add a Source
============

AvailableCloud AvailableSelf-Managed Community (OSS)AvailableSelf-Managed EnterpriseSetting up a new source in Airbyte is a quick and simple process! When viewing the Airbyte UI, you'll see the main navigation bar on the left side of your screen. Click the **Sources**tab to bring up a list of all available sources.

You can use the provided search bar, or simply scroll down the list to find the source you want to replicate data from. Let's use a demo source, Faker, as an example. Clicking on the **Sample Data (Faker)**card will bring us to its setup page.

!The left half of the page contains a set of fields that you will have to fill out. In the **Source name**field, you can enter a name of your choosing to help you identify this instance of the connector. By default, this will be set to the name of the source (ie, `Sample Data (Faker)`).

Each connector in Airbyte will have its own set of authentication methods and configurable parameters. In the case of Sample Data (Faker), you can adjust the number of records you want returned in your `Users`data, and optionally adjust additional configuration settings. You can always refer to your source's provided setup guide for specific instructions on filling out each field.

infoSome sources will have an **Optional Fields**tab. You can open this tab to view and configure any additional optional parameters that exist for the souce, but you do not have to do so to successfully set up the connector.



