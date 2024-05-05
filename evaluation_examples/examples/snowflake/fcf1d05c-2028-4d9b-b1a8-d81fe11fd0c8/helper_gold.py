import snowflake.snowpark as snowpark
from snowflake.snowpark.types import *

schema_for_file = StructType([
    StructField("employee_id", IntegerType()),
    StructField("first_name", StringType()),
    StructField("last_name", StringType()), 
    StructField("department_id", StringType()),
    StructField("salary", FloatType())
])

fileLocation = "@COMPANY.PUBLIC.stage/data.csv"
outputTableName = "employees"

def main(session: snowpark.Session):
  df_reader = session.read.schema(schema_for_file)
  df = df_reader.csv(fileLocation)
  df.write.mode("overwrite").save_as_table(outputTableName)

  return outputTableName + " table successfully written from stage"