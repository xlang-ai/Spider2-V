Documentation Source:
www.metabase.com/learn/administration/metabase-in-production.md

Documentation Title:
How to run Metabase in production

Documentation Content:
If you're self-hosting Metabase, here are some benchmarks and best practices.

This article describes what a production-ready setup of Metabase looks like, including server sizing, best practices, and pitfalls to avoid. This article is for people who are interested in self-hosting Metabase. If you want us to run Metabase for you, just sign up for a free trial.

What’s in the Metabase JARA JAR and a database are all you needWhy you need to use a separate application databaseIf you’ve already started using the default H2 database* Metabase application and database servers and their sizing
	Metabase application server sizeMetabase application database server size
Each Metabase environment must have its own dedicated application database* Maintenance
	Metabase server maintenanceMetabase application database maintenanceData warehouse server maintenance
Example load testAsync processes* Observability and some metrics to keep an eye on
	Metabase applicationMetabase application databaseWhen to increase the connection pool size
Using a load balancerLogsMetabase over HTTPS* Pitfalls to avoid
	We recommend that you avoid services that claim to scale automagicallyAvoid services that shut down servers when they’re not in useIssues with running on other cloud providers

What’s in the Metabase JAR
--------------------------

For context, Metabase is a web application. Its backend is written in Clojure, and its frontend is written in JavaScript, Typescript, and Clojurescript using the React framework.

By default, the entire application is self contained: the backend and the web server that serves the frontend are shipped in the same bundle. The bundle is a JAR file, which can be run anywhere a Java runtime environment is installed.

Metabase also ships a Docker container that packages up the JRE and Metabase JAR (which you can also run with Podman).

A JAR and a database are all you need
-------------------------------------

!To run Metabase in production, you need two things:

1. Either a Metabase JAR or the Docker image.
2.



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
www.metabase.com/docs/v0.49/installation-and-operation/running-metabase-on-debian.md

Documentation Title:
Running Metabase on Debian as a service with nginx

Documentation Content:
proxy requests to Metabase instance
server {
 listen 80;
 listen [::]:80;
 server_name your.domain.com;
 location / {
 proxy_pass http://127.0.0.1:3000;
 }
}`### Register your Metabase service

Now, it’s time to register our Metabase service with `systemd`so it will start up at system boot. We’ll also ensure our log file is created and owned by the unprivileged user our service runs the `metabase.jar`as.

`sudo systemctl daemon-reload
sudo systemctl start metabase.service
sudo systemctl status metabase.service`Once we are ok here, enable the service to startup during boot.

`sudo systemctl enable metabase.service`Start, stop, or restart Metabase
--------------------------------

Now, whenever you need to start, stop, or restart Metabase, all you need to do is:

`sudo systemctl start metabase.service
sudo systemctl stop metabase.service
sudo systemctl restart metabase.service`Read docs for other versions of Metabase.
 

Did this article help you?
 

Yes
 No
 Send
 Thanks for your feedback!

Want to improve these docs? Propose a change.##### Subscribe to our newsletter

Stay in touch with updates and news from Metabase. No spam, ever.



Documentation Source:
www.metabase.com/learn/administration/metabase-at-scale.md

Documentation Title:
Metabase at scale

Documentation Content:
Keep your browser up to date

Metabase is a web application, and can benefit from the latest and greatest versions of browsers like Firefox, Chrome, Edge, and Safari.

Supported deployments
---------------------

There are many ways to set up Metabase; some of our favorites include:

* AWS Elastic Beanstalk: Check out our guide to setting up Metabase on Elastic Beanstalk. We use Elastic Beanstalk to host our internal Metabase application.
* Docker: See running Metabase on Docker.

Google Cloud Platform, Microsoft Azure, Digital Ocean, and other cloud providers offer other great alternatives for hosting your Metabase application.

Hosted Metabase
---------------

If you don’t want to deal with the care and feeding of a Metabase application, Metabase offers a hosted solution. You still have to ensure your data sources are performant, but you no longer have to manage running the Metabase application.

Getting help
------------

If you still have questions, chances are someone’s already had the same question. Check out the Metabase discussion forumand search for your issue. If you can’t find a solution, submit a question of your own.

« PreviousNext »Did this article help you?
 

Yes
 No
 Send
 Thanks for your feedback!



