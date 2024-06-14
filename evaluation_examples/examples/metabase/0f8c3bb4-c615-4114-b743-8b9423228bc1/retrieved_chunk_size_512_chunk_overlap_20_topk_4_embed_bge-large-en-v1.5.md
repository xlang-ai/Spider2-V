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
www.metabase.com/docs/v0.49/people-and-groups/managing.md

Documentation Title:
Managing people and groups

Documentation Content:
when!Analytics dashboards
 Share insights with anyone, anywhere!SQL editor
 For advanced data users!Sandboxing
 Set boundaries around your data!Models
 A starting point for questions!Permissions
 Keep your data secure and private!CSV upload
 Go beyond VLOOKUPDocumentationResources!Learn!Blog!Events!Customers!Discussion!Partners!Community Stories!Startup Guide to Financial Modeling
 New!Community Data Stack Report
 NewPricingLog inv0.49People and Groups
Managing people and groups
==========================

To start managing people, click on the **gear**icon > **Admin settings**> **People**. You’ll see a list of all the people in your organization.

!Creating an account
-------------------

To add a new person, click **Invite someone**in the upper right corner. You’ll be prompted to enter their email, and optionally their first and last names–only the email is required.

Click **Create**to activate an account. An account becomes active once you click **Create**, even if the person never signs into the account. The account remains active until you deactivate the account. If you’re on a paid Metabase plan, all active accounts will count toward your user account total. If one person has more than one account, each account will count toward the total (see how billing works).

If you’ve already configured Metabase to use email, Metabase will send the person an email inviting them to log into Metabase. If you haven’t yet setup email for your Metabase, Metabase will give you a temporary password that you’ll have to manually send to the person.

Editing an account
------------------

You can edit someone’s name and email address by clicking the three dots icon and choosing **Edit user**.

Be careful: changing an account’s email address *will change the address the person will use to log in to Metabase*.

Adding a user attribute
-----------------------

User attributes is only available on Proand Enterpriseplans (both self-hosted and on Metabase Cloud).

To add a user attribute manually:

1. Go to **Admin settings**> **People**.
2. Find the person’s account and click the **three dot**(…) menu.
3. Click **Edit user**.
4.



Documentation Source:
www.metabase.com/docs/v0.49/people-and-groups/managing.md

Documentation Title:
Managing people and groups

Documentation Content:
At the top right of the screen, click the **gear**icon > **Admin settings**> **People**> **Groups**.
2. Select the group you want the person to manage. If the person isn’t already in the group, you’ll need to add that person to the group.
3. Find the person you want to promote, hover over their member type, and click the up arrow to promote them to group manager. If you want to demote them, click on the down arrow.

Further reading
---------------

* Configure Single Sign-On (SSO).
* Permissions strategies.
* Multi-tenant permissions.
Read docs for other versions of Metabase.
 

Did this article help you?
 

Yes
 No
 Send
 Thanks for your feedback!

Want to improve these docs? Propose a change.##### Subscribe to our newsletter

Stay in touch with updates and news from Metabase. No spam, ever.



Documentation Source:
www.metabase.com/docs/v0.49/embedding/interactive-embedding-quick-start-guide.md

Documentation Title:
Interactive embedding quick start

Documentation Content:
Add a `groups`key to your token

Recall the `signUserToken`function used to create the JWTs. Add a `groups`key to the signed token that maps to an array. Metabase will look at the values in that array to see if any of the values map to a group in Metabase (We’ll walk through mapping groups in a bit).

`constsignUserToken=user=>jwt.sign({email:user.email,first_name:user.firstName,last_name:user.lastName,groups:["Customer-Acme"],exp:Math.round(Date.now()/1000)+60*10,// 10 minute expiration},METABASE_JWT_SHARED_SECRET,);`### Create a group in Metabase

In Metabase, click the **gear**icon and go to **Admin settings**> **People**> **Groups**. Click the **Create a group**button. Add a group that corresponds with a group in your app. If you’re using the sample app, add a group called `Customer Acme`.



