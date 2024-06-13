Documentation Source:
www.metabase.com/docs/v0.49/questions/native-editor/writing-sql.md

Documentation Title:
The SQL editor

Documentation Content:
| Database | Do this | Avoid |
| --- | --- | --- |
| BigQuery |`FROM `dataset.table```FROM dataset.table`
| --- |
| Oracle |`FROM "schema"."table"``FROM schema.table`

For more help, see Troubleshooting SQL error messages.

Explore SQL question results using the Query Builder
----------------------------------------------------

On saved SQL questions without parameters, you’ll get the **Explore results**button. It will create a new Query Builder question that uses the SQL question results as a data source.

!To enable drill-through, turn a SQL question into a model and set the data types
--------------------------------------------------------------------------------

Visualizations created with SQL do not have drill-throughcapability. To enable drill-through on a SQL question, you can turn it into a model:

1. Save the SQL question and turn it into a model.
2. Edit the column metadatain the model’s settings. Make sure to set the data types for all the columns.
3. Create a Query Builder questionbased on the model. You should be able to use drill-through on this question, if you configured the metadata correctly.

Learn more
----------

Best practices for writing SQL queries* SQL troubleshooting guide.
Read docs for other versions of Metabase.
 

Did this article help you?
 

Yes
 No
 Send
 Thanks for your feedback!

Want to improve these docs? Propose a change.##### Subscribe to our newsletter

Stay in touch with updates and news from Metabase. No spam, ever.



Documentation Source:
www.metabase.com/docs/v0.49/data-modeling/models.md

Documentation Title:
Models

Documentation Content:
Create a model from a saved question

1. Ask a questionusing either the query builder or the SQL editor, or select an existing saved question that you want to convert to a model.
2. Save the question.
3. Click on the **…**> **Turn this into a model**.

!Model detail page
-----------------

To view a model’s detail page:

* From a collection: click on the **book**icon next to a model.
* From a model: click on the **info**button in the upper right, then click **Model details**.

!Here you’ll see several tabs:

* **Used by**: lists the items based on the model.
* **Schema**: lists the fields in the model.
* **Actions**: lists the actions in the model, and allows you to create new actions.

The model detail page also shows some basic info about the model:

* Description
* Contact (who wrote the model)
* Backing table(s)

To start a new question based on the model, click **Explore**.

To edit the model’s underlying query, click **Edit definition**.

You can also edit the model’s metadata.

Add metadata to columns in a model
----------------------------------

Metadata is the secret sauce of models. When you write a SQL query, Metabase can display the results, but it can’t “know” what kind of data it’s returning (like it can with questions built using the query builder). What this means in practice is that people won’t be able to drill-through the results, or explore the results with the query builder, because Metabase doesn’t understand what the results are. With models, however, you can tell Metabase what kind of data is in each returned column so that Metabase can still do its drill-through magic. Metadata will also make filtering nicer by showing the correct filter widget, and it will help Metabase to pick the right visualization for the results.

If you only set one kind of metadata, set the **Column type**to let Metabase know what kind of data it’s working with.



Documentation Source:
www.metabase.com/learn/data-modeling/models.md

Documentation Title:
Models in Metabase

Documentation Content:
!Adding metadata to a model is key
---------------------------------

This is the model’s superpower, and it’s especially useful for models built with SQL queries, as Metabase doesn’t know the column types returned by a SQL query.

!Clicking on the model’s name will bring up the model sidebar, which gives us the option to **Customize metadata**. Here we can give columns friendlier names, add descriptions to the columns (which will show up on hover), and tell Metabase what type of data the column contains.

!If we were instead to use a *SQL query*to create that same customer model (see A model exampleabove), Metabase wouldn’t automatically be able to do its usual drill-though magic.

But we can restore the drill-through menu and all the other Metabase magic if we add some metadata to the model’s columns (that is, to the fields returned by the model’s definition, its query).

For example, if this was the query defining our model:

`SELECTorders.user_idASid,people.created_atASjoin_date,people.stateASstate,people.sourceASsource,Sum(orders.total)AStotal,Count(*)ASorder_count,Sum(orders.total)/Count(*)ASavg_totalFROMordersLEFTJOINpeopleONorders.user_id=people.idGROUPBYid,city,state,zip,source`Metabase wouldn’t automatically know what kind of data type the `state`or `total`or any other column was. If, however, we manually set the type for each result column in the model’s metadata, Metabase will then be able to present the drill-through menu on charts, as well as know which kind of filters it should use for that column (e.g., filters for numbers will have different options than for dates or categories).

Models can surface individual records in search
-----------------------------------------------

Another neat metadata feature with models: you can opt to index values from a modelso that they show up in Metabase’s search results.

Here we’re toggling on the option to **Surface individual records in search by matching against this column**(bottom right):

!For example, you could index a column in a model with customer names so people can type in a customer like Hudson Borer and jump straight to the detail view for that customer.



Documentation Source:
www.metabase.com/docs/v0.49/data-modeling/models.md

Documentation Title:
Models

Documentation Content:
Create a model from scratch

1. In the upper right, click **New +**> **Model**.
2. Choose either the query builder or a native query (if you want to use SQL). The advantage of using the query builder is that Metabase will be able to fill out some of the metadata for you; if you use SQL, you’ll have to fill out that metadata manually.
3. Select your data.
4. Create and save your query.



