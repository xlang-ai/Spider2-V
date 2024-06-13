Documentation Source:
docs.snowflake.com/en/sql-reference/sql/drop-table.md

Documentation Title:
DROP TABLE | Snowflake Documentation

Documentation Content:
```
SHOWTABLESLIKE't2%';+---------------------------------+------+---------------+-------------+-----------+------------+------------+------+-------+--------------+----------------+| created_on                      | name | database_name | schema_name | kind      | comment    | cluster_by | rows | bytes | owner        | retention_time ||---------------------------------+------+---------------+-------------+-----------+------------+------------+------+-------+--------------+----------------+| Tue, 17 Mar 2015 16:48:16 -0700 | T2   | TESTDB        | PUBLIC      | TABLE     |            |            |    5 | 4096  | PUBLIC       |              1 |+---------------------------------+------+---------------+-------------+-----------+------------+------------+------+-------+--------------+----------------+DROPTABLEt2;+--------------------------+| status                   ||--------------------------|| T2 successfully dropped. |+--------------------------+SHOWTABLESLIKE't2%';+------------+------+---------------+-------------+------+---------+------------+------+-------+-------+----------------+| created_on | name | database_name | schema_name | kind | comment | cluster_by | rows | bytes | owner | retention_time ||------------+------+---------------+-------------+------+---------+------------+------+-------+-------+----------------|+------------+------+---------------+-------------+------+---------+------------+------+-------+-------+----------------+
```
CopyDrop the table again, but don’t raise an error if the table does not exist:


```
DROPTABLEIFEXISTSt2;+------------------------------------------------------------+| status                                                     ||------------------------------------------------------------|| Drop statement executed successfully (T2 already dropped). |+------------------------------------------------------------+
```
CopyWas this page helpful?

YesNoVisit SnowflakeJoin the conversationDevelop with SnowflakeShare your feedbackRead the latest on our blogGet your own certificationPrivacy NoticeSite Terms© 2024Snowflake, Inc. All Rights Reserved.On this page

SyntaxParametersUsage notesExamplesLanguage: **English**EnglishFrançaisDeutsch日本語한국어Português



Documentation Source:
docs.snowflake.com/en/sql-reference/sql/drop-schema.md

Documentation Title:
DROP SCHEMA | Snowflake Documentation

Documentation Content:
```
DROPSCHEMAmyschema;+--------------------------------+| status                         ||--------------------------------|| MYSCHEMA successfully dropped. |+--------------------------------+SHOWSCHEMAS;+---------------------------------+--------------------+------------+------------+---------------+--------+-----------------------------------------------------------+---------+----------------+| created_on                      | name               | is_default | is_current | database_name | owner  | comment                                                   | options | retention_time ||---------------------------------+--------------------+------------+------------+---------------+--------+-----------------------------------------------------------+---------+----------------|| Fri, 13 May 2016 17:26:07 -0700 | INFORMATION_SCHEMA | N          | N          | MYTESTDB      |        | Views describing the contents of schemas in this database |         |              1 || Tue, 17 Mar 2015 16:57:04 -0700 | PUBLIC             | N          | Y          | MYTESTDB      | PUBLIC |                                                           |         |              1 |+---------------------------------+--------------------+------------+------------+---------------+--------+-----------------------------------------------------------+---------+----------------+
```
CopyWas this page helpful?

YesNoVisit SnowflakeJoin the conversationDevelop with SnowflakeShare your feedbackRead the latest on our blogGet your own certificationPrivacy NoticeSite Terms© 2024Snowflake, Inc. All Rights Reserved.On this page

SyntaxParametersUsage notesExamplesLanguage: **English**EnglishFrançaisDeutsch日本語한국어Português



Documentation Source:
docs.snowflake.com/en/sql-reference/sql/undrop-schema.md

Documentation Title:
UNDROP SCHEMA | Snowflake Documentation

Documentation Content:
```
UNDROPSCHEMAmyschema;+----------------------------------------+| status                                 ||----------------------------------------|| Schema MYSCHEMA successfully restored. |+----------------------------------------+SHOWSCHEMASHISTORY;+---------------------------------+--------------------+------------+------------+---------------+--------+-----------------------------------------------------------+---------+----------------+------------+| created_on                      | name               | is_default | is_current | database_name | owner  | comment                                                   | options | retention_time | dropped_on ||---------------------------------+--------------------+------------+------------+---------------+--------+-----------------------------------------------------------+---------+----------------+------------|| Fri, 13 May 2016 17:26:07 -0700 | INFORMATION_SCHEMA | N          | N          | MYTESTDB      |        | Views describing the contents of schemas in this database |         |              1 | [NULL]     || Tue, 17 Mar 2015 17:18:42 -0700 | MYSCHEMA           | N          | N          | MYTESTDB      | PUBLIC |                                                           |         |              1 | [NULL]     || Tue, 17 Mar 2015 16:57:04 -0700 | PUBLIC             | N          | Y          | MYTESTDB      | PUBLIC |                                                           |         |              1 | [NULL]     |+---------------------------------+--------------------+------------+------------+---------------+--------+-----------------------------------------------------------+---------+----------------+------------+
```
CopyWas this page helpful?

YesNoVisit SnowflakeJoin the conversationDevelop with SnowflakeShare your feedbackRead the latest on our blogGet your own certificationPrivacy NoticeSite Terms© 2024Snowflake, Inc. All Rights Reserved.On this page

SyntaxParametersUsage notesExamplesLanguage: **English**EnglishFrançaisDeutsch日本語한국어Português



Documentation Source:
docs.snowflake.com/en/sql-reference/info-schema/table_storage_metrics.md

Documentation Title:
TABLE_STORAGE_METRICS View | Snowflake Documentation

Documentation Content:
|TABLE\_CREATED

TIMESTAMP\_LTZ

Date and time at which the table was created.


|TABLE\_DROPPED

TIMESTAMP\_LTZ

Date and time at which the table was dropped. NULL if table has not been dropped.


|TABLE\_ENTERED\_FAILSAFE

TIMESTAMP\_LTZ

Date and time at which the table, if dropped, entered the Fail-safe state, or NULL. In this state, the table cannot be restored using UNDROP.


|CATALOG\_CREATED

TIMESTAMP\_LTZ

Date and time at which the database containing the table was created.


|CATALOG\_DROPPED

TIMESTAMP\_LTZ

Date and time at which the database containing the table was dropped.


|SCHEMA\_CREATED

TIMESTAMP\_LTZ

Date and time at which the schema containing the table was created.


|SCHEMA\_DROPPED

TIMESTAMP\_LTZ

Date and time at which the schema containing the table was dropped.


|COMMENT

TEXT

Comment for the table.



Usage Notes¶
------------

There may be a 1-2 hour delay in updating storage related statistics for active\_bytes, time\_travel\_bytes,
failsafe\_bytes, and retained\_for\_clone\_bytes.

* ID and CLONE\_GROUP\_ID:



