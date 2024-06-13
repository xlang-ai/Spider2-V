Documentation Source:
superset.apache.org/docs/contributing/resources/index.md

Documentation Title:
Resources | Superset

Documentation Content:
DATETIMEextra\_json: TEXTid: INTEGERdatabase\_id: INTEGERis\_physical: BOOLEANis\_managed\_externally: BOOLEANname: TEXTexpression: TEXTexternal\_url: TEXTcreated\_by\_fk: INTEGERchanged\_by\_fk: INTEGERuuid: BINARY(16)TableColumn (table\_columns)created\_on: DATETIMEchanged\_on: DATETIMEid: INTEGERis\_active: BOOLEANtype: TEXTgroupby: BOOLEANfilterable: BOOLEANdescription: TEXTtable\_id: INTEGERis\_dttm: BOOLEANexpression: TEXTextra: TEXTcreated\_by\_fk: INTEGERchanged\_by\_fk: INTEGERuuid: BINARY(16)column\_name: VARCHAR(255)verbose\_name: VARCHAR(1024)advanced\_data\_type: VARCHAR(255)python\_date\_format: VARCHAR(255)DatabaseUserOAuth2Tokens (database\_user\_oauth2\_tokens)created\_on: DATETIMEchanged\_on: DATETIMEid: INTEGERuser\_id: INTEGERdatabase\_id: INTEGERaccess\_token: BLOBaccess\_token\_expiration: DATETIMErefresh\_token: BLOBcreated\_by\_fk: INTEGERchanged\_by\_fk: INTEGERDynamicPlugin (dynamic\_plugin)created\_on: DATETIMEchanged\_on: DATETIMEid: INTEGERname: TEXTkey: TEXTbundle\_url: TEXTcreated\_by\_fk: INTEGERchanged\_by\_fk: INTEGERTag (tag)created\_on: DATETIMEchanged\_on: DATETIMEid: INTEGERdescription: TEXTcreated\_by\_fk: INTEGERchanged\_by\_fk: INTEGERname: VARCHAR(250)type: VARCHAR(12)AnnotationLayer (annotation\_layer)created\_on: DATETIMEchanged\_on: DATETIMEid: INTEGERdescr: TEXTcreated\_by\_fk: INTEGERchanged\_by\_fk: INTEGERname: VARCHAR(250)UserAttribute (user\_attribute)created\_on: DATETIMEchanged\_on: DATETIMEid: INTEGERuser\_id: INTEGERwelcome\_dashboard\_id: INTEGERcreated\_by\_fk: INTEGERchanged\_by\_fk: INTEGERavatar\_url: VARCHAR(100)Dashboard (dashboards)created\_on: DATETIMEchanged\_on: DATETIMEid: INTEGERposition\_json: TEXTdescription: TEXTcss: TEXTcertified\_by:



Documentation Source:
superset.apache.org/docs/contributing/resources/index.md

Documentation Title:
Resources | Superset

Documentation Content:
DATETIMEchanged\_on: DATETIMEid: INTEGERpassword: BLOBcache\_timeout: INTEGERselect\_as\_create\_table\_as: BOOLEANexpose\_in\_sqllab: BOOLEANallow\_run\_async: BOOLEANallow\_file\_upload: BOOLEANallow\_ctas: BOOLEANallow\_cvas: BOOLEANallow\_dml: BOOLEANextra: TEXTencrypted\_extra: BLOBimpersonate\_user: BOOLEANserver\_cert: BLOBis\_managed\_externally: BOOLEANexternal\_url: TEXTcreated\_by\_fk: INTEGERchanged\_by\_fk: INTEGERuuid: BINARY(16)verbose\_name: VARCHAR(250)database\_name: VARCHAR(250)sqlalchemy\_uri: VARCHAR(1024)configuration\_method: VARCHAR(255)force\_ctas\_schema: VARCHAR(250)Table (sl\_tables)created\_on: DATETIMEchanged\_on: DATETIMEextra\_json: TEXTid: INTEGERdatabase\_id: INTEGERcatalog: TEXTschema: TEXTname: TEXTis\_managed\_externally: BOOLEANexternal\_url: TEXTcreated\_by\_fk: INTEGERchanged\_by\_fk: INTEGERuuid: BINARY(16)Dataset (sl\_datasets)created\_on: DATETIMEchanged\_on: DATETIMEextra\_json: TEXTid: INTEGERdatabase\_id: INTEGERis\_physical: BOOLEANis\_managed\_externally: BOOLEANname: TEXTexpression: TEXTexternal\_url: TEXTcreated\_by\_fk: INTEGERchanged\_by\_fk: INTEGERuuid: BINARY(16)TableColumn (table\_columns)created\_on: DATETIMEchanged\_on: DATETIMEid: INTEGERis\_active: BOOLEANtype: TEXTgroupby: BOOLEANfilterable: BOOLEANdescription: TEXTtable\_id: INTEGERis\_dttm: BOOLEANexpression: TEXTextra: TEXTcreated\_by\_fk: INTEGERchanged\_by\_fk: INTEGERuuid: BINARY(16)column\_name: VARCHAR(255)verbose\_name: VARCHAR(1024)advanced\_data\_type: VARCHAR(255)python\_date\_format: VARCHAR(255)DatabaseUserOAuth2Tokens (database\_user\_oauth2\_tokens)created\_on: DATETIMEchanged\_on: DATETIMEid: INTEGERuser\_id: INTEGERdatabase\_id: INTEGERaccess\_token:



Documentation Source:
superset.apache.org/docs/using-superset/creating-your-first-dashboard/index.md

Documentation Title:
Creating Your First Dashboard | Superset

Documentation Content:
Registering a new table​

Now that you’ve configured a data source, you can select specific tables (called **Datasets**in Superset)
that you want exposed in Superset for querying.

Navigate to **Data ‣ Datasets**and select the **+ Dataset**button in the top right corner.

!A modal window should pop up in front of you. Select your **Database**,
**Schema**, and **Table**using the drop downs that appear. In the following example,
we register the **cleaned\_sales\_data**table from the **examples**database.

!To finish, click the **Add**button in the bottom right corner. You should now see your dataset in the list of datasets.



Documentation Source:
superset.apache.org/docs/configuration/sql-templating/index.md

Documentation Title:
SQL Templating | Superset

Documentation Content:
By default, the following variables are
made available in the Jinja context:

* `columns`: columns which to group by in the query
* `filter`: filters applied in the query
* `from_dttm`: start `datetime`value from the selected time range (`None`if undefined)
* `to_dttm`: end `datetime`value from the selected time range (`None`if undefined)
* `groupby`: columns which to group by in the query (deprecated)
* `metrics`: aggregate expressions in the query
* `row_limit`: row limit of the query
* `row_offset`: row offset of the query
* `table_columns`: columns available in the dataset
* `time_column`: temporal column of the query (`None`if undefined)
* `time_grain`: selected time grain (`None`if undefined)

For example, to add a time range to a virtual dataset, you can write the following:

`SELECT*FROMtblWHEREdttm_col >'{{ from_dttm }}'anddttm_col <'{{ to_dttm }}'`You can also use Jinja's logicto make your query robust to clearing the timerange filter:

`SELECT*FROMtblWHERE({%iffrom_dttm isnotnone %}dttm_col >'{{ from_dttm }}'AND{%endif %}{%ifto_dttm isnotnone %}dttm_col <'{{ to_dttm }}'AND{%endif %}true)`Note how the Jinja parameters are called within double brackets in the query, and without in the
logic blocks.

To add custom functionality to the Jinja context, you need to overload the default Jinja
context in your environment by defining the `JINJA_CONTEXT_ADDONS`in your superset configuration
(`superset_config.py`). Objects referenced in this dictionary are made available for users to use
where the Jinja context is made available.

`JINJA_CONTEXT_ADDONS ={'my_crazy_macro':lambdax:x*2,}`Default values for jinja templates can be specified via `Parameters`menu in the SQL Lab user interface.



