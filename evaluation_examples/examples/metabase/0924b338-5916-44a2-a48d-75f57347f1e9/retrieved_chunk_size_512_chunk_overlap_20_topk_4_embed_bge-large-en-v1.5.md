Documentation Source:
www.metabase.com/learn/getting-started/sharing-work.md

Documentation Title:
Sharing your work with others

Documentation Content:
Create a dashboard with saved questions, and set up an alert to get notified when your question returns something interesting.

Saving questionsCreating a dashboardSharing answers directlySet up an alert for your question
You can use Metabase all on your own, but it becomes even more useful when you start sharing your answers with other people on your team or in your organization. The first step is saving some of your questions.

Saving questions
----------------

Sometimes you’ll find yourself asking certain questions again and again, whether it’s running regular reports, looking up something about an important segment of users, or just answering the same question for other people in your company. To keep from repeating the same set of steps each time you want to ask the same question, you can save your questions to use later.

To do this, click on the **Save**button in the top-right of the query builder.

!Metabase will take a stab at giving your question a meaningful name, but you can (and should) use your own naming convention that’ll help you and others find your questions later on. You can also pick which collectionto save your question in. You can think of collections like folders, to which you can add permissions.

!Save the question you created as “Orders over $40 grouped by month”. When you save a question, Metabase asks if you want to add the question to a new or existing dashboard. Let’s say “yes” and then click on **Create new dashboard**. The dialog prompts you to create a new dashboard and give it a name and description. You can name it anything you want—we’ll call ours `My First Dashboard`.

!Creating a dashboard
--------------------

Dashboards are great when you have a set of answers that you want to view together. Your saved questions will be displayed as *cards*on the dashboard, which you can resize and move around.

So, after you click the button to create your dashboard, you should see your chart as a little card.

!You can move and resize your chart so you can get it looking just how you want it. We’ll make ours a bit wider to let those data points breathe:

!Don’t forget to click **Save**at the top to save your work when you’re done.



Documentation Source:
www.metabase.com/docs/v0.49/dashboards/introduction.md

Documentation Title:
Introduction to dashboards

Documentation Content:
when!Analytics dashboards
 Share insights with anyone, anywhere!SQL editor
 For advanced data users!Sandboxing
 Set boundaries around your data!Models
 A starting point for questions!Permissions
 Keep your data secure and private!CSV upload
 Go beyond VLOOKUPDocumentationResources!Learn!Blog!Events!Customers!Discussion!Partners!Community Stories!Startup Guide to Financial Modeling
 New!Community Data Stack Report
 NewPricingLog inv0.49Dashboards
Introduction to dashboards
==========================

!What is a dashboard?
--------------------

**Dashboards**group a set of questions into tabs on a single page. You can think of dashboards as shareable reports that feature a set of related questions. You can set up subscriptions to dashboardsvia email or Slack to receive the exported results of the dashboard’s questions.

A dashboard comprises a set of cards arranged on a grid. These cards can be:

* Questions, such as tables, charts, or maps
Text and header cardsLink cards
You can add filter widgets to dashboardsthat filter data identically across multiple questions, and customize what happens when people click on a chart or a table.

You can make as many dashboards as you want. Go nuts.

How to create a dashboard
-------------------------

In the top right of the screen, click the **+ New**> **Dashboard**. Give your new dashboard a name and a description, choose which collectionsthe dashboard should go in, then click **Create**, and Metabase will take you to your shiny new dashboard.

Adding questions to a dashboard
-------------------------------

There are two ways to add questions to a dashboard: from the dashboard, or from the question you want to add.

* **From a question**: You can add a newly saved question to a dashboard directly from the modal that pops up after you save the question for the first time. You can also add a question to a dashboard by clicking on the ellipsis (**…**) at the top right of a question and selecting **Add to dashboard**.
* **From a dashboard**: Click on the **pencil**icon to **edit the dashboard**.



Documentation Source:
www.metabase.com/learn/dashboards/filters.md

Documentation Title:
Adding filters to dashboards with SQL questions

Documentation Content:
To learn more, check out our documentation on metadata editing.

Connecting a dashboard filter widget to a field filter variable
---------------------------------------------------------------

So we have our SQL question with a Field Filter variable in a `WHERE`clause, and it’s time to add that question to a dashboard.

Next, we’ll need to:

* Create a dashboard.
* Add our question to a dashboard.
* Add a filter widget to that dashboard.
* Connect that dashboard filter widget to the field filter variable in our SQL question.

Let’s create a dashboard(we’ll give our dashboard the wildly unimaginative name `Dashboard with filter widgets`).

Then we’ll add our SQL question to the dashboard.

Next, we’re going to add a filter widget to our dashboard. Click on the **pencil**icon to enter Dashboard edit mode, then:

* Click on the **filter icon**to add a filter widget to the dashboard.
* Under `What do we want to filter`, we’ll select `Time`.
* For `What kind of filter?`, we’ll select `Date filter`.
* Next, we’ll need to connect our widget to the Field Filter variable in our question. Click on the dropdown menu in the center of our question, and select our `Created At`Field Filter variable.
* Click the **Done**button at the top of the screen.
* Then **Save**the dashboard.

!Now we’re all wired up, and we’re ready to test out our new Date filter. This particular widget type gives us an abundance of options. Let’s look at orders for the past six months.

!Connecting a SQL question to a dropdown filter widget on a dashboard
--------------------------------------------------------------------

Let’s say we want to have a dashboard filter widget to filter products by category, and we want people to be able to select the available categories from a dropdown list. To set this up, we’ll put a field filter variable in our SQL query, and map it to the `category`field in the `products`table. Then we’ll map the dashboard filter to that variable. Let’s walk through it.

!First, create a dashboard. Let’s call it “Dashboard with SQL question and dropdown filter” (so our mission is clear). Save the dashboard.

Next, ask a new Native/SQL question to get all fields from the `products`table.



Documentation Source:
www.metabase.com/learn/administration/serialization.md

Documentation Title:
Serialization: preloading dashboards in a new Metabase instance

Documentation Content:
Or rather, let’s let Metabase create some dashboards for us!

In the `Try These X-Rays Based On Your Data`section, click on the card with a **yellow lightning bolt**that says something like `A look at Products`. Metabase will generate a set of questions for you that you can save as a dashboard.

!Click on the **Save this**button, and Metabase will save the dashboard and its questions in a collectiontitled something like `A look at Products`.

This collection will be saved to a parent collection titled `Automatically Generated Dashboards`. You can find this collection by clicking on the Metabase logo in the upper left of the navigation bar to return to the home screen. From the home page, in the **Our Analytics**section, click on the `Automatically Generated Dashboards`section. From there you should see the collection `A look at your Products table`.

!Next, create a new collection. You can call it whatever you like; we’ll use the exciting name `Default collection`, and save it to the **Our Analytics**collection.

!Then we’ll move the `A look at Products`collection to our newly created `Default collection`. On the `A look at Products`collection page, click on the ellipses **…**and select **Move**.

Step 4 - Export from source Metabase
------------------------------------

Here’s where we actually start using Metabase’s serializationfeature.

With our `metabase-source`instance set up with some questions, now it’s time to export this data and import it into our `metabase-target`. That way we don’t have to manually recreate our Default Collection in the target Metabase.

Let’s first create a directory in our `/tmp`directory called `metabase_data`to store our export:

`cd/tmp
mkdir metabase_data`Next, we’ll run the export command.



