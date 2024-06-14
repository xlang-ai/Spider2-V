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
`importosimportpytestfromairflow.models importDagBagdefget_dags():"""Generate a tuple of dag_id,  in the DagBag"""dag_bag =DagBag(include_examples=False)defstrip_path_prefix(path):returnos.path.relpath(path,os.environ.get("AIRFLOW_HOME"))return[(k,v,strip_path_prefix(v.fileloc))fork,v indag_bag.dags.items()]APPROVED_TAGS ={"customer_success","op_analytics","product"}@pytest.mark.parametrize("dag_id,dag,fileloc",get_dags(),ids=[x[2]forx inget_dags()])deftest_dag_tags(dag_id,dag,fileloc):"""test if a DAG is tagged and if those TAGs are in the approved list"""assertdag.tags,f"{dag_id}in {fileloc}has no tags"ifAPPROVED_TAGS:assertnotset(dag.tags)-APPROVED_TAGS`tipYou can view the attributes and methods available for the `dag`model in the Airflow documentation.

You can also set requirements at the task level by accessing the `tasks`attribute within the `dag`model, which contains a list of all task objects of a DAG. The test below checks that all DAGs contain at least one task and all tasks use `trigger_rule="all_success"`.

`@pytest.mark.parametrize("dag_id,dag,fileloc",get_dags(),ids=[x[2]forx inget_dags()])deftest_dag_tags(dag_id,dag,fileloc):"""test if all DAGs contain a task and all tasks use the trigger_rule all_success"""assertdag.tasks,f"{dag_id}in {fileloc}has no tasks"fortask indag.tasks:t_rule =task.trigger_ruleassert(t_rule =="all_success"),f"{task}in {dag_id}has the trigger rule {t_rule}"`Implement DAG validation tests​
-------------------------------

Airflow offers different ways to run DAG validation tests using any Python test runner. This section gives an overview of the most common implementation methods. If you are new to testing Airflow DAGs, you can quickly get started by using Astro CLI commands.



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
Use `dag.test()`with the Astro CLI​

If you use the Astro CLI exclusively and do not have the `airflow`package installed locally, you can still debug using `dag.test()`by running `astro dev start`, entering the scheduler container with `astro dev bash -s`, and executing `python `from within the Docker container. Unlike using the base `airflow`package, this testing method requires starting up a complete Airflow environment.



