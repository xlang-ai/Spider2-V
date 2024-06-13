CREATE OR REPLACE DATABASE IMDB;

CREATE OR REPLACE SCHEMA IMDB.PUBLIC;

CREATE OR REPLACE TABLE IMDB.PUBLIC.MOVIES (
    Movie_name STRING,
    Release_year INT,
    Duration INT,
    Rating FLOAT,
    Meta_score FLOAT,
    Votes STRING,
    Genre STRING,
    Director STRING,
    Cast STRING,
    Gross STRING
);

CREATE OR REPLACE FILE FORMAT imdb_csv_format TYPE = csv FIELD_DELIMITER = ',' RECORD_DELIMITER = '\n' SKIP_HEADER = 1 FIELD_OPTIONALLY_ENCLOSED_BY='"' NULL_IF=('NA');

CREATE OR REPLACE STAGE IMDB.PUBLIC.stage FILE_FORMAT = imdb_csv_format;

PUT file://evaluation_examples/examples/snowflake/334c5af8-bfa0-4a97-aade-e667c7533cbb/imdb_top_2000_movies.csv @IMDB.PUBLIC.stage;

COPY INTO IMDB.PUBLIC.MOVIES FROM @IMDB.PUBLIC.stage;