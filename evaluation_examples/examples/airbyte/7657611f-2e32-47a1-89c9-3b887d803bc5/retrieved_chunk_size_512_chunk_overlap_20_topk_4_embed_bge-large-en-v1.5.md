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
airbyte.com/docs.airbyte.com/integrations/sources/faker.md

Documentation Title:
Faker | Airbyte Documentation

Documentation Content:
Config fields reference

FieldTypeProperty name›Countintegercount›Seedintegerseed›Records Per Stream Sliceintegerrecords\_per\_slice›Always Updatedbooleanalways\_updated›ParallelismintegerparallelismChangelog​
----------



| Version | Date | Pull Request | Subject |
| --- | --- | --- | --- |
| 6.1.0 | 2024-04-08 |36898 Update car prices and years |
| --- | --- | --- |
| 6.0.3 | 2024-03-15 |36167 Make 'count' an optional config parameter. |
| 6.0.2 | 2024-02-12 |35174 Manage dependencies with Poetry. |
| 6.0.1 | 2024-02-12 |35172 Base image migration: remove Dockerfile and use the python-connector-base image |
| 6.0.0 | 2024-01-30 |34644 Declare 'id' columns as primary keys.



Documentation Source:
airbyte.com/docs.airbyte.com/integrations/sources/faker.md

Documentation Title:
Faker | Airbyte Documentation

Documentation Content:
|
| 5.0.2 | 2024-01-17 |34344 Ensure unique state messages |
| 5.0.1 | 2023-01-08 |34033 Add standard entrypoints for usage with AirbyteLib |
| 5.0.0 | 2023-08-08 |29213 Change all `*id`fields and `products.year`to be integer |
| 4.0.0 | 2023-07-19 |28485 Bump to test publication |
| 3.0.2 | 2023-07-07 |27807 Bump to test publication |
| 3.0.1 | 2023-06-28 |27807 Fix bug with purchase stream updated\_at |
| 3.0.0 | 2023-06-23 |27684 Stream cursor is now `updated_at`& remove `records_per_sync`option |
| 2.1.0 | 2023-05-08 |25903 Add user.address (object) |
| 2.0.3 | 2023-02-20 |23259 bump to test publication |
| 2.0.2 | 2023-02-20 |23259 bump to test publication |
| 2.0.1 | 2023-01-30 |22117 `source-faker`goes beta |
| 2.0.0 | 2022-12-14 | 20492and 20741 | Decouple stream states for better parallelism |
| 1.0.0 | 2022-11-28 |19490 Faker uses the CDK; rename streams to be lower-case (breaking), add determinism to random purchases, and rename |
| 0.2.1 | 2022-10-14 |19197 Emit `AirbyteEstimateTraceMessage` |
| 0.2.0 | 2022-10-14 |18021 Move to mimesis for speed!



Documentation Source:
airbyte.com/docs.airbyte.com/integrations/sources/faker.md

Documentation Title:
Faker | Airbyte Documentation

Documentation Content:
|
| 0.1.8 | 2022-10-12 |17889 Bump to test publish command (2) |
| 0.1.7 | 2022-10-11 |17848 Bump to test publish command |
| 0.1.6 | 2022-09-07 |16418 Log start of each stream |
| 0.1.5 | 2022-06-10 |13695 Emit timestamps in the proper ISO format |
| 0.1.4 | 2022-05-27 |13298 Test publication flow |
| 0.1.3 | 2022-05-27 |13248 Add options for records\_per\_sync and page\_size |
| 0.1.2 | 2022-05-26 |13248 Test publication flow |
| 0.1.1 | 2022-05-26 |13235 Publish for AMD and ARM (M1 Macs) & remove User.birthdate |
| 0.1.0 | 2022-04-12 |11738 The Faker Source is created |

Edit this pagePreviousFacebook Pages Migration GuideNextSample Data (Faker) Migration Guide* Sync overview
	Output schemaFeaturesRequirements
ReferenceChangelog
Was this page helpful?YesNo



