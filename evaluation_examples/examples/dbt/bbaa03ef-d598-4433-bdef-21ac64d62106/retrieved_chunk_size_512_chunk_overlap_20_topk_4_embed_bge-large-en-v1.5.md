Documentation Source:
docs.getdbt.com/guides/redshift8722.md

Documentation Title:
Quickstart for dbt Cloud and Redshift | dbt Developer Hub

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
docs.getdbt.com/guides/redshift5f72.md

Documentation Title:
Quickstart for dbt Cloud and Redshift | dbt Developer Hub

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
docs.getdbt.com/guides/redshift.md

Documentation Title:
Quickstart for dbt Cloud and Redshift | dbt Developer Hub

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
docs.getdbt.com/guides/starburst-galaxy.md

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



