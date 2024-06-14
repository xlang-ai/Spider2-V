Documentation Source:
docs.snowflake.com/en/user-guide/data-load-dirtables-pipeline.md

Documentation Title:
Building a data processing pipeline using a directory table | Snowflake Documentation

Documentation Content:
```
select*fromprod_reviews;+------------------+----------------------------------+| FILE_NAME        | FILE_DATA                        ||------------------+----------------------------------|| prod_review1.pdf | {                                ||                  |   "FirstName": "John",           ||                  |   "LastName": "Johnson",         ||                  |   "Middle Name": "Michael",      ||                  |   "Product": "Tennis Shoes",     ||                  |   "Purchase Date": "03/15/2022", ||                  |   "Recommend": "Yes"             ||                  | }                                || prod_review2.pdf | {                                ||                  |   "FirstName": "Emily",          ||                  |   "LastName": "Smith",           ||                  |   "Middle Name": "Ann",          ||                  |   "Product": "Red Skateboard",   ||                  |   "Purchase Date": "01/10/2023", ||                  |   "Recommend": "MayBe"           ||                  | }                                |+------------------+----------------------------------+
```
CopyFinally, you can create a view that parses the objects in the FILE\_DATAcolumn into separate columns.
You can then query the view to analyze and work with the file contents.


```
CREATEORREPLACEVIEWprod_review_info_vASWITHfile_dataAS(SELECTfile_name,parse_json(file_data)ASfile_dataFROMprod_reviews)SELECTfile_name,file_data:FirstName::varcharASfirst_name,file_data:LastName::varcharASlast_name,file_data:"Middle Name"::varcharASmiddle_name,file_data:Product::varcharASproduct,file_data:"Purchase Date"::dateASpurchase_date,file_data:Recommend::varcharASrecommended,build_scoped_file_url(@my_pdf_stage,file_name)ASscoped_review_urlFROMfile_data;SELECT*FROMprod_review_info_v;+------------------+------------+-----------+-------------+----------------+---------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+| FILE_NAME        | FIRST_NAME | LAST_NAME | MIDDLE_NAME | PRODUCT        | PURCHASE_DATE | RECOMMENDED | SCOPED_REVIEW_URL                                                                                                                                                                                                                                                                                                                                                                                                              ||------------------+------------+-----------+-------------+----------------+---------------+-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|| prod_review1.



Documentation Source:
docs.snowflake.com/en/user-guide/querying-metadata.md

Documentation Title:
Querying Metadata for Staged Files | Snowflake Documentation

Documentation Content:
```
CREATEORREPLACETABLEtable1(filenamevarchar,file_row_numberint,file_content_keyvarchar,file_last_modifiedtimestamp_ntz,start_scan_timetimestamp_ltz,col1varchar,col2varchar);COPYINTOtable1(filename,file_row_number,file_content_key,file_last_modified,start_scan_time,col1,col2)FROM(SELECTMETADATA$FILENAME,METADATA$FILE_ROW_NUMBER,METADATA$FILE_CONTENT_KEY,METADATA$FILE_LAST_MODIFIED,METADATA$START_SCAN_TIME,t.$1,t.$2FROM@mystage1/data1.csv.gz(file_format=>myformat)t);SELECT*FROMtable1;+--------------+-----------------+---------------------------+-------------------------+-------------------------------+------+------+| FILENAME     | FILE_ROW_NUMBER | FILE_CONTENT_KEY          | FILE_LAST_MODIFIED      |  START_SCAN_TIME              | COL1 | COL2 ||--------------+-----------------+---------------------------+-------------------------+-------------------------------+------+------+| data1.csv.gz | 1               | 39ab11bb2cdeacdcdac1234d9 | 2022-08-03 10:15:26.000 | 2023-02-02 01:31:00.778 +0000 | a    | b    || data1.csv.gz | 2               | 2289aab2abcdeaacaaac348d0 | 2022-09-10 11:15:55.000 | 2023-02-02 01:31:00.778 +0000 | c    | d    |+--------------+-----------------+---------------------------+-------------------------+-------------------------------+------+------+
```
CopyWas this page helpful?

YesNoVisit SnowflakeJoin the conversationDevelop with SnowflakeShare your feedbackRead the latest on our blogGet your own certificationPrivacy NoticeSite Terms© 2024Snowflake, Inc. All Rights Reserved.On this page

Metadata ColumnsQuery LimitationsQuery ExamplesLanguage: **English**EnglishFrançaisDeutsch日本語한국어Português



Documentation Source:
docs.snowflake.com/en/user-guide/querying-metadata.md

Documentation Title:
Querying Metadata for Staged Files | Snowflake Documentation

Documentation Content:
000 |  2023-02-02 01:31:00.755 +0000| g  | h  || data1.csv.gz      |                        1 | 39ab11bb2cdeacdcdac1234d9 |     2022-08-03 10:15:26.000 |  2023-02-02 01:31:00.778 +0000| a  | b  || data1.csv.gz      |                        2 | 2289aab2abcdeaacaaac348d0 |     2022-09-10 11:15:55.000 |  2023-02-02 01:31:00.778 +0000| c  | d  |+-------------------+--------------------------+---------------------------+-----------------------------+-------------------------------+----+----+SELECTMETADATA$FILENAME,METADATA$FILE_ROW_NUMBER,METADATA$FILE_CONTENT_KEY,METADATA$FILE_LAST_MODIFIED,METADATA$START_SCAN_TIME,t.$1,t.$2FROM@mystage1t;+-------------------+--------------------------+---------------------------+-----------------------------+-------------------------------+-----+------+| METADATA$FILENAME | METADATA$FILE_ROW_NUMBER | METADATA$FILE_CONTENT_KEY | METADATA$FILE_LAST_MODIFIED |      METADATA$START_SCAN_TIME | $1  | $2   ||-------------------+--------------------------+---------------------------+-----------------------------+-------------------------------+-----+------|| data2.csv.gz      |                        1 | aaa11bb2cccccaaaaac1234d9 |     2022-05-01 10:15:57.000 |  2023-02-02 01:31:00.713 +0000| e|f | NULL || data2.csv.gz      |                        2 | aa387aabb2ccedaaaaac123b8 |     2022-05-01 10:05:35.000 |  2023-02-02 01:31:00.755 +0000| g|h | NULL || data1.csv.



Documentation Source:
docs.snowflake.com/en/user-guide/tutorials/snowflake-in-20minutes.md

Documentation Title:
Snowflake in 20 minutes | Snowflake Documentation

Documentation Content:
Listing the staged files (Optional)¶

You can list the staged files using the LISTcommand.


```
LIST@sf_tuts.public.%emp_basic;
```
CopyThe following is an example result:


```
+--------------------+------+----------------------------------+------------------------------+| name               | size | md5                              | last_modified                ||--------------------+------+----------------------------------+------------------------------|| employees01.csv.gz |  288 | a851f2cc56138b0cd16cb603a97e74b1 | Tue, 9 Jan 2018 15:31:44 GMT || employees02.csv.gz |  288 | 125f5645ea500b0fde0cdd5f54029db9 | Tue, 9 Jan 2018 15:31:44 GMT || employees03.csv.gz |  304 | eafee33d3e62f079a054260503ddb921 | Tue, 9 Jan 2018 15:31:45 GMT || employees04.csv.gz |  304 | 9984ab077684fbcec93ae37479fa2f4d | Tue, 9 Jan 2018 15:31:44 GMT || employees05.csv.gz |  304 | 8ad4dc63a095332e158786cb6e8532d0 | Tue, 9 Jan 2018 15:31:44 GMT |+--------------------+------+----------------------------------+------------------------------+
```
Copy data into target tables¶
-----------------------------

To load your staged data into the target table, execute COPY INTO .

The COPY INTO command uses the virtual warehouse you created
in Create Snowflake objectsto copy files.



