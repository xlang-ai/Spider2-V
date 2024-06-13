Documentation Source:
www.metabase.com/learn/visualization/bar-charts.md

Documentation Title:
Master the bar chart visualization

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



Documentation Source:
www.metabase.com/docs/v0.49/troubleshooting-guide/visualization.md

Documentation Title:
Troubleshooting question and dashboard visualizations

Documentation Content:
when!Analytics dashboards
 Share insights with anyone, anywhere!SQL editor
 For advanced data users!Sandboxing
 Set boundaries around your data!Models
 A starting point for questions!Permissions
 Keep your data secure and private!CSV upload
 Go beyond VLOOKUPDocumentationResources!Learn!Blog!Events!Customers!Discussion!Partners!Community Stories!Startup Guide to Financial Modeling
 New!Community Data Stack Report
 NewPricingLog inv0.49Troubleshooting Guide
Troubleshooting question and dashboard visualizations
=====================================================

To start, check if your current browser settings are compatible with Metabase:

1. Clear your browser cache, and refresh your page.
2. Disable all extensions and plugins. Load the page again.
3. Give it one last shot—try opening your page in a private/incognito session, or a different browser.

Formatting dashboard cards
--------------------------

1. Make sure that you’re making and saving changes from the card’s settings(*not*the original question’s settings).
2. Reset your card’s visualization settings.

**Explanation**The visualization settings on a card are independent of the settings on the original question. When you first create a question, your selected visualization type is saved along with the query. When you add that question to a dashboard, the dashboard will display the same visualization as the original question by default. You can override the original visualization type by using the card’s visualization settings.

Visualizing SQL questions
-------------------------

Go to your SQL question and change the visualization typeto a table. Then, check if any of the following situations apply to the raw query results:

* Aggregations (counts, sums, etc.) are wrong.
* Results have duplicated rows.
* Results are missing rows.

**Explanation**If your question or dashboard card is powered by a handwritten SQL queryrather than the query builder, your visualization is going to be more sensitive to changes in the underlying data (for example, renamed fields, or the sudden appearance of a wild null value). To learn more, read about Common reasons for unexpected query results.

If you’re having problems with things like SQL syntax errors or SQL variables, see Troubleshooting SQL questionsfor more help.

Related problems
----------------

* My dates and times are wrong.



Documentation Source:
www.metabase.com/learn/visualization/index.md

Documentation Title:
Visualizing data

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



Documentation Source:
www.metabase.com/learn/visualization/histograms.md

Documentation Title:
Visualize your data as a histogram

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



