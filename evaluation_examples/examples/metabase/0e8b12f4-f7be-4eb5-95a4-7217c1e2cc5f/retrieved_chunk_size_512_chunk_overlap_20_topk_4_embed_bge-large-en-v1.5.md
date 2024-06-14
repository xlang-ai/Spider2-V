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
www.metabase.com/docs/v0.49/questions/query-builder/introduction.md

Documentation Title:
Asking questions

Documentation Content:
Creating custom columns

!Custom columns are helpful when you need to create a new column based on a calculation, such as subtracting the value of one column from another, or extracting a portion of an existing text column. Custom columns that you add aren’t permanently added to your table; they’ll only be present in the given question.

You can use the following math operators in your formulas: `+`, `–`, `*`(multiplication), and `/`(division), along with a whole host of spreadsheet-like functions. You can also use parentheses to clarify the order of operations.

Adding or removing columns in a table
-------------------------------------

When viewing tables, you can click on the **gear**icon in the bottom left to bring up the columns picker. Click **Add or remove columns**to search for and pick columns, including columns from related tables.

!Sorting results
---------------

!The sorting step lets you pick one or more columns to sort your results by. For each column you pick, you can also choose whether to sort ascending or descending; just click the arrow to change from ascending (up arrow) to descending (down arrow).

Setting a row limit
-------------------

The row limit step lets you limit how many rows you want from the previous results. When used in conjunction with sorting, this can let you do things like create a top-10 list, by first sorting by one of the columns in your result, then adding a row limit of 10. Unlike other steps, the row limit step can only be added at the end of your question.

Viewing the SQL that powers your question
-----------------------------------------

Under the hood, all Metabase questions are SQL (gasp!). If you’re curious to see the SQL that will get run when you ask your question, you can click the little console icon in the top-right of the notebook editor. In the modal that opens up, you’ll also be given the option to start a new query in the SQL editor using this generated SQL as a starting point (assuming you have SQL permissionsto that database). It’s a nice little shortcut to have Metabase write some boilerplate SQL for you, but then allows you to tweak and customize the query.

Play around with saved questions
--------------------------------

Each time you start modifying a saved question, Metabase will create a new question for you.



Documentation Source:
www.metabase.com/learn/questions/drill-through.md

Documentation Title:
Create interactive charts

Documentation Content:
Use SQL to create a model

If you write a question using SQL, you won’t get drill-through out of the box. But you can still get the Action Menu if you:

1. Write a question in SQL that brings together the starting data you need, like you’re creating a view for people to query. So don’t pre-filter or pre-summarize the data (aside from filtering out rows and columns you wish to exclude from the “view”).
2. Save that question and turn it into a model.
3. Edit the model’s metadatato specify each column’s type. If Metabase knows which type of data each column contains, it can work its drill-through sorcery.

From there, you can either let people use the model as the starting point for people to ask questions with the query builder, or you can create query builder questions based on that model for people to play around with.

The other option for SQL-based questions is to…



Documentation Source:
www.metabase.com/learn/getting-started/tour-of-metabase.md

Documentation Title:
A tour of Metabase

Documentation Content:
Native queries

Use the **native query editor**to compose questions in the database’s native query languages (typically SQL for relational databases, but also other query languages for data sources like MongoDB). For questions written in SQL, you can use variables in your code to create SQL templates, including field filtervariables that can create smart dropdown filters.

!Like query builder questions, you can use the results of models or saved questionsas starting points for new questions, just as you would a table or view. For example, to reference question 123 like so:

`WITHgizmo_ordersAS#{123}`### Create models to use as starting data for new questions

Modelsare built with questions from either the query builder or the SQL editor. You can use them to pull together data from multiple tables, with custom, calculated columns, and column descriptions and other metadata, to create great starting data for people to ask new questions. For example, you could build a model for “Active users”, or “Priority orders”, or however you want to model your business.

If you find that you’re using the same saved question over and over as your starting data for new questions, you may want to convert that saved question to a model, which will let you add metadata like column descriptions and column types. You can also refer to models in SQL queries, just like we did above with saved questions.



