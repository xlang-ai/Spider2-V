Documentation Source:
www.metabase.com/learn/visualization/how-to-create-pivot-tables.md

Documentation Title:
Creating pivot tables

Documentation Content:
Order *within*a single bucket matters, so let’s start by simply rearranging the table within a single bucket: the rows bucket. If we switch the order of fields to use for table rows, putting `Created At`above `User → State`, the table will rearrange itself:

!Now the table groups first by year, then gives a breakdown of orders for each state across each product category.

We can also switch fields *between*the buckets, like moving `Product → Category`from a column to a row, and `User → State`from a row to a column.

!You can also turn off subtotals for a given row grouping:

!Like with flat tables, we have some sorting and formatting options, and we can click on values in the table to bring up the drill-through menu, which will lets us drill through the data.

!How to create pivot tables: limitations
---------------------------------------

Pivot tables only work with relational databases that support joins and expressions, so you won’t be able to use them with databases like MongoDB. They also only work with questions composed with the query builder. The workaround here is that if you must use SQL to compose a question, you can save that question, then use its results as the starting pointfor a query builder question in order to build a question. The trick here is to do your aggregation and grouping in the GUI question. That is, use the SQL question to grab the raw data you want to work with (maybe create a model), then start a new GUI question to filter, summarize, and group that data.

For example, to use a SQL question to build the pivot table we created above, you’d first write a SQL query to get the raw data you want to work with:

`SELECTpeople.state,products.category,orders.subtotal,orders.created_atFROMordersINNERJOINproductsONorders.product_id=products.idINNERJOINpeopleONorders.user_id=people.id`Notice that we’re just grabbing records here; there’s no summarizing or grouping. Next, we save that SQL question (here as `Raw data for pivot table`), and start a new query builder question that uses the results of that question as its starting data.



Documentation Source:
www.metabase.com/docs/v0.49/questions/sharing/visualizations/pivot-table.md

Documentation Title:
Pivot table

Documentation Content:
when!Analytics dashboards
 Share insights with anyone, anywhere!SQL editor
 For advanced data users!Sandboxing
 Set boundaries around your data!Models
 A starting point for questions!Permissions
 Keep your data secure and private!CSV upload
 Go beyond VLOOKUPDocumentationResources!Learn!Blog!Events!Customers!Discussion!Partners!Community Stories!Startup Guide to Financial Modeling
 New!Community Data Stack Report
 NewPricingLog inv0.49Questions
Pivot table
===========

Pivot tables allow you swap rows and columns, group data, and include subtotals in your table. You can group one or more metrics by one or more dimensions.

Pivot tables are not currently available for the following databases in Metabase:

* Druid
* Google Analytics
* MongoDB

Pivot tables work for simple and custom questions with summarized data for all other officially supported databases. They don’t work for questions that lack aggregate data, and they don’t work for questions written in SQL, as Metabase would need to modify your SQL code in order to calculate subtotals. If you really need to use SQL, the workaround here is to create your question in two steps: first do all the complex things you need to do in SQL, save the results as a question, then use that saved SQL question as the starting point for a new GUI question which summarizes that data.

In the settings for the Pivot Table visualization, you can assign fields to one of three “buckets”:

* Fields to use for the table **rows**
* Fields to use for the table **columns**
* Fields to use for the table **values**

Let’s say we ask the following question in the notebook editor:

!From the `Orders`table, we’ve summarized by the count of orders and the average order total, and grouped by `User → State`, `Product → Category`, and `Created At`binned by year. Here’s our question visualized as a pivot table:

!We’ve assigned the fields `User → State`and `Created At`to table rows, and assigned the `Product -> Category`field to generate our columns: Doohickey, Gadget, and so on. We can drag and drop dimensions between the row and column buckets, and add aggregations to the table values bucket.



Documentation Source:
www.metabase.com/learn/visualization/how-to-create-pivot-tables.md

Documentation Title:
Creating pivot tables

Documentation Content:
For each group (say Alaska in 2017), we count the number of orders and add up the subtotals for those orders. (Note that, even though we’ve only selected the `Orders`table in the data section, Metabase will automatically join the `Products`and `People`tables to get the State and Category data.)

The resulting table is a regular one, with rows for each combination of state, year, and product category.

Now, let’s say that for each state, we also want to know the sum of the annual subtotals for each state (e.g., how much money did orders for Doohickey products make in Alaska for all years?). To find out, we could add up the subtotals ourselves, or use a pivot table to calculate that figure for us. At the bottom left of your screen, click **Visualization**> **Pivot table**.

!In our pivot table, Metabase has set the rows, columns, and values as follows:

* rows: `User → State`and `Created At`(by year)
* columns: `Product → Category`
* values: `Count`and `Sum of Subtotal`

Like the flat table, the pivot table lets us see, for example, that in 2020 our customers in Alaska (AK) have purchased a combined 11 Doohickey products for $867.63. But now the pivot table has grouped the rows related to Alaska, and given a subtotal for those Alaskan rows, allowing us to see the answer to our question: Alaskans purchased 103 Doohickeys from 2016–2020, totaling $6,900.43.

In addition to the group subtotals, the pivot table also includes both row and column grand totals:

* Row grand total example: the total number of Doohickey orders placed across all states.
* Column grand total example: the sum of all subtotals in Alaska across all product categories.

We can navigate the table by collapsing and expanding groups of rows:

!Now, let’s try pivoting the table. In the bottom left of the screen, we’ll click on **Settings**. To pivot the table, we’ll move fields between the three buckets: rows, columns, and values.



Documentation Source:
www.metabase.com/learn/visualization/how-to-create-pivot-tables.md

Documentation Title:
Creating pivot tables

Documentation Content:
!Now we can count, sum, and group our results:

!When we visualize this question, we’ll now be able to use the pivot table visualization to see the group subtotals and grand totals.

Further reading
---------------

Visualization types« PreviousNext »Did this article help you?
 

Yes
 No
 Send
 Thanks for your feedback!



