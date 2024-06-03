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
www.metabase.com/docs/v0.49/api/database.md

Documentation Title:
Database

Documentation Content:
PARAMS:

- `id`value must be an integer greater than zero.
`POST /api/database/sample_database`Add the sample database as a new `Database`.

You must be a superuser to do this.

`POST /api/database/validate`Validate that we can connect to a database given a set of details.

You must be a superuser to do this.



Documentation Source:
www.metabase.com/learn/administration/serialization.md

Documentation Title:
Serialization: preloading dashboards in a new Metabase instance

Documentation Content:
Add users to our source Metabase

Let’s add one Admin account, and two basic users to our metabase-source instance.

You can add users to your Metabase manually(i.e., in the Metabase application), but here’s a quick bash script that creates an Admin user (the initial user) and two basic users:

You’ll need to have jqinstalled to handle the JSON in this script.

`#!/bin/shADMIN_EMAIL=${MB_ADMIN_EMAIL:-admin@metabase.local}ADMIN_PASSWORD=${MB_ADMIN_PASSWORD:-Metapass123}METABASE_HOST=${MB_HOSTNAME}METABASE_PORT=${MB_PORT:-3000}echo"⌚︎ Waiting for Metabase to start"while(!curl -s-m5 http://${METABASE_HOST}:${METABASE_PORT}/api/session/properties -o/dev/null);do sleep 5;done

echo"😎 Creating admin user"SETUP_TOKEN=$(curl -s-m5 -XGET \-H"Content-Type: application/json"\http://${METABASE_HOST}:${METABASE_PORT}/api/session/properties \| jq -r'.



Documentation Source:
www.metabase.com/learn/administration/metabase-api.md

Documentation Title:
Working with the Metabase API

Documentation Content:
« PreviousNext »Did this article help you?
 

Yes
 No
 Send
 Thanks for your feedback!



