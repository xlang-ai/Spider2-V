Documentation Source:
superset.apache.org/docs/contributing/resources/index.md

Documentation Title:
Resources | Superset

Documentation Content:
DATETIMEchanged\_by\_fk: INTEGERuuid: BINARY(16)resource: VARCHAR(32)Log (logs)id: INTEGERuser\_id: INTEGERdashboard\_id: INTEGERslice\_id: INTEGERjson: TEXTdttm: DATETIMEduration\_ms: INTEGERaction: VARCHAR(512)referrer: VARCHAR(1024)KeyValue (keyvalue)id: INTEGERvalue: TEXTViewMenu (ab\_view\_menu)id: INTEGERname: VARCHAR(250)PermissionView (ab\_permission\_view)id: INTEGERpermission\_id: INTEGERview\_menu\_id: INTEGERRegisterUser (ab\_register\_user)id: INTEGERregistration\_date: DATETIMEfirst\_name: VARCHAR(64)last\_name: VARCHAR(64)username: VARCHAR(64)password: VARCHAR(256)email: VARCHAR(64)registration\_hash: VARCHAR(256)Permission (ab\_permission)id: INTEGERname: VARCHAR(100)User (ab\_user)id: INTEGERactive: BOOLEANlast\_login: DATETIMElogin\_count: INTEGERfail\_login\_count: INTEGERcreated\_on: DATETIMEchanged\_on: DATETIMEcreated\_by\_fk: INTEGERchanged\_by\_fk: INTEGERfirst\_name: VARCHAR(64)last\_name: VARCHAR(64)username: VARCHAR(64)password: VARCHAR(256)email: VARCHAR(320)Role (ab\_role)id: INTEGERname: VARCHAR(64)ReportRecipients (report\_recipient)created\_on: DATETIMEchanged\_on: DATETIMEid: INTEGERrecipient\_config\_json: TEXTreport\_schedule\_id: INTEGERcreated\_by\_fk: INTEGERchanged\_by\_fk: INTEGERtype: VARCHAR(50)ReportSchedule (report\_schedule)created\_on: DATETIMEchanged\_on: DATETIMEextra\_json: TEXTid: INTEGERdescription: TEXTcontext\_markdown: TEXTactive: BOOLEANsql: TEXTchart\_id: INTEGERdashboard\_id: INTEGERdatabase\_id: INTEGERlast\_eval\_dttm: DATETIMElast\_value: FLOATlast\_value\_row\_json: TEXTvalidator\_config\_json: TEXTlog\_retention: INTEGERgrace\_period: INTEGERworking\_timeout: INTEGERforce\_screenshot: BOOLEANcustom\_width: INTEGERcustom\_height: INTEGERcreated\_by\_fk:



Documentation Source:
superset.apache.org/docs/using-superset/issue-codes/index.md

Documentation Title:
Issue Codes | Superset

Documentation Content:
Please make sure the query has a single statement and it's a SELECT statement.

Issue 1026​
-----------

Query is too complex and takes too long to run.The submitted query might be too complex to run under the time limit defined by your Superset administrator. Please double check your query and verify if it can be optimized. Alternatively, contact your administrator to increase the timeout period.

Issue 1027​
-----------

The database is currently running too many queries.The database might be under heavy load, running too many queries. Please try again later, or contact an administrator for further assistance.

Issue 1028​
-----------

One or more parameters specified in the query are malformed.The query contains one or more malformed template parameters. Please check your query and confirm that all template parameters are surround by double braces, for example, "{{ ds }}". Then, try running your query again.

Issue 1029​
-----------

The object does not exist in this database.Either the schema, column, or table do not exist in the database.

Issue 1030​
-----------

The query potentially has a syntax error.The query might have a syntax error. Please check and run again.

Issue 1031​
-----------

The results backend no longer has the data from the query.The results from the query might have been deleted from the results backend after some period. Please re-run your query.

Issue 1032​
-----------

The query associated with the results was deleted.The query associated with the stored results no longer exists. Please re-run your query.

Issue 1033​
-----------

The results stored in the backend were stored in a different format, and no longer can be deserialized.The query results were stored in a format that is no longer supported. Please re-run your query.

Issue 1034​
-----------

The database port provided is invalid.Please check that the provided database port is an integer between 0 and 65535 (inclusive).

Issue 1035​
-----------

Failed to start remote query on a worker.The query was not started by an asynchronous worker. Please reach out to your administrator for further assistance.

Issue 1036​
-----------

The database was deleted.The operation failed because the database referenced no longer exists. Please reach out to your administrator for further assistance.



Documentation Source:
superset.apache.org/docs/contributing/resources/index.md

Documentation Title:
Resources | Superset

Documentation Content:
(query)tracking\_url: TEXTextra\_json: TEXTid: INTEGERdatabase\_id: INTEGERuser\_id: INTEGERsql: TEXTselect\_sql: TEXTexecuted\_sql: TEXTlimit: INTEGERselect\_as\_cta: BOOLEANselect\_as\_cta\_used: BOOLEANprogress: INTEGERrows: INTEGERerror\_message: TEXTchanged\_on: DATETIMEclient\_id: VARCHAR(11)tmp\_table\_name: VARCHAR(256)tmp\_schema\_name: VARCHAR(256)status: VARCHAR(16)tab\_name: VARCHAR(256)sql\_editor\_id: VARCHAR(256)schema: VARCHAR(256)catalog: VARCHAR(256)limiting\_factor: VARCHAR(18)ctas\_method: VARCHAR(16)results\_key: VARCHAR(64)start\_time: NUMERIC(20, 6)start\_running\_time: NUMERIC(20, 6)end\_time: NUMERIC(20, 6)end\_result\_backend\_time: NUMERIC(20, 6)TabState (tab\_state)created\_on: DATETIMEchanged\_on: DATETIMEextra\_json: TEXTid: INTEGERuser\_id: INTEGERactive: BOOLEANdatabase\_id: INTEGERsql: TEXTquery\_limit: INTEGERlatest\_query\_id: INTEGERautorun: BOOLEANtemplate\_params: TEXThide\_left\_bar: BOOLEANsaved\_query\_id: INTEGERcreated\_by\_fk: INTEGERchanged\_by\_fk: INTEGERlabel: VARCHAR(256)schema: VARCHAR(256)catalog: VARCHAR(256)SavedQuery (saved\_query)created\_on: DATETIMEchanged\_on: DATETIMEextra\_json: TEXTid: INTEGERuser\_id: INTEGERdb\_id: INTEGERdescription: TEXTsql: TEXTtemplate\_parameters: TEXTrows: INTEGERlast\_run: DATETIMEcreated\_by\_fk: INTEGERchanged\_by\_fk: INTEGERuuid: BINARY(16)schema: VARCHAR(128)catalog: VARCHAR(256)label: VARCHAR(256)RowLevelSecurityFilter (row\_level\_security\_filters)created\_on: DATETIMEchanged\_on: DATETIMEid: INTEGERdescription: TEXTclause: TEXTcreated\_by\_fk: INTEGERchanged\_by\_fk: INTEGERname: VARCHAR(255)filter\_type:



Documentation Source:
superset.apache.org/docs/contributing/resources/index.md

Documentation Title:
Resources | Superset

Documentation Content:
VARCHAR(64)last\_name: VARCHAR(64)username: VARCHAR(64)password: VARCHAR(256)email: VARCHAR(320)Role (ab\_role)id: INTEGERname: VARCHAR(64)ReportRecipients (report\_recipient)created\_on: DATETIMEchanged\_on: DATETIMEid: INTEGERrecipient\_config\_json: TEXTreport\_schedule\_id: INTEGERcreated\_by\_fk: INTEGERchanged\_by\_fk: INTEGERtype: VARCHAR(50)ReportSchedule (report\_schedule)created\_on: DATETIMEchanged\_on: DATETIMEextra\_json: TEXTid: INTEGERdescription: TEXTcontext\_markdown: TEXTactive: BOOLEANsql: TEXTchart\_id: INTEGERdashboard\_id: INTEGERdatabase\_id: INTEGERlast\_eval\_dttm: DATETIMElast\_value: FLOATlast\_value\_row\_json: TEXTvalidator\_config\_json: TEXTlog\_retention: INTEGERgrace\_period: INTEGERworking\_timeout: INTEGERforce\_screenshot: BOOLEANcustom\_width: INTEGERcustom\_height: INTEGERcreated\_by\_fk: INTEGERchanged\_by\_fk: INTEGERtype: VARCHAR(50)name: VARCHAR(150)crontab: VARCHAR(1000)creation\_method: VARCHAR(255)timezone: VARCHAR(100)report\_format: VARCHAR(50)last\_state: VARCHAR(50)validator\_type: VARCHAR(100)ReportExecutionLog (report\_execution\_log)id: INTEGERscheduled\_dttm: DATETIMEstart\_dttm: DATETIMEend\_dttm: DATETIMEvalue: FLOATvalue\_row\_json: TEXTerror\_message: TEXTreport\_schedule\_id: INTEGERuuid: BINARY(16)state: VARCHAR(50)Apache Superset ERDSQL LabData AssetsCoreSystemInherited from Flask App Builder (FAB)Alerts & ReportsTableSchema (table\_schema)created\_on: DATETIMEchanged\_on: DATETIMEextra\_json: TEXTid: INTEGERtab\_state\_id: INTEGERdatabase\_id: INTEGERdescription: TEXTexpanded: BOOLEANcreated\_by\_fk: INTEGERchanged\_by\_fk: INTEGERschema: VARCHAR(256)catalog: VARCHAR(256)table: VARCHAR(256)Query (query)tracking\_url: TEXTextra\_json: TEXTid: INTEGERdatabase\_id:



