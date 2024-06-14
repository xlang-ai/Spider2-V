Documentation Source:
www.metabase.com/docs/v0.49/configuring-metabase/email.md

Documentation Title:
Email

Documentation Content:
when!Analytics dashboards
 Share insights with anyone, anywhere!SQL editor
 For advanced data users!Sandboxing
 Set boundaries around your data!Models
 A starting point for questions!Permissions
 Keep your data secure and private!CSV upload
 Go beyond VLOOKUPDocumentationResources!Learn!Blog!Events!Customers!Discussion!Partners!Community Stories!Startup Guide to Financial Modeling
 New!Community Data Stack Report
 NewPricingLog inv0.49Configuring Metabase
Email
=====

Once you connect your database to Metabase, you’ll want to configure an email account to send system notifications to your organization’s users. Metabase uses email to reset passwords, onboard new users, and notify you when something happens.

To edit email settings:

1. Click on the **gear**icon in the upper right.
2. Select **Admin Settings**.
3. From the default **Settings**tab, click on **Email**in the left sidebar.

Metabase Cloud
--------------

Metabase Cloud manages an email server for you, so you don’t need to set up email (and you won’t see SMTP settings in your Admin console).

If you like, you can still set up:

* a name for your Cloud email account (from name)
* an email address to recieve email replies (reply-to address)

Configuring your email account
------------------------------

For Metabase to send messages to your organization’s users, you’ll need to set up an email account to send emails via **SMTP**(simple mail transfer protocol), which is an email standard that secures emails with SSL security protection.

To start, go to the Admin Panel from the dropdown menu in the top right of Metabase, then from the Settings page, click on **Email**in the left menu.

You should see this form:

!Here you’ll set:

* **SMTP HOST**: The address of the SMTP server that handles your emails.
* **SMTP PORT**: The port your SMTP server uses for outgoing emails.
* **SMTP SECURITY**:
	+ None
	+ SSL
	+ TLS
	+ STARTTLS
* **SMTP Username**.
* **SMTP Password**.

You’ll also need to specify your:

* **From address**: The email address you want to use for the sender of emails.



Documentation Source:
www.metabase.com/docs/v0.49/configuring-metabase/email.md

Documentation Title:
Email

Documentation Content:
Recommended email settings

* SSL is strongly recommended because it’s more secure and gives your account extra protection from threats.
* If your email service has a whitelist of email addresses that are allowed to send email, be sure to whitelist the email address that you put in the **From Address**field to ensure you and your teammates receive all emails from Metabase.

Notes for common email services
-------------------------------

Google AppsAmazon SESMandrill



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
www.metabase.com/docs/v0.49/api/email.md

Documentation Title:
Email

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
Email
=====

/api/email endpoints.

`DELETE /api/email/`Clear all email related settings. You must be a superuser or have `setting`permission to do this.

`POST /api/email/test`Send a test email using the SMTP Settings. You must be a superuser or have `setting`permission to do this.
 Returns `{:ok true}`if we were able to send the message successfully, otherwise a standard 400 error response.

`PUT /api/email/`Update multiple email Settings. You must be a superuser or have `setting`permission to do this.



