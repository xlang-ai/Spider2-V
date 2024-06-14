Documentation Source:
www.metabase.com/learn/visualization/histograms.md

Documentation Title:
Visualize your data as a histogram

Documentation Content:
Learn when to use a histogram, and how Metabase makes it easy to create histograms.

Histograms versus bar chartsCreate a histogramEdit a histogramFurther reading
We’ll walk through creating a **histogram**, which is a type of bar chart that displays groups of data across a continuous range. Histograms are helpful for gaining insights into how much of an item people are likely to buy, the price range they are likely to purchase within, or even the time of year that most people make purchases.

Histograms versus bar charts
----------------------------

Histograms are a type of bar chart. While the bars on a typical bar chart represent categorical groups, the bars on a histogram represent ranges along a continuous, quantifiable spectrum.

In other words, you split the data into bins in order to view the distribution of values within a range. The bins are of equal length (and can be empty), and the bins are contiguous. The height of each bar represents the count (or proportion) of the items in the bin. The number of bins is up to the user, though Metabase will automatically select the number of bins for you.

Here’s a bar chart that displays the count of people from the People table grouped by referral source.

!Here’s the histogram we’ll create in the walkthrough below.

!Metabase makes it easy to create a histogram. In fact, if the data is suitable for a histogram, Metabase will automatically create a histogram for you.

Create a histogram
------------------

Follow along with Metabase’s **Sample Database**to create the histogram detailed below.

Select **+ New**> **Question**. In the **Query Builder**under **Pick your starting data**, choose **Raw Data**> **Sample Database**, and select the `Orders`table. Then **Visualize**the results.

Once you’re viewing the Orders table, click **Summarize**. Scroll down and select `Total`, and click the `+`button to add the grouping. Metabase will automatically create a histogram for you!

!The histogram shows that customers are most likely to make purchases totaling in the $40-60 range. If you hover over one of the bars, Metabase will display the count of orders in that range.



Documentation Source:
www.metabase.com/learn/visualization/histograms.md

Documentation Title:
Visualize your data as a histogram

Documentation Content:
You can also click on a bar to drill-through the dataand see the orders that compose the bar.

Edit a histogram
----------------

Metabase gives you a lot of knobs for customizing a bar chart. For now, we’ll hone in on the settings that make histograms shine.

Metabase will automatically set the number of bins, but you can change how Metabase bins the data. Click **Summarize**, scroll down to `# Total`, and click on `Auto binned`. A dropdown menu will present the options: `Auto bin`, 10, 50, or 100 bins, or `Don't bin`.

!Click the **Settings**> **Axes**. The x-axis scale currently says `Histogram`. Metabase detects when your bar chartshould present as a histogram, and selects the best x-axis scale for your visualization.

If you toggle between the three options, you’ll see that `Histogram`is the only axes option in which the bars are flush with each other. The flush bars communicate that the x-axis represents a continuous range of data. Linear axes are good for displaying data in categories. Ordinal axes are good for displaying data that’s grouped in distinct number categories. For example, displaying how many ratings you receive that are either 1, 2, 3, 4, or 5.

Ordinals differ from histograms because ordinals group by distinct number values, rather than a continuous range of values.

You can also change the scale of the y-axis to make your chart easier to interpret. If the range of your data along the y-axis is tall, consider using a logarithmic scale. If your range is compact, you can display counts using a power scale (though you’ll probably never need to do this).

Happy histogramming!

Further reading
---------------

We’ll cover more visualizations types in future posts. In the meantime, check out:

Visualization optionsMaster the bar chart visualizationDrill-through charts with the action menu
« PreviousNext »Did this article help you?
 

Yes
 No
 Send
 Thanks for your feedback!



Documentation Source:
www.metabase.com/learn/visualization/histograms.md

Documentation Title:
Visualize your data as a histogram

Documentation Content:
Subscribe to our newsletter

Stay in touch with updates and news from Metabase. No spam, ever.



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



