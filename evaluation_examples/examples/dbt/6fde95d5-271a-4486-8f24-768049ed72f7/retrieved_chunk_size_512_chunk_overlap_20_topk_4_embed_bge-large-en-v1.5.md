Documentation Source:
docs.getdbt.com/guides/bigquery121c.md

Documentation Title:
Quickstart for dbt Cloud and BigQuery | dbt Developer Hub

Documentation Content:
Name the new branch `add-customers-model`.

1. Click the **...**next to the `models`directory, then select **Create file**.
2. Name the file `customers.sql`, then click **Create**.
3. Copy the following query into the file and click **Save**.

`withcustomers as(selectid ascustomer_id,first_name,last_namefrom`dbt-tutorial`.jaffle_shop.customers),orders as(selectid asorder_id,user_id ascustomer_id,order_date,statusfrom`dbt-tutorial`.jaffle_shop.orders),customer_orders as(selectcustomer_id,min(order_date)asfirst_order_date,max(order_date)asmost_recent_order_date,count(order_id)asnumber_of_ordersfromordersgroupby1),final as(selectcustomers.customer_id,customers.first_name,customers.last_name,customer_orders.first_order_date,customer_orders.most_recent_order_date,coalesce(customer_orders.number_of_orders,0)asnumber_of_ordersfromcustomersleftjoincustomer_orders using(customer_id))select*fromfinal`- Enter `dbt run`in the command prompt at the bottom of the screen. You should get a successful run and see the three models.
Later, you can connect your business intelligence (BI) tools to these views and tables so they only read cleaned up data rather than raw data in your BI tool.



Documentation Source:
docs.getdbt.com/guides/bigquery8722.md

Documentation Title:
Quickstart for dbt Cloud and BigQuery | dbt Developer Hub

Documentation Content:
Name the new branch `add-customers-model`.

1. Click the **...**next to the `models`directory, then select **Create file**.
2. Name the file `customers.sql`, then click **Create**.
3. Copy the following query into the file and click **Save**.

`withcustomers as(selectid ascustomer_id,first_name,last_namefrom`dbt-tutorial`.jaffle_shop.customers),orders as(selectid asorder_id,user_id ascustomer_id,order_date,statusfrom`dbt-tutorial`.jaffle_shop.orders),customer_orders as(selectcustomer_id,min(order_date)asfirst_order_date,max(order_date)asmost_recent_order_date,count(order_id)asnumber_of_ordersfromordersgroupby1),final as(selectcustomers.customer_id,customers.first_name,customers.last_name,customer_orders.first_order_date,customer_orders.most_recent_order_date,coalesce(customer_orders.number_of_orders,0)asnumber_of_ordersfromcustomersleftjoincustomer_orders using(customer_id))select*fromfinal`- Enter `dbt run`in the command prompt at the bottom of the screen. You should get a successful run and see the three models.
Later, you can connect your business intelligence (BI) tools to these views and tables so they only read cleaned up data rather than raw data in your BI tool.



Documentation Source:
docs.getdbt.com/guides/bigquery367a.md

Documentation Title:
Quickstart for dbt Cloud and BigQuery | dbt Developer Hub

Documentation Content:
Name the new branch `add-customers-model`.

1. Click the **...**next to the `models`directory, then select **Create file**.
2. Name the file `customers.sql`, then click **Create**.
3. Copy the following query into the file and click **Save**.

`withcustomers as(selectid ascustomer_id,first_name,last_namefrom`dbt-tutorial`.jaffle_shop.customers),orders as(selectid asorder_id,user_id ascustomer_id,order_date,statusfrom`dbt-tutorial`.jaffle_shop.orders),customer_orders as(selectcustomer_id,min(order_date)asfirst_order_date,max(order_date)asmost_recent_order_date,count(order_id)asnumber_of_ordersfromordersgroupby1),final as(selectcustomers.customer_id,customers.first_name,customers.last_name,customer_orders.first_order_date,customer_orders.most_recent_order_date,coalesce(customer_orders.number_of_orders,0)asnumber_of_ordersfromcustomersleftjoincustomer_orders using(customer_id))select*fromfinal`- Enter `dbt run`in the command prompt at the bottom of the screen. You should get a successful run and see the three models.
Later, you can connect your business intelligence (BI) tools to these views and tables so they only read cleaned up data rather than raw data in your BI tool.



Documentation Source:
docs.getdbt.com/guides/bigquery.md

Documentation Title:
Quickstart for dbt Cloud and BigQuery | dbt Developer Hub

Documentation Content:
Name the new branch `add-customers-model`.

1. Click the **...**next to the `models`directory, then select **Create file**.
2. Name the file `customers.sql`, then click **Create**.
3. Copy the following query into the file and click **Save**.

`withcustomers as(selectid ascustomer_id,first_name,last_namefrom`dbt-tutorial`.jaffle_shop.customers),orders as(selectid asorder_id,user_id ascustomer_id,order_date,statusfrom`dbt-tutorial`.jaffle_shop.orders),customer_orders as(selectcustomer_id,min(order_date)asfirst_order_date,max(order_date)asmost_recent_order_date,count(order_id)asnumber_of_ordersfromordersgroupby1),final as(selectcustomers.customer_id,customers.first_name,customers.last_name,customer_orders.first_order_date,customer_orders.most_recent_order_date,coalesce(customer_orders.number_of_orders,0)asnumber_of_ordersfromcustomersleftjoincustomer_orders using(customer_id))select*fromfinal`- Enter `dbt run`in the command prompt at the bottom of the screen. You should get a successful run and see the three models.
Later, you can connect your business intelligence (BI) tools to these views and tables so they only read cleaned up data rather than raw data in your BI tool.



