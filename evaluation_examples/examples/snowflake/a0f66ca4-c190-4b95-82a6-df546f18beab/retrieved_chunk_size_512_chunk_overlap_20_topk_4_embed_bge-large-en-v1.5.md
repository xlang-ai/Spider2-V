Documentation Source:
docs.snowflake.com/en/user-guide/tutorials/users-and-roles-tutorial.md

Documentation Title:
Create users and grant roles | Snowflake Documentation

Documentation Content:
```
CREATEORREPLACEUSERsnowmanPASSWORD='sn0wf@ll'LOGIN_NAME='snowstorm'FIRST_NAME='Snow'LAST_NAME='Storm'EMAIL='snow.storm@snowflake.com'MUST_CHANGE_PASSWORD=trueDEFAULT_WAREHOUSE=COMPUTE_WH;
```
CopyThis command returns the following output:

User SNOWMAN successfully created.If you were creating a real user in a real Snowflake account, you would now send the
following information in a secure manner to the person who would need to access
this new account:

Snowflake Account URL: the Snowflake account link where the user will log in.
You can find this link at the top of your browser
(for example: https://app.snowflake.com/myorg/myaccount/,
where myorgis the Snowflake organization ID, and myaccountis the account ID).

LOGIN\_NAME, as specified in the CREATE USER command.

PASSWORD, as specified in the CREATE USER command.

Step 5. Grant a system role and warehouse access to the user¶
-------------------------------------------------------------

Now that you have created a user, you can use the SECURITYADMIN role to grant the
SYSADMIN role to the user, as well as grant USAGE on the COMPUTE\_WH warehouse.

Granting a role to another role creates a parent-child relationship between the roles
(also referred to as a role hierarchy). Granting a role to a user enables the user to perform
all operations allowed by the role (through the access privileges granted to the role).

The SYSADMIN role has privileges to create warehouses, databases, and database objects
in an account and grant those privileges to other roles. Only grant this role to users who should
have these privileges. For information about other system-defined roles, see
see Overview of Access Control.

To grant the user access to a role and a warehouse, do the following:

1. In the open worksheet, place your cursor in the USE ROLEline,
then select Run.


```
USEROLESECURITYADMIN;
```
Copy
2. Place your cursor in the GRANT ROLEline, enter the name of the user you created,
then select Run.


```
GRANTROLESYSADMINTOUSERsnowman;
```
Copy
3. Place your cursor in the GRANT USAGE line, then select Run.



Documentation Source:
docs.snowflake.com/en/user-guide/tutorials/users-and-roles-tutorial.md

Documentation Title:
Create users and grant roles | Snowflake Documentation

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

Step 2. Open the [Template] worksheet¶
--------------------------------------

You can use worksheets to write and run SQL commands on your database.
Your trial account has access to a pre-loaded template worksheet for this tutorial.
The worksheet contains the SQL commands that you will run to set the role context,
create a user, and grant role privileges. Because it is a template worksheet, you
will be invited to enter your own values for certain SQL parameters.

For more information about worksheets, see Getting started with worksheets.

To open the worksheet:

Select Projects» Worksheetsto open the list of worksheets.

2. Open [Template] Adding a user and granting roles.

Your browser looks similar to the following image.

!Step 3. Set the role to use¶
----------------------------

The role you use determines the privileges you have. In this tutorial, use the
USERADMIN system role so that you can create and manage users and roles in your
account. For more information, see Overview of Access Control.

To set the role to use, do the following:

1. In the open worksheet, place your cursor in the USE ROLEline.



Documentation Source:
docs.snowflake.com/en/user-guide/tutorials/users-and-roles-tutorial.md

Documentation Title:
Create users and grant roles | Snowflake Documentation

Documentation Content:
```
USEROLEUSERADMIN;
```
Copy
2. In the upper-right corner of the worksheet, select Run.

Note

In this tutorial, run SQL statements one at a time. Do not select Run All.
Step 4. Create a user¶
----------------------

A Snowflake user has login credentials. When a user is granted a role, the user can
perform all the operations that the role allows, via the privileges that were
granted to the role. For more information, see User management.

In this step of the tutorial, you create a user with a name, a password, and some
other properties.

In the open worksheet, place your cursor in the CREATE USERline,
insert a username and other parameter values of your choice (an example is shown below), and
select Run.

For MUST\_CHANGE\_PASSWORD, set the value to true, which ensures that a password
reset is requested on first login. For DEFAULT\_WAREHOUSE, use COMPUTE\_WH.



Documentation Source:
docs.snowflake.com/en/user-guide/admin-user-management.md

Documentation Title:
User management | Snowflake Documentation

Documentation Content:
Using Snowsight¶

Sign in to Snowsight.

Select Admin» Users & Roles.

Select + User.

In the User Namefield, enter a unique identifier for the user. The user uses this identifier to sign in to Snowflake unless you
specify a login name.

Optionally specify an email address for the user in the Emailfield.

In the Passwordand Confirm Passwordfields, enter the password for the user.

Optionally add a comment explaining why you created the user.

Leave the Force user to change password on first time logincheckbox selected to force the user to change their password when they
sign in.

9. Optionally select Advanced User Optionsto specify additional details about the user:


	Login Nameto use instead of the User Namewhen signing in to Snowflake.
	
	Display Namethat appears after signing in.
	
	First Nameand Last Nameto complete the user profile.
	
	Default Role, Default Warehouse, and Default Namespace.
Select Create User.



