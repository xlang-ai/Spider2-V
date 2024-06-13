Documentation Source:
www.metabase.com/docs/v0.49/data-modeling/json-unfolding.md

Documentation Title:
Working with JSON

Documentation Content:
when!Analytics dashboards
 Share insights with anyone, anywhere!SQL editor
 For advanced data users!Sandboxing
 Set boundaries around your data!Models
 A starting point for questions!Permissions
 Keep your data secure and private!CSV upload
 Go beyond VLOOKUPDocumentationResources!Learn!Blog!Events!Customers!Discussion!Partners!Community Stories!Startup Guide to Financial Modeling
 New!Community Data Stack Report
 NewPricingLog inv0.49Data Modeling
Working with JSON
=================

With some databases, Metabase can unfold JSON columns into their component fields, which you can then filter on using the query builder.

Here is a table with a column that contains JSON.

!Metabase can unfold that JSON column so that each key in the JSON object gets its own column in the table. Here are the unfolded fields of the table with the JSON column pictured above:

!And here are the values as seen in the table:

!This unfolding allows you to filter for values found in the original JSON object.

Metabase will prefix the unfolded column names with the name of the original column that contained the JSON. You can change the column names in **Admin settings**> Table metadata, or by creating a modeland editing the column metadata.

Toggling JSON unfolding for a database
--------------------------------------

If you notice a hit to performance from this JSON unfolding, we recommend turning it off.

To turn off JSON unfolding for a database:

1. Click on the **Gear**in the upper right.
2. Select **Admin settings**
3. Visit the **Databases**tab.
4. Select the relevant database.
5. Click **Show advanced options**.
6. Toggle **Allow unfolding of JSON columns**.
7. Scroll down and click the **Save changes**button.
8. Click **Sync database schema now**.
9. Click **Re-scan field values now**.

Toggling JSON unfolding for a specific column
---------------------------------------------

If performance degrades, or you’d rather keep the JSON contained in the original column, you can turn off unfolding for individual fields in their settings.

1. Click on the **Gear**in the upper right.
2. Select **Admin settings**.
3. Visit the **Table metadata**tab.
4.



Documentation Source:
www.metabase.com/docs/v0.49/databases/connections/postgresql.md

Documentation Title:
PostgreSQL

Documentation Content:
Unfold JSON Columns

For PostgreSQL databases, Metabase can unfold JSON columns into component fields to yield a table where each JSON key becomes a column. JSON unfolding is on by default, but you can turn off JSON unfolding if performance is slow.

If you turn on JSON unfolding, you can also toggle the unfolding for individual columns in table metadata.



Documentation Source:
www.metabase.com/docs/v0.49/data-modeling/json-unfolding.md

Documentation Title:
Working with JSON

Documentation Content:
Select **Admin settings**.
3. Visit the **Table metadata**tab.
4. Select the database that contains the field you want to update.
5. Select the table that contains the field.
6. Select the field containing the original JSON
7. Scroll to the **Unfold JSON**option and select **Yes**or **No**. If the column was unfolded, Metabase will have hidden this JSON columnn from view, so if you want the JSON column to be visible again, you’ll need to change the column’s visibility to **Everywhere**.
8. Scroll down and click on the **Re-scan this field**.

!For JSON unfolding to work, the column’s data type must be JSON
---------------------------------------------------------------

For example, if you upload a CSV with JSON in it, you might need to update the data/type in the database. Note that you can’t edit the data type via Metabase; you can only change its field type. So even if the field type in Metabase is `Field containing JSON`, if the data/type isn’t `JSON`, Metabase won’t give you the option to unfold the column. You’ll need to change the column type in the database itself.

Databases that support JSON unfolding
-------------------------------------

PostgreSQLMySQLRead docs for other versions of Metabase.
 

Did this article help you?
 

Yes
 No
 Send
 Thanks for your feedback!

Want to improve these docs? Propose a change.##### Subscribe to our newsletter

Stay in touch with updates and news from Metabase. No spam, ever.



Documentation Source:
www.metabase.com/docs/v0.49/databases/connections/mysql.md

Documentation Title:
MySQL

Documentation Content:
Unfold JSON Columns

For MySQL databases, Metabase can unfold JSON columns into component fields to yield a table where each JSON key becomes a column. JSON unfolding is on by default, but you can turn off JSON unfolding if performance is slow.

If you turn on JSON unfolding, you can also toggle the unfolding for individual columns in table metadata.



