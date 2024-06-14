Documentation Source:
docs.snowflake.com/en/sql-reference/functions/max_by.md

Documentation Title:
MAX_BY | Snowflake Documentation

Documentation Content:
```
SELECT*FROMemployees;
```
Copy
```
+-------------+---------------+--------+| EMPLOYEE_ID | DEPARTMENT_ID | SALARY ||-------------+---------------+--------||        1001 |            10 |  10000 ||        1020 |            10 |   9000 ||        1030 |            10 |   8000 ||         900 |            20 |  15000 ||        2000 |            20 |   NULL ||        2010 |            20 |  15000 ||        2020 |            20 |   8000 |+-------------+---------------+--------+
```
The following example returns the ID of the employee with the highest salary:


```
SELECTMAX_BY(employee_id,salary)FROMemployees;
```
Copy
```
+-----------------------------+| MAX_BY(EMPLOYEE_ID, SALARY) ||-----------------------------||                         900 |+-----------------------------+
```
Note the following:

Because more than one row contains the maximum value for the salarycolumn, the function is non-deterministic and might
return the employee ID for a different row in subsequent executions.

The function ignores the NULL value in the salarycolumn when determining the rows with the maximum values.


The following example returns an ARRAY containing the IDs of the employees with the three highest salaries:



Documentation Source:
docs.snowflake.com/en/user-guide/queries-hierarchical.md

Documentation Title:
Querying Hierarchical Data | Snowflake Documentation

Documentation Content:
```
SELECTemps.title,emps.employee_ID,mgrs.employee_IDASMANAGER_ID,mgrs.titleAS"MANAGER TITLE"FROMemployeesASempsLEFTOUTERJOINemployeesASmgrsONemps.manager_ID=mgrs.employee_IDORDERBYmgrs.employee_IDNULLSFIRST,emps.employee_ID;+----------------------------+-------------+------------+----------------------------+| TITLE                      | EMPLOYEE_ID | MANAGER_ID | MANAGER TITLE              ||----------------------------+-------------+------------+----------------------------|| President                  |           1 |       NULL | NULL                       || Vice President Engineering |          10 |          1 | President                  || Vice President HR          |          20 |          1 | President                  || Programmer                 |         100 |         10 | Vice President Engineering || QA Engineer                |         101 |         10 | Vice President Engineering || Health Insurance Analyst   |         200 |         20 | Vice President HR          |+----------------------------+-------------+------------+----------------------------+
```
CopyThis concept can be extended to as many levels as needed, as long as you know how many levels are needed. But if
the number of levels changes, the queries need to change.

Using CONNECT BY or Recursive CTEs to Query Hierarchical Data¶
--------------------------------------------------------------

Snowflake provides two ways to query hierarchical data in which the number of levels is not known in advance:

Recursive CTEs (common table expressions).

`CONNECTBY`clauses.



Documentation Source:
docs.snowflake.com/en/user-guide/queries-hierarchical.md

Documentation Title:
Querying Hierarchical Data | Snowflake Documentation

Documentation Content:
```
CREATEORREPLACETABLEemployees(titleVARCHAR,employee_IDINTEGER,manager_IDINTEGER);
```
Copy
```
INSERTINTOemployees(title,employee_ID,manager_ID)VALUES('President',1,NULL),-- The President has no manager.('Vice President Engineering',10,1),('Programmer',100,10),('QA Engineer',101,10),('Vice President HR',20,1),('Health Insurance Analyst',200,20);
```
CopyStoring an entire hierarchy of data in one table works best if all levels
of the hierarchy store the same data – in our example, employee ID, title, etc.
If the data at different levels doesn’t fit the same record structure, then
storing all the data in one table might not be practical.

Using Joins to Query Hierarchical Data¶
---------------------------------------

In a two-level hierarchy (for example, managers and employees), the data can be queried with a two-way join:


```
SELECTemployees.title,employees.employee_ID,managers.employee_IDASMANAGER_ID,managers.titleAS"MANAGER TITLE"FROMemployees,managersWHEREemployees.manager_ID=managers.employee_IDORDERBYemployees.title;+----------------------------+-------------+------------+---------------+| TITLE                      | EMPLOYEE_ID | MANAGER_ID | MANAGER TITLE ||----------------------------+-------------+------------+---------------|| Vice President Engineering |          10 |          1 | President     || Vice President HR          |          20 |          1 | President     |+----------------------------+-------------+------------+---------------+
```
CopyIn a three-level hierarchy, you can use a 3-way join:



Documentation Source:
docs.snowflake.com/en/user-guide/tutorials/tasty-bytes-python-load.md

Documentation Title:
Load and query sample data using Snowpark Python | Snowflake Documentation

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

Step 2. Open the Python worksheet¶
----------------------------------

You can use Python worksheets to write and run Python code. Your trial account has access
to a pre-loaded Python worksheet for this tutorial. The worksheet has the Python code that
you will run to create a database, load data into it, and query the data. For more information
about Python worksheets, see Writing Snowpark Code in Python Worksheets.

To open the pre-loaded tutorial Python worksheet:

Select Projects» Worksheetsto open the list of worksheets.

2. Open [Tutorial] Using Python to load and query sample data.

Your worksheet looks similar to the following image.

!This pre-loaded Python worksheet automatically uses the ACCOUNTADMIN system role so that
you can view and manage objects in your account. For more information, see
Using the ACCOUNTADMIN Role.

The worksheet also uses the COMPUTE\_WH virtual warehouse. A warehouse provides
the required resources to create and manage objects and run SQL commands. These
resources include CPU, memory, and temporary storage. For more information, see
Virtual warehouses.

Step 3. Learn how to use Python worksheets¶
-------------------------------------------

Python worksheets let you use Snowpark Pythonin Snowsight to run SQL statements. This step in this tutorial describes the code in each step
in the Python worksheet. When you use a Python worksheet, you cannot run individual blocks of
code separately. You must run the whole worksheet. Before you select Runin the worksheet,
review the following steps so that you better understand the Python code.

1. In the open Python worksheet, this step includes the following code:



