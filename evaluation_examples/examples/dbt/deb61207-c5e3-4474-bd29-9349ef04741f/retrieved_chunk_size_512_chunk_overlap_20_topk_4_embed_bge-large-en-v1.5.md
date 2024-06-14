Documentation Source:
docs.getdbt.com/guides/redshift8722.md

Documentation Title:
Quickstart for dbt Cloud and Redshift | dbt Developer Hub

Documentation Content:
FAQs​

Change the way your model is materialized​
------------------------------------------

One of the most powerful features of dbt is that you can change the way a model is materialized in your warehouse, simply by changing a configuration value. You can change things between tables and views by changing a keyword rather than writing the data definition language (DDL) to do this behind the scenes.

By default, everything gets created as a view. You can override that at the directory level so everything in that directory will materialize to a different materialization.

1. Edit your `dbt_project.yml`file.


	* Update your project `name`to:
	
	dbt\_project.ymlname:'jaffle\_shop'
	* Configure `jaffle_shop`so everything in it will be materialized as a table; and configure `example`so everything in it will be materialized as a view. Update your `models`config block to:
	
	dbt\_project.yml`models:jaffle_shop:+materialized:tableexample:+materialized:view`
	Click **Save**.
2. Enter the `dbt run`command. Your `customers`model should now be built as a table!

infoTo do this, dbt had to first run a `drop view`statement (or API call on BigQuery), then a `create table as`statement.
3. Edit `models/customers.sql`to override the `dbt_project.yml`for the `customers`model only by adding the following snippet to the top, and click **Save**: 

models/customers.sql`{{config(materialized='view')}}withcustomers as(selectid ascustomer_id...)`
4. Enter the `dbt run`command. Your model, `customers`, should now build as a view.
5. BigQuery users need to run `dbt run --full-refresh`instead of `dbt run`to full apply materialization changes.
Enter the `dbt run --full-refresh`command for this to take effect in your warehouse.



Documentation Source:
docs.getdbt.com/guides/redshift5f72.md

Documentation Title:
Quickstart for dbt Cloud and Redshift | dbt Developer Hub

Documentation Content:
FAQs​

Change the way your model is materialized​
------------------------------------------

One of the most powerful features of dbt is that you can change the way a model is materialized in your warehouse, simply by changing a configuration value. You can change things between tables and views by changing a keyword rather than writing the data definition language (DDL) to do this behind the scenes.

By default, everything gets created as a view. You can override that at the directory level so everything in that directory will materialize to a different materialization.

1. Edit your `dbt_project.yml`file.


	* Update your project `name`to:
	
	dbt\_project.ymlname:'jaffle\_shop'
	* Configure `jaffle_shop`so everything in it will be materialized as a table; and configure `example`so everything in it will be materialized as a view. Update your `models`config block to:
	
	dbt\_project.yml`models:jaffle_shop:+materialized:tableexample:+materialized:view`
	Click **Save**.
2. Enter the `dbt run`command. Your `customers`model should now be built as a table!

infoTo do this, dbt had to first run a `drop view`statement (or API call on BigQuery), then a `create table as`statement.
3. Edit `models/customers.sql`to override the `dbt_project.yml`for the `customers`model only by adding the following snippet to the top, and click **Save**: 

models/customers.sql`{{config(materialized='view')}}withcustomers as(selectid ascustomer_id...)`
4. Enter the `dbt run`command. Your model, `customers`, should now build as a view.
5. BigQuery users need to run `dbt run --full-refresh`instead of `dbt run`to full apply materialization changes.
Enter the `dbt run --full-refresh`command for this to take effect in your warehouse.



Documentation Source:
docs.getdbt.com/guides/databricks5f72.md

Documentation Title:
Quickstart for dbt Cloud and Databricks | dbt Developer Hub

Documentation Content:
FAQs​

Change the way your model is materialized​
------------------------------------------

One of the most powerful features of dbt is that you can change the way a model is materialized in your warehouse, simply by changing a configuration value. You can change things between tables and views by changing a keyword rather than writing the data definition language (DDL) to do this behind the scenes.

By default, everything gets created as a view. You can override that at the directory level so everything in that directory will materialize to a different materialization.

1. Edit your `dbt_project.yml`file.


	* Update your project `name`to:
	
	dbt\_project.ymlname:'jaffle\_shop'
	* Configure `jaffle_shop`so everything in it will be materialized as a table; and configure `example`so everything in it will be materialized as a view. Update your `models`config block to:
	
	dbt\_project.yml`models:jaffle_shop:+materialized:tableexample:+materialized:view`
	Click **Save**.
2. Enter the `dbt run`command. Your `customers`model should now be built as a table!

infoTo do this, dbt had to first run a `drop view`statement (or API call on BigQuery), then a `create table as`statement.
3. Edit `models/customers.sql`to override the `dbt_project.yml`for the `customers`model only by adding the following snippet to the top, and click **Save**: 

models/customers.sql`{{config(materialized='view')}}withcustomers as(selectid ascustomer_id...)`
4. Enter the `dbt run`command. Your model, `customers`, should now build as a view.
5. BigQuery users need to run `dbt run --full-refresh`instead of `dbt run`to full apply materialization changes.
Enter the `dbt run --full-refresh`command for this to take effect in your warehouse.



Documentation Source:
docs.getdbt.com/guides/databricks121c.md

Documentation Title:
Quickstart for dbt Cloud and Databricks | dbt Developer Hub

Documentation Content:
FAQs​

Change the way your model is materialized​
------------------------------------------

One of the most powerful features of dbt is that you can change the way a model is materialized in your warehouse, simply by changing a configuration value. You can change things between tables and views by changing a keyword rather than writing the data definition language (DDL) to do this behind the scenes.

By default, everything gets created as a view. You can override that at the directory level so everything in that directory will materialize to a different materialization.

1. Edit your `dbt_project.yml`file.


	* Update your project `name`to:
	
	dbt\_project.ymlname:'jaffle\_shop'
	* Configure `jaffle_shop`so everything in it will be materialized as a table; and configure `example`so everything in it will be materialized as a view. Update your `models`config block to:
	
	dbt\_project.yml`models:jaffle_shop:+materialized:tableexample:+materialized:view`
	Click **Save**.
2. Enter the `dbt run`command. Your `customers`model should now be built as a table!

infoTo do this, dbt had to first run a `drop view`statement (or API call on BigQuery), then a `create table as`statement.
3. Edit `models/customers.sql`to override the `dbt_project.yml`for the `customers`model only by adding the following snippet to the top, and click **Save**: 

models/customers.sql`{{config(materialized='view')}}withcustomers as(selectid ascustomer_id...)`
4. Enter the `dbt run`command. Your model, `customers`, should now build as a view.
5. BigQuery users need to run `dbt run --full-refresh`instead of `dbt run`to full apply materialization changes.
Enter the `dbt run --full-refresh`command for this to take effect in your warehouse.



