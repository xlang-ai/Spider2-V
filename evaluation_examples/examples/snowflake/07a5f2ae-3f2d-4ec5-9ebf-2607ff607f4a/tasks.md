# TO-DO List Today

1. Create a Snowflake database "tasty_bytes" with schema "food"

2. Create a table "menu" in schema "food" with columns and types defined in Desktop/columns.json

3. Create a stage called "awsstage" in schema "food", and link it to Amazon S3 bucket "s3://sfquickstarts/tastybytes/raw_pos/menu/menu.csv.gz"

3. Load data from stage "awsstage" into the table "menu"