Documentation Source:
www.metabase.com/docs/v0.49/installation-and-operation/running-the-metabase-jar-file.md

Documentation Title:
Running the Metabase JAR file

Documentation Content:
3. Create a new directory and move the Metabase JAR into it

When you run Metabase, Metabase will create some new files, so it’s important to put the Metabase Jar file in a new directory before running it (so move it out of your downloads folder and put it a new directory).

On posix systems, the commands would look something like this:

Assuming you downloaded to `/Users/person/Downloads`:

`mkdir ~/metabase`then

`mv /Users/person/Downloads/metabase.jar ~/metabase`### 4. Change into your new Metabase directory and run the jar

Change into the directory you created in step 2:

`cd ~/metabase`Now that you have Java working you can run the JAR from a terminal with:

`java -jar metabase.jar`Metabase will start using the default settings. You should see some log entries starting to run in your terminal window showing you the application progress as it starts up. Once Metabase is fully started you’ll see a confirmation such as:

`...
06-19 10:29:34 INFO metabase.task :: Initializing task CheckForNewVersions
06-19 10:29:34 INFO metabase.task :: Initializing task SendAnonymousUsageStats
06-19 10:29:34 INFO metabase.task :: Initializing task SendAbandomentEmails
06-19 10:29:34 INFO metabase.task :: Initializing task SendPulses
06-19 10:29:34 INFO metabase.task :: Initializing task SendFollowUpEmails
06-19 10:29:34 INFO metabase.task :: Initializing task TaskHistoryCleanup
06-19 10:29:34 INFO metabase.core :: Metabase Initialization COMPLETE`At this point you’re ready to go! You can access your new Metabase server on port 3000, most likely at `http://localhost:3000`.

You can use another port than 3000 by setting the `MB_JETTY_PORT`environment variablebefore running the jar.

If you are using a paid version of Metabase, be sure to activate your license.



Documentation Source:
www.metabase.com/docs/v0.49/installation-and-operation/running-the-metabase-jar-file.md

Documentation Title:
Running the Metabase JAR file

Documentation Content:
Production application database

Here are some databases we support.

For example, say you want to use PostgreSQL. You would get a PostgreSQL service up and running and create an empty database:

`createdb metabaseappdb`You can call your app db whatever you want. And there’s no need to create any tables in that database; Metabase will do that for you. You’ll just need to set environment variables for Metabase to use on startup so Metabase knows how to connect to this database.

You’ll create a directory for your Metabase like in the steps listed above for the Local installation, but when it’s time to run the `java -jar`command to start up the JAR, you’ll prefix the command with some environment variables to tell Metabase how to connect to the `metabaseappdb`you created:

`export MB_DB_TYPE=postgres
export MB_DB_DBNAME=metabaseappdb
export MB_DB_PORT=5432
export MB_DB_USER=username
export MB_DB_PASS=password
export MB_DB_HOST=localhost
java -jar metabase.jar`The above command would connect Metabase to your Postgres database, `metabaseappdb`via `localhost:5432`with the user account `username`and password `password`. If you’re running Metabase as a service, you’ll put these environment variables in a separate configuration file.



Documentation Source:
www.metabase.com/docs/v0.49/installation-and-operation/running-the-metabase-jar-file.md

Documentation Title:
Running the Metabase JAR file

Documentation Content:
1. Install Java JRE

You may already have Java installed. To check the version, open a terminal and run:

`java -version`If Java isn’t installed, you’ll need to install Java before you can run Metabase. We recommend version 11 of JRE from Eclipse Temurinwith HotSpot JVM. You can run Metabase wherever Java 11 runs. The particular processor architecture shouldn’t matter (although we only test Metabase for x86 and ARM).



Documentation Source:
www.metabase.com/docs/v0.49/installation-and-operation/running-the-metabase-jar-file.md

Documentation Title:
Running the Metabase JAR file

Documentation Content:
when!Analytics dashboards
 Share insights with anyone, anywhere!SQL editor
 For advanced data users!Sandboxing
 Set boundaries around your data!Models
 A starting point for questions!Permissions
 Keep your data secure and private!CSV upload
 Go beyond VLOOKUPDocumentationResources!Learn!Blog!Events!Customers!Discussion!Partners!Community Stories!Startup Guide to Financial Modeling
 New!Community Data Stack Report
 NewPricingLog inv0.49Installation and Operation
Running the Metabase OSS JAR file
=================================

To run the free, Open Source version of Metabase via a JAR file, you will need to have a Java Runtime Environment (JRE) installed on your system.

If you have a token for the Pro or Enterprise editionsof Metabase, see Activating your Metabase commercial license.

Quick start
-----------

The quick start is intended for running Metabase locally. See below for instructions on running Metabase in production.

If you have Java installed:

1. Download the JAR file for Metabase OSS. If you’re on a Proor Enterpriseplan, download the JAR for the Enterprise Edition.
2. Create a new directory and move the Metabase JAR into it.
3. Change into your new Metabase directory and run the JAR.

`java -jar metabase.jar`Metabase will log its progress in the terminal as it starts up. Wait until you see “Metabase Initialization Complete” and visit `http://localhost:3000/setup`.

If you are using a paid version, be sure to activate your license.

Local installation
------------------

If you just want to try Metabase out, play around with Metabase, or just use Metabase on your local machine, Metabase ships with a default application database that you can use. **This setup is not meant for production**. If you intend to run Metabase for real at your organization, see Production installation.

The below instructions are the same as the quick start above, just with a little more context around each step.



