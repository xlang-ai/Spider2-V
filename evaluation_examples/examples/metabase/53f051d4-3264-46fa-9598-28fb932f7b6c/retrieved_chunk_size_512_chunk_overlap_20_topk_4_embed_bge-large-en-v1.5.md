Documentation Source:
www.metabase.com/learn/administration/serialization.md

Documentation Title:
Serialization: preloading dashboards in a new Metabase instance

Documentation Content:
["setup-token"]')MB_TOKEN=$(curl -s-XPOST \-H"Content-type: application/json"\http://${METABASE_HOST}:${METABASE_PORT}/api/setup \-d'{
 "token": "'${SETUP_TOKEN}'",
 "user": {
 "email": "'${ADMIN_EMAIL}'",
 "first_name": "Metabase",
 "last_name": "Admin",
 "password": "'${ADMIN_PASSWORD}'"
 },
 "prefs": {
 "allow_tracking": false,
 "site_name": "Metawhat"
 }
}'| jq -r'.id')echo-e"\n👥 Creating some basic users: "curl -s"http://${METABASE_HOST}:${METABASE_PORT}/api/user"\-H'Content-Type: application/json'\-H"X-Metabase-Session: ${MB_TOKEN}"\-d'{"first_name":"Basic","last_name":"User","email":"basic@somewhere.com","login_attributes":{"region_filter":"WA"},"password":"'${ADMIN_PASSWORD}'"}'curl -s"http://${METABASE_HOST}:${METABASE_PORT}/api/user"\-H'Content-Type: application/json'\-H"X-Metabase-Session: ${MB_TOKEN}"\-d'{"first_name":"Basic 2","last_name":"User","email":"basic2@somewhere.com","login_attributes":{"region_filter":"CA"},"password":"'${ADMIN_PASSWORD}'"}'echo-e"\n👥 Basic users created!"`Save the above code as `create_users.sh`, and make it executable:

`chmod+x create_users.sh`Then run:

`MB_HOSTNAME=localhost MB_PORT=5001 ./create_users.sh`With your metabase-source instance up, and your users created, open up `http://localhost:5001`and sign in as the admin user you created. The user ID is `admin@metabase.local`and the password is `Metapass123`.

You should see a fresh instance of Metabase.

!Once you log in, activate your license key.

Step 3 - Create dashboards and collections in the source Metabase
-----------------------------------------------------------------

We’ll need some application data to export, so let’s create some dashboards using the Sample Databaseincluded with Metabase.



Documentation Source:
www.metabase.com/docs/v0.49/api/setup.md

Documentation Title:
Setup

Documentation Content:
PARAMS:

`token``POST /api/setup/`Special endpoint for creating the first user during setup. This endpoint both creates the user AND logs them in and
 returns a session ID. This endpoint can also be used to add a database, create and invite a second admin, and/or
 set specific settings from the setup flow.



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
www.metabase.com/docs/v0.49/api/setup.md

Documentation Title:
Setup

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
Setup
=====

API endpoints for Setup.

`GET /api/setup/admin_checklist`Return various “admin checklist” steps and whether they’ve been completed. You must be a superuser to see this!

`GET /api/setup/user_defaults`Returns object containing default user details for initial setup, if configured,
 and if the provided token value matches the token in the configuration value.



