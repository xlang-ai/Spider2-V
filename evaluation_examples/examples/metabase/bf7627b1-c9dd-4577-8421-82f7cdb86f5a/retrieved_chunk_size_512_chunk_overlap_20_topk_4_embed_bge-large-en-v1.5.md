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
www.metabase.com/docs/v0.49/databases/uploads.md

Documentation Title:
Uploading data

Documentation Content:
Models

You can archive a model by clicking on the three dots in the upper right and selecting **Archive**.

For deleting models completely, see Deleting items permanently.



Documentation Source:
www.metabase.com/docs/v0.49/exploration-and-organization/history.md

Documentation Title:
History

Documentation Content:
Unarchiving multiple items

You can unarchive multiple items at once from the same collection:

1. Go to the collection.
2. Hover over the icon beside the name of the item and click the checkbox that appears.
3. When you’re done selecting your items, click **Unarchive**at the bottom of the page.

Deleting items permanently
--------------------------

1. Open the main Metabase sidebar.
2. Click the `...`beside the “Collections” header in the sidebar.
3. Click **View archive**.
4. Hover over the item and click the **trash bin**icon.

The item will get permanently deleted from your application database.

Remember that archivingand deleting items can have unanticipated ripple effects on related dashboards, subscriptions, and SQL questions.

We recommend archiving because you can always unarchive if something breaks. If you delete an item and accidentally break something, you might have to recreate all of that work from scratch (unless you’re prepared to revert to a backup of your application database).



