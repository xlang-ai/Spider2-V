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
www.metabase.com/learn/sql-questions/sql-variables.md

Documentation Title:
Create filter widgets for charts using SQL variables

Documentation Content:
Now we’re ready to plug in values into our Subtotal widget, and filter for orders with Subtotals greater than that value:

!### Making a basic input variable optional

If we want to make the filter widget optional, we can enclose the `WHERE`clause in double brackets:

`SELECT*FROMorders[[WHEREsubtotal>{{subtotal_var}}]]`With the `WHERE`clause in brackets, if the viewer does not enter a subtotal, and no default is set, the query would simply return all records from the `Orders`table (i.e., Metabase would only run `SELECT * FROM orders`).



Documentation Source:
www.metabase.com/docs/v0.49/exploration-and-organization/exploration.md

Documentation Title:
Basic exploration

Documentation Content:
If you click on a part of a chart, such as a bar in a bar chart, or a dot on a line chart, you’ll see the **Action menu**, with actions you can take to dive deeper into that result, branch off from it in a different direction, or see automatic insights to X-raythe data.

!In this example of orders by product category per month, clicking on a data point on this line chart gives us the ability to:

* **See these Orders**: See a list of the orders for a particular month.
* **See this month by week**.
* **Break out by …**: See things like the Gizmo orders in June 2023 broken out by the status of the customer (e.g., `new`or `VIP`). Different charts will have different breakout options, such as **Location**and **Time**.
* **Automatic insights**: See orders for a particular category over a shorter time range.
* **Filter by this value**: update the chart based on the value you clicked: equal to, less than, greater than, or not equal to.

Note that while charts created with SQL don’t currently have the drill-through menu, you can add SQL questions to a dashboard and customize their click behavior. You can send people to a custom destination(like another dashboard or an external URL), or have the clicked value update a dashboard filter.

Clicking on a table cell will often allow you to filter the results using a comparison operator, like =, >, or <. For example, you can click on a table cell, and select the less than operator `<`to filter for values that are less than the selected value.

!Lastly, clicking on the ID of an item in a table gives you the option to go to a detail view for that single record. For example, you can click on a customer’s ID to see the profile view for that customer.

!When you add questions to a dashboard, you can have even more control over what happens when people click on your chart. In addition to the default drill-through menu, you can add a custom destinationor update a filter. Check out interactive dashboards. to learn more.



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



