Documentation Source:
www.metabase.com/learn/visualization/funnel.md

Documentation Title:
Funnel charts

Documentation Content:
Use funnel charts to show progression through steps.

* Funnel chart example using the query builderKeeping the steps sorted with a custom column
Funnel chart example using SQL* Funnel chart queryKeeping the steps sorted in SQL

!Funnel charts visualize how a **measure**breaks out across a series of **steps**. Typically they’re used to show how many people make it through a particular sequence, such as a checkout flow on a website. The first step (or gate) would be how many people visited your site. Then how many people viewed a product page (step 2), how many added that item to their cart (step 3), and so on.

We’ll walk through how to build a funnel chart in Metabase using the Sample Database included with your installation so you can follow along. We’ll show examples both in the query builder and the sql editor:

Query builderSQl editor
The Sample Database doesn’t contain events; it’s just four tables with order, product, and customer information. So we’ll have to get a little creative here to come up with examples for funnel charts.

Funnel chart example using the query builder
--------------------------------------------

Here’s a contrived example. We’re going to pretend that the steps in our funnel are product categories (because we don’t have anything like statuses or pages or other progressions in our Sample Database). Here’s the notebook viewof our query:

!What we’ve done is joined the `Orders`and `Products`tables (see Joins in Metabase), summarized the count of orders, and grouped those counts by product category. Then we’ve sorted the results by count, descending. To get a funnel chart, we clicked on **Visualization**in the bottom left, and selected **Funnel**. In the settings of a funnel chart, under the **Data**tab, you can set the **Step**(in this case we’re using the product category) and the **Measure**(the count of orders).

!Notice that in the **Settings -> Display**tab, you can change the **Funnel type**to “Bar chart”, which is another valid way of representing the data. The advantage of a funnel chart (beyond the visual metaphor) is that Metabase will also show the percentage of the measure that made it through each step.



Documentation Source:
www.metabase.com/learn/visualization/funnel.md

Documentation Title:
Funnel charts

Documentation Content:
Subscribe to our newsletter

Stay in touch with updates and news from Metabase. No spam, ever.



Documentation Source:
www.metabase.com/learn/visualization/funnel.md

Documentation Title:
Funnel charts

Documentation Content:
Keeping the steps sorted with a custom column

If the count in each step doesn’t naturally decrease, you may need to sort the steps manually to preserve the actual progression of steps. For example, if you have the same count in successive steps, the steps could get swapped in the funnel chart, like if Metabase defaults to sorting the steps alphabetically to break the tie. Likewise if you have funnels that can expand in count at certain steps (new people entering the funnel halfway through, for example) the funnel will default to descending counts, which will mess up your step order.

In these cases, you can create an additional column to number the steps, and sort by step to enforce the correct funnel sequence. Using the above query as an example, we could modify it to preserve the sequence by adding another column, `step`, and then sorting by `step`.

!Here’s the custom expression:

`case([Products - Product Name → Category] = "Widget", 1, [Products - Product Name → Category] = "Gadget", 2, [Products - Product Name → Category] = "Gizmo", 3, [Products - Product Name → Category] = "Doohickey", 4)`Basically, we’re saying Widgets are step 1 of the funnel, Gadgets are step 2, and so on.

Funnel chart example using SQL
------------------------------

Another contrived example using the Sample Database: let’s say we learn that customers with the highest lifetime value are those that place orders from all four of our product categories: Doohickeys, Gadgets, Gizmos, and Widgets. So for this example, we want to see how our customers break out based on how many different categories of products they’ve ordered.

A crucial distinction to make here is that we’re not trying to see the distribution of customers, i.e., we’re not trying to see if how many customers ordered from just one product category, how many order from two categories, and so on. We’re going to take all the customers who placed an order for any category as step one. For the next step, we’re going to winnow that population down to only those who placed orders in at least two product categories, then three categories, then four.

Let’s say we have a customer pool of one hundred customers who placed orders.



Documentation Source:
www.metabase.com/learn/visualization/funnel.md

Documentation Title:
Funnel charts

Documentation Content:
when!Analytics dashboards
 Share insights with anyone, anywhere!SQL editor
 For advanced data users!Sandboxing
 Set boundaries around your data!Models
 A starting point for questions!Permissions
 Keep your data secure and private!CSV upload
 Go beyond VLOOKUPDocumentationResources!Learn!Blog!Events!Customers!Discussion!Partners!Community Stories!Startup Guide to Financial Modeling
 New!Community Data Stack Report
 NewPricingLog in1. !Getting Started
	Getting started with MetabaseSharing your work with othersExploring data with Metabase's data browserNext steps: advanced Metabase features for data analystsBeyond BI: other problems you can solve with MetabaseA tour of Metabase
2. !Data fundamentals
	A guide to the data landscapeA short overview of databasesData types and metadataDatabase table relationshipsMeasures and dimensionsData normalizationTypes of databasesData warehouse vs data lake vs data martData cubes
3. !Asking questions
	Create interactive chartsCustom expressions in the notebook editorJoins in MetabaseMulti-level aggregationSearching your tables and questionsCleaning and formatting text
4. !Working with SQL
	Best practices for writing SQL queriesCreate filter widgets for charts using SQL variablesField Filters: create smart filter widgets for SQL questionsWorking with dates in SQLSQL snippets: reuse and share SQL codeSimplify complex queries with Common Table Expressions (CTEs)SQL Snippets vs. Saved Questions vs. ViewsCombining tables with joinsSQL join typesSQL trick: ordering bars in a chartHow to calculate customer lifetime value (LTV) with SQL
5. !Debugging SQL
	Debugging SQL syntax errorsDebugging SQL query logicDebugging duplicated data in SQL query resultsDebugging missing data in SQL query results
6. !Visualizing data
	Which chart should you use?Guide to line chartsMaster the bar chart visualizationVisualize your data as a histogramVisualizing data with mapsAlmost everything you can do with the table visualizationCreating pivot tablesFunnel charts
7.



