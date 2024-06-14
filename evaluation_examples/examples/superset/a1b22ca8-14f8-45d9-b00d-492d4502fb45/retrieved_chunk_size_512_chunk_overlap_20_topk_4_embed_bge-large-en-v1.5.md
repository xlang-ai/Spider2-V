Documentation Source:
superset.apache.org/docs/using-superset/exploring-data/index.md

Documentation Title:
Exploring Data in Superset | Superset

Documentation Content:
Publishing Your Dashboard​

If you have followed all of the steps outlined in the previous section, you should have a dashboard
that looks like the below. If you would like, you can rearrange the elements of the dashboard by
selecting **Edit dashboard**and dragging and dropping.

If you would like to make your dashboard available to other users, simply select Draft next to the
title of your dashboard on the top left to change your dashboard to be in Published state. You can
also favorite this dashboard by selecting the star.

!### Annotations​

Annotations allow you to add additional context to your chart. In this section, we will add an
annotation to the Tutorial Line Chart we made in a previous section. Specifically, we will add the
dates when some flights were cancelled by the UK’s Civil Aviation Authority in response to the
eruption of the Grímsvötn volcano in Iceland (23-25 May 2011).

First, add an annotation layer by navigating to Manage ‣ Annotation Layers. Add a new annotation
layer by selecting the green plus sign to add a new record. Enter the name Volcanic Eruptions and
save. We can use this layer to refer to a number of different annotations.

Next, add an annotation by navigating to Manage ‣ Annotations and then create a new annotation by
selecting the green plus sign. Then, select the Volcanic Eruptions layer, add a short description
Grímsvötn and the eruption dates (23-25 May 2011) before finally saving.

!Then, navigate to the line chart by going to Charts then selecting Tutorial Line Chart from the
list. Next, go to the Annotations and Layers section and select Add Annotation Layer. Within this
dialogue:

* Name the layer as Volcanic Eruptions
* Change the Annotation Layer Type to Event
* Set the Annotation Source as Superset annotation
* Specify the Annotation Layer as Volcanic Eruptions

!Select **Apply**to see your annotation shown on the chart.

!If you wish, you can change how your annotation looks by changing the settings in the Display
configuration section. Otherwise, select **OK**and finally **Save**to save your chart.



Documentation Source:
superset.apache.org/docs/contributing/guidelines/index.md

Documentation Title:
Guidelines | Superset

Documentation Content:
How to refer to UI elements​

When writing about a UI element, use the same capitalization as used in the UI.

For example, if an input field is labeled “Name” then you refer to this as the “Name input field”. Similarly, if a button has the label “Save” in it, then it is correct to refer to the “Save button”.

Where a product page is titled “Settings”, you refer to this in writing as follows:
“Edit your personal information on the Settings page”.

Often a product page will have the same title as the objects it contains. In this case, refer to the page as it appears in the UI, and the objects as common nouns:

* Upload a dashboard on the Dashboards page
* Go to Dashboards
* View dashboard
* View all dashboards
* Upload CSS templates on the CSS templates page
* Queries that you save will appear on the Saved queries page
* Create custom queries in SQL Lab then create dashboards



Documentation Source:
superset.apache.org/docs/contributing/development/index.md

Documentation Title:
Setting up a Development Environment | Superset

Documentation Content:
Adding a DB migration​

1. Alter the model you want to change. This example will add a `Column`Annotations model.

Example commit
2. Generate the migration file

superset db migrate -m 'add\_metadata\_column\_to\_annotation\_model'This will generate a file in `migrations/version/{SHA}_this_will_be_in_the_migration_filename.py`.

Example commit
3. Upgrade the DB

superset db upgradeThe output should look like this:

`INFO [alembic.runtime.migration] Context impl SQLiteImpl.INFO [alembic.runtime.migration] Will assume transactional DDL.INFO [alembic.runtime.migration] Running upgrade 1a1d627ebd8e -> 40a0a483dd12, add_metadata_column_to_annotation_model.py`
4. Add column to view

Since there is a new column, we need to add it to the AppBuilder Model view.

Example commit
5. Test the migration's `down`method

superset db downgradeThe output should look like this:

`INFO [alembic.runtime.migration] Context impl SQLiteImpl.INFO [alembic.runtime.migration] Will assume transactional DDL.INFO [alembic.runtime.migration] Running downgrade 40a0a483dd12 -> 1a1d627ebd8e, add_metadata_column_to_annotation_model.py`



Documentation Source:
superset.apache.org/docs/using-superset/exploring-data/index.md

Documentation Title:
Exploring Data in Superset | Superset

Documentation Content:
Otherwise, select **OK**and finally **Save**to save your chart. If you keep
the default selection to overwrite the chart, your annotation will be saved to the chart and also
appear automatically in the Tutorial Dashboard.



