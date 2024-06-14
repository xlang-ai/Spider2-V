Documentation Source:
docs.getdbt.com/reference/resource-properties/description.md

Documentation Title:
description | dbt Developer Hub

Documentation Content:
Add a simple description to a model and column​

models/schema.yml`version:2models:-name:dim_customersdescription:One record per customercolumns:-name:customer_iddescription:Primary key`### Add a multiline description to a model​

You can use YAML block notationto split a longer description over multiple lines:

models/schema.yml`version:2models:-name:dim_customersdescription:>One record per customer. Note that a customer must have made a purchase tobe included in this  — customer accounts that were created but neverused have been filtered out.columns:-name:customer_iddescription:Primary key.`### Use some markdown in a description​

You can use markdown in your descriptions, but you may need to quote your description to ensure the YAML parser doesn't get confused by special characters!

models/schema.yml`version:2models:-name:dim_customersdescription: "**Read more**"columns:-name:customer_iddescription:Primary key.`### Use a docs block in a description​

If you have a long description, especially if it contains markdown, it may make more sense to leverage a `docs`block. A benefit of this approach is that code editors will correctly highlight markdown, making it easier to debug as you write.

models/schema.yml`version:2models:-name:fct_ordersdescription:This table has basic information about orders,as well as some derived facts based on paymentscolumns:-name:statusdescription:'{{ doc("orders_status") }}'`models/docs.md`{% docs orders_status %}Orders can be one of the following statuses:| status | description ||----------------|---------------------------------------------------------------------------|| placed | The order has been placed but has not yet left the warehouse || shipped | The order has been shipped to the customer and is currently in transit || completed | The order has been received by the customer || returned | The order has been returned by the customer and received at the warehouse |{% enddocs %}`### Link to another model in a description​

You can use relative links to link to another model. It's a little hacky — but to do this:

1. Serve your docs site.
2. Navigate to the model you want to link to, e.g. `http://127.0.0.1:8080/#!/model/model.jaffle_shop.stg_stripe__payments`
3.



Documentation Source:
docs.getdbt.com/guides/manual-install5f72.md

Documentation Title:
Quickstart for dbt Core from a manual install | dbt Developer Hub

Documentation Content:
FAQs​

What tests are available for me to use in dbt? Can I add my own custom tests?Does my test file need to be named `schema.yml`?Document your models​
---------------------

Adding documentationto your project allows you to describe your models in rich detail, and share that information with your team. Here, we're going to add some basic documentation to our project.

1. Update your `models/schema.yml`file to include some descriptions, such as those below.

models/schema.yml`version:2models:-name:customersdescription:One record per customercolumns:-name:customer_iddescription:Primary keytests:-unique-not_null-name:first_order_datedescription:NULL when a customer has not yet placed an order.-name:stg_customersdescription:This model cleans up customer datacolumns:-name:customer_iddescription:Primary keytests:-unique-not_null-name:stg_ordersdescription:This model cleans up order datacolumns:-name:order_iddescription:Primary keytests:-unique-not_null-name:statustests:-accepted_values:values:['placed','shipped','completed','return_pending','returned']-name:customer_idtests:-not_null-relationships:to:ref('stg_customers')field:customer_id`
Run `dbt docs generate`to generate the documentation for your project. dbt introspects your project and your warehouse to generate a JSONfile with rich documentation about your project.

- Run `dbt docs serve`command to launch the documentation in a local website.



Documentation Source:
docs.getdbt.com/guides/bigquery5f72.md

Documentation Title:
Quickstart for dbt Cloud and BigQuery | dbt Developer Hub

Documentation Content:
FAQs​

What tests are available for me to use in dbt? Can I add my own custom tests?Does my test file need to be named `schema.yml`?Document your models​
---------------------

Adding documentationto your project allows you to describe your models in rich detail, and share that information with your team. Here, we're going to add some basic documentation to our project.

1. Update your `models/schema.yml`file to include some descriptions, such as those below.

models/schema.yml`version:2models:-name:customersdescription:One record per customercolumns:-name:customer_iddescription:Primary keytests:-unique-not_null-name:first_order_datedescription:NULL when a customer has not yet placed an order.-name:stg_customersdescription:This model cleans up customer datacolumns:-name:customer_iddescription:Primary keytests:-unique-not_null-name:stg_ordersdescription:This model cleans up order datacolumns:-name:order_iddescription:Primary keytests:-unique-not_null-name:statustests:-accepted_values:values:['placed','shipped','completed','return_pending','returned']-name:customer_idtests:-not_null-relationships:to:ref('stg_customers')field:customer_id`
Run `dbt docs generate`to generate the documentation for your project. dbt introspects your project and your warehouse to generate a JSONfile with rich documentation about your project.

- Click the book icon in the Develop interface to launch documentation in a new tab.



Documentation Source:
docs.getdbt.com/guides/microsoft-fabric.md

Documentation Title:
Quickstart for dbt Cloud and Microsoft Fabric | dbt Developer Hub

Documentation Content:
FAQs​

What tests are available for me to use in dbt? Can I add my own custom tests?Does my test file need to be named `schema.yml`?Document your models​
---------------------

Adding documentationto your project allows you to describe your models in rich detail, and share that information with your team. Here, we're going to add some basic documentation to our project.

1. Update your `models/schema.yml`file to include some descriptions, such as those below.

models/schema.yml`version:2models:-name:customersdescription:One record per customercolumns:-name:customer_iddescription:Primary keytests:-unique-not_null-name:first_order_datedescription:NULL when a customer has not yet placed an order.-name:stg_customersdescription:This model cleans up customer datacolumns:-name:customer_iddescription:Primary keytests:-unique-not_null-name:stg_ordersdescription:This model cleans up order datacolumns:-name:order_iddescription:Primary keytests:-unique-not_null-name:statustests:-accepted_values:values:['placed','shipped','completed','return_pending','returned']-name:customer_idtests:-not_null-relationships:to:ref('stg_customers')field:customer_id`
Run `dbt docs generate`to generate the documentation for your project. dbt introspects your project and your warehouse to generate a JSONfile with rich documentation about your project.

- Click the book icon in the Develop interface to launch documentation in a new tab.



