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
cloud.google.com/bigquery/docs/reference/standard-sql/dml-syntax.md

Documentation Title:
Data manipulation language (DML) statements in GoogleSQL  |  BigQuery  |  Google Cloud

Documentation Content:
`INSERT`using explicit values

`INSERT dataset.Inventory (product, quantity)
VALUES('top load washer', 10),
 ('front load washer', 20),
 ('dryer', 30),
 ('refrigerator', 10),
 ('microwave', 20),
 ('dishwasher', 30),
 ('oven', 5)`
```
+-------------------+----------+--------------------+
|      product      | quantity | supply_constrained |
+-------------------+----------+--------------------+
| dishwasher        |       30 |               NULL |
| dryer             |       30 |               NULL |
| front load washer |       20 |               NULL |
| microwave         |       20 |               NULL |
| oven              |        5 |               NULL |
| refrigerator      |       10 |               NULL |
| top load washer   |       10 |               NULL |
+-------------------+----------+--------------------+

```
If you set a default value for a column, then you can use the `DEFAULT`keyword
in place of a value to insert the default value:

`ALTER TABLE dataset.NewArrivals ALTER COLUMN quantity SET DEFAULT 100;

INSERT dataset.NewArrivals (product, quantity, warehouse)
VALUES('top load washer', DEFAULT, 'warehouse #1'),
 ('dryer', 200, 'warehouse #2'),
 ('oven', 300, 'warehouse #3');`
```
+-----------------+----------+--------------+
|     product     | quantity |  warehouse   |
+-----------------+----------+--------------+
| dryer           |      200 | warehouse #2 |
| oven            |      300 | warehouse #3 |
| top load washer |      100 | warehouse #1 |
+-----------------+----------+--------------+

```



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
```
+-------+-------+------+
| a     | b     | c    |
+-------+-------+------+
| val_a | val_b | NULL |
| val_a | NULL  | NULL |
+-------+-------+------+

```
You can specify connection-level default values settings in
`default_missing_value_interpretation`within the `AppendRowsRequest`message. If the value is set to
`DEFAULT_VALUE`, the missing value will pick up the default value even when the column is
presented in the user schema.

You can also specify request-level default values in the
`missing_value_interpretations`map within the
`AppendRowsRequest`message.
Each key is the name of a column and its
valueindicates how to interpret missing values.

For example, the map `{'col1': NULL_VALUE, 'col2': DEFAULT_VALUE}`means that all missing values in `col1`are interpreted as `NULL`, and
all missing values in `col2`are interpreted as the default value set for `col2`in the table schema.

If a field is not in this map and has missing values, then the missing values
are interpreted as `NULL`.

Keys can only be top-level column names. Keys can't be struct subfields, such as
`col1.subfield1`.

Use the `insertAll`API method
-----------------------------

The `tabledata.insertAll`API methodpopulates default values at the row level when data is written to a table.
If a row is missing columns with default values, then the default values are
applied to those columns.

For example, suppose you have the following
table schema:


```
[
  {
    "name": "a",
    "mode": "NULLABLE",
    "type": "STRING",
  },
  {
    "name": "b",
    "mode": "NULLABLE",
    "type": "STRING",
    "defaultValueExpression": "'default_b'"
  },
  {
    "name": "c",
    "mode": "NULLABLE",
    "type": "STRING",
    "defaultValueExpression": "'default_c'"
  }
]

```
Suppose you stream the following values to the table:



