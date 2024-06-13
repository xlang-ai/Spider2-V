Documentation Source:
www.metabase.com/docs/v0.49/databases/connecting.md

Documentation Title:
Adding and managing databases

Documentation Content:
Syncing and scanning databases
------------------------------

See Syncing and scanning.

Deleting databases
------------------

**Caution: Deleting a database is irreversible! All saved questions and dashboard cards based on the database will be deleted as well!**Go to **Admin settings**> **Databases**> your database and click **Remove this database**.

Restoring the Sample Database
-----------------------------

If you’ve deleted the Metabase Sample Database, go to **Admin settings**> **Databases**and click **Bring the Sample Database back**.

Troubleshooting
---------------

Troubleshooting database connectionsTroubleshooting syncs, scans, and fingerprinting* Search or ask the Metabase community.
* Search for known bugs or limitations.

Further reading
---------------

* Metadata editing.
* Setting data access permissions.
* Metabase at scale.
Read docs for other versions of Metabase.
 

Did this article help you?
 

Yes
 No
 Send
 Thanks for your feedback!

Want to improve these docs? Propose a change.##### Subscribe to our newsletter

Stay in touch with updates and news from Metabase. No spam, ever.



Documentation Source:
www.metabase.com/docs/v0.49/api/database.md

Documentation Title:
Database

Documentation Content:
when!Analytics dashboards
 Share insights with anyone, anywhere!SQL editor
 For advanced data users!Sandboxing
 Set boundaries around your data!Models
 A starting point for questions!Permissions
 Keep your data secure and private!CSV upload
 Go beyond VLOOKUPDocumentationResources!Learn!Blog!Events!Customers!Discussion!Partners!Community Stories!Startup Guide to Financial Modeling
 New!Community Data Stack Report
 NewPricingLog inv0.49Api
Database
========

/api/database endpoints.

`DELETE /api/database/:id`Delete a `Database`.

You must be a superuser to do this.



Documentation Source:
www.metabase.com/learn/getting-started/introduction.md

Documentation Title:
Getting started with Metabase

Documentation Content:
Get to know your way around Metabase and create your first question using the sample database.

Installation and setupThe Metabase home pageAsking a new questionFiltering dataPreviewing resultsSummarizing dataGrouping our resultsChanging the visualizationNext up
Metabase is a simple and powerful analytics tool which lets anyone learn and make decisions from their company’s data—no technical knowledge required.

Installation and setup
----------------------

If your Metabase isn’t up and running yet, check out:

Installing MetabaseSetting up Metabase
The Metabase home page
----------------------

!Fresh out of the box, Metabase will show you a few things on the home page:

* Some automatic explorationsof your tables that you can look at and save as dashboard.
* A navigation sidebar that lists:
	+ **Home**button to return to your Metabase home page.
	+ **Collections**, where you’ll store all of your questions, dashboards, and models. You have your own personal collection to store drafts and experiments that aren’t yet ready to share.
	+ **Data**section, which lists all of the data sources your Metabase is connected to.
	+ **Settings**(the **gear**icon in the upper right).

You can also **Bookmark**your favorite items, and they’ll appear toward the top of the navigation sidebar.

To open and close the navigation sidebar, click on the Metabase logo in the upper left.

!Asking a new question
---------------------

A questionin Metabase is a query, the results of that query, and the visualization and formatting of those results (even if that visualization is just a table). Questions have titles, IDs, and unique URLs you can copy and share with others.

You can play around with a question by filtering and summarizing its results, save those explorations as new questions, and add questions to dashboards. But we’re getting ahead of ourselves; for the next few examples, we’ll be using the Sample Databasethat comes with Metabase.

Click on **+ New**in the main nav, and select **Question**.



Documentation Source:
www.metabase.com/learn/permissions/data-permissions.md

Documentation Title:
Guide to data permissions

Documentation Content:
2. Click on the dropdown menu at the **All Users**row and **Data access**column.
3. Select **No self-service**.
4. Click **Save changes**in the banner that appears at the top.

!Selecting **No self-service**for All Users to the Sample Database will:

Prevent All Users from seeing any data from the Sample Database in the data browser.

Prevent All Users from using the query builder to create questions using data from the Sample Database.

Continue to allow All Users to *view the results*(but not access the underlying data) from questions and dashboards that use Sample Database tables, as long as these questions and dashboards are saved in collections that match the collection permissionsfor your All Users group.



