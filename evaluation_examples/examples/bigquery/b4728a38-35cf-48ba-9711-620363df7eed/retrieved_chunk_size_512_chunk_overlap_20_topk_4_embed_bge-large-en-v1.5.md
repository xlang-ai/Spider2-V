Documentation Source:
cloud.google.com/bigquery/docs/default-values.md

Documentation Title:
Specify default column values  |  BigQuery  |  Google Cloud

Documentation Content:
```
+------+-------+
| a    | b     |
+------+-------+
| val1 | hello |
| val2 | hello |
+------+-------+

```
If a column has type `STRUCT`, then you must set the default value for the
entire `STRUCT`field. You cannot set the default value for a subset of the
fields. The
default value for an array cannot be `NULL`or contain any `NULL`elements.
The following example creates a table called `complex_table`and sets a
default value for the column `struct_col`, which contains nested fields,
including an `ARRAY`type:


```
CREATE TABLE mydataset.complex_table (
  struct_col STRUCT, y ARRAY>
    DEFAULT ((CURRENT_TIMESTAMP(), NULL),
             [DATE '2022-01-01', CURRENT_DATE()])
);

```
You can't set default values that violate a constraint on the column, such as
a default value that doesn't conform to a
parameterized typeor a `NULL`default value when the column's modeis `REQUIRED`.

Change default values
---------------------

To change the default value for a column, select one of the following options:



Documentation Source:
cloud.google.com/bigquery/docs/default-values.md

Documentation Title:
Specify default column values  |  BigQuery  |  Google Cloud

Documentation Content:
Console

1. In the Google Cloud console, go to the **BigQuery**page.

Go to BigQuery
In the **Explorer**panel, expand your project and dataset, then select
the table.

In the details panel, click the **Schema**tab.

Click **Edit schema**. You might need to scroll to see this button.

In the **Current schema**page, locate the top-level field that you want
to change.

Enter the default value for that field.

Click **Save**.



Documentation Source:
cloud.google.com/bigquery/docs/default-values.md

Documentation Title:
Specify default column values  |  BigQuery  |  Google Cloud

Documentation Content:
Console

1. In the Google Cloud console, go to the **BigQuery**page.

Go to BigQuery
In the **Explorer**panel, expand your project and dataset, then select
the table.

In the details panel, click the **Schema**tab.

Click **Edit schema**. You might need to scroll to see this button.

In the **Current schema**page, locate the top-level field that you want
to change.

Enter `NULL`for the default value.

Click **Save**.



Documentation Source:
cloud.google.com/bigquery/docs/default-values.md

Documentation Title:
Specify default column values  |  BigQuery  |  Google Cloud

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
 HomeBigQueryDocumentationGuides
Send feedback
 
 Stay organized with collections
 Save and categorize content based on your preferences.
 Specify default column values
=============================

This page describes how to set a default value for a column in a
BigQuery table. When you add a row to a table that doesn't contain
data for a column with a default value, the default value is written to the
column instead.

Default value expression
------------------------

The default value expression for a column must be a
literalor one of the
following functions:

`CURRENT_DATE``CURRENT_DATETIME``CURRENT_TIME``CURRENT_TIMESTAMP``GENERATE_UUID``RAND``SESSION_USER``ST_GEOGPOINT`
You can compose a STRUCT or ARRAY default value with these functions, such as
`[CURRENT_DATE(), DATE '2020-01-01']`.

Functions are evaluated when the data is written to the table.
The type of the default value must match or
coerceto the type of the column it applies to. If no default value is set, the default
value is `NULL`.

Set default values
------------------

You can set the default value for columns when you create a new table. You use the
`CREATE TABLE`DDL statementand add the `DEFAULT`keyword and default value expression after the column name
and type. The following example creates a table called `simple_table`with two
`STRING`columns, `a`and `b`. Column `b`has the default value `'hello'`.


```
CREATE TABLE mydataset.simple_table (
  a STRING,
  b STRING DEFAULT 'hello');

```
When you insert data into `simple_table`that omits column `b`, the default
value `'hello'`is used instead—for example:


```
INSERT mydataset.simple_table (a) VALUES ('val1'), ('val2');

```
The table `simple_table`contains the following values:



