CREATE OR REPLACE DATABASE STUDENTS;

CREATE OR REPLACE SCHEMA STUDENTS.PUBLIC;

CREATE OR REPLACE FILE FORMAT students_csv_format TYPE = csv FIELD_DELIMITER = ',' RECORD_DELIMITER = '\n' SKIP_HEADER = 1 FIELD_OPTIONALLY_ENCLOSED_BY='"' NULL_IF=('NA');

CREATE OR REPLACE STAGE STUDENTS.PUBLIC.stage FILE_FORMAT = students_csv_format;

PUT file://evaluation_examples/examples/snowflake/fcf1d05c-2028-4d9b-b1a8-d81fe11fd0c8/data.csv @STUDENTS.PUBLIC.stage;
