Documentation Source:
release-1-7-2.dagster.dagster-docs.io/concepts/partitions-schedules-sensors/sensors.md

Documentation Title:
Sensors | Dagster Docs

Documentation Content:
@sensor(job=log_file_job)defmy_directory_sensor():forfilename inos.listdir(MY_DIRECTORY):filepath =os.path.join(MY_DIRECTORY,filename)ifos.path.isfile(filepath):yieldRunRequest(run_key=filename,run_config=RunConfig(ops={"process_file":FileConfig(filename=filename)}),)`This sensor iterates through all the files in `MY_DIRECTORY`and yields a `RunRequest`for each file. Note that despite the `yield`syntax, the function will run to completion before any runs are submitted.

To write a sensor that materializes assets, you can build a job that materializes assets:

`asset_job =define_asset_job("asset_job","*")@sensor(job=asset_job)defmaterializes_asset_sensor():yieldRunRequest(...)`Once a sensor is added to a `Definitions`object with the job it yields a `RunRequest`for, it can be started and will start creating runs. You can start or stop sensors in the Dagster UI, or by setting the default status to `DefaultSensorStatus.RUNNING`in code:

`@sensor(job=asset_job,default_status=DefaultSensorStatus.RUNNING)defmy_running_sensor():...`If you manually start or stop a sensor in the UI, that will override any default status that is set in code.

Once your sensor is started, if you're running a Dagster daemonas part of your deployment, the sensor will begin executing immediately without needing to restart the dagster-daemon process.

Idempotence and cursors#
------------------------

When instigating runs based on external events, you usually want to run exactly one job run for each event. There are two ways to define your sensors to avoid creating duplicate runs for your events:

Using a `run_key`Using cursors



Documentation Source:
release-1-7-2.dagster.dagster-docs.io/concepts/partitions-schedules-sensors/sensors.md

Documentation Title:
Sensors | Dagster Docs

Documentation Content:
For example, here is our directory sensor that now provides a `SkipReason`when no files are encountered:

`@sensor(job=log_file_job)defmy_directory_sensor_with_skip_reasons():has_files =Falseforfilename inos.listdir(MY_DIRECTORY):filepath =os.path.join(MY_DIRECTORY,filename)ifos.path.isfile(filepath):yieldRunRequest(run_key=filename,run_config={"ops":{"process_file":{"config":{"filename":filename}}}},)has_files =Trueifnothas_files:yieldSkipReason(f"No files found in {MY_DIRECTORY}.")`Using resources in sensors#
---------------------------

Dagster's resourcessystem can be used with sensors to make it easier to call out to external systems and to make components of a sensor easier to plug in for testing purposes.

To specify resource dependencies, annotate the resource as a parameter to the sensor's function. Resources are provided by attaching them to your `Definitions`call.

Here, a resource is provided which provides access to an external API. The same resource could be used in the job that the sensor triggers.

`fromdagster import(sensor,RunRequest,SensorEvaluationContext,ConfigurableResource,job,Definitions,RunConfig,)importrequests
fromtyping importList

classUsersAPI(ConfigurableResource):url:strdeffetch_users(self)->List[str]:returnrequests.get(self.url).json()@jobdefprocess_user():...@sensor(job=process_user)defprocess_new_users_sensor(context:SensorEvaluationContext,users_api:UsersAPI,):last_user =int(context.cursor)ifcontext.cursor else0users =users_api.fetch_users()num_users =len(users)foruser_id inusers[last_user:]:yieldRunRequest(run_key=user_id,tags={"user_id":user_id},)context.update_cursor(str(num_users))defs =Definitions(jobs=[process_user],sensors=[process_new_users_sensor],resources={"users_api":UsersAPI(url="https://my-api.com/users")},)`For more information on resources, refer to the Resources documentation. To see how to test schedules with resources, refer to the section on Testing sensors with resources.

Logging in sensors#
-------------------

Sensor logs are stored in yourDagster instance's compute log storage.



Documentation Source:
release-1-7-2.dagster.dagster-docs.io/concepts/partitions-schedules-sensors/sensors.md

Documentation Title:
Sensors | Dagster Docs

Documentation Content:
You should ensure that your compute log storage is configured to view your sensor logs.Any sensor can emit log messages during its evaluation function:

`@sensor(job=the_job)deflogs_then_skips(context):context.log.info("Logging from a sensor!")returnSkipReason("Nothing to do")`These logs can be viewed when inspecting a tick in the tick history view on the corresponding sensor page.

Testing sensors#
----------------

Via the Dagster UIVia the CLIVia Python### Via the Dagster UI#

**Before you test**: Test evaluations of sensors run the sensor's underlying Python function, meaning that any side effects contained within that sensor's function may be executed.In the UI, you can manually trigger a test evaluation of a sensor and view the results.

Click **Overview > Sensors**.

Click the sensor you want to test.

3. Click the **Test Sensor**button, located near the top right corner of the page.

!
4. You'll be prompted to provide a cursor value. You can use the existing cursor for the sensor (which will be prepopulated) or enter a different value. If you're not using cursors, leave this field blank.

!
5. Click **Evaluate**to fire the sensor. A window containing the result of the evaluation will display, whether it's run requests, a skip reason, or a Python error:

!If the run was successful, then for each produced run request, you can open the launchpad pre-scaffolded with the config produced by that run request. You'll also see a new computed cursor value from the evaluation, with the option to persist the value.
Monitoring sensors in the Dagster UI#
-------------------------------------

Using the UI, you can monitor and operate sensors. The UI provides multiple views that help with observing sensor evaluations, skip reasons, and errors.

To view all sensors, navigate to **Overview > Sensors**. Here, you can start and stop sensors, and view their frequency, last tick, and last run:

!Click on any sensor to test the sensor, monitor all sensor evaluations on a timeline, and view a table of runs launched by the sensor.



Documentation Source:
release-1-7-2.dagster.dagster-docs.io/_apidocs/schedules-sensors.md

Documentation Title:
Dagster Docs

Documentation Content:
```
instance=DagsterInstance.ephemeral()result=my_job.execute_in_process(instance=instance)dagster_run=result.dagster_rundagster_event=result.get_job_success_event()# or get_job_failure_event()context=build_run_status_sensor_context(sensor_name="run_status_sensor_to_invoke",dagster_instance=instance,dagster_run=dagster_run,dagster_event=dagster_event,)run_status_sensor_to_invoke(context)
```
@dagster.run\_status\_sensor(run\_status, *name=None*, *minimum\_interval\_seconds=None*, *description=None*, *monitored\_jobs=None*, *job\_selection=None*, *monitor\_all\_code\_locations=None*, *default\_status=DefaultSensorStatus.STOPPED*, *request\_job=None*, *request\_jobs=None*, *monitor\_all\_repositories=None*)[source]¶Creates a sensor that reacts to a given status of job execution, where the decorated
function will be run when a job is at the given status.

Takes a RunStatusSensorContext.

Parameters:**run\_status**(*DagsterRunStatus*) – The status of run execution which will be
monitored by the sensor.

**name**(*Optional**[**str**]*) – The name of the sensor. Defaults to the name of the decorated function.

**minimum\_interval\_seconds**(*Optional**[**int**]*) – The minimum number of seconds that will elapse
between sensor evaluations.

**description**(*Optional**[**str**]*) – A human-readable description of the sensor.

**monitored\_jobs**(*Optional**[**List**[**Union**[**JobDefinition**,* *GraphDefinition**,* *UnresolvedAssetJobDefinition**,* *RepositorySelector**,* *JobSelector**,* *CodeLocationSelector**]**]**]*) – Jobs in the current code locations that will be monitored by this sensor. Defaults to None, which means the alert will
be sent when any job in the code location matches the requested run\_status. Jobs in external repositories can be monitored by using
RepositorySelector or JobSelector.

**monitor\_all\_code\_locations**(*Optional**[**bool**]*) – If set to True, the sensor will monitor all runs in the Dagster instance.



