Documentation Source:
docs.snowflake.com/en/user-guide/cleanrooms/external-data-gcp.md

Documentation Title:
Snowflake Data Clean Room: External data from Google Cloud Platform | Snowflake Documentation

Documentation Content:
Authenticate the connector¶

You are now ready to authenticate the connector to make sure it can access the GCP bucket. To authenticate the connector:

In the left navigation of the clean room, select Connectorsand expand the Google Cloudsection. If you are signed out of the
clean room, see Sign in to the web app.

Select the GCP bucket you are connecting to, and select Authenticate.

Remove access to external data on GCP¶
--------------------------------------

To remove access to a GCP bucket from a clean room environment:

Navigate to the sign in page.

Enter your email address, and select Continue.

Enter your password.

If you are associated with multiple clean room environments, select the Snowflake account you want to use.

In the left navigation, select Connectors, then expand the Google Cloudsection.

Find the GCP bucket that is currently connected, and select the trash can icon.

Was this page helpful?

YesNoVisit SnowflakeJoin the conversationDevelop with SnowflakeShare your feedbackRead the latest on our blogGet your own certificationPrivacy NoticeSite Terms© 2024Snowflake, Inc. All Rights Reserved.On this page

Connect to a Google Cloud Platform bucketRemove access to external data on GCPRelated content

Introduction to Snowflake Data Clean RoomsSnowflake Data Clean Room: External data from an Amazon S3 bucketSnowflake Data Clean Room: External data from Azure Blob StorageLanguage: **English**EnglishFrançaisDeutsch日本語한국어Português



Documentation Source:
docs.snowflake.com/en/user-guide/client-redirect.md

Documentation Title:
Redirecting client connections | Snowflake Documentation

Documentation Content:
Drop a connection using Snowsight¶

!Preview Feature— Open

Client Redirect in Snowsight is available to all accounts that are Business Critical Edition (or higher).
Currently this feature is not supported for accounts using private connectivity.

To delete a connection, you must sign in as a user with the ACCOUNTADMIN role to the *source*account with the primary connection.

Sign in to Snowsight and navigate to Admin» Accounts.

Select Client Redirect.

Locate the connection you want to delete. Select the Moremenu (…) in the last column of the row.

Select Drop, then select Drop Connection



Documentation Source:
docs.snowflake.com/en/user-guide/cleanrooms/tutorials/cleanroom-web-app-tutorial.md

Documentation Title:
Tutorial: Get started with the web app of a Snowflake Data Clean Room | Snowflake Documentation

Documentation Content:
Delete the clean room¶

Deleting a clean room in the provider account removes it from both the provider account and the consumer account.

To delete a clean room:

Navigate to the sign in page.

Enter your email address, and select Continue.

Enter your password.

Select the Snowflake account that you used as the provider account.

In the left navigation, select Clean Rooms.

On the Createdtab, find the Tutorialtile and select the More icon (!).

Select Delete.

Select Proceed.

Learn more¶
-----------

Supported Regions for Feature

Available in select regions on Amazon Web Services and Microsoft Azure. See Available regions.

Congratulations! You have now used the web app to create and share a clean room as a provider. You have also acted as the consumer
who is using the clean room to analyze data within a privacy-preserving environment.

You can use the following resources to learn more:

For general information, see Introduction to Snowflake Data Clean Rooms.

For more information about the web app, see Snowflake Data Clean Rooms: Web app overview.

For information about using the developer APIs to work with a Snowflake Data Clean Room programmatically, see
Snowflake Data Clean Rooms: Developer APIs overview.

Was this page helpful?

YesNoVisit SnowflakeJoin the conversationDevelop with SnowflakeShare your feedbackRead the latest on our blogGet your own certificationPrivacy NoticeSite Terms© 2024Snowflake, Inc. All Rights Reserved.Language: **English**EnglishFrançaisDeutsch日本語한국어Português



Documentation Source:
docs.snowflake.com/en/user-guide/cleanrooms/external-data-azure.md

Documentation Title:
Snowflake Data Clean Room: External data from Azure Blob Storage | Snowflake Documentation

Documentation Content:
Authenticate the connector¶

You are now ready to authenticate the connector to make sure it can access Azure Blob Storage. To authenticate the connector:

In the clean room environment, select Connectorsand expand the Microsoft Azuresection. If you are signed out of the
clean room, see Sign in to the web app.

Select the blob storage you are connecting to, and select Authenticate.

Remove access to external data on AWS¶
--------------------------------------

To remove access to Azure Blob Storage from a clean room environment:

Navigate to the sign in page.

Enter your email address, and select Continue.

Enter your password.

If you are associated with multiple clean room environments, select the Snowflake account you want to use.

In the left navigation, select Connectorsand expand the Microsoft Azuresection.

Find the blob storage that is currently connected, and select the trash can icon.

Was this page helpful?

YesNoVisit SnowflakeJoin the conversationDevelop with SnowflakeShare your feedbackRead the latest on our blogGet your own certificationPrivacy NoticeSite Terms© 2024Snowflake, Inc. All Rights Reserved.On this page

Connect to Azure Blob StorageRemove access to external data on AWSRelated content

Introduction to Snowflake Data Clean RoomsSnowflake Data Clean Room: External data from an Amazon S3 bucketSnowflake Data Clean Room: External data from Google Cloud PlatformLanguage: **English**EnglishFrançaisDeutsch日本語한국어Português



