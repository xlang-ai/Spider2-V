Documentation Source:
docs.getdbt.com/docs/collaborate/documentation.md

Documentation Title:
About documentation | dbt Developer Hub

Documentation Content:
Here's an example docs site:

!Auto-generated dbt documentation websiteAdding descriptions to your project​
------------------------------------

To add descriptions to your project, use the `description:`key in the same files where you declare tests, like so:

models/.yml`version:2models:-name:eventsdescription:This table contains clickstream events from the marketing websitecolumns:-name:event_iddescription:This is a unique identifier for the eventtests:-unique-not_null-name:user-idquote:truedescription:The user who performed the eventtests:-not_null`Generating project documentation​
---------------------------------

You can generate a documentation site for your project (with or without descriptions) using the CLI.

First, run `dbt docs generate`— this command tells dbt to compile relevant information about your dbt project and warehouse into `manifest.json`and `catalog.json`files respectively. To see the documentation for all columns and not just columns described in your project, ensure that you have created the models with `dbt run`beforehand.

Then, run `dbt docs serve`to use these `.json`files to populate a local website.

FAQs​
-----

Are there any example dbt documentation sites?Using Docs Blocks​
------------------



Documentation Source:
docs.getdbt.com/reference/resource-properties/description.md

Documentation Title:
description | dbt Developer Hub

Documentation Content:
Copy the url\_path, i.e. everything after `http://127.0.0.1:8080/`, so in this case `#!/model/model.jaffle_shop.stg_stripe__payments`
4. Paste it as the link

models/schema.yml`version:2models:-name:customersdescription: "Filtering done based on stg_stripe__payments"columns:-name:customer_iddescription:Primary key`### Include an image from your repo in your descriptions​

This section applies to dbt Core users only. Including an image from your repository ensures your images are version-controlled. 

Both dbt Cloud and dbt Core users can include an image from the web, which offers dynamic content, reduced repository size, accessibility, and ease of collaboration.

To include an image in your model's `description`field:

1. Add the file in a subdirectory, e.g. `assets/dbt-logo.svg`
2. Set the `asset-paths`configin your `dbt_project.yml`file so that this directory gets copied to the `target/`directory as part of `dbt docs generate`

dbt\_project.ymlasset-paths:["assets"]- Use a Markdown link to the image in your `description:`
models/schema.yml`version:2models:-name:customersdescription: "!dbt Logo"columns:-name:customer_iddescription:Primary key`Run `dbt docs generate`— the `assets`directory will be copied to the `target`directory

Run `dbt docs serve`— the image will be rendered as part of your project documentation:


If mixing images and text, also consider using a docs block.



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
docs.getdbt.com/guides/manual-installd41b.md

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



