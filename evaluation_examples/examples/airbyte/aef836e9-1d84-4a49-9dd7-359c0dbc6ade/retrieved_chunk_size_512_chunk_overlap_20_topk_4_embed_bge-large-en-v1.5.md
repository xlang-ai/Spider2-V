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
airbyte.com/docs.airbyte.com/integrations/destinations/snowflake.md

Documentation Title:
Snowflake | Airbyte Documentation

Documentation Content:
2.3 | 2023-10-17 |#31191 Improve typing+deduping performance by filtering new raw records on extracted\_at |
| 3.2.2 | 2023-10-10 |#31194 Deallocate unused per stream buffer memory when empty |
| 3.2.1 | 2023-10-10 |#31083 Fix precision of numeric values in async destinations |
| 3.2.0 | 2023-10-09 |#31149 No longer fail syncs when PKs are null - try do dedupe anyway |
| 3.1.22 | 2023-10-06 |#31153 Increase jvm GC retries |
| 3.1.21 | 2023-10-06 |#31139 Bump CDK version |
| 3.1.20 | 2023-10-06 |#31129 Reduce async buffer size |
| 3.1.19 | 2023-10-04 |#31082 Revert null PK checks |
| 3.1.18 | 2023-10-01 |#30779 Final table PK columns become non-null and skip check for null PKs in raw records (performance) |
| 3.1.17 | 2023-09-29 |#30938 Upgrade snowflake-jdbc driver |
| 3.1.16 | 2023-09-28 |#30835 Fix regression from 3.1.15 in supporting concurrent syncs with identical stream name but different namespace |
| 3.1.15 | 2023-09-26 |#30775 Increase async block size |
| 3.1.14 | 2023-09-27 |#30739 Fix column name collision detection |
| 3.1.13 | 2023-09-19 |#30599 Support concurrent syncs with identical stream name but different namespace |
| 3.1.12 | 2023-09-21 |#30671 Reduce async buffer size |
| 3.1.11 | 2023-09-19 |#30592 Internal code changes |
| 3.1.



