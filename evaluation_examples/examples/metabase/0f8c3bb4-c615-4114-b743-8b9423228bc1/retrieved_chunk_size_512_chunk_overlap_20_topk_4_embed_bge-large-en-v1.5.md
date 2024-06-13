Documentation Source:
www.metabase.com/learn/permissions/collection-permissions.md

Documentation Title:
Working with collection permissions

Documentation Content:
Configuring permissions to “Our analytics”
------------------------------------------

We’re going to revoke access to **Our analytics**, because Metabase grants the *most permissive*level of access across all of the groups that someone belongs to.

You can’t remove people from the All Users group, so if you give All Users **Curate**permissions to **Our analytics**, then that’ll always be the most permissive setting for everyone who uses your Metabase, regardless of any other group that you put people in.

1. Go to **Admin settings**> **Permissions**> **Collections**> **Our analytics**.
2. Click on the dropdown menu at the **All Users**row and **Collection access**column..
3. Select **No access**. Toggle on **Also change sub-collections**so that these permissions apply to all sub-collections nested under **Our analytics**.

!Creating new groups and collections
-----------------------------------

Next, we’ll create groups to match our Canoes and Sailboats teams. Go to **Admin settings**> **People**> **Groups**> Create a group, and call the group “Canoes”.

To create a new collection, we’ll go to the Metabase homepage and click **+ New**> **Collection**. We’ll create two collections named after our new groups, and save each of those collections inside **Our analytics**.

Setting collection permissions
------------------------------

We’ll set up collection permissions for the Canoes collection first, so that:

* The Canoes group can view and edit questions, dashboards, and models saved in the Canoes collection.
* The Canoes group can move, re-name, or archive the Canoes collection.
* The Sailboats group can only view the work that’s saved in the Canoes collection.

You can navigate back to **Admin settings**and go to the collection permissions page for each collection, or you can set up permissions directly from the Metabase homepage.

1. Click on the Canoes collection in the sidebar.
2. Click on the **lock icon**to open a collection permissions modal.
3. Select **Curate**from the dropdown menu for the **Canoes**row and **Collection access**column.
4. Select **View**from the dropdown menu for the **Sailboats**row and **Collection access**column.



Documentation Source:
www.metabase.com/docs/v0.49/people-and-groups/managing.md

Documentation Title:
Managing people and groups

Documentation Content:
All users

The **All Users**group is another special one. Every Metabase user is always a member of this group, though they can also be a member of as many other groups as you want. We recommend using the All Users group as a way to set default access levels for new Metabase users. If you have Google single sign-onenabled, new users who join that way will be automatically added to the All Users group.

It’s important that your All Users group should never have *greater*access for an item than a group for which you’re trying to restrict access — otherwise the more permissive setting will win out. See Setting permissions.

Creating a group
----------------

Go to **Admin settings**> **People**> **Groups**, and click the **Add a group**button.

We recommend creating groups that correspond to the teams your company or organization has, such as Human Resources, Engineering, Finance, and so on. By default, newly created groups don’t have access to anything.

To remove a group, click the X icon to the right of a group in the list to remove it (remember, you can’t remove the special default groups).

Adding people to groups
-----------------------

To add people to that group, click into a group and then click **Add members**.

To remove someone from that group, click on the **X**to the right of the group member.

You can also add or remove people from groups from the **People**list using the dropdown in the **Groups**column.

Group managers
--------------

Group managers is only available on Proand Enterpriseplans (both self-hosted and on Metabase Cloud).

**Group managers**can manage other people within their group.

Group managers can:

* Add or remove people from their group (that is, people who already have accounts in your Metabase).
* View all people in the **Admin settings**> **People**tab.
* Promote other people to group manager, or demote them from group manager to member.
* Rename their group.

Group managers are not admins, so their powers are limited. They cannot create new groups or invite new people to your Metabase.

Promoting/demoting group managers
---------------------------------

To promote someone to become a group manager:

1.



Documentation Source:
www.metabase.com/docs/v0.49/developers-guide/contributing.md

Documentation Title:
Contributing to Metabase

Documentation Content:
Help us triage and support other users

Spend time on discourse.metabase.com and on new issues and try to reproduce the bugs reported. For people having trouble with their databases where you have significant knowledge, help them out. Who knows, maybe they’ll end up helping you with something in the future.

It is helpful if you understand our prioritization frameworkwhen responding.



Documentation Source:
www.metabase.com/learn/getting-started/tour-of-metabase.md

Documentation Title:
A tour of Metabase

Documentation Content:
Submit a PR, or fork the source code

Metabase is open source, so if Metabase lacks a feature you need, you can always build it yourself. Check out our releasesto see the features we’ve added recently, and the roadmapfor what we’re working on next.

Further reading
---------------

* Stay up to date on our blog.
* Questions? See if they’ve been answered on our forum, or post a question yourself.
* Beyond BI: other problems you can solve with Metabase.

« PreviousNext »Did this article help you?
 

Yes
 No
 Send
 Thanks for your feedback!



