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
docs.snowflake.com/en/sql-reference/constructs/where.md

Documentation Title:
WHERE | Snowflake Documentation

Documentation Content:
```
createtabledepartments(department_IDINTEGER,department_nameVARCHAR,locationVARCHAR);insertintodepartments(department_id,department_name,location)values(10,'CUSTOMER SUPPORT','CHICAGO'),(40,'RESEARCH','BOSTON'),(80,'Department with no employees yet','CHICAGO'),(90,'Department with no projects or employees yet','EREHWON');createtableprojects(project_idinteger,project_namevarchar,department_idinteger);insertintoprojects(project_id,project_name,department_id)values(4000,'Detect fake product reviews',40),(4001,'Detect false insurance claims',10),(9000,'Project with no employees yet',80),(9099,'Project with no department or employees yet',NULL);createtableemployees(employee_IDINTEGER,employee_nameVARCHAR,department_idINTEGER,project_idINTEGER);insertintoemployees(employee_id,employee_name,department_id,project_id)values(1012,'May Aidez',10,NULL),(1040,'Devi Nobel',40,4000),(1041,'Alfred Mendeleev',40,4001);
```
CopyExecute a 3-way inner join. This does not use (+)(or the OUTER keyword) and is therefore an inner join. The
output includes only rows for which there is a department, project, and employee:


```
SELECTd.department_name,p.project_name,e.employee_nameFROMdepartmentsd,projectsp,employeeseWHEREp.department_id=d.department_idANDe.project_id=p.project_idORDERBYd.department_id,p.project_id,e.employee_id;+------------------+-------------------------------+------------------+| DEPARTMENT_NAME  | PROJECT_NAME                  | EMPLOYEE_NAME    ||------------------+-------------------------------+------------------|| CUSTOMER SUPPORT | Detect false insurance claims | Alfred Mendeleev || RESEARCH         | Detect fake product reviews   | Devi Nobel       |+------------------+-------------------------------+------------------+
```
CopyPerform an outer join. This is similar to the preceding statement exceptthat this uses (+)to make the
second join a right outer join. The effect is that if a department is included in the output, then all of that
department’s projects are included, even if those projects have no employees:



