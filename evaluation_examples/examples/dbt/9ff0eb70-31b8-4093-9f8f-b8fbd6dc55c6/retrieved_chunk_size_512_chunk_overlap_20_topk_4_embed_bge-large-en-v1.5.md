Documentation Source:
docs.getdbt.com/guides/bigquery8722.md

Documentation Title:
Quickstart for dbt Cloud and BigQuery | dbt Developer Hub

Documentation Content:
FAQs​

Build models on top of other models​
------------------------------------

As a best practice in SQL, you should separate logic that cleans up your data from logic that transforms your data. You have already started doing this in the existing query by using common table expressions (CTEs).

Now you can experiment by separating the logic out into separate models and using the reffunction to build models on top of other models:

!The DAG we want for our dbt projectCreate a new SQL file, `models/stg_customers.sql`, with the SQL from the `customers`CTE in our original query.

2. Create a second new SQL file, `models/stg_orders.sql`, with the SQL from the `orders`CTE in our original query.

models/stg\_customers.sql`selectid ascustomer_id,first_name,last_namefrom`dbt-tutorial`.jaffle_shop.customers`models/stg\_orders.sql`selectid asorder_id,user_id ascustomer_id,order_date,statusfrom`dbt-tutorial`.jaffle_shop.orders`
3. Edit the SQL in your `models/customers.sql`file as follows:

models/customers.sql`withcustomers as(select*from{{ ref('stg_customers')}}),orders as(select*from{{ ref('stg_orders')}}),customer_orders as(selectcustomer_id,min(order_date)asfirst_order_date,max(order_date)asmost_recent_order_date,count(order_id)asnumber_of_ordersfromordersgroupby1),final as(selectcustomers.customer_id,customers.first_name,customers.last_name,customer_orders.first_order_date,customer_orders.most_recent_order_date,coalesce(customer_orders.number_of_orders,0)asnumber_of_ordersfromcustomersleftjoincustomer_orders using(customer_id))select*fromfinal`
4. Execute `dbt run`.

This time, when you performed a `dbt run`, separate views/tables were created for `stg_customers`, `stg_orders`and `customers`. dbt inferred the order to run these models. Because `customers`depends on `stg_customers`and `stg_orders`, dbt builds `customers`last. You do not need to explicitly define these dependencies.



Documentation Source:
docs.getdbt.com/guides/bigquery367a.md

Documentation Title:
Quickstart for dbt Cloud and BigQuery | dbt Developer Hub

Documentation Content:
FAQs​

Build models on top of other models​
------------------------------------

As a best practice in SQL, you should separate logic that cleans up your data from logic that transforms your data. You have already started doing this in the existing query by using common table expressions (CTEs).

Now you can experiment by separating the logic out into separate models and using the reffunction to build models on top of other models:

!The DAG we want for our dbt projectCreate a new SQL file, `models/stg_customers.sql`, with the SQL from the `customers`CTE in our original query.

2. Create a second new SQL file, `models/stg_orders.sql`, with the SQL from the `orders`CTE in our original query.

models/stg\_customers.sql`selectid ascustomer_id,first_name,last_namefrom`dbt-tutorial`.jaffle_shop.customers`models/stg\_orders.sql`selectid asorder_id,user_id ascustomer_id,order_date,statusfrom`dbt-tutorial`.jaffle_shop.orders`
3. Edit the SQL in your `models/customers.sql`file as follows:

models/customers.sql`withcustomers as(select*from{{ ref('stg_customers')}}),orders as(select*from{{ ref('stg_orders')}}),customer_orders as(selectcustomer_id,min(order_date)asfirst_order_date,max(order_date)asmost_recent_order_date,count(order_id)asnumber_of_ordersfromordersgroupby1),final as(selectcustomers.customer_id,customers.first_name,customers.last_name,customer_orders.first_order_date,customer_orders.most_recent_order_date,coalesce(customer_orders.number_of_orders,0)asnumber_of_ordersfromcustomersleftjoincustomer_orders using(customer_id))select*fromfinal`
4. Execute `dbt run`.

This time, when you performed a `dbt run`, separate views/tables were created for `stg_customers`, `stg_orders`and `customers`. dbt inferred the order to run these models. Because `customers`depends on `stg_customers`and `stg_orders`, dbt builds `customers`last. You do not need to explicitly define these dependencies.



Documentation Source:
docs.getdbt.com/guides/bigquery121c.md

Documentation Title:
Quickstart for dbt Cloud and BigQuery | dbt Developer Hub

Documentation Content:
FAQs​

Build models on top of other models​
------------------------------------

As a best practice in SQL, you should separate logic that cleans up your data from logic that transforms your data. You have already started doing this in the existing query by using common table expressions (CTEs).

Now you can experiment by separating the logic out into separate models and using the reffunction to build models on top of other models:

!The DAG we want for our dbt projectCreate a new SQL file, `models/stg_customers.sql`, with the SQL from the `customers`CTE in our original query.

2. Create a second new SQL file, `models/stg_orders.sql`, with the SQL from the `orders`CTE in our original query.

models/stg\_customers.sql`selectid ascustomer_id,first_name,last_namefrom`dbt-tutorial`.jaffle_shop.customers`models/stg\_orders.sql`selectid asorder_id,user_id ascustomer_id,order_date,statusfrom`dbt-tutorial`.jaffle_shop.orders`
3. Edit the SQL in your `models/customers.sql`file as follows:

models/customers.sql`withcustomers as(select*from{{ ref('stg_customers')}}),orders as(select*from{{ ref('stg_orders')}}),customer_orders as(selectcustomer_id,min(order_date)asfirst_order_date,max(order_date)asmost_recent_order_date,count(order_id)asnumber_of_ordersfromordersgroupby1),final as(selectcustomers.customer_id,customers.first_name,customers.last_name,customer_orders.first_order_date,customer_orders.most_recent_order_date,coalesce(customer_orders.number_of_orders,0)asnumber_of_ordersfromcustomersleftjoincustomer_orders using(customer_id))select*fromfinal`
4. Execute `dbt run`.

This time, when you performed a `dbt run`, separate views/tables were created for `stg_customers`, `stg_orders`and `customers`. dbt inferred the order to run these models. Because `customers`depends on `stg_customers`and `stg_orders`, dbt builds `customers`last. You do not need to explicitly define these dependencies.



Documentation Source:
docs.getdbt.com/guides/bigquery5f72.md

Documentation Title:
Quickstart for dbt Cloud and BigQuery | dbt Developer Hub

Documentation Content:
FAQs​

Build models on top of other models​
------------------------------------

As a best practice in SQL, you should separate logic that cleans up your data from logic that transforms your data. You have already started doing this in the existing query by using common table expressions (CTEs).

Now you can experiment by separating the logic out into separate models and using the reffunction to build models on top of other models:

!The DAG we want for our dbt projectCreate a new SQL file, `models/stg_customers.sql`, with the SQL from the `customers`CTE in our original query.

2. Create a second new SQL file, `models/stg_orders.sql`, with the SQL from the `orders`CTE in our original query.

models/stg\_customers.sql`selectid ascustomer_id,first_name,last_namefrom`dbt-tutorial`.jaffle_shop.customers`models/stg\_orders.sql`selectid asorder_id,user_id ascustomer_id,order_date,statusfrom`dbt-tutorial`.jaffle_shop.orders`
3. Edit the SQL in your `models/customers.sql`file as follows:

models/customers.sql`withcustomers as(select*from{{ ref('stg_customers')}}),orders as(select*from{{ ref('stg_orders')}}),customer_orders as(selectcustomer_id,min(order_date)asfirst_order_date,max(order_date)asmost_recent_order_date,count(order_id)asnumber_of_ordersfromordersgroupby1),final as(selectcustomers.customer_id,customers.first_name,customers.last_name,customer_orders.first_order_date,customer_orders.most_recent_order_date,coalesce(customer_orders.number_of_orders,0)asnumber_of_ordersfromcustomersleftjoincustomer_orders using(customer_id))select*fromfinal`
4. Execute `dbt run`.

This time, when you performed a `dbt run`, separate views/tables were created for `stg_customers`, `stg_orders`and `customers`. dbt inferred the order to run these models. Because `customers`depends on `stg_customers`and `stg_orders`, dbt builds `customers`last. You do not need to explicitly define these dependencies.



