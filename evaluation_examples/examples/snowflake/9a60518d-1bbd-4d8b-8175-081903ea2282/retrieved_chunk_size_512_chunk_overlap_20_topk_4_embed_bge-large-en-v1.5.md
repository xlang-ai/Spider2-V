Documentation Source:
docs.snowflake.com/en/user-guide/data-exchange-managing-data-listings.md

Documentation Title:
Managing data listings | Snowflake Documentation

Documentation Content:
Creating and publishing a data listing¶

To create a free or personalized data listing:

In Snowsight, navigate to Data Products» Private Sharing.

Select the Share Datadrop-down list and select a data exchange.

In the New Listingdialog box, enter the listing title as it appears to the consumers and select the listing type. For more information about listing type, see Types of Listings.

4. Complete each of the sections for the new listing. You can save the draft at any time to finish it later. For a description of each section and related fields, see Listings Capabilities Reference.

For a free listing, to associate a share with the listing, when editing the Datasection:

Note

Until a listing is published, it can only be associated with a share in the local/primary account. After the listing is published, it can be associated with a share in additional regions that you have selected.


	Select Select Data.
	
	2. If a secure share exists, navigate to the share and select it. If a share does not exist, navigate to the desired database and select the database objects you wish to add to the share.
	
	Note
	
	If you do not see a share, it is either already attached to another listing, or has been previously shared with consumers.
	Select Done.
	
	(Optional) You can change the default name for the secure share.
	
	Select Save.
5. Once you complete all of the sections, select Publishto publish the listing to the selected regions.

The Publishbutton is not activated if:


	Any of the provided sample SQL queries fail validation. For more information, see Data listing fields.
	
	You are not the share owner.



Documentation Source:
docs.snowflake.com/en/user-guide/data-exchange-managing-data-listings.md

Documentation Title:
Managing data listings | Snowflake Documentation

Documentation Content:
Approving consumer requests for data listings in a remote region¶

Note

For **personalized**listings, data is not automatically available in remote regions. The provider is responsible for replicating their data to each of these regions.

For **free**listings, you have an option to pre-associate a share with the listing in a remote region. This allows consumers to get the share instantly without submitting a request. You can also replicate data and attach a share to a listing after receiving a request from the first consumer in a region. Once the listing is attached to the share, all consumers in that region can access the share instantly.

You can specify whether a listing can be fulfilled by a select provider account(s) or by any account in the organization.

To approve a request for a data listing submitted by a consumer:

Note

If the consumer is in a different region, before attaching a share, you must set up replication of data to the account in each remote region. For more information, see Sharing data securely across regions and cloud platforms.

Navigate to Data Products» Private Sharing.

Select the Requeststab.

Select Reviewnext to the listing name.

In the Associate Secure Sharesection, select an account where you wish to create the share.

Select the role that owns the share and the shared database objects (or has the necessary privileges on the database objects to be able to add them to a share).

select Select Data.

7. If a secure share exists, navigate to the share and select it. If a share does not exist, navigate to the desired database and select the database objects you wish to add to the share.

Note

If you do not see a share, it is either already attached to another listing, or has been previously shared with consumers.
Select Done.

(Optional) You can change the default name for the secure share.

10. Select Fullfill Request.

Tip

If you receive an error when fulfilling a request for a remote region, consider the following:


	Has the remote account been added to the Marketplace as a provider?
	
	Is the remote account part of the same organization as the account you published the listing from?
	
	Did you create a new share using the ACCOUNTADMIN role?
	
	Have you added other consumers to the share you are trying to attach?



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
docs.snowflake.com/en/user-guide/data-exchange-managing-data-listings.md

Documentation Title:
Managing data listings | Snowflake Documentation

Documentation Content:
Editing a data listing¶

When you publish a new version of the listing, it overwrites the previously published listing. If you remove a region that was previously available, consumers in that region will no longer have access to the shared dataset.

To edit a data listing:

Sign in to Snowsightas an ACCOUNTADMIN.

In the navigation menu, click Data Products» Private Sharing» Shared by My Account.

Click the name of the listing you wish to update.

Next to the listing title, click New Draft.

Click Editfor the section you wish to update.

Click Publish.



