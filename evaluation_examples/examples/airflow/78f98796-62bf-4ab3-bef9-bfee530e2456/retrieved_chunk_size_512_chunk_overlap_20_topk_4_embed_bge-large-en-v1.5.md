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
Setup​

To use `dag.test()`, you only need to add a few lines of code to the end of your DAG file. If you are using a traditional DAG context, call `dag.test()`after your DAG declaration. If you are using the `@dag`decorator, assign your DAG function to a new object and call the method on that object.

* Traditional DAG context
* @dag decorator

`fromairflow.models.dag importDAGfrompendulum importdatetimefromairflow.operators.empty importEmptyOperatorwithDAG(dag_id="simple_classic_dag",start_date=datetime(2023,1,1),schedule="@daily",catchup=False,)asdag:# assigning the context to an object is mandatory for using dag.test()t1 =EmptyOperator(task_id="t1")if__name__ =="__main__":dag.test()``fromairflow.decorators importdagfrompendulum importdatetimefromairflow.operators.empty importEmptyOperator@dag(start_date=datetime(2023,1,1),schedule="@daily",catchup=False,)defmy_dag():t1 =EmptyOperator(task_id="t1")dag_object =my_dag()if__name__ =="__main__":dag_object.test()`You can run the `.test()`method with popular debugging tools such as:

* VSCode.
* PyCharm.
* Tools like The Python Debuggerand the built-in `breakpoint()`function. These allow you to run `dag.test()`from the command line by running `python `.



Documentation Source:
docs.astronomer.io/learn/testing-airflow.md

Documentation Title:
Test Airflow DAGs | Astronomer Documentation

Documentation Content:
Use `dag.test()`with the Astro CLI​

If you use the Astro CLI exclusively and do not have the `airflow`package installed locally, you can still debug using `dag.test()`by running `astro dev start`, entering the scheduler container with `astro dev bash -s`, and executing `python `from within the Docker container. Unlike using the base `airflow`package, this testing method requires starting up a complete Airflow environment.



Documentation Source:
docs.astronomer.io/learn/testing-airflow.md

Documentation Title:
Test Airflow DAGs | Astronomer Documentation

Documentation Content:
----------------------

YesNoSign up for Developer Updates
-----------------------------

Get a summary of new Astro features once a month.

SubmitYou can unsubscribe at any time. By proceeding you agree to our Privacy Policy, our Website Termsand to receive emails from Astronomer.

Edit this pagePreviousSharing code between multiple projectsNextAirflow tutorialsAssumed knowledge* Write DAG validation testsCommon DAG validation tests
* Implement DAG validation tests
	Airflow CLIThe Astro CLITest DAGs in a CI/CD pipeline
Add test data or files for local testing* Debug interactively with dag.test()
	PrerequisitesSetupUse `dag.test()`with the Astro CLIUse variables and connections in dag.test()
* Unit testingMocking
Data quality checksLegal·Privacy·Security·Cookie Preferences!!© Astronomer 2023. Various trademarks held by their respective owners.



