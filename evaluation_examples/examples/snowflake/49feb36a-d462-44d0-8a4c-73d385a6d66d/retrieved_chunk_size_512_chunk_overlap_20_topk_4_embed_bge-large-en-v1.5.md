Documentation Source:
docs.snowflake.com/en/user-guide/tutorials/snowflake-in-20minutes.md

Documentation Title:
Snowflake in 20 minutes | Snowflake Documentation

Documentation Content:
```
INSERTINTOemp_basicVALUES('Clementine','Adamou','cadamou@sf_tuts.com','10510 Sachs Road','Klenak','2017-9-22'),('Marlowe','De Anesy','madamouc@sf_tuts.co.uk','36768 Northfield Plaza','Fangshan','2017-1-26');
```
Copy### Query rows based on email address¶

Return a list of email addresses with United Kingdom top-level domains using the [ NOT ] LIKEfunction:


```
SELECTemailFROMemp_basicWHEREemailLIKE'%.uk';
```
CopyThe following is an example result:


```
+--------------------------+| EMAIL                    ||--------------------------|| gbassfordo@sf_tuts.co.uk || rtalmadgej@sf_tuts.co.uk || madamouc@sf_tuts.co.uk   |+--------------------------+
```



Documentation Source:
docs.snowflake.com/en/user-guide/tutorials/data-quality-tutorial-start.md

Documentation Title:
Tutorial: Getting started with data metric functions | Snowflake Documentation

Documentation Content:
```
USEWAREHOUSEdq_tutorial_wh;INSERTINTOcustomers(account_number,city,country,email,first_name,last_name,phone,state,street,zip_code)VALUES(1589420,'san francisco','usa','john.doe@','john','doe',1234567890,null,null,null);INSERTINTOcustomers(account_number,city,country,email,first_name,last_name,phone,state,street,zip_code)VALUES(8028387,'san francisco','usa','bart.simpson@example.com','bart','simpson',1012023030,null,'market st',94102);INSERTINTOcustomers(account_number,city,country,email,first_name,last_name,phone,state,street,zip_code)VALUES(1589420,'san francisco','usa','john.doe@example.com','john','doe',1234567890,'ca','concar dr',94402),(2834123,'san mateo','usa','jane.doe@example.com','jane','doe',3641252911,'ca','concar dr',94402),(4829381,'san mateo','usa','jim.doe@example.com','jim','doe',3641252912,'ca','concar dr',94402),(9821802,'san francisco','usa','susan.smith@example.com','susan','smith',1234567891,'ca','geary st',94121),(8028387,'san francisco','usa','bart.simpson@example.com','bart','simpson',1012023030,'ca','market st',94102);
```
CopyCreate and work with DMFs¶
--------------------------

In the following sections, we will create a user-defined DMF to measure the count of invalid email addresses and subsequently do the
following:

Schedule the DMF to run every 5 minutes.

Check the DMF table references (find the tables the DMF is set on).

Query a built-in view that contains the result of calling the scheduled DMF.

Unset the DMF from the table to avoid unnecessary serverless credit usage.



Documentation Source:
docs.snowflake.com/en/user-guide/admin-account-identifier.md

Documentation Title:
Account identifiers | Snowflake Documentation

Documentation Content:
|Canada (Central) ca-central-1aws\_ca\_central\_1
|South America (Sao Paulo) sa-east-1aws\_sa\_east\_1
|EU (Ireland) eu-west-1aws\_eu\_west\_1
|Europe (London) eu-west-2aws\_eu\_west\_2
|EU (Paris) eu-west-3aws\_eu\_west\_3
|EU (Frankfurt) eu-central-1aws\_eu\_central\_1
|EU (Zurich) eu-central-2aws\_eu\_central\_2
|EU (Stockholm) eu-north-1aws\_eu\_north\_1
|Asia Pacific (Tokyo) ap-northeast-1aws\_ap\_northeast\_1
|Asia Pacific (Osaka) ap-northeast-3aws\_ap\_northeast\_3
|Asia Pacific (Seoul) ap-northeast-2aws\_ap\_northeast\_2
|Asia Pacific (Mumbai) ap-south-1aws\_ap\_south\_1
|Asia Pacific (Singapore) ap-southeast-1aws\_ap\_southeast\_1
|Asia Pacific (Sydney) ap-southeast-2aws\_ap\_southeast\_2
|Asia Pacific (Jakarta) ap-southeast-3aws\_ap\_southeast\_3
**Google Cloud Platform (GCP)**|US Central1 (Iowa) us-central1gcp\_us\_central1
|US East4 (N. Virginia) us-east4gcp\_us\_east4
|Europe West2 (London) europe-west2gcp\_europe\_west2
|Europe West4 (Netherlands) europe-west4gcp\_europe\_west4
**Microsoft Azure**|West US 2 (Washington) westus2azure\_westus2
|Central US (Iowa) centralusazure\_centralus
|South Central US (Texas) southcentralusazure\_southcentralus
|East US 2 (Virginia) eastus2azure\_eastus2
|US Gov Virginia usgovvirginiaazure\_usgovvirginiaAvailable only for accounts on Business Critical (or higher);



Documentation Source:
docs.snowflake.com/en/release-notes/2024/other/2024-02-21.md

Documentation Title:
February 21, 2024 — Data sharing & collaboration for accounts in U.S. government regions | Snowflake Documentation

Documentation Content:
government regions.

After accepting the cross-region disclaimer, anyone in your account with the required privileges can do the following:

Publish free and limited trial listings on the Snowflake Marketplace.

Share free listings directly with consumers.

Access and install free and limited trial listings from the Snowflake Marketplace.

Install free listings shared directly with your account.


Some limitations apply. For more details, see:

Prepare to provide listings from accounts in U.S. government regionsPrepare to access listings from accounts in U.S. government regionsLimitations for accessing listings from accounts in U.S. government regionsWas this page helpful?

YesNoVisit SnowflakeJoin the conversationDevelop with SnowflakeShare your feedbackRead the latest on our blogGet your own certificationPrivacy NoticeSite Terms© 2024Snowflake, Inc. All Rights Reserved.Language: **English**EnglishFrançaisDeutsch日本語한국어Português



