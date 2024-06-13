Documentation Source:
docs.astronomer.io/astro/cli/test-your-astro-project-locally.md

Documentation Title:
Test your Astro project | Astronomer Documentation

Documentation Content:
Run tests with pytest​

To run unit tests on your Astro project, run:

astro dev pytestThis command runs all tests in your project's `tests`directory with pytest, a testing framework for Python. With pytest, you can test custom Python code and operators locally without having to start a local Airflow environment.

The `tests`directory in your Astro project includes an example DAG test called `test_dag_example.py`. This test checks that:

* All Airflow tasks have required arguments.
* DAG IDs are unique across the Astro project.
* DAGs have no cycles.
* There are no general import or syntax errors.

This test is just an example of the kinds of pytests one could run to test thier DAGs. You may want to alter this test or create new ones that better fit the context of your DAGs. `astro dev pytest`will run any pytest file that you add to the `tests`directory. For more information about this command, see the CLI command reference.

Test before an Astro Runtime upgrade​
-------------------------------------

You can use `astro dev upgrade-test`to test your local Astro project against a new version of Astro Runtime to prepare for an upgrade. By default, the command runs the following tests in order to create reports that can help you determine whether your upgrade will be successful:

* **Dependency test**: Identify the packages that have been added, removed, or changed in the upgrade version.
* **DAG test**: Identify Python DAG `import`errors in the upgrade version.

To run these tests, open your Astro project and run:

astro dev upgrade-testIf the tests are successful, the Astro CLI creates a folder in your Astro project called `upgrade-test---`. The folder will contain the following reports:

* `pip_freeze_`: The output of the `pip freeze`with your current version.
* `pip_freeze_`: The output of the `pip freeze`with your upgrade version.
* `dependency_compare.txt`: The result of the dependency test.
* `Dockerfile`: The updated file used in the upgrade test.
* `dag-test-results.html`: The results of the DAG test.

Use the test results to fix any major package changes or broken DAGs before you upgrade.



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
docs.astronomer.io/astro/cli/release-notes.md

Documentation Title:
Astro CLI release notes | Astronomer Documentation

Documentation Content:
New command to run DAG unit tests with pytest​

You can now run custom unit tests for all DAGs in your Astro project with `astro dev pytest`, a new Astro CLI command that uses pytest, a common testing framework for Python. As part of this change, new Astro projects created via `astro dev init`now include a `tests`directory, which includes one example pytest built by Astronomer.

When you run this command, the Astro CLI creates a local Python environment that includes your DAG code, dependencies, and Astro Runtime Docker image. The CLI then runs any pytests in the `tests`directory and shows you the results of those tests in your terminal. You can add as many custom tests to this directory as you'd like.

For example, you can use this command to run tests that check for:

* Python and Airflow syntax errors.
* Import errors.
* Dependency conflicts.
* Unique DAG IDs.

These tests don't require a fully functional Airflow environment in order to execute, which makes this Astro CLI command the fastest and easiest way to test DAGs locally.

In addition to running tests locally, you can also run pytest as part of the Astro deploy process. To do so, specify the `--pytest`flag when running `astro deploy`. This ensures that your code push to Astro automatically fails if any DAGs do not pass all pytests specified in the `tests`directory of your Astro project. For more information, see Test your Astro project locally.



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



