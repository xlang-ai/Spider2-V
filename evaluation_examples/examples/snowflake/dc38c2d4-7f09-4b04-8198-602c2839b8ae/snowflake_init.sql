CREATE OR REPLACE DATABASE COMPANY;

CREATE OR REPLACE SCHEMA COMPANY.PUBLIC;

CREATE OR REPLACE FILE FORMAT company_csv_format TYPE = csv FIELD_DELIMITER = ',' RECORD_DELIMITER = '\n' SKIP_HEADER = 1 FIELD_OPTIONALLY_ENCLOSED_BY='"' NULL_IF=('NA');

CREATE OR REPLACE STAGE COMPANY.PUBLIC.stage FILE_FORMAT = company_csv_format;

CREATE OR REPLACE TABLE COMPANY.PUBLIC.EMPLOYEES (
    employee_id INTEGER,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department_id VARCHAR(50),
    salary FLOAT
);

CREATE OR REPLACE TABLE COMPANY.PUBLIC.DEPARTMENTS (
    department_id INTEGER,
    department_name VARCHAR(50)
);

PUT file://evaluation_examples/examples/snowflake/6f202e46-7c5d-4673-844d-bdc627c87a1e/employees.csv @COMPANY.PUBLIC.stage;

PUT file://evaluation_examples/examples/snowflake/6f202e46-7c5d-4673-844d-bdc627c87a1e/departments.csv @COMPANY.PUBLIC.stage;

COPY INTO COMPANY.PUBLIC.EMPLOYEES FROM @COMPANY.PUBLIC.stage/employees.csv;

COPY INTO COMPANY.PUBLIC.DEPARTMENTS FROM @COMPANY.PUBLIC.stage/departments.csv;

