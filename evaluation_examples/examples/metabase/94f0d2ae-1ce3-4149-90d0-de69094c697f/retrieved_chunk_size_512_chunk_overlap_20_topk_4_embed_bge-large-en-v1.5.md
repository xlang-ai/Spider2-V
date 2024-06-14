Documentation Source:
www.metabase.com/docs/v0.49/configuring-metabase/config-file.md

Documentation Title:
Configuration file

Documentation Content:
Additionally, you can specify a user account as an admin by using the `is_superuser: true`key.

In the following example, assuming that the Metabase hasn’t already been set up (which creates the first user) both users `first@example.com`and `admin@example.com`will be admins: `first@example.com`because it’s the first user account on the list, and `admin@example.com`because that user has the `is_superuser`flag set to true.

`version: 1
config:
 users:
 - first_name: First
 last_name: Person
 password: metabot1
 email: first@example.com
 - first_name: Normal
 last_name: Person
 password: metabot1
 email: normal@example.com
 - first_name: Admin
 last_name: Person
 password: metabot1
 is_superuser: true
 email: admin@example.com`If the Metabase has already been set up, then `first @example.com`will be loaded as a normal user.

Databases
---------

On a new Metabase, the example below sets up an admin user account and one database connection.

`version: 1
config:
 users:
 - first_name: Cam
 last_name: Era
 password: 2cans3cans4cans
 email: cam@example.com
 databases:
 - name: test-data (Postgres)
 engine: postgres
 details:
 host: localhost
 port: 5432
 user: dbuser
 password: "{{ env POSTGRES_TEST_DATA_PASSWORD }}"
 dbname: test-data`To determine which keys you can specify for a database, check out the fields available in Metabase itself for the database that you want to add.

Referring to environment variables in the `config.yml`
------------------------------------------------------

As shown in the Databases example above, environment variables can be specified with `{{ template-tags }}`like `{{ env POSTGRES_TEST_DATA_PASSWORD }}`or `[[options {{template-tags}}]]`.

Metabase doesn’t support recursive expansion, so if one of your environment variables references *another*environment variable, you’re going to have a bad time.

Disable initial database sync
-----------------------------

When loading a data model from a serialized export, you want to disable the scheduler so that the Metabase doesn’t try to sync.



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
www.metabase.com/docs/v0.49/configuring-metabase/setting-up-metabase.md

Documentation Title:
Setting up Metabase

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
Setting up Metabase
===================

This guide will help you set up Metabase once you’ve gotten it installed. If you haven’t installed Metabase yet, you can get Metabase here.

Start Metabase up for the first time and you’ll see this screen:
!

Go ahead and click **Let’s get started**.

Setting up an admin account
---------------------------

The first thing you’ll need to do is set up an admin account. The account you create when you first install Metabase is an admin account by default — handy! If you’ve installed Metabase on a production server, you should be really careful to remember the password for this account since it will be used to add other users, connect to databases, set up email, and more. You can also create additional admin accounts later.

For now, let’s just create an account for ourselves to explore Metabase. Type in your info, and when you’re ready to continue, click the **Next**button.

!What will you use Metabase for?
-------------------------------

Let us know your plans with Metabase so that we can best guide you.

!* Self-service analytics for my own company
* Embedding analytics into my application
* A bit of both
* Not sure yet

Don’t worry about picking the wrong option. If you say you’re interested in embedding, Metabase will display a card with a link to the embedding settings when you (the admin) first log in to your instance. Just a little convenience thing, that’s all.

Gathering your database info
----------------------------

At this point you’ll need to gather some information about the database you want to use with Metabase.



Documentation Source:
www.metabase.com/learn/administration/metabase-api.md

Documentation Title:
Working with the Metabase API

Documentation Content:
Provision a Metabase instance

In addition to using environment variables, you can use the Metabase API to setup an instance of Metabase. Once you have installed Metabase using your preferred method, and the Metabase server is up and running, you can create the first user (as an Admin) by posting to a special endpoint, /api/setup. This `/api/setup`endpoint:

* Creates the first user as an Admin (superuser).
* Logs them in.
* Returns a session ID.

You can then configure settings using the `/api/settings`endpoint, set up email using the `/api/email`endpoint, and use the `/api/setup/admin_checklist`endpoint to verify your setup progress.

!### Add a data source

You can add a new database using the `POST /api/database/`endpoint, and validate that database’s connection details using the `/api/setup/validate`endpoint. Once you’ve connected the database to your Metabase instance, you can rescan the database and update the schema metadata. You can even add our trusty Sample Databaseas a new database to your instance with `POST /api/database/sample_database`.

Here’s an example database creation call for a Redshiftdatabase.

`curl -s-XPOST \-H"Content-type: application/json"\-H'x-api-key: YOUR_API_KEY'\http://localhost:3000/api/database \-d'{
 "engine": "redshift",
 "name": "Redshift",
 "details": {
 "host": "redshift.aws.com",
 "port": "5432",
 "db": "dev",
 "user": "root",
 "password": "password"
 }
 }'`### Set up users, groups, and permissions

You can use the `/api/user`endpoints to create, update, and disable users, or the `/api/permissions`endpoints to set up groups or add users to them.



