Documentation Source:
www.metabase.com/docs/v0.49/installation-and-operation/backing-up-metabase-application-data.md

Documentation Title:
Backing up Metabase

Documentation Content:
If you’re running the Metabase JAR

1. Navigate to your Metabase directory.
2. If your Metabase is running, stop the Metabase process. You can either close the terminal or kill the process with CTRL-C. If you are running the process as a service, then stop the service.
3. Copy the application database file (called `metabase.db.mv.db`) and keep that copy somewhere safe. That’s it.
4. Restart Metabase: `java -jar metabase.jar`or start the service again.



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
www.metabase.com/docs/v0.49/installation-and-operation/upgrading-metabase.md

Documentation Title:
Upgrading Metabase

Documentation Content:
Upgrading a JAR running locally

If you’re running the JVM Jar file directly:

Back up your application database.

2. Download the latest version of the JAR file:


	Metabase Open Source JARMetabase Pro or Enterprise JAR
Use a terminal to access your existing Metabase process and kill it (usually CTRL-C).

Replace the existing JAR file (`metabase.jar`) in your Metabase directory with the newer version.

5. Restart the server:

`java -jar metabase.jar`

On startup, Metabase will perform any tasks it needs to complete the upgrade. Once Metabase has completed those tasks, you’ll be running the new version.



Documentation Source:
www.metabase.com/docs/v0.49/installation-and-operation/running-the-metabase-jar-file.md

Documentation Title:
Running the Metabase JAR file

Documentation Content:
1. Install Java JRE

You may already have Java installed. To check the version, open a terminal and run:

`java -version`If Java isn’t installed, you’ll need to install Java before you can run Metabase. We recommend version 11 of JRE from Eclipse Temurinwith HotSpot JVM. You can run Metabase wherever Java 11 runs. The particular processor architecture shouldn’t matter (although we only test Metabase for x86 and ARM).



