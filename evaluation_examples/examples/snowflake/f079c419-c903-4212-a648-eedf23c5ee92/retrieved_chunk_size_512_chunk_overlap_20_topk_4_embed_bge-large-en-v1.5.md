Documentation Source:
docs.snowflake.com/en/user-guide/data-exchange-using.md

Documentation Title:
Configuring and using a Data Exchange | Snowflake Documentation

Documentation Content:
Accessing the shared data¶

If your request for a listing in the Data Exchange is approved:

Sign in to Snowsight.

Select Data Products» Private Sharing.

Select the Shared With Youtab.

Locate the listing you requested and select Get Datafor the listing.

Enter the name for the database to create in your account from the share.

Select roles that you want to have access to the database created from the share.

7. Accept Snowflake’s consumer terms and the provider’s terms of use. You only need to accept the listing terms when you create a database from a share for the first time.

Note

Accepting terms using SQL is not supported.
Select Create Database.


After you create the database from share, the Get Databutton is replaced with the View Databasebutton.

See also: Usage metrics shared with providers

Was this page helpful?

YesNoVisit SnowflakeJoin the conversationDevelop with SnowflakeShare your feedbackRead the latest on our blogGet your own certificationPrivacy NoticeSite Terms© 2024Snowflake, Inc. All Rights Reserved.On this page

Data Exchange adminData providersData consumersLanguage: **English**EnglishFrançaisDeutsch日本語한국어Português



Documentation Source:
docs.snowflake.com/en/user-guide/data-exchange-using.md

Documentation Title:
Configuring and using a Data Exchange | Snowflake Documentation

Documentation Content:
Viewing listing requests¶

To view requests that you made for data in a Data Exchange, use the Requeststab.

Sign in to Snowsight.

Select Data Products» Private Sharing.

Select the Requeststab.

Select Inbound.


Note

To see requests from listings on the Snowflake Marketplace, such as those for personalized listings or free listings in another region,
use Provider Studio.
See Managing Listing Requests as a Provider.

If a request is denied, a comment is provided next to the request, explaining the reason for denial. In such cases, you can make the necessary adjustments and resubmit your request.



Documentation Source:
docs.snowflake.com/en/user-guide/tutorials/tasty-bytes-sql-load.md

Documentation Title:
Load and query sample data using SQL | Snowflake Documentation

Documentation Content:
Note

This tutorial is only available to users with a trial account. The sample worksheet is not available
for other types of accounts.

Step 1. Sign in using Snowsight¶
--------------------------------

To access Snowsight over the public Internet, do the following:

In a supported web browser, navigate to https://app.snowflake.com.

Provide your account identifieror account URL.
If you’ve previously signed in to Snowsight, you might see an account name that you can select.

Sign in using your Snowflake account credentials.

Step 2. Open the SQL worksheet for loading and querying data¶
-------------------------------------------------------------

You can use worksheets to write and run SQL commands on your Snowflake database. Your trial account has access
to a pre-loaded worksheet for this tutorial. The worksheet has the SQL commands that
you will run to create a database, load data into it, and query the data. For more information
about worksheets, see Getting started with worksheets.

To open the pre-loaded tutorial worksheet:

Select Projects» Worksheetsto open the list of worksheets.

2. Open [Tutorial] Using SQL to load and query sample data.

Your worksheet looks similar to the following image.

!Step 3. Set the role and warehouse to use¶
------------------------------------------

The role you use determines the privileges you have. In this tutorial, use the
ACCOUNTADMIN system role so that you can view and manage objects in your account.
For more information, see Using the ACCOUNTADMIN Role.

A warehouse provides the required resources to create and manage objects and run
SQL commands. These resources include CPU, memory, and temporary storage. Your
trial account has a virtual warehouse (compute\_wh) that you can use for this
tutorial. For more information, see Virtual warehouses.

To set the role and warehouse to use, do the following:

1. In the open worksheet, place your cursor in the USE ROLE line.


```
USEROLEaccountadmin;
```
Copy
2. In the upper-right corner of the worksheet, select Run.

Note

In this tutorial, run SQL statements one at a time. Do not select Run All.
3. Place your cursor in the USE WAREHOUSE line, then select Run.



Documentation Source:
docs.snowflake.com/en/user-guide/data-exchange-using.md

Documentation Title:
Configuring and using a Data Exchange | Snowflake Documentation

Documentation Content:
How do I access the Data Exchange to browse listings?¶

All users can browse listings in the Data Exchange, but only users with the ACCOUNTADMIN role or the IMPORT SHAREprivilege can get or request data.

If you do not have sufficient privileges, you can do one of the following:

Request your ACCOUNTADMIN to grant you the IMPORT SHARE privilege.

Request your ACCOUNTADMIN to get data, and grant you IMPORTED PRIVILEGES on the database created from the share.
For more information, see Granting privileges on a shared database.


To access the listings available to you as a consumer of the Data Exchange:

Sign in to Snowsight.

Select Data Products» Private Sharing.

Select the Shared With Youtab.



