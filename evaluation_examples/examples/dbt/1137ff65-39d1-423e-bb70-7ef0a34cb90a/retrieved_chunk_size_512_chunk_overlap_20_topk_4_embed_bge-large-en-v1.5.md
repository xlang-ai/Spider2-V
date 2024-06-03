Documentation Source:
docs.getdbt.com/blog/kimball-dimensional-model.md

Documentation Title:
Building a Kimball dimensional model with dbt | dbt Developer Blog

Documentation Content:
`version:2models:-name:dim_productcolumns:-name:product_key description:The surrogate key of the producttests:-not_null-unique-name:productid description:The natural key of the producttests:-not_null-unique-name:product_name description:The product nametests:-not_null`### Step 8: Build dbt models​

Execute the dbt runand dbt testcommands to run and test your dbt models: 

dbt run && dbt test We have now completed all the steps to create a dimension table. We can now repeat the same steps to all dimension tables that we have identified earlier. Make sure to create all dimension tables before moving on to the next part. 

Part 5: Create the fact table​
------------------------------

After we have created all required dimension tables, we can now create the fact table for `fct_sales`.



Documentation Source:
docs.getdbt.com/guides/manual-install0c17.md

Documentation Title:
Quickstart for dbt Core from a manual install | dbt Developer Hub

Documentation Content:
Build your first models​

Now that you set up your sample project, you can get to the fun part — building models!
In the next steps, you will take a sample query and turn it into a model in your dbt project.

Checkout a new git branch​
--------------------------

Check out a new git branch to work on new code:

- Create a new branch by using the `checkout`command and passing the `-b`flag:
`$ gitcheckout -badd-customers-model>Switched to a new branch `add-customer-model``Build your first model​
-----------------------

1. Open your project in your favorite code editor.
2. Create a new SQL file in the `models`directory, named `models/customers.sql`.
3. Paste the following query into the `models/customers.sql`file.

* BigQuery
* Databricks
* Redshift
* Snowflake

`withcustomers as(selectid ascustomer_id,first_name,last_namefrom`dbt-tutorial`.jaffle_shop.customers),orders as(selectid asorder_id,user_id ascustomer_id,order_date,statusfrom`dbt-tutorial`.jaffle_shop.orders),customer_orders as(selectcustomer_id,min(order_date)asfirst_order_date,max(order_date)asmost_recent_order_date,count(order_id)asnumber_of_ordersfromordersgroupby1),final as(selectcustomers.customer_id,customers.first_name,customers.last_name,customer_orders.first_order_date,customer_orders.most_recent_order_date,coalesce(customer_orders.number_of_orders,0)asnumber_of_ordersfromcustomersleftjoincustomer_orders using(customer_id))select*fromfinal``withcustomers as(selectid ascustomer_id,first_name,last_namefromjaffle_shop_customers),orders as(selectid asorder_id,user_id ascustomer_id,order_date,statusfromjaffle_shop_orders),customer_orders as(selectcustomer_id,min(order_date)asfirst_order_date,max(order_date)asmost_recent_order_date,count(order_id)asnumber_of_ordersfromordersgroupby1),final as(selectcustomers.customer_id,customers.first_name,customers.last_name,customer_orders.first_order_date,customer_orders.most_recent_order_date,coalesce(customer_orders.



Documentation Source:
docs.getdbt.com/guides/manual-install121c.md

Documentation Title:
Quickstart for dbt Core from a manual install | dbt Developer Hub

Documentation Content:
Build your first models​

Now that you set up your sample project, you can get to the fun part — building models!
In the next steps, you will take a sample query and turn it into a model in your dbt project.

Checkout a new git branch​
--------------------------

Check out a new git branch to work on new code:

- Create a new branch by using the `checkout`command and passing the `-b`flag:
`$ gitcheckout -badd-customers-model>Switched to a new branch `add-customer-model``Build your first model​
-----------------------

1. Open your project in your favorite code editor.
2. Create a new SQL file in the `models`directory, named `models/customers.sql`.
3. Paste the following query into the `models/customers.sql`file.

* BigQuery
* Databricks
* Redshift
* Snowflake

`withcustomers as(selectid ascustomer_id,first_name,last_namefrom`dbt-tutorial`.jaffle_shop.customers),orders as(selectid asorder_id,user_id ascustomer_id,order_date,statusfrom`dbt-tutorial`.jaffle_shop.orders),customer_orders as(selectcustomer_id,min(order_date)asfirst_order_date,max(order_date)asmost_recent_order_date,count(order_id)asnumber_of_ordersfromordersgroupby1),final as(selectcustomers.customer_id,customers.first_name,customers.last_name,customer_orders.first_order_date,customer_orders.most_recent_order_date,coalesce(customer_orders.number_of_orders,0)asnumber_of_ordersfromcustomersleftjoincustomer_orders using(customer_id))select*fromfinal``withcustomers as(selectid ascustomer_id,first_name,last_namefromjaffle_shop_customers),orders as(selectid asorder_id,user_id ascustomer_id,order_date,statusfromjaffle_shop_orders),customer_orders as(selectcustomer_id,min(order_date)asfirst_order_date,max(order_date)asmost_recent_order_date,count(order_id)asnumber_of_ordersfromordersgroupby1),final as(selectcustomers.customer_id,customers.first_name,customers.last_name,customer_orders.first_order_date,customer_orders.most_recent_order_date,coalesce(customer_orders.



Documentation Source:
docs.getdbt.com/guides/manual-install5f72.md

Documentation Title:
Quickstart for dbt Core from a manual install | dbt Developer Hub

Documentation Content:
Build your first models​

Now that you set up your sample project, you can get to the fun part — building models!
In the next steps, you will take a sample query and turn it into a model in your dbt project.

Checkout a new git branch​
--------------------------

Check out a new git branch to work on new code:

- Create a new branch by using the `checkout`command and passing the `-b`flag:
`$ gitcheckout -badd-customers-model>Switched to a new branch `add-customer-model``Build your first model​
-----------------------

1. Open your project in your favorite code editor.
2. Create a new SQL file in the `models`directory, named `models/customers.sql`.
3. Paste the following query into the `models/customers.sql`file.

* BigQuery
* Databricks
* Redshift
* Snowflake

`withcustomers as(selectid ascustomer_id,first_name,last_namefrom`dbt-tutorial`.jaffle_shop.customers),orders as(selectid asorder_id,user_id ascustomer_id,order_date,statusfrom`dbt-tutorial`.jaffle_shop.orders),customer_orders as(selectcustomer_id,min(order_date)asfirst_order_date,max(order_date)asmost_recent_order_date,count(order_id)asnumber_of_ordersfromordersgroupby1),final as(selectcustomers.customer_id,customers.first_name,customers.last_name,customer_orders.first_order_date,customer_orders.most_recent_order_date,coalesce(customer_orders.number_of_orders,0)asnumber_of_ordersfromcustomersleftjoincustomer_orders using(customer_id))select*fromfinal``withcustomers as(selectid ascustomer_id,first_name,last_namefromjaffle_shop_customers),orders as(selectid asorder_id,user_id ascustomer_id,order_date,statusfromjaffle_shop_orders),customer_orders as(selectcustomer_id,min(order_date)asfirst_order_date,max(order_date)asmost_recent_order_date,count(order_id)asnumber_of_ordersfromordersgroupby1),final as(selectcustomers.customer_id,customers.first_name,customers.last_name,customer_orders.first_order_date,customer_orders.most_recent_order_date,coalesce(customer_orders.



