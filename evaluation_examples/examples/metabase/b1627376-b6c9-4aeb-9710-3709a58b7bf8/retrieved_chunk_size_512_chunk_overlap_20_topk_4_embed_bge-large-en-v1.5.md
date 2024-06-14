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
www.metabase.com/learn/dashboards/build-a-record-lookup-tool.md

Documentation Title:
Build a record lookup tool with Metabase

Documentation Content:
Let’s change the formatting for our aggregate columns, which we can do by clicking on the heading for that column, then clicking on the **gears icon**.

!We’ll change `Column title`to “Total money spent”, toggle `Show a mini bar chart`, and set `Where to display the unit of currency`to every cell.

!The **mini bar chart**will show the cell’s value relative to the range of values in the column, which makes it easy to see how much money our customers spend compared with other customers.

We’ll do the same for the discount total column: add mini bar chart, rename heading, show currency in every cell.

!We can also throw in some conditional formatting for the table as a whole. In the bottom left of our screen, we’ll click on the **Settings button**for the question, and Metabase will slide out the **Settings sidebar**. At the top of the sidebar, we’ll select the **Conditional formatting tab**. For example, we can highlight the row in blue for big spenders (customers who’ve dropped more than $1,000 on our products), and highlight rows in red if we’ve given them more than $30 in discounts (so we know we should probably cool it on the discounts for that customer).

!With our list all dressed up, let’s save it as `Customer list`.

Add our question to a dashboard
-------------------------------

To be able to look up a customer, we’ll need to be able to filter this table by ID and name. We *could*filter at the question level, but in this case it’s better to have our list be in a dashboard: it gives us more options, like being able to have a filter widget that can filter additional lists or charts we might want to add in the future, or allowing us to customize what happens when people click on a value in a column.

We’ll create a new dashboardand title it (literally) “Customer lookup tool.” Next, we’ll add our `Customer list`question to our new dashboard.

Add filters to the dashboard
----------------------------

Since we want people to be able to look up customers by either their `ID`or `Name`, we’ll need to add a filter widget for each lookup method.



