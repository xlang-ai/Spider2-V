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
**jobs**(*Optional**[**Sequence**[**Union**[**GraphDefinition**,* *JobDefinition**,* *UnresolvedAssetJobDefinition**]**]**]*) – (experimental) A list of jobs to be executed when the sensor fires.

**default\_status**(*DefaultSensorStatus*) – Whether the sensor starts as running or not. The default
status can be overridden from the Dagster UI or via the GraphQL API.

**asset\_selection**(*Optional**[**Union**[**str**,* *Sequence**[**str**]**,* *Sequence**[**AssetKey**]**,* *Sequence**[**Union**[**AssetsDefinition**,* *SourceAsset**]**]**,* *AssetSelection**]**]*) – (Experimental) an asset selection to launch a run for if the sensor condition is met.
This can be provided instead of specifying a job.

classdagster.SensorDefinition(*name=None*, \*, *evaluation\_fn=None*, *job\_name=None*, *minimum\_interval\_seconds=None*, *description=None*, *job=None*, *jobs=None*, *default\_status=DefaultSensorStatus.STOPPED*, *asset\_selection=None*, *required\_resource\_keys=None*)[source]¶Define a sensor that initiates a set of runs based on some external state.

Parameters:* **evaluation\_fn**(*Callable**[**[**SensorEvaluationContext**]**]*) – 

The core evaluation function for the
sensor, which is run at an interval to determine whether a run should be launched or
not. Takes a SensorEvaluationContext.

This function must return a generator, which must yield either a single SkipReason
or one or more RunRequest objects.
**name**(*Optional**[**str**]*) – The name of the sensor to create. Defaults to name of evaluation\_fn

**minimum\_interval\_seconds**(*Optional**[**int**]*) – The minimum number of seconds that will elapse
between sensor evaluations.

**description**(*Optional**[**str**]*) – A human-readable description of the sensor.

**job**(*Optional**[**GraphDefinition**,* *JobDefinition**,* *UnresolvedAssetJob**]*) – The job to execute when this sensor fires.



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
release-1-7-2.dagster.dagster-docs.io/_apidocs/schedules-sensors.md

Documentation Title:
Dagster Docs

Documentation Content:
Takes a SensorEvaluationContextand an EventLogEntry corresponding to an
AssetMaterialization event.

Parameters:**asset\_key**(*AssetKey*) – The asset\_key this sensor monitors.

**name**(*Optional**[**str**]*) – The name of the sensor. Defaults to the name of the decorated
function.

**minimum\_interval\_seconds**(*Optional**[**int**]*) – The minimum number of seconds that will elapse
between sensor evaluations.

**description**(*Optional**[**str**]*) – A human-readable description of the sensor.

**job**(*Optional**[**Union**[**GraphDefinition**,* *JobDefinition**,* *UnresolvedAssetJobDefinition**]**]*) – The
job to be executed when the sensor fires.

**jobs**(*Optional**[**Sequence**[**Union**[**GraphDefinition**,* *JobDefinition**,* *UnresolvedAssetJobDefinition**]**]**]*) – (experimental) A list of jobs to be executed when the sensor fires.

**default\_status**(*DefaultSensorStatus*) – Whether the sensor starts as running or not. The default
status can be overridden from the Dagster UI or via the GraphQL API.

Example


```
fromdagsterimportAssetKey,EventLogEntry,SensorEvaluationContext,asset_sensor@asset_sensor(asset_key=AssetKey("my_table"),job=my_job)defmy_asset_sensor(context:SensorEvaluationContext,asset_event:EventLogEntry):returnRunRequest(run_key=context.cursor,run_config={"ops":{"read_materialization":{"config":{"asset_key":asset_event.dagster_event.asset_key.path,}}}},)
```
classdagster.AssetSensorDefinition(name, asset\_key, job\_name, asset\_materialization\_fn, *minimum\_interval\_seconds=None*, *description=None*, *job=None*, *jobs=None*, *default\_status=DefaultSensorStatus.STOPPED*, *required\_resource\_keys=None*)[source]¶Define an asset sensor that initiates a set of runs based on the materialization of a given
asset.

If the asset has been materialized multiple times between since the last sensor tick, the
evaluation function will only be invoked once, with the latest materialization.

Parameters:**name**(*str*) – The name of the sensor to create.



