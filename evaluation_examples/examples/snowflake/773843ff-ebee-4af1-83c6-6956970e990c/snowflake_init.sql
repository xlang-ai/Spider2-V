CREATE OR REPLACE DATABASE VIDEOS;

CREATE OR REPLACE SCHEMA VIDEOS.PUBLIC;

CREATE OR REPLACE FILE FORMAT videos_csv_format TYPE = csv FIELD_DELIMITER = ',' RECORD_DELIMITER = '\n' SKIP_HEADER = 1 FIELD_OPTIONALLY_ENCLOSED_BY='"' NULL_IF=('NA');

CREATE OR REPLACE STAGE VIDEOS.PUBLIC.stage FILE_FORMAT = videos_csv_format;

CREATE OR REPLACE TABLE VIDEOS.PUBLIC.SUBSCRIPTIONS (
    customer_id VARCHAR(50),
    created_date VARCHAR(50),
    canceled_date VARCHAR(50),
    subscription_cost VARCHAR(50),
    subscription_interval VARCHAR(50),
    was_subscription_paid VARCHAR(50)
);

PUT file://evaluation_examples/examples/snowflake/773843ff-ebee-4af1-83c6-6956970e990c/Subscription.csv @VIDEOS.PUBLIC.stage;

COPY INTO VIDEOS.PUBLIC.SUBSCRIPTIONS FROM @VIDEOS.PUBLIC.stage/Subscription.csv;