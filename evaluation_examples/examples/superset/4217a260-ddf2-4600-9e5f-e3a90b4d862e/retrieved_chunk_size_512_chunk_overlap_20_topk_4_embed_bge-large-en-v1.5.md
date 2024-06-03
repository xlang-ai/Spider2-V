Documentation Source:
superset.apache.org/docs/contributing/development/index.md

Documentation Title:
Setting up a Development Environment | Superset

Documentation Content:
)​
------------------------------

Setting things up to squeeze an "hello world" into any part of Superset should be as simple as

docker-composeupNote that:

* this will pull/build docker images and run a cluster of services, including:
	+ A Superset **Flask web server**, mounting the local python repo/code
	+ A Superset **Celery worker**, also mounting the local python repo/code
	+ A Superset **Node service**, mounting, compiling and bundling the JS/TS assets
	+ A Superset **Node websocket service**to power the async backend
	+ **Postgres**as the metadata database and to store example datasets, charts and dashboards whic
	should be populated upon startup
	+ **Redis**as the message queue for our async backend and caching backend
* It'll load up examples into the database upon first startup
* all other details and pointers available in
docker-compose.yml
* The local repository is mounted withing the services, meaning updating
the code on the host will be reflected in the docker images
* Superset is served at localhost:8088/
* You can login with admin/admin

cautionSince `docker-compose`is primarily designed to run a set of containers on **a single host**and can't credibly support **high availability**as a result, we do not support nor recommend
using our `docker-compose`constructs to support production-type use-cases. For single host
environments, we recommend using minikubealong
our installing on k8sdocumentation.
configured to be secure.

Installing Development Tools​
-----------------------------

noteWhile docker-compose simplifies a lot of the setup, there are still
many things you'll want to set up locally to power your IDE, and things like
**commit hooks**, **linters**, and **test-runners**. Note that you can do these
things inside docker images with commands like `docker-compose exec superset_app bash`for
instance, but many people like to run that tooling from their host.



Documentation Source:
superset.apache.org/docs/contributing/index.md

Documentation Title:
Contributing to Superset | Superset

Documentation Content:
Report Bug​

The best way to report a bug is to file an issue on GitHub. Please include:

* Your operating system name and version.
* Superset version.
* Detailed steps to reproduce the bug.
* Any details about your local setup that might be helpful in troubleshooting.

When posting Python stack traces, please quote them using
Markdown blocks.

*Please note that feature requests opened as GitHub Issues will be moved to Discussions.*### Submit Ideas or Feature Requests​

The best way is to start an "Ideas" Discussion threadon GitHub:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that your contributions are as welcome as anyone's :)

To propose large features or major changes to codebase, and help usher in those changes, please create a **Superset Improvement Proposal (SIP)**. See template from SIP-0



Documentation Source:
superset.apache.org/docs/contributing/development/index.md

Documentation Title:
Setting up a Development Environment | Superset

Documentation Content:
fs.inotify.max\_user\_watches=524288Save the file and exit editor.
To confirm that the change succeeded, run the following command to load the updated value of max\_user\_watches from sysctl.conf:

sudosysctl -p#### Webpack dev server​

The dev server by default starts at `http://localhost:9000`and proxies the backend requests to `http://localhost:8088`.

So a typical development workflow is the following:

1. run Superset locallyusing Flask, on port `8088`— but don't access it directly,`# Install Superset and dependencies, plus load your virtual environment first, as detailed above.superset run -p 8088--with-threads --reload --debugger --debug`
2. in parallel, run the Webpack dev server locally on port `9000`,npmrun dev-server
3. access `http://localhost:9000`(the Webpack server, *not*Flask) in your web browser. This will use the hot-reloading front-end assets from the Webpack development server while redirecting back-end queries to Flask/Superset: your changes on Superset codebase — either front or back-end — will then be reflected live in the browser.

It's possible to change the Webpack server settings:

`# Start the dev server at http://localhost:9000npmrun dev-server# Run the dev server on a non-default portnpmrun dev-server -- --port=9001# Proxy backend requests to a Flask server running on a non-default portnpmrun dev-server -- --env=--supersetPort=8081# Proxy to a remote backend but serve local assetsnpmrun dev-server -- --env=--superset=https://superset-dev.example.com`The `--superset=`option is useful in case you want to debug a production issue or have to setup Superset behind a firewall. It allows you to run Flask server in another environment while keep assets building locally for the best developer experience.



Documentation Source:
superset.apache.org/docs/installation/docker-compose/index.md

Documentation Title:
Docker Compose | Superset

Documentation Content:
Skip to main content!!DocumentationGetting StartedFAQCommunityResourcesGitHubSlackMailing ListStack OverflowGet StartedSearchIntroductionQuickstart* Installation
	KubernetesPyPIDocker ComposeUpgrading SupersetDocker Builds
ConfigurationUsing SupersetContributingSecurityFAQAPI
Edit this page on GitHubInstallationDocker Compose
On this pageUsing Docker Compose
====================

!cautionSince `docker-compose`is primarily designed to run a set of containers on **a single host**and can't support requirements for **high availability**, we do not support nor recommend
using our `docker-compose`constructs to support production-type use-cases. For single host
environments, we recommend using minikubealong
our installing on k8sdocumentation.

As mentioned in our quickstart guidee, The fastest way to try
Superset locally is using Docker Compose on a Linux or Mac OSX
computer. Superset does not have official support for Windows. It's also the easiest
way to launch a fully functioning **development environment**quickly.

Note that there are 3 major ways we support to run docker-compose:

1. **docker-compose.yml:**for interactive development, where we mount your local folder with the
frontend/backend files that you can edit and experience the changes you
make in the app in real time
2. **docker-compose-non-dev.yml**where we just build a more immutable image based on the
local branch and get all the required images running. Changes in the local branch
at the time you fire this up will be reflected, but changes to the code
while `up`won't be reflected in the app
3. **docker-compose-image-tag.yml**where we fetch an image from docker-hub say for the
`3.0.0`release for instance, and fire it up so you can try it. Here what's in
the local branch has no effects on what's running, we just fetch and run
pre-built images from docker-hub

More on these two approaches after setting up the requirements for either.

Requirements​
-------------

Note that this documentation assumes that you have Docker,
docker-compose, and
gitinstalled.

1.



