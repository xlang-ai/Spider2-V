CREATE OR REPLACE DATABASE COMPANY;

CREATE OR REPLACE SCHEMA COMPANY.PUBLIC;

CREATE OR REPLACE FILE FORMAT company_csv_format TYPE = csv FIELD_DELIMITER = ',' RECORD_DELIMITER = '\n' SKIP_HEADER = 1 FIELD_OPTIONALLY_ENCLOSED_BY='"' NULL_IF=('NA');

CREATE OR REPLACE STAGE COMPANY.PUBLIC.stage FILE_FORMAT = company_csv_format;

PUT file://evaluation_examples/examples/snowflake/fcf1d05c-2028-4d9b-b1a8-d81fe11fd0c8/data.csv @COMPANY.PUBLIC.stage;