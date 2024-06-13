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
www.metabase.com/docs/v0.49/questions/query-builder/introduction.md

Documentation Title:
Asking questions

Documentation Content:
when!Analytics dashboards
 Share insights with anyone, anywhere!SQL editor
 For advanced data users!Sandboxing
 Set boundaries around your data!Models
 A starting point for questions!Permissions
 Keep your data secure and private!CSV upload
 Go beyond VLOOKUPDocumentationResources!Learn!Blog!Events!Customers!Discussion!Partners!Community Stories!Startup Guide to Financial Modeling
 New!Community Data Stack Report
 NewPricingLog inv0.49Questions
Asking questions
================

Metabase’s two core concepts are questions and their corresponding answers. To ask a question in Metabase, click the **+ New**button in the upper right of the main navigation bar, and select either:

* Question
SQL query
This page covers how to ask a question using Metabase’s graphical query builder, the “Question” option.

Creating a new question with the query builder
----------------------------------------------

From the **+ New**dropdown, select **Question**, then pick your starting data:

You can start a question from:

* **A model**. A modelis a special kind of saved question meant to be used as a good starting point for questions. Sometimes these are called derived tables, as they usually pull together data from multiple raw tables.
* **Raw data**. You’ll need to specify the database and the table in that database as the starting point for your question.
* A **saved question**. You can use the results of any question as the starting point for a new question.

Note that there are some kinds of saved questions that can’t be used as source data:

* Druid questions
* Mongo questions
* Questions that use `Cumulative Sum`or `Cumulative Count`aggregations
* Questions that have columns that are named the same or similar thing, like `Count`and `Count 2`

The query builder
-----------------

Once you select your data, Metabase will take you to the query builder. Say you selected **Raw data**> **Sample database**> **Orders**, then you’ll see something like this:

!This is the query builder’s notebook editor. It has three default steps.



Documentation Source:
www.metabase.com/learn/getting-started/tour-of-metabase.md

Documentation Title:
A tour of Metabase

Documentation Content:
Create interactive dashboards

You can organize questions and models into a dashboard with tabs, and contextualize them with Markdowntext cards.

!You can add filters to dashboards and connect them to fields on questions to narrow the results.

!You can link filters, create custom destinations(to send people to another dashboard or external URL), or even have a chart update a filter on click.

To keep people posted on key metrics, you can set up dashboard subscriptionsvia email or Slack.

!### Embed questions and dashboards

You can embed charts and dashboardsusing iframes. On some paid plans, you can even embed the full Metabase app, which allows you to do things like deliver multi-tenant, self-service analytics.

Find things and stay organized
------------------------------

Things in this case being databases and their analysis: the questions, dashboards, and collections you and your teams create.



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



