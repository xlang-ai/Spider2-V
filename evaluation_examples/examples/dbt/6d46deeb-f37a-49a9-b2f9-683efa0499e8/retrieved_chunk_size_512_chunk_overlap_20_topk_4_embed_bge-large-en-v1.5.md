Documentation Source:
docs.snowflake.com/en/user-guide/tutorials/snowflake-in-20minutes.md

Documentation Title:
Snowflake in 20 minutes | Snowflake Documentation

Documentation Content:
Download the set of sample data files. Right-click the name of the archive
	file, getting-started.zip, and save the link/file to your local file system.
	
	Unzip the sample files. The tutorial assumes you unpacked files into one of the following directories:
	Linux/macOS: /tmp
	
	Windows: C:\\tempEach file has five data records. The data uses a comma (,) character as field
delimiter. The following is an example record:


```
Althea,Featherstone,afeatherstona@sf_tuts.com,"8172 Browning Street, Apt B",Calatrava,7/12/2017

```
Copy

There are no blank spaces before or after the commas separating the
fields in each record. This is the default that Snowflake expects when loading CSV data.

Log in to SnowSQL¶
------------------

After you have SnowSQL, start SnowSQL to connect to Snowflake:

Open a command line window.

2. Start SnowSQL:


```
$snowsql-a-u

```
CopyWhere:


	is the unique identifier for your Snowflake account.The preferred format of the account identifieris as follows:
	
	`organization_name-account_name`Names of your Snowflake organization and account. For more information, see Format 1 (preferred): Account name in your organization.
	
	is the login name for your Snowflake user.Note

If your account has an identity provider (IdP) that has been defined for your account, you can use a web browser to authenticate instead of a password, as the following example demonstrates:


```
$snowsql-a-u--authenticatorexternalbrowser

```
CopyFor more information, see Using a web browser for federated authentication/SSO.
When SnowSQL prompts you, enter the password for your Snowflake user.



Documentation Source:
docs.snowflake.com/en/developer-guide/sql-api/authenticating.md

Documentation Title:
Authenticating to the server | Snowflake Documentation

Documentation Content:
1. Generate the fingerprint (a SHA-256 hash) of the public key for the user. Prefix the fingerprint with SHA256:.
	For example:
	
	`SHA256:hash`You can also execute the SQL DESCRIBE USERcommand to get the value from
	the RSA\_PUBLIC\_KEY\_FP property.
	2. Generate a JSON Web Token (JWT)with the following fields in the payload:
	
	
	
	|Field
	
	Description
	
	Example
	
	
	|  |
	|iss Issuer of the JWT. Set it to the following value:`account_identifier.user.SHA256:public_key_fingerprint`where: 	* account\_identifieris your Snowflake account identifier.If you are using the account locator, exclude any region information from 	the account locator. 	useris your Snowflake user name.`SHA256:public_key_fingerprint`is the fingerprint that you generated in the previous step.NoteThe account\_identifierand uservalues must use all uppercase characters. If your account ID contains periods (.), you must replace them with hyphens (-), as periods in an account identifier cause the JWT to be invalid. |`MYORGANIZATION-MYACCOUNT.MYUSER.SHA256:public_key_fingerprint`
	| --- |
	|sub Subject for the JWT. Set it to the following value:`account_identifier.user` |MYORGANIZATION-MYACCOUNT.MYUSER
	|iatIssue time for the JWT in UTC. Set the value to the current time value as either seconds or milliseconds.
	
	1615370644(seconds) .1615370644000(milliseconds)
	
	
	|exp Expiration time for the JWT in UTC. You can specify the value as either seconds or milliseconds.NoteThe JWT is valid for at most one hour after the token is issued, even if you specify a longer expiration time. |1615374184(seconds) .1615374184000(milliseconds)
	3. In each API request that you send, set the following headers:
	
	
		* `Authorization:BearerJWT`where JWTis the token that you generated.
		`X-Snowflake-Authorization-Token-Type:KEYPAIR_JWT`



Documentation Source:
docs.snowflake.com/en/developer-guide/snowflake-cli-v2/connecting/manage-connections.md

Documentation Title:
Managing connections | Snowflake Documentation

Documentation Content:
```
snowsql-q"select 42;"--temporary-connection\--accountmyaccount\--userjdoe

```
Copy
```
select 42;+----+| 42 ||----|| 42 |+----+
```
You can use the following command options to override connection attributes:

`--account,--accountnameTEXT`: Name assigned to your Snowflake account.

`--user,--usernameTEXT`: Username to connect to Snowflake.

* `--passwordTEXT`: Snowflake password.

Caution

For improved security, Snowflake strongly recommends using the $SNOWFLAKE\_PASSWORD environment variable so the password is not included in the logs.
`--authenticatorTEXT`: Snowflake authenticator.

`--private-key-pathTEXT`: Snowflake private key path.

`--database,--dbnameTEXT`: Database to use.

`--schema,--schemanameTEXT`: Database schema to use.

`--role,--rolenameTEXT`: Role to use.

`--warehouseTEXT`: Warehouse to use.

`--temporary-connection[-x]`: Use the connection defined with command line parameters instead of one defined in config.toml.

How to use a different configuration file¶
------------------------------------------

In some situations, such as a continuous integration, continuous deployment (CI/CD) environment, you might prefer
to create dedicated configuration files for testing and deployment pipelines instead of defining all of the possible
configurations in a Snowflake default configuration file.

If you want to use a different configuration file instead of your default file, you can use the
--config-fileoption for the snowcommand, such as:


```
snow--config-file="my_config.toml"connectiontest
```
CopyWas this page helpful?

YesNoVisit SnowflakeJoin the conversationDevelop with SnowflakeShare your feedbackRead the latest on our blogGet your own certificationPrivacy NoticeSite Terms© 2024Snowflake, Inc. All Rights Reserved.On this page

How to test a connectionHow to use a temporary connectionHow to use a different configuration fileRelated content

Snowflake CLIConnecting to Snowflake and configuring Snowflake CLISpecifying your Snowflake credentialsConfigure loggingsnow connection commandsLanguage: **English**EnglishFrançaisDeutsch日本語한국어Português



Documentation Source:
docs.snowflake.com/en/user-guide/connecting.md

Documentation Title:
Logging in to Snowflake | Snowflake Documentation

Documentation Content:
Using private connectivity¶

After completing the configuration to use private connectivity,
access Snowsight:

* To sign in to Snowsight with private connectivity directly, without having been logged in to the Classic Console previously:


	1. Enter either of the following URLs in the browser location bar:
	
	
		`https://app-orgname-account_name.privatelink.snowflakecomputing.com``https://app.cloud_region_id.privatelink.snowflakecomputing.com`Where:
	
	
		orgnameis the name of your Snowflake organization.
		
		account\_nameis the unique name of your account within your organization.
		
		cloud\_region\_idis the identifier for the cloud region (controlled by the cloud platform).After signing in, you can find these details in the account selector in Snowsight.
	
	For details, see Locate your Snowflake account information in Snowsightand Format 1 (preferred): Account name in your organization.
	
	Note
	
	If you are unsure of the values to enter, please contact your internal Snowflake administrator before contacting Snowflake
	Support.
	Enter your Snowflake credentials.
* Starting from the Classic Console, to sign in to Snowsight using private connectivity to the Snowflake service:


	Sign in to the Classic Console.
	
	2. In the upper-right corner of the Classic Console, select Snowsight!.
	
	Snowsight opens in a new tab or window.

For more information about the tasks you can perform in Snowsight, refer to Snowsight quick tour.

Logging in Using SnowSQL¶
-------------------------

SnowSQL is the command line client for connecting to Snowflake to execute SQL queries and perform all DDL and DML operations, including loading data into and unloading data out of database tables.



