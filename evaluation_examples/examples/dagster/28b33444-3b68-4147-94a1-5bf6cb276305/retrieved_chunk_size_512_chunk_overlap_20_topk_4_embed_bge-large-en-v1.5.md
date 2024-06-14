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
release-1-7-2.dagster.dagster-docs.io/concepts/partitions-schedules-sensors/sensors.md

Documentation Title:
Sensors | Dagster Docs

Documentation Content:
Cross-code location run status sensors

Sometimes, you may want to monitor jobs in a code location other than the one where the sensor is defined. You can use special identifiers `CodeLocationSelector`and `JobSelector`to tell a run status sensor to monitor jobs in another code location:

`@run_status_sensor(monitored_jobs=[CodeLocationSelector(location_name="defs")],run_status=DagsterRunStatus.SUCCESS,)defcode_location_a_sensor():# when any job in code_location_a succeeds, this sensor will triggersend_slack_alert()@run_failure_sensor(monitored_jobs=[JobSelector(location_name="defs",repository_name="code_location_a",job_name="data_update",)],)defcode_location_a_data_update_failure_sensor():# when the data_update job in code_location_a fails, this sensor will triggersend_slack_alert()`You can also monitor every job in your Dagster instance by specifying `monitor_all_code_locations=True`on the sensor decorator. Note that `monitor_all_code_locations`cannot be used along with jobs specified via `monitored_jobs`.

`@run_status_sensor(monitor_all_code_locations=True,run_status=DagsterRunStatus.SUCCESS,)defsensor_monitor_all_code_locations():# when any job in the Dagster instance succeeds, this sensor will triggersend_slack_alert()`Testing run status sensors#
---------------------------

As with other sensors, you can directly invoke run status sensors. However, the `context`provided via `run_status_sensor`and `run_failure_sensor`contain objects that are typically only available during run time. Below you'll find code snippets that demonstrate how to build the context so that you can directly invoke your function in unit tests.

If you had written a status sensor like this (assuming you implemented the function `email_alert`elsewhere):

`@run_status_sensor(run_status=DagsterRunStatus.SUCCESS)defmy_email_sensor(context:RunStatusSensorContext):message =f'Job "{context.dagster_run.job_name}" succeeded.'email_alert(message)`We can first write a simple job that will succeed:

`@opdefsucceeds():return1@jobdefmy_job_succeeds():succeeds()`Then we can execute this job and pull the attributes we need to build the `context`.



