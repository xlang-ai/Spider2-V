CREATE OR REPLACE DATABASE SALES;

CREATE OR REPLACE SCHEMA SALES.PUBLIC;

CREATE OR REPLACE FILE FORMAT sales_csv_format TYPE = csv FIELD_DELIMITER = ',' RECORD_DELIMITER = '\n' SKIP_HEADER = 1 FIELD_OPTIONALLY_ENCLOSED_BY='"' NULL_IF=('NA');

CREATE OR REPLACE STAGE SALES.PUBLIC.stage FILE_FORMAT = sales_csv_format;

CREATE OR REPLACE TABLE SALES.PUBLIC.ORDERS (
    order_id INT,
    order_date DATE,
    region VARCHAR(50),
    product_category VARCHAR(50),
    product_name VARCHAR(50),
    quantity INT,
    unit_price FLOAT
);

PUT file://evaluation_examples/examples/snowflake/b31539d0-734c-4af1-ab1e-9601df8f873f/sales_data.csv @SALES.PUBLIC.stage;

COPY INTO SALES.PUBLIC.ORDERS FROM @SALES.PUBLIC.stage/sales_data.csv;
