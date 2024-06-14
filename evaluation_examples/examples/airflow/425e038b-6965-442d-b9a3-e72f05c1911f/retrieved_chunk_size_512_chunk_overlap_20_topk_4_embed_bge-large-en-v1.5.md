Documentation Source:
docs.astronomer.io/learn/cross-dag-dependencies.md

Documentation Title:
Cross-DAG dependencies | Astronomer Documentation

Documentation Content:
Cross-deployment dependencies on Astro​

To implement cross-DAG dependencies on two different Airflow environments on Astro, follow the guidance in Cross-deployment dependencies.

Was this page helpful?
----------------------

YesNoSign up for Developer Updates
-----------------------------

Get a summary of new Astro features once a month.

SubmitYou can unsubscribe at any time. By proceeding you agree to our Privacy Policy, our Website Termsand to receive emails from Astronomer.

Edit this pagePreviousContextNextCustom hooks and operatorsAssumed knowledge* Implement cross-DAG dependencies
	Dataset dependenciesTriggerDagRunOperatorExternalTaskSensorAirflow API
DAG dependencies view* Cross-deployment dependenciesCross-deployment dependencies on Astro
Legal·Privacy·Security·Cookie Preferences!!© Astronomer 2023. Various trademarks held by their respective owners.



Documentation Source:
docs.astronomer.io/learn/testing-airflow.md

Documentation Title:
Test Airflow DAGs | Astronomer Documentation

Documentation Content:
Test DAGs in a CI/CD pipeline​

You can use CI/CD tools to test and deploy your Airflow code. By installing the Astro CLI into your CI/CD process, you can test your DAGs before deploying them to a production environment. See set up CI/CDfor example implementations.

infoAstronomer customers can use the Astro GitHub integration, which allows you to automatically deploy code from a GitHUb repository to an Astro deployment, viewing Git metadata in the Astro UI. See Deploy code with the Astro GitHub integration.

Add test data or files for local testing​
-----------------------------------------

Use the `include`folder of your Astro project to store files for testing locally, such as test data or a dbt project file. The files in your `include`folder are included in your deploys to Astro, but they are not parsed by Airflow. Therefore, you don't need to specify them in `.airflowignore`to prevent parsing.

If you're running Airflow locally, apply your changes by refreshing the Airflow UI.

Debug interactively with dag.test()​
------------------------------------

The `dag.test()`method allows you to run all tasks in a DAG within a single serialized Python process, without running the Airflow scheduler. The `dag.test()`method lets you iterate faster and use IDE debugging tools when developing DAGs.

This functionality replaces the deprecated DebugExecutor. Learn more in the Airflow documentation.



Documentation Source:
docs.astronomer.io/learn/testing-airflow.md

Documentation Title:
Test Airflow DAGs | Astronomer Documentation

Documentation Content:
Prerequisites​

Ensure that your testing environment has:

* Airflow 2.5.0or later. You can check your version by running `airflow version`.
* All provider packages that your DAG uses.
* An initialized Airflow metadata database, if your DAG uses elements of the metadata database like XCom. The Airflow metadata database is created when Airflow is first run in an environment. You can check that it exists with `airflow db check`and initialize a new database with `airflow db migrate`(`airflow db init`in Airflow versions pre-2.7).

You may wish to install these requirements and test your DAGs in a virtualenvto avoid dependency conflicts in your local environment.



Documentation Source:
docs.astronomer.io/learn/testing-airflow.md

Documentation Title:
Test Airflow DAGs | Astronomer Documentation

Documentation Content:
Use `dag.test()`with the Astro CLI​

If you use the Astro CLI exclusively and do not have the `airflow`package installed locally, you can still debug using `dag.test()`by running `astro dev start`, entering the scheduler container with `astro dev bash -s`, and executing `python `from within the Docker container. Unlike using the base `airflow`package, this testing method requires starting up a complete Airflow environment.



