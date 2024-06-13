Documentation Source:
docs.getdbt.com/docs/build/data-tests.md

Documentation Title:
Add data tests to your DAG | dbt Developer Hub

Documentation Content:
Example​

To add a generic (or "schema") test to your project:

- Add a `.yml`file to your `models`directory, e.g. `models/schema.yml`, with the following content (you may need to adjust the `name:`values for an existing model)
models/schema.yml`version:2models:-name:orderscolumns:-name:order_idtests:-unique-not_null`- Run the `dbt test`command:
`$ dbt testFound 3 models, 2 tests, 0 snapshots, 0 analyses, 130 macros, 0 operations, 0 seed files, 0 sources17:31:05 | Concurrency: 1 threads (target='learn')17:31:05 |17:31:05 | 1 of 2 START test not_null_order_order_id..................... [RUN]17:31:06 | 1 of 2 PASS not_null_order_order_id........................... [PASS in 0.99s]17:31:06 | 2 of 2 START test unique_order_order_id....................... [RUN]17:31:07 | 2 of 2 PASS unique_order_order_id............................. [PASS in 0.79s]17:31:07 |17:31:07 | Finished running 2 tests in 7.17s.Completed successfullyDone. PASS=2 WARN=0 ERROR=0 SKIP=0 TOTAL=2`- Check out the SQL dbt is running by either:
	* **dbt Cloud:**checking the Details tab.
	* **dbt Core:**checking the `target/compiled`directory
**Unique test*** Compiled SQL
* Templated SQL

`select*from(selectorder_idfromanalytics.orderswhereorder_id isnotnullgroupbyorder_idhavingcount(*)>1)validation_errors``select*from(select{{ column_name }}from{{ model }}where{{ column_name }} isnotnullgroupby{{ column_name }}havingcount(*)>1)validation_errors`**Not null test*** Compiled SQL
* Templated SQL

`select*fromanalytics.orderswhereorder_id isnull``select*from{{ model }}where{{ column_name }} isnull`Storing test failures​
----------------------

Normally, a data test query will calculate failures as part of its execution.



Documentation Source:
docs.getdbt.com/guides/starburst-galaxyd41b.md

Documentation Title:
Quickstart for dbt Cloud and Starburst Galaxy | dbt Developer Hub

Documentation Content:
FAQs​

As I create more models, how should I keep my project organized? What should I name my models?Add tests to your models​
-------------------------

Adding teststo a project helps validate that your models are working correctly.

To add tests to your project:

Create a new YAML file in the `models`directory, named `models/schema.yml`

2. Add the following contents to the file:

models/schema.yml`version:2models:-name:customerscolumns:-name:customer_idtests:-unique-not_null-name:stg_customerscolumns:-name:customer_idtests:-unique-not_null-name:stg_orderscolumns:-name:order_idtests:-unique-not_null-name:statustests:-accepted_values:values:['placed','shipped','completed','return_pending','returned']-name:customer_idtests:-not_null-relationships:to:ref('stg_customers')field:customer_id`
Run `dbt test`, and confirm that all your tests passed.


When you run `dbt test`, dbt iterates through your YAML files, and constructs a query for each test. Each query will return the number of records that fail the test. If this number is 0, then the test is successful.



Documentation Source:
docs.getdbt.com/guides/starburst-galaxy121c.md

Documentation Title:
Quickstart for dbt Cloud and Starburst Galaxy | dbt Developer Hub

Documentation Content:
FAQs​

As I create more models, how should I keep my project organized? What should I name my models?Add tests to your models​
-------------------------

Adding teststo a project helps validate that your models are working correctly.

To add tests to your project:

Create a new YAML file in the `models`directory, named `models/schema.yml`

2. Add the following contents to the file:

models/schema.yml`version:2models:-name:customerscolumns:-name:customer_idtests:-unique-not_null-name:stg_customerscolumns:-name:customer_idtests:-unique-not_null-name:stg_orderscolumns:-name:order_idtests:-unique-not_null-name:statustests:-accepted_values:values:['placed','shipped','completed','return_pending','returned']-name:customer_idtests:-not_null-relationships:to:ref('stg_customers')field:customer_id`
Run `dbt test`, and confirm that all your tests passed.


When you run `dbt test`, dbt iterates through your YAML files, and constructs a query for each test. Each query will return the number of records that fail the test. If this number is 0, then the test is successful.



Documentation Source:
docs.getdbt.com/guides/starburst-galaxy8722.md

Documentation Title:
Quickstart for dbt Cloud and Starburst Galaxy | dbt Developer Hub

Documentation Content:
FAQs​

As I create more models, how should I keep my project organized? What should I name my models?Add tests to your models​
-------------------------

Adding teststo a project helps validate that your models are working correctly.

To add tests to your project:

Create a new YAML file in the `models`directory, named `models/schema.yml`

2. Add the following contents to the file:

models/schema.yml`version:2models:-name:customerscolumns:-name:customer_idtests:-unique-not_null-name:stg_customerscolumns:-name:customer_idtests:-unique-not_null-name:stg_orderscolumns:-name:order_idtests:-unique-not_null-name:statustests:-accepted_values:values:['placed','shipped','completed','return_pending','returned']-name:customer_idtests:-not_null-relationships:to:ref('stg_customers')field:customer_id`
Run `dbt test`, and confirm that all your tests passed.


When you run `dbt test`, dbt iterates through your YAML files, and constructs a query for each test. Each query will return the number of records that fail the test. If this number is 0, then the test is successful.



