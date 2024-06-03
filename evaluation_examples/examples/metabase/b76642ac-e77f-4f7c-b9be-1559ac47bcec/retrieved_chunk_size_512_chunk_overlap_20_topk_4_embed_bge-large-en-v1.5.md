Documentation Source:
www.metabase.com/learn/getting-started/introduction.md

Documentation Title:
Getting started with Metabase

Documentation Content:
Click on **+ New**in the main nav, and select **Question**. You can start a new question from:

* A model
* A raw table
* A saved question

For now, let’s start from **Raw data**> **Sample database**> **Orders**. Metabase will open up the query builder.

!Filtering data
--------------

The `Orders`table has a bunch of fake data in it about product orders from a made-up company. Let’s say we want to know:

*How many orders have been placed with a subtotal (before tax) greater than $40?*More precisely, this question translates to: “How many records (or rows) are in the `Orders`table that have a value greater than 40 in the `Subtotal`column?”

To find out, we want to filter the data by the field we’re interested in, which in this case is the `Subtotal`. Then we want to count the filtered rows.

!In the **Filter**step, we’ll click the purple **Add filters to narrow your answer**button, and we’ll select `Subtotal`as the column to filter on. In the dropdown menu, change “Equal to” to “Greater than”, enter 40 in the input field, then click **Add filter**.

Previewing results
------------------

With each step, you can click on the triangle on the right to preview the results so far.

!As expected, all of the subtotals are over $40 after the filter has been applied.

To close the preview, you can click on the **X**in the upper right of the preview.

Summarizing data
----------------

When we ask things like “how many,” “what’s the total,” “what’s the average,” etc., we’re talking about summarizing our data. That is, we’re talking about metrics. The metric in this case the number (or count) of orders after we’ve filtered for orders greater than $40. We’ll click the **Pick the metric you want to see**button in the **Summarize**step and select **Count of rows**.

When we click **Visualize**, Metabase will show us that there were 16,309 orders with a subtotal greater than $40.



Documentation Source:
www.metabase.com/learn/getting-started/introduction.md

Documentation Title:
Getting started with Metabase

Documentation Content:
Said another way, there were 16,309 records in the `Orders`table that made it through our filter.

Grouping our results
--------------------

That count is useful, but it would be even more useful if we knew *when*our customers placed these big orders—more specifically, if we knew how many greater-than-40 orders people placed each month.

We can return to the editor by hitting the back button, or by clicking on the **Editor**button in the upper right (the icon looks like a bulleted list). Alternatively, we can also click on the **Filter**and **Summarize**buttons to revise our question while staying on this page.

Since we want to group our results by month, we’ll click **Summarize**. If we open the **Summarize sidebar**, below where we picked our metric, there’s a list of all the columns that we can use to group our data together. The column we want to group by is `Created At`, because grouping by the orders’ creation date will give us separate counts of orders over $40 for each month, based on when each order was placed (or `Created_at`). We’ll select `Created At`, and Metabase immediately shows us a line chart of the orders over time. The default grouping for `Created_At`is by month, but if we wanted to group by date, week, year, or something else, we could do that by clicking **by month**next to `Created At`and selecting a different option from the dropdown.

!We can keep tweaking our question using the sidebar, or return to our notebook by clicking on the **Editor**button. Here’s our updated question with the new summarize step:

!Changing the visualization
--------------------------

Metabase can present the answers to questions in a variety of ways. To change the visualization, just select one of the options from the **Visualization sidebar**.

If we want to check the results as a table, we can click the little toggle at the bottom center of the page to toggle from our chart to the table of data and back again.

For other visualization options, click the blue **Visualization**button in the bottom left. For example, let’s visualize our question as an **area chart**.



Documentation Source:
www.metabase.com/learn/questions/custom-expressions.md

Documentation Title:
Custom expressions in the notebook editor

Documentation Content:
Metabase will slide out a **Formatting sidebar**with options. Let’s change the style to **Percent**, and bump up the number of decimal places to **2**. And since the title `Discount percentage`takes up a lot of space, let’s rename the column to `Discount %`.

There’s an option to add a **mini bar chart**as well. This bar chart won’t show the percentage with respect to 100%; instead the mini bar chart will show us the discount percentage relative to the discount percentage given to other orders. Let’s leave the mini bar chart off for now.

Here’s the finished question with the added `Discount %`column:

!Custom filters
--------------

Metabase comes with a lot of filtering options out of the box, but you can design more sophisticated filters using custom filter expressions. These are particularly useful for creating filters that use `OR`statements, and that’s what we’ll be covering here.

Normally in the query builder, when we add multiple filters to our question, Metabase implicitly combines the filters with an `AND`operator. For example, if we add a filter for products that are `Enormous`and a filter for products that are `Aerodynamic`, our question will only return products that are both `Enormous`AND `Aerodynamic`, which (enormous, aerodynamic products) do not exist in Metabase’s Sample Database.

To filter for products that are either `Enormous`OR `Aerodynamic`, we’ll select **Custom Expression**from the **Filter**dropdown, and use the `contains`function to check if the product has either `Enormous`or `Aerodynamic`somewhere in the title.

`contains(string1, string2)``contains`checks to see if string1 contains string2 within it. So `string1`is the string to check (the haystack), and `string2`is the text to look for (the needle).



Documentation Source:
www.metabase.com/docs/v0.49/questions/query-builder/introduction.md

Documentation Title:
Asking questions

Documentation Content:
Creating custom columns

!Custom columns are helpful when you need to create a new column based on a calculation, such as subtracting the value of one column from another, or extracting a portion of an existing text column. Custom columns that you add aren’t permanently added to your table; they’ll only be present in the given question.

You can use the following math operators in your formulas: `+`, `–`, `*`(multiplication), and `/`(division), along with a whole host of spreadsheet-like functions. You can also use parentheses to clarify the order of operations.

Adding or removing columns in a table
-------------------------------------

When viewing tables, you can click on the **gear**icon in the bottom left to bring up the columns picker. Click **Add or remove columns**to search for and pick columns, including columns from related tables.

!Sorting results
---------------

!The sorting step lets you pick one or more columns to sort your results by. For each column you pick, you can also choose whether to sort ascending or descending; just click the arrow to change from ascending (up arrow) to descending (down arrow).

Setting a row limit
-------------------

The row limit step lets you limit how many rows you want from the previous results. When used in conjunction with sorting, this can let you do things like create a top-10 list, by first sorting by one of the columns in your result, then adding a row limit of 10. Unlike other steps, the row limit step can only be added at the end of your question.

Viewing the SQL that powers your question
-----------------------------------------

Under the hood, all Metabase questions are SQL (gasp!). If you’re curious to see the SQL that will get run when you ask your question, you can click the little console icon in the top-right of the notebook editor. In the modal that opens up, you’ll also be given the option to start a new query in the SQL editor using this generated SQL as a starting point (assuming you have SQL permissionsto that database). It’s a nice little shortcut to have Metabase write some boilerplate SQL for you, but then allows you to tweak and customize the query.

Play around with saved questions
--------------------------------

Each time you start modifying a saved question, Metabase will create a new question for you.



