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
PARAMS:

- `id`value must be an integer greater than zero.
`POST /api/database/sample_database`Add the sample database as a new `Database`.

You must be a superuser to do this.

`POST /api/database/validate`Validate that we can connect to a database given a set of details.

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
www.metabase.com/docs/v0.49/configuring-metabase/setting-up-metabase.md

Documentation Title:
Setting up Metabase

Documentation Content:
We won’t be able to connect to your database without it, but you’d like to deal with all of this later, that’s okay: just click **I’ll add my data later**. Metabase comes with a Sample Databasethat you can play around with to get a feel for how Metabase works.

If you’re ready to connect, here’s what you’ll need:

* The **hostname**of the server where your database lives
* The **port**the database server uses
* The **database name**
* The **username**you use for the database
* The **password**you use for the database

If you don’t have this information handy, the person responsible for administering the database should have it.

Connect to your database
------------------------

Now that you have your database info you can connect to your database. Sweet, sweet data at last. Just go ahead and put your info into this form and click **Next**.

!For more on connecting to databases, see Adding and managing databases.

Usage data preferences
----------------------

One last quick thing that you’ll have to decide is if it’s okay for us to collect some anonymous info about how you use the product — it helps us make Metabase better. Like the box says:

* Metabase never collects anything about your data or question results.
* All collection is completely anonymous.
* Collection can be turned off at any point in your admin settings.

!If you’re ready to start using Metabase, go ahead and click **Next**.

Staying in touch
----------------

At this point you are all set and ready to use Metabase. Since we like keeping in touch with our friends we made it easy to sign up for our newsletter (infrequent emails) with a single click!

!Once you’re done here simply follow the link to **Take me to Metabase**. And if you decided to skip the newsletter sign-up, it’s cool, we still like you :)

Getting started with Metabase
-----------------------------

For a tutorial on getting up and running with questions and dashboards, head over to Learn Metabase.

If you’d like more technical resources to set up your data stack with Metabase, connect with a Metabase Expert.



