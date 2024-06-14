Documentation Source:
www.metabase.com/docs/v0.49/questions/sharing/visualizations/map.md

Documentation Title:
Maps

Documentation Content:
World Map

To visualize your results in the format of a map of the world broken out by country, your result must contain a column with two-letter country codes.

!### United States Map

!Creating a map of the United States from your data requires your results to contain a column that contains names of states or two-letter state codes. This lets you do things like visualize the count of your users broken out by state, with darker states representing more users.

Pin map
-------

If your results contains latitude and longitude fields, Metabase will try to display the results as a pin map of the world. Metabase will put one pin on the map for each row in your table, based on the latitude and longitude fields. You can try this with the Sample Database that’s included in Metabase: start a new question and select the People table, use `raw data`for your view, and choose the Map option for your visualization. You’ll see a map of the world, with each dot representing the latitude and longitude coordinates of a single person from the People table.

!When you open up the Map options, you can manually switch between a region map (e.g., United States) and a pin map. If you’re using a region map, you can also choose which field to use as the measurement, and which field to use as the region (e.g., State or Country).

Custom maps
-----------

Metabase also allows administrators to add custom maps via GeoJSON filesthrough the Metabase **Admin Panel**.

Further reading
---------------

- Visualizing data with maps.
Read docs for other versions of Metabase.
 

Did this article help you?
 

Yes
 No
 Send
 Thanks for your feedback!

Want to improve these docs? Propose a change.##### Subscribe to our newsletter

Stay in touch with updates and news from Metabase. No spam, ever.



Documentation Source:
www.metabase.com/learn/visualization/maps.md

Documentation Title:
Visualizing data with maps

Documentation Content:
Matches are case-sensitive; if the country or state codes listed in your database are lowercase or contain extra spaces, Metabase won’t recognize them.

Pin map
-------

A pin map represents data geographically using discrete markers, and requires coordinates — latitude and longitude — to generate. Let’s start an example by visualizing the `People`table found within the `Sample Database`. Once you’re viewing the table, you’ll notice that this table contains four pieces of geographic information: city, state, latitude, and longitude.

Select **Visualization**, and scroll to the **Map**icon. With your latitude and longitude fields set correctly, Metabase will produce a pin map by default, placing markers on the map at those coordinates. The pins are locating customers, but you can also use a pin map to locate businesses partners, company branch locations, or shipping addresses, as long as those records contains coordinates.

!Hovering over a pin provides additional information.

Other cool things you can do with pin maps:

* Double click to zoom in on an area.
* Click and drag the map to move to a different area.
* Click on a pin to drill-throughto additional information.

!If your pin is linked to other tables, or there’s too much information to fit in the tooltip, clicking on the point will take you to a details page that displays a list of fields, as well as a list of connected tables. Clicking a relationship to another table directs you to a list of the instances where the current pin and the other table intersect. In this case, Metabase displays orders placed by that person.

Region map
----------

Region maps display data across a geographic area by coloring parts of that area according to a value. Grouping people by region can be a great way to detect patterns in your customer base. Let’s generate a region map using the same `People`table within the `Sample Database`. Summarize the data by selecting the green **Summarize**button at the top righthand corner of your screen. If you count the number of records by `State`, Metabase will produce a region map, displaying a map of the United States, with the varying shades representing how many records are present for each state.

Here’s a drill-throughon Texas to see how user creation has been tracking.



Documentation Source:
www.metabase.com/learn/visualization/maps.md

Documentation Title:
Visualizing data with maps

Documentation Content:
How to use pin maps, region maps, and grid maps to visualize data in Metabase.

Map typesMake your data compatible with mappingPin mapRegion mapGrid map* Additional features (pin map and grid map)
	Save as default viewDraw box to filter
* Common problems with maps
	Choosing an inappropriate field for map coordinatesNot having a map of the region you needForgetting that pin maps may only show a subset of dataNot summarizing data for region and grid mapsWhen adding a map, the browser stops responding or throws an error
Further reading
This article covers how to visualize data using maps in Metabase. The maps of the United States used throughout this article were created using the Sample Databasethat comes with every Metabase installation.

Map types
---------

Metabase features three map types:

* Pin mapsmark specific locations.
* Region mapsgroup data by country or state.
* Grid mapsdistribute a large number of points over a specified area.

Any of these map types can be used with our two default map options: the United States and the world. For a different map (for example, one that focuses on a specific region of the world), you can upload a custom mapin GeoJSON format.

!If you have a column with two-letter country codes, Metabase will automatically select the world map. If your data contains names of U.S. states, or two-letter state codes, Metabase will select the map of the United States.

Make your data compatible with mapping
--------------------------------------

If you plan on using a map visualization, you’ll need to make sure your data is compatible with map visualizations in two ways:

* Field types in your metadata
Field typesCountry codes
To edit metadata, go to your Data Model admin settings. Confirm that all your field types are set as a `Location`data type. For example, the `State`and `Longitude`fields both have their corresponding field type listed, but `Latitude`has no field type. To add the field type, click the dropdown menu in the `Type`column and select `Latitude`.

!To create a world map or US region map, make sure that your country or state codes match the standardized two-letter format specified by the International Organization for Standardization (ISO).



Documentation Source:
www.metabase.com/docs/v0.49/people-and-groups/start.md

Documentation Title:
People overview

Documentation Content:
UpcomingMetabase for advanced usersRegister Now!×Product
 Use Cases!Self-service Analytics
 Business intelligence for everyone!Embedded Analytics
 Create seamless in-product analyticsMetabase Plans!Starter and Open Source
 Self-service BI in 5 minutes!Pro
 Advanced tools and controls!Enterprise
 White-glove treatmentPlatform!Data Sources!Security!Cloud!Professional Services
 NewWatch a 5-minute demoto see how to set up and publish a dashboard

!Features
 !Query builder
 Get answers in a few clicks!Drill-through
 Pull threads in your data!Usage analytics
 NewSee who did what, when!Analytics dashboards
 Share insights with anyone, anywhere!SQL editor
 For advanced data users!Sandboxing
 Set boundaries around your data!Models
 A starting point for questions!Permissions
 Keep your data secure and private!CSV upload
 Go beyond VLOOKUPNewMetabase 49:New tools for dashboard creators, data sharers, and more
 

DocumentationResources
 !Learn
 Guides on working with data!Blog
 News, updates, and ideas!Events
 Join a live event or watch on demand!Customers
 Real companies, real data, real stories!Discussion
 Share and connect with other users!Metabase Experts
 Find an expert partner!Community Stories
 Practical advice from our community!Startup Guide to Financial Modeling
 NewModeling financial data with Metabase!Community Data Stack Report
 NewSee how others work with dataRecent Blog Posts!Set up a basic pipeline for log analysisEmbed a Metabase dashboard in ZendeskKeeping tabs on embedded analyticsPricingLog inGet startedProductUse Cases!Self-service Analytics
 Business intelligence for everyone!Embedded Analytics
 Create seamless in-product analyticsMetabase Plans!Starter and Open Source!Pro!EnterprisePlatform!Data Sources!Security!Cloud!Professional Services
 NewFeatures!Query builder
 Get answers in a few clicks!Drill-through
 Pull threads in your data!Collections and verified items
 Keep things organized!Usage analytics
 NewSee who did what, when!Analytics dashboards
 Share insights with anyone,



