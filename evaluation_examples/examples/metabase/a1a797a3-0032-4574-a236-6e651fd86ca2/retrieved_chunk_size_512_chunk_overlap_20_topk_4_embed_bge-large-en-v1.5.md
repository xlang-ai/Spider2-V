Documentation Source:
www.metabase.com/docs/v0.49/troubleshooting-guide/cant-log-in.md

Documentation Title:
People can't log in to Metabase

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
People can’t log in to Metabase
===============================

No access to Metabase login page
--------------------------------

If you’re not a Metabase admin, you’ll have to tag them for help here.

1. Check that you have the correct site URLfrom **Settings**> **Admin settings**> **General**.
2. Check if the account is deactivated.

No access to Metabase Cloud account
-----------------------------------

The admin password for `store.metabase.com`(where you can find payment and subscription info) is not necessarily the same as the password for your Metabase instance (where you log in to look at data).

If you’ve forgotten your Metabase Cloud admin password, you can contact supportto reset the password.

Related topics
--------------

* Troubleshooting SAML.
* Troubleshooting LDAP.
* Resetting someone’s password.
* Resetting the admin password.
* Deleting an account that’s set up incorrectly.

Are you still stuck?
--------------------

If you can’t solve your problem using the troubleshooting guides:

* Search or ask the Metabase community.
* Search for known bugs or limitations.
Read docs for other versions of Metabase.
 

Did this article help you?
 

Yes
 No
 Send
 Thanks for your feedback!

Want to improve these docs? Propose a change.##### Subscribe to our newsletter

Stay in touch with updates and news from Metabase. No spam, ever.



Documentation Source:
www.metabase.com/docs/v0.49/api/util.md

Documentation Title:
Util

Documentation Content:
PARAMS:

- `password`password is too common.
« Back to API indexRead docs for other versions of Metabase.
 

Did this article help you?
 

Yes
 No
 Send
 Thanks for your feedback!

Want to improve these docs? Propose a change.##### Subscribe to our newsletter

Stay in touch with updates and news from Metabase. No spam, ever.



Documentation Source:
www.metabase.com/docs/v0.49/configuring-metabase/setting-up-metabase.md

Documentation Title:
Setting up Metabase

Documentation Content:
We won’t be able to connect to your database without it, but you’d like to deal with all of this later, that’s okay: just click **I’ll add my data later**. Metabase comes with a Sample Databasethat you can play around with to get a feel for how Metabase works.

If you’re ready to connect, here’s what you’ll need:

* The **hostname**of the server where your database lives
* The **port**the database server uses
* The **database name**
* The **username**you use for the database
* The **password**you use for the database

If you don’t have this information handy, the person responsible for administering the database should have it.

Connect to your database
------------------------

Now that you have your database info you can connect to your database. Sweet, sweet data at last. Just go ahead and put your info into this form and click **Next**.

!For more on connecting to databases, see Adding and managing databases.

Usage data preferences
----------------------

One last quick thing that you’ll have to decide is if it’s okay for us to collect some anonymous info about how you use the product — it helps us make Metabase better. Like the box says:

* Metabase never collects anything about your data or question results.
* All collection is completely anonymous.
* Collection can be turned off at any point in your admin settings.

!If you’re ready to start using Metabase, go ahead and click **Next**.

Staying in touch
----------------

At this point you are all set and ready to use Metabase. Since we like keeping in touch with our friends we made it easy to sign up for our newsletter (infrequent emails) with a single click!

!Once you’re done here simply follow the link to **Take me to Metabase**. And if you decided to skip the newsletter sign-up, it’s cool, we still like you :)

Getting started with Metabase
-----------------------------

For a tutorial on getting up and running with questions and dashboards, head over to Learn Metabase.

If you’d like more technical resources to set up your data stack with Metabase, connect with a Metabase Expert.



Documentation Source:
www.metabase.com/learn/administration/metabase-api.md

Documentation Title:
Working with the Metabase API

Documentation Content:
You can also use a session token to authenticate your requests. To get a session token, submit a request to the `/api/session`endpoint with your username and password:

`curl -XPOST \-H"Content-Type: application/json"\-d'{"username": "person@metabase.com", "password": "fakepassword"}'\http://localhost:3000/api/session`If you’re working with a remote server, you’ll need replace `localhost:3000`with your server address. This request will return a JSON object with a key called `id`and the token as the key’s value, e.g.:

`{"id":"38f4939c-ad7f-4cbe-ae54-30946daf8593"}`You can then include that session token in the headers of your subsequent requests like this:

`"X-Metabase-Session":"38f4939c-ad7f-4cbe-ae54-30946daf8593"`Some things to note about sessions:

* *By default, sessions are good for 14 days*. You can configure this session duration by setting the environment variable `MB_SESSION_AGE`(value is in minutes).
* *You should cache credentials*to reuse them until they expire, because logins are rate-limited for security.
*Invalid and expired session tokens return a 401 (Unauthorized) status code.** *Handle 401 status codes gracefully*. We recommend writing your code to fetch a new session token and automatically retry a request when the API returns a 401 status code.
* *Some endpoints require that the user be an admin, also known as a superuser*. Endpoints that require admin or superuser status (admin = superuser) generally say so in their documentation. They will return a 403 (Forbidden) status codeif the current user is not an admin.
* *If you would like an alternative authentication mechanism*feel free to upvote this feature request.

In short: use an API keyinstead.

Have fun
--------

If you have found this tutorial interesting, you can spin up a local instance of Metabase, experiment with the API, and have fun! If you get stuck, check out our forumto see if anyone’s run into a similar issue, or post a new question.



