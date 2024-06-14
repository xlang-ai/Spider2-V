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



Documentation Source:
superset.apache.org/docs/quickstart/index.md

Documentation Title:
Quickstart | Superset

Documentation Content:
1. Get Superset​

$ gitclone https://github.com/apache/superset### 2. Start the latest official release of Superset​

`# Enter the repository you just cloned$ cdsuperset# Fire up Superset using Docker Compose$ dockercompose -f docker-compose-image-tag.yml up`This may take a moment as Docker Compose will fetch the underlying
container images and will load up some examples. Once all containers
are downloaded and the output settles, you're ready to log in.



Documentation Source:
superset.apache.org/docs/installation/docker-compose/index.md

Documentation Title:
Docker Compose | Superset

Documentation Content:
Option 1 - for an interactive development environment​

dockercompose uptipWhen running in development mode the `superset-node`container needs to finish building assets in order for the UI to render properly. If you would just
like to try out Superset without making any code changes follow the steps documented for
`production`or a specific version below.

tipBy default, we mount the local superset-frontend folder here and run `npm install`as well
as `npm run dev`which triggers webpack to compile/bundle the frontend code. Depending
on your local setup, especially if you have less than 16GB of memory, it may be very slow to
perform those operations. In this case, we recommend you set the env var
`BUILD_SUPERSET_FRONTEND_IN_DOCKER`to `false`, and to run this locally instead in a terminal.
Simply trigger `npm i && npm run dev`, this should be MUCH faster.



