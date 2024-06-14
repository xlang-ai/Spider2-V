Documentation Source:
docs.getdbt.com/guides/manual-install121c.md

Documentation Title:
Quickstart for dbt Core from a manual install | dbt Developer Hub

Documentation Content:
!The starter project in a code editor- dbt provides the following values in the `dbt_project.yml`file:
dbt\_project.yml`name:jaffle_shop # Change from the default, `my_new_project`...profile:jaffle_shop # Change from the default profile name, `default`...models:jaffle_shop:# Change from `my_new_project` to match the previous value for `name:`...`Connect to BigQuery​
--------------------

When developing locally, dbt connects to your data warehouseusing a profile, which is a YAML file with all the connection details to your warehouse. 

1. Create a file in the `~/.dbt/`directory named `profiles.yml`.
2. Move your BigQuery keyfile into this directory.
3. Copy the following and paste into the new profiles.yml file. Make sure you update the values where noted.

profiles.yml`jaffle_shop:# this needs to match the profile in your dbt_project.yml filetarget:devoutputs:dev:type:bigquerymethod:service-accountkeyfile:/Users/BBaggins/.dbt/dbt-tutorial-project-331118.json # replace this with the full path to your keyfileproject:grand-highway-265418# Replace this with your project iddataset:dbt_bbagins # Replace this with dbt_your_name, e.g. dbt_bilbothreads:1timeout_seconds:300location:USpriority:interactive`- Run the `debug`command from your project to confirm that you can successfully connect:
`$ dbt debug>Connection test: OK connection ok`!A successful dbt debug command### FAQs​

My data team uses a different data warehouse. What should my profiles.yml file look like for my warehouse?Perform your first dbt run​
---------------------------

Our sample project has some example models in it. We're going to check that we can run them to confirm everything is in order.

- Enter the `run`command to build example models:
dbt runYou should have an output that looks like this:

!A successful dbt run commandCommit your changes​
--------------------

Commit your changes so that the repository contains the latest code.

- Link the GitHub repository you created to your dbt project by running the following commands in Terminal.



Documentation Source:
docs.getdbt.com/guides/manual-install8722.md

Documentation Title:
Quickstart for dbt Core from a manual install | dbt Developer Hub

Documentation Content:
!The starter project in a code editor- dbt provides the following values in the `dbt_project.yml`file:
dbt\_project.yml`name:jaffle_shop # Change from the default, `my_new_project`...profile:jaffle_shop # Change from the default profile name, `default`...models:jaffle_shop:# Change from `my_new_project` to match the previous value for `name:`...`Connect to BigQuery​
--------------------

When developing locally, dbt connects to your data warehouseusing a profile, which is a YAML file with all the connection details to your warehouse. 

1. Create a file in the `~/.dbt/`directory named `profiles.yml`.
2. Move your BigQuery keyfile into this directory.
3. Copy the following and paste into the new profiles.yml file. Make sure you update the values where noted.

profiles.yml`jaffle_shop:# this needs to match the profile in your dbt_project.yml filetarget:devoutputs:dev:type:bigquerymethod:service-accountkeyfile:/Users/BBaggins/.dbt/dbt-tutorial-project-331118.json # replace this with the full path to your keyfileproject:grand-highway-265418# Replace this with your project iddataset:dbt_bbagins # Replace this with dbt_your_name, e.g. dbt_bilbothreads:1timeout_seconds:300location:USpriority:interactive`- Run the `debug`command from your project to confirm that you can successfully connect:
`$ dbt debug>Connection test: OK connection ok`!A successful dbt debug command### FAQs​

My data team uses a different data warehouse. What should my profiles.yml file look like for my warehouse?Perform your first dbt run​
---------------------------

Our sample project has some example models in it. We're going to check that we can run them to confirm everything is in order.

- Enter the `run`command to build example models:
dbt runYou should have an output that looks like this:

!A successful dbt run commandCommit your changes​
--------------------

Commit your changes so that the repository contains the latest code.

- Link the GitHub repository you created to your dbt project by running the following commands in Terminal.



Documentation Source:
docs.getdbt.com/guides/manual-install5f72.md

Documentation Title:
Quickstart for dbt Core from a manual install | dbt Developer Hub

Documentation Content:
!The starter project in a code editor- dbt provides the following values in the `dbt_project.yml`file:
dbt\_project.yml`name:jaffle_shop # Change from the default, `my_new_project`...profile:jaffle_shop # Change from the default profile name, `default`...models:jaffle_shop:# Change from `my_new_project` to match the previous value for `name:`...`Connect to BigQuery​
--------------------

When developing locally, dbt connects to your data warehouseusing a profile, which is a YAML file with all the connection details to your warehouse. 

1. Create a file in the `~/.dbt/`directory named `profiles.yml`.
2. Move your BigQuery keyfile into this directory.
3. Copy the following and paste into the new profiles.yml file. Make sure you update the values where noted.

profiles.yml`jaffle_shop:# this needs to match the profile in your dbt_project.yml filetarget:devoutputs:dev:type:bigquerymethod:service-accountkeyfile:/Users/BBaggins/.dbt/dbt-tutorial-project-331118.json # replace this with the full path to your keyfileproject:grand-highway-265418# Replace this with your project iddataset:dbt_bbagins # Replace this with dbt_your_name, e.g. dbt_bilbothreads:1timeout_seconds:300location:USpriority:interactive`- Run the `debug`command from your project to confirm that you can successfully connect:
`$ dbt debug>Connection test: OK connection ok`!A successful dbt debug command### FAQs​

My data team uses a different data warehouse. What should my profiles.yml file look like for my warehouse?Perform your first dbt run​
---------------------------

Our sample project has some example models in it. We're going to check that we can run them to confirm everything is in order.

- Enter the `run`command to build example models:
dbt runYou should have an output that looks like this:

!A successful dbt run commandCommit your changes​
--------------------

Commit your changes so that the repository contains the latest code.

- Link the GitHub repository you created to your dbt project by running the following commands in Terminal.



Documentation Source:
docs.getdbt.com/guides/manual-install0c17.md

Documentation Title:
Quickstart for dbt Core from a manual install | dbt Developer Hub

Documentation Content:
!The starter project in a code editor- dbt provides the following values in the `dbt_project.yml`file:
dbt\_project.yml`name:jaffle_shop # Change from the default, `my_new_project`...profile:jaffle_shop # Change from the default profile name, `default`...models:jaffle_shop:# Change from `my_new_project` to match the previous value for `name:`...`Connect to BigQuery​
--------------------

When developing locally, dbt connects to your data warehouseusing a profile, which is a YAML file with all the connection details to your warehouse. 

1. Create a file in the `~/.dbt/`directory named `profiles.yml`.
2. Move your BigQuery keyfile into this directory.
3. Copy the following and paste into the new profiles.yml file. Make sure you update the values where noted.

profiles.yml`jaffle_shop:# this needs to match the profile in your dbt_project.yml filetarget:devoutputs:dev:type:bigquerymethod:service-accountkeyfile:/Users/BBaggins/.dbt/dbt-tutorial-project-331118.json # replace this with the full path to your keyfileproject:grand-highway-265418# Replace this with your project iddataset:dbt_bbagins # Replace this with dbt_your_name, e.g. dbt_bilbothreads:1timeout_seconds:300location:USpriority:interactive`- Run the `debug`command from your project to confirm that you can successfully connect:
`$ dbt debug>Connection test: OK connection ok`!A successful dbt debug command### FAQs​

My data team uses a different data warehouse. What should my profiles.yml file look like for my warehouse?Perform your first dbt run​
---------------------------

Our sample project has some example models in it. We're going to check that we can run them to confirm everything is in order.

- Enter the `run`command to build example models:
dbt runYou should have an output that looks like this:

!A successful dbt run commandCommit your changes​
--------------------

Commit your changes so that the repository contains the latest code.

- Link the GitHub repository you created to your dbt project by running the following commands in Terminal.



