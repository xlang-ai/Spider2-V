Documentation Source:
www.metabase.com/docs/v0.49/questions/native-editor/writing-sql.md

Documentation Title:
The SQL editor

Documentation Content:
Running query selections

You can run your SQL query by pressing **ctrl + enter**on Windows and Linux, or **⌘ + return**on a Mac. You can also run only part of a query by highlighting the part you’d like to run before clicking the run button or using the run shortcut key.

Questions asked using SQL can be saved, downloaded, converted to models, and added to dashboards just like questions asked using the query builder.

You can also refer to models and saved questionsin your SQL queries.

Using SQL filters
-----------------

If you or someone else wrote a SQL query that includes variables, that question might have filter widgets at the top of the screen above the editor. Filter widgets let you modify the SQL query before it’s run, changing the results you might get.

!Writing SQL queries that use variables or parameters can be very powerful, but it’s also a bit more advanced, so that topic has its own page if you’d like to learn more.

SQL snippets
------------

You can use SQL snippetsto save, reuse, and share SQL code across multiple questions that are composed using the SQL editor.

How Metabase executes SQL queries
---------------------------------

When you run a query from the SQL editor, Metabase sends the query to your database exactly as it is written. Any results or errors displayed in Metabase are the same as the results or errors that you would get if you ran the query directly against your database. If the SQL syntax of your query doesn’t match the SQL dialect used by your database, your database won’t be able to run the query.

Question version history
------------------------

For questions, dashboards, and models, Metabase keeps a version history for the previous fifteen versions of that item.

See History.

Your SQL syntax must match the dialect used by the database
-----------------------------------------------------------

Make sure your SQL dialect matches the database you’ve selected. Common errors:



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
www.metabase.com/learn/sql-questions/organizing-sql.md

Documentation Title:
SQL Snippets vs. Saved Questions vs. Views

Documentation Content:
Subscribe to our newsletter

Stay in touch with updates and news from Metabase. No spam, ever.



Documentation Source:
www.metabase.com/docs/v0.49/permissions/data-sandboxes.md

Documentation Title:
Data sandboxes

Documentation Content:
Creating a SQL question for Metabase to display in an custom sandbox

In an advanced data sandbox, Metabase will display a saved question in place of an original table to a particular group.

**Use a SQL question**to define the exact rows and columns to be included in the sandbox. If you use a query builder (GUI) question, you might accidentally expose extra data, since GUI questions can include data from other saved questions or models.

Make sure to save the SQL question in an admin-only collection (collection permissionsset to **No access**for all groups except Administrators). For more info, see Permissions conflicts: saved SQL questions.



