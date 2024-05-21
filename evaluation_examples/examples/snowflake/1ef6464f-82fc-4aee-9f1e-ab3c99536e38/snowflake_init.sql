CREATE OR REPLACE DATABASE DB;

CREATE OR REPLACE SCHEMA DB.PUBLIC;

CREATE OR REPLACE FILE FORMAT salary_csv_format TYPE = csv FIELD_DELIMITER = ',' RECORD_DELIMITER = '\n' SKIP_HEADER = 1 FIELD_OPTIONALLY_ENCLOSED_BY='"' NULL_IF=('NA');

CREATE OR REPLACE STAGE DB.PUBLIC.stage FILE_FORMAT = salary_csv_format;

CREATE OR REPLACE TABLE DB.PUBLIC.SALARY (
    age INTEGER,
    gender VARCHAR(50),
    education_level VARCHAR(50),
    job_title VARCHAR(50),
    years_of_experience INTEGER,
    salary INTEGER
);

PUT file://evaluation_examples/examples/snowflake/1ef6464f-82fc-4aee-9f1e-ab3c99536e38/data.csv @DB.PUBLIC.stage;

COPY INTO DB.PUBLIC.SALARY FROM @DB.PUBLIC.stage/data.csv;