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
The table will have two columns:-- the Step: number of categories (our step),-- and the count of customers (our measure).SELECT'Ordered from one category'AS"Step: number of categories",Count(*)ASCustomersFROMcat_oneUNIONSELECT'Ordered from two categories'AS"Step: number of categories",Count(*)ASCustomersFROMcat_twoUNIONSELECT'Ordered from three categories'AS"Step: number of categories",Count(*)ASCustomersFROMcat_threeUNIONSELECT'Ordered from four categories'AS"Step: number of categories",Count(*)ASCustomersFROMcat_fourORDERBYcustomersDESC`Which should yield:

`| Step: number of categories | CUSTOMERS |
|-------------------------------|-----------|
| Ordered from one category | 1,746 |
| Ordered from two categories | 1,632 |
| Ordered from three categories | 1,428 |
| Ordered from four categories | 1,031 |`Now all we have to do is click on **Visualization**in the bottom left and select **Funnel**.

If you open up the **Settings**tab, you can change up the **Step**or the **Measure**. In the **Display**tab, you can change the chart from a funnel to a bar chart (though as mentioned above, you’ll lose both the visual metaphor and the measure’s percentage with respect to the first step).

!### Keeping the steps sorted in SQL

Like above with the query builder, to enforce the step order, you can add an additional column (which we’ll call “step”:

`SELECT'Ordered from one category'AS"Step: number of categories",Count(*)ASCustomers,1asstepFROMcat_oneUNIONSELECT'Ordered from two categories'AS"Step: number of categories",Count(*)ASCustomers,2asstepFROMcat_twoUNIONSELECT'Ordered from three categories'AS"Step: number of categories",Count(*)ASCustomers,3asstepFROMcat_threeUNIONSELECT'Ordered from four categories'AS"Step: number of categories",Count(*)ASCustomers,4asstepFROMcat_fourORDERBYstep`« PreviousNext »Did this article help you?
 

Yes
 No
 Send
 Thanks for your feedback!



Documentation Source:
www.metabase.com/learn/index.md

Documentation Title:
Learn Metabase

Documentation Content:
This guide will help you pick the right visualization for the job.
	2. Guide to line chartsWhat we talk about when we talk about line charts: time series, trend lines, alerts, and more.
	3. Master the bar chart visualizationCreate a bar chart and customize it with visualization settings.
	4. Visualize your data as a histogramLearn when to use a histogram, and how Metabase makes it easy to create histograms.
	5. Visualizing data with mapsHow to use pin maps, region maps, and grid maps to visualize data in Metabase.
	6. Almost everything you can do with the table visualizationLearn how to set up conditional formatting, mini bar charts, value formatting, and more.
	7. Creating pivot tablesLearn how to create pivot tables using different databases in Metabase.
	8. Funnel chartsUse funnel charts to show progression through steps.Explore this topic
 !!
7. TopicBuilding dashboards
-------------------How to build interactive dashboards.

8 articles
 !
	1. BI dashboard best practicesLearn how to make great business intelligence dashboards.
	2. Linking filters in dashboardsLink filters in dashboards to limit the choices available in one filter based on the current selection of another filter.
	3. Custom destinations: choose what happens when people click on charts in your dashboardYou can set up dashboard cards to send people to dashboards, saved questions, and URLs, and use values from the card to update filters at the destination, or parameterize links to external sites.
	4. Cross-filtering: using a chart to update a dashboard filterWith just a few clicks, you can configure any chart or table to update a dashboard filter.
	5. Adding filters to dashboards with SQL questionsHow to add filter widgets to dashboards and connect them to Field Filter variables in a SQL question.
	6. Build a record lookup tool with MetabaseHow to use Metabase to build an internal lookup tool to quickly find details about your customers, orders, or other data.
	7. Why you should regularly edit your dashboardsEditing dashboards is more than just maintaining your tools; it helps keep you focused on the right priorities.
	8.



