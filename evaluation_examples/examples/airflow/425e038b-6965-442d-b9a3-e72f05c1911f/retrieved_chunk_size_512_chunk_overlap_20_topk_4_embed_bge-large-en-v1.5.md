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
docs.astronomer.io/learn/debugging-dags.md

Documentation Title:
Debug DAGs | Astronomer Documentation

Documentation Content:
Import errors due to dependency conflicts​

A frequent cause of DAG import errors is not having the necessary packages installed in your Airflow environment. You might be missing provider packagesthat are required for using specific operators or hooks, or you might be missing Python packages used in Airflow tasks.

In an Astro project, you can install OS-level packages by adding them to your `packages.txt`file. You can install Python-level packages, such as provider packages, by adding them to your `requirements.txt`file. If you need to install packages using a specific package manager, consider doing so by adding a bash command to your Dockerfile.

To prevent compatibility issues when new packages are released, Astronomer recommends pinning a package version to your project. For example, adding `astronomer-providers[all]==1.14.0`to your `requirements.txt`file ensures that no future releases of `astronomer-providers`causes compatibility issues. If no version is pinned, Airflow will always use the latest available version.

If you are using the Astro CLI, packages are installed in the scheduler Docker container. You can confirm that a package is installed correctly by running:

astro dev bash--scheduler"pip freeze | grep "If you have conflicting package versions or need to run multiple Python versions, you can run tasks in different environments using a few different operators:

* KubernetesPodOperator: Runs a task in a separate Kubernetes Pod.
* ExternalPythonOperator: Runs a task in a predefined virtual environment.
* PythonVirtualEnvOperator: Runs a task in a temporary virtual environment.

If many Airflow tasks share a set of alternate package and version requirements a common pattern is to run them in two or more separate Airflow deployments.



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
docs.astronomer.io/learn/cross-dag-dependencies.md

Documentation Title:
Cross-DAG dependencies | Astronomer Documentation

Documentation Content:
In the example below, we use an authorization token.

!DAG dependencies view​
----------------------

The cross-DAG dependencies view shows all DAG dependencies in your Airflow environment as long as they are implemented using one of the following methods:

* Using dataset driven scheduling
* Using a TriggerDagRunOperator
* Using an ExternalTaskSensor

To view dependencies in the UI, go to **Browse**> **DAG Dependencies**or by click **Graph**within the **Datasets**tab. The following image shows the dependencies created by the TriggerDagRunOperator and ExternalTaskSensor example DAGs.

!When DAGs are scheduled depending on datasets, both the DAG containing the producing task and the dataset are shown upstream of the consuming DAG.

!To see all dependencies between datasets and DAGs, click on the **Datasets**tab in the Airflow UI.

!Cross-deployment dependencies​
------------------------------

It is sometimes necessary to implement cross-DAG dependencies where the DAGs do not exist in the same Airflow deployment. The TriggerDagRunOperator, ExternalTaskSensor, and dataset methods are designed to work with DAGs in the same Airflow environment, so they are not ideal for cross-Airflow deployments. The Airflow API is ideal for this use case. In this section, you'll learn how to implement this method on Astro, but the general concepts are also applicable to your Airflow environments.



