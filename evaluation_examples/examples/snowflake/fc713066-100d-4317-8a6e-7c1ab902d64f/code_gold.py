import snowflake.snowpark as snowpark
from snowflake.snowpark.functions import col
from snowflake.snowpark.types import *
def main(session: snowpark.Session):
    # Use SQL to create Tasty_Food Database
    session.sql('CREATE OR REPLACE DATABASE tasty_food;').collect()
    # Use SQL to create our Raw POS (Point-of-Sale) Schema
    session.sql('CREATE OR REPLACE SCHEMA tasty_food.raw_pos;').collect()
    # Use SQL to create Stage
    session.sql('CREATE OR REPLACE STAGE tasty_food.public.stage url = "s3://sfquickstarts/tastybytes/" file_format = (type = csv);').collect()
    # Define our Menu Schema
    menu_schema = StructType([StructField("menu_id",IntegerType()),\
                     StructField("menu_type_id",IntegerType()),\
                     StructField("menu_type",StringType()),\
                     StructField("truck_brand_name",StringType()),\
                     StructField("menu_item_id",IntegerType()),\
                     StructField("menu_item_name",StringType()),\
                     StructField("item_category",StringType()),\
                     StructField("item_subcategory",StringType()),\
                     StructField("cost_of_goods_usd",IntegerType()),\
                     StructField("sale_price_usd",IntegerType()),\
                     StructField("menu_item_health_metrics_obj",VariantType())])
    # Create a Dataframe from our Menu file from our Stage
    df_stage_read = session.read.schema(menu_schema).csv('@tasty_food.public.stage/raw_pos/menu/')
    # Save our Dataframe as a Menu table in our Tasty Bytes Database and Raw POS Schema
    df_stage_read.write.mode("overwrite").save_as_table("tasty_food.raw_pos.menu")
    # Create a new Dataframe reading from our Menu table and filtering for the Freezing Point brand
    df_menu_query_result = session.table("tasty_food.raw_pos.menu").filter(col("menu_type") == "Ice Cream")
    # return our Dataframe
    return df_menu_query_result