Documentation Source:
docs.snowflake.com/en/user-guide/tutorials/snowflake-in-20minutes.md

Documentation Title:
Snowflake in 20 minutes | Snowflake Documentation

Documentation Content:
Listing the staged files (Optional)¶

You can list the staged files using the LISTcommand.


```
LIST@sf_tuts.public.%emp_basic;
```
CopyThe following is an example result:


```
+--------------------+------+----------------------------------+------------------------------+| name               | size | md5                              | last_modified                ||--------------------+------+----------------------------------+------------------------------|| employees01.csv.gz |  288 | a851f2cc56138b0cd16cb603a97e74b1 | Tue, 9 Jan 2018 15:31:44 GMT || employees02.csv.gz |  288 | 125f5645ea500b0fde0cdd5f54029db9 | Tue, 9 Jan 2018 15:31:44 GMT || employees03.csv.gz |  304 | eafee33d3e62f079a054260503ddb921 | Tue, 9 Jan 2018 15:31:45 GMT || employees04.csv.gz |  304 | 9984ab077684fbcec93ae37479fa2f4d | Tue, 9 Jan 2018 15:31:44 GMT || employees05.csv.gz |  304 | 8ad4dc63a095332e158786cb6e8532d0 | Tue, 9 Jan 2018 15:31:44 GMT |+--------------------+------+----------------------------------+------------------------------+
```
Copy data into target tables¶
-----------------------------

To load your staged data into the target table, execute COPY INTO .

The COPY INTO command uses the virtual warehouse you created
in Create Snowflake objectsto copy files.



Documentation Source:
docs.snowflake.com/en/user-guide/querying-metadata.md

Documentation Title:
Querying Metadata for Staged Files | Snowflake Documentation

Documentation Content:
000 |  2023-02-02 01:31:00.755 +0000| g  | h  || data1.csv.gz      |                        1 | 39ab11bb2cdeacdcdac1234d9 |     2022-08-03 10:15:26.000 |  2023-02-02 01:31:00.778 +0000| a  | b  || data1.csv.gz      |                        2 | 2289aab2abcdeaacaaac348d0 |     2022-09-10 11:15:55.000 |  2023-02-02 01:31:00.778 +0000| c  | d  |+-------------------+--------------------------+---------------------------+-----------------------------+-------------------------------+----+----+SELECTMETADATA$FILENAME,METADATA$FILE_ROW_NUMBER,METADATA$FILE_CONTENT_KEY,METADATA$FILE_LAST_MODIFIED,METADATA$START_SCAN_TIME,t.$1,t.$2FROM@mystage1t;+-------------------+--------------------------+---------------------------+-----------------------------+-------------------------------+-----+------+| METADATA$FILENAME | METADATA$FILE_ROW_NUMBER | METADATA$FILE_CONTENT_KEY | METADATA$FILE_LAST_MODIFIED |      METADATA$START_SCAN_TIME | $1  | $2   ||-------------------+--------------------------+---------------------------+-----------------------------+-------------------------------+-----+------|| data2.csv.gz      |                        1 | aaa11bb2cccccaaaaac1234d9 |     2022-05-01 10:15:57.000 |  2023-02-02 01:31:00.713 +0000| e|f | NULL || data2.csv.gz      |                        2 | aa387aabb2ccedaaaaac123b8 |     2022-05-01 10:05:35.000 |  2023-02-02 01:31:00.755 +0000| g|h | NULL || data1.csv.



Documentation Source:
docs.snowflake.com/en/user-guide/tutorials/snowflake-in-20minutes.md

Documentation Title:
Snowflake in 20 minutes | Snowflake Documentation

Documentation Content:
```
+--------------------+--------+-------------+-------------+-------------+-------------+-------------+------------------+-----------------------+-------------------------+| file               | status | rows_parsed | rows_loaded | error_limit | errors_seen | first_error | first_error_line | first_error_character | first_error_column_name ||--------------------+--------+-------------+-------------+-------------+-------------+-------------+------------------+-----------------------+-------------------------|| employees02.csv.gz | LOADED |           5 |           5 |           1 |           0 | NULL        |             NULL |                  NULL | NULL                    || employees04.csv.gz | LOADED |           5 |           5 |           1 |           0 | NULL        |             NULL |                  NULL | NULL                    || employees05.csv.gz | LOADED |           5 |           5 |           1 |           0 | NULL        |             NULL |                  NULL | NULL                    || employees03.csv.gz | LOADED |           5 |           5 |           1 |           0 | NULL        |             NULL |                  NULL | NULL                    || employees01.csv.gz | LOADED |           5 |           5 |           1 |           0 | NULL        |             NULL |                  NULL | NULL                    |+--------------------+--------+-------------+-------------+-------------+-------------+-------------+------------------+-----------------------+-------------------------+
```
Query loaded data¶
------------------

You can query the data loaded in the emp\_basictable using standard SQLand any supported
functionsand
operators.

You can also manipulate the data, such as updating the loaded data or inserting more data, using standard DML commands.



Documentation Source:
docs.snowflake.com/en/release-notes/2023/7_20.md

Documentation Title:
June 14-15, 2023 — 7.20 Release Notes | Snowflake Documentation

Documentation Content:
Load Files From a Stage Into a Table — *General Availability*¶

With this release, we are pleased to announce the general availability of loading files from a stage into a table by using Snowsight.

For more information, refer to Load a file from a stage into an existing table.

Was this page helpful?

YesNoVisit SnowflakeJoin the conversationDevelop with SnowflakeShare your feedbackRead the latest on our blogGet your own certificationPrivacy NoticeSite Terms© 2024Snowflake, Inc. All Rights Reserved.On this page

New FeaturesSecurity UpdatesSQL UpdatesData Governance UpdatesWeb Interface UpdatesLanguage: **English**EnglishFrançaisDeutsch日本語한국어Português



