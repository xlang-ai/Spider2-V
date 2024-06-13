Documentation Source:
airbyte.com/tutorials/how-to-use-airflow-and-airbyte-together.md

Documentation Title:
A step-by-step guide to setting up and configuring Airbyte and Airflow to work together | Airbyte

Documentation Content:
By default the path that you specify will be located inside **/tmp/airbyte\_local**. In this tutorial I set the destination to **/json\_from\_faker**, which means that the data will be copied to**/tmp/airbyte\_local/json\_from\_faker**on the localhost where Airbyte is running. After specifying the Destination Path, click on Set up destination. 

!

Configure the Local JSON destination

‍

This will take you to a page to set up the connection. Set the replication frequency to **Manual**(since we will use Airflow to trigger Airbyte syncs rather than using Airbyte’s scheduler) and then click on **Set up connection**as highlighted in the image below.

!

Specify connection settings

‍

Trigger a sync from the **Sample Data (faker)**source to the **Local JSON**output by clicking on **Sync now**as highlighted in the image below.

!

Manually trigger a sync from the UI

‍

The sync should take a few seconds, at which point you should see that the sync has succeed as shown below.

!

After the sync has completed

‍

You can now confirm if some sample data has been copied to the expected location. As previously mentioned, for this example the JSON data can be seen in **/tmp/airbyte\_local\_json\_from\_faker**. Because there were three streams generated, the following three JSON files should be available: 

`_airbyte_raw_products.jsonl 
_airbyte_raw_users.jsonl
_airbyte_raw_purchases.jsonl`You have now created a simple example connection in Airbyte which can be manually triggered. A manually triggered connection is ideal for situations where you wish to use an external orchestrator. 

In the next section you will see how to trigger a manual sync on this connection by hitting a REST endpoint directly. After that, you will see how Airflow can be used to hit that same endpoint to trigger synchronizations. 

Test the API endpoints with cURL
--------------------------------

Before using the REST endpoint from within Airflow, it is useful to verify that it is working as expected.



Documentation Source:
airbyte.com/docs.airbyte.com/integrations/sources/faker.md

Documentation Title:
Faker | Airbyte Documentation

Documentation Content:
| Feature | Supported?(Yes/No) | Notes |
| --- | --- | --- |
| Full Refresh Sync | Yes |
| --- | --- |
| Incremental Sync | Yes |
| Namespaces | No |

Of note, if you choose `Incremental Sync`, state will be maintained between syncs, and once you hit
`count`records, no new records will be added.

You can choose a specific `seed`(integer) as an option for this connector which will guarantee that
the same fake records are generated each time. Otherwise, random data will be created on each
subsequent sync.



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
airbyte.com/docs.airbyte.com/integrations/sources/faker.md

Documentation Title:
Faker | Airbyte Documentation

Documentation Content:
io APIStravaStripeSugar CRMSurveyCTOSurveyMonkeySurveySparrowTalkdesk ExploreTempoTeradataThe Guardian APITiDBTikTok MarketingTimelyTMDbTodoistToggl APITPL/3PL CentralTrelloTrustPilotTVMaze ScheduleTwilioTwilio TaskrouterTwitterTyntec SMSTypeformUnleashUS Census APIVantage APIVictorOpsVisma e-conomicVitallyWaiteraidWeatherstackWebflowWhisky HunterWikipedia PageviewsWooCommerceWordpressWorkableWorkrampWrikeXeroXKCDYahoo Finance PriceYandex MetricaYotpoYouniumYouTube AnalyticsZapier Supported StorageZencartZendesk ChatZendesk SellZendesk SunshineZendesk SupportZendesk TalkZenefitsZenloopZoho CRMZoomZuora
	DestinationsCustom or New Connector
Build a ConnectorConnector Support Levels* Using Airbyte
Getting StartedConfiguring ConnectionsManaging Syncs* Managing Airbyte
Deploy AirbyteSelf-Managed EnterpriseUpgrading AirbyteConfiguring AirbyteAccess ManagementAirbyte at ScaleSecurityIntegrating with AirbyteAccount Management* Developer Guides
API documentationTerraform DocumentationUsing PyAirbyteUnderstand AirbyteContribute to AirbyteLicenses* Community
Getting SupportCode of Conduct* Product Updates
RoadmapRelease Notes
Connector CatalogSourcesFaker
On this pageAvailabilityAvailableAirbyte CloudAvailableAirbyte OSSAvailablePyAirbyteSupport LevelCommunityLatest Version6.1.0!Faker
=====

Sync overview​
--------------

The Sample Data (Faker) source generates sample data using the python
`mimesis`package.



