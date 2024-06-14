Documentation Source:
www.metabase.com/docs/v0.49/people-and-groups/managing.md

Documentation Title:
Managing people and groups

Documentation Content:
* If they log in using Google credentials, Metabase displays a Google icon.
* If they log in using an email address and password stored in Metabase, no icon is shown.

Note that the type of user is set when the account is first created: if you create a user in Metabase, but that person then logs in via Google or some other form of SSO, the latter’s icon will *not*show up next to their name.

Resetting someone’s password
----------------------------

If you’ve already configured your email settings, people can reset their passwords using the “forgot password” link on the login screen. If you haven’t yet configured your email settings, they will see a message telling them to ask an admin to reset their password for them.

To reset a password for someone, just click the three dots icon next to their account and choose **Reset Password**. If you haven’t configured your email settingsyet, you’ll be given a temporary password that you’ll have to share with that person. Otherwise, they’ll receive a password reset email.

Resetting the admin password
----------------------------

If you’re using Metabase Cloud, contact supportto reset your admin password.

If you’re a Metabase admin and have access to the server console, you can get Metabase to send you a password reset token:

1. Stop the running Metabase application.
2. Restart Metabase with `reset-password email@example.com`, where “email@example.com” is the email associated with the admin account:
 `java -jar metabase.jar reset-password email@example.com`
3. Metabase will print out a random token like this:

`...
Resetting password for email@example.com...

OK [[[1_7db2b600-d538-4aeb-b4f7-0cf5b1970d89]]]`
4. Start Metabase normally again (*without*the `reset-password`option).
5. Navigate to it in your browser using the path `/auth/reset_password/:token`, where “:token” is the token that was generated from the step above.



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



Documentation Source:
www.metabase.com/docs/v0.49/api/session.md

Documentation Title:
Session

Documentation Content:
PARAMS:

`username`value must be a non-blank string.

`password`value must be a non-blank string.

`request`
`POST /api/session/forgot_password`Send a reset email when user has forgotten their password.



