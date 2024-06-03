Documentation Source:
docs.astronomer.io/learn/use-case-airflow-mlflow.md

Documentation Title:
Predict possum tail length using MLflow, Airflow, and linear regression | Astronomer Documentation

Documentation Content:
Project overview​

This project consists of three DAGs which have dependency relationships through Airflow datasets.

!The `feature_eng`DAG prepares the MLflow experiment and builds prediction features from the possum data.

!The `train`DAG trains a RidgeCV model on the engineered features from `feature_eng`and then registers the model with MLflow using operators from the MLflow Airflow provider.

!The `predict`DAG uses the trained model from `train`to create predictions and plot them against the target values.

!Note that the model is trained on the whole dataset and predictions are made on the same data. In a real world scenario you'd want to split the data into a training, validation, and test set.



Documentation Source:
docs.astronomer.io/learn/use-case-airflow-mlflow.md

Documentation Title:
Predict possum tail length using MLflow, Airflow, and linear regression | Astronomer Documentation

Documentation Content:
`@aql.dataframe()defbuild_features(raw_df:DataFrame,experiment_id:str,target_column:str,categorical_columns:list,numeric_columns:list,)->DataFrame:# ...scaler =StandardScaler()withmlflow.start_run(experiment_id=experiment_id,run_name="Scaler")asrun:X_encoded =pd.DataFrame(scaler.fit_transform(X_encoded),columns=X_encoded.columns)mlflow.sklearn.log_model(scaler,artifact_path="scaler")mlflow.log_metrics(pd.DataFrame(scaler.mean_,index=X_encoded.columns)[0].to_dict())# ...returnX_encoded # return a pandas DataFrame`You can view the Scaler run in the MLflow UI at `localhost:5000`.

!#### Model training DAG​

Airflow datasetslet you schedule DAGs based on when a specific file or database is updated in a separate DAG. In this example, the model training DAG is scheduled to run as soon as the last task in the feature engineering DAG completes.

`@dag(schedule=[Dataset("s3://"+DATA_BUCKET_NAME +"_"+FILE_PATH)],start_date=datetime(2023,1,1),catchup=False,)`The `fetch_feature_df`task pulls the feature dataframe that was pushed to XComin the previous DAG.

`@taskdeffetch_feature_df(**context):"Fetch the feature dataframe from the feature engineering DAG."feature_df =context["ti"].xcom_pull(dag_id="feature_eng",task_ids="build_features",include_prior_dates=True)returnfeature_df`The ID number of the MLflow experiment is retrieved using the MLflowClientHook in the `fetch_experiment_id`task in order to track model training in the same experiment.

The `train_model`task, defined with the `@aql.dataframe`decorator, shows how model training can be parameterized when using Airflow. In this example, the hyperparameters, the `target_colum`, and the model class are hardcoded, but they could also be retrieved from upstream tasks via XComor passed into manual runs of the DAG using DAG params.

The project is set up to train the scikit-learn RidgeCV modelto predict the tail length of possums using information such as their age, total length, or skull width.



Documentation Source:
docs.astronomer.io/learn/use-case-airflow-mlflow.md

Documentation Title:
Predict possum tail length using MLflow, Airflow, and linear regression | Astronomer Documentation

Documentation Content:
Feature engineering DAG​

The feature engineering DAG starts with a task that creates the necessary object storage buckets in the resource provided as `AWS_CONN_ID`using the S3CreateBucketOperator. By default, the project uses a local MinIO instance, which is created when starting the Astro project. If you want to use remote object storage, you can change the `AWS_CONN_ID`in the `.env`file and provide your AWS credentials credentials.
The operator is dynamically mappedover a list of bucket names to create all buckets in parallel.

`create_buckets_if_not_exists =S3CreateBucketOperator.partial(task_id="create_buckets_if_not_exists",aws_conn_id=AWS_CONN_ID,).expand(bucket_name=[DATA_BUCKET_NAME,MLFLOW_ARTIFACT_BUCKET,XCOM_BUCKET])`The `prepare_mlflow_experiment`task groupcontains a pattern that lists all existing experiments in the MLflow instance connected via the `MLFLOW_CONN_ID`. It also creates a new experiment with a specified name if it does not exist yet using the @task.branch decorator. The MLflowClientHookcontains the `run`method that creates the new experiment by making a call to the MLflow API.

`@taskdefcreate_experiment(experiment_name,artifact_bucket):"""Create a new MLFlow experiment with a specified name.Save artifacts to the specified S3 bucket."""mlflow_hook =MLflowClientHook(mlflow_conn_id=MLFLOW_CONN_ID)new_experiment_information =mlflow_hook.run(endpoint="api/2.0/mlflow/experiments/create",request_params={"name":experiment_name,"artifact_location":f"s3://{artifact_bucket}/",},).json()returnnew_experiment_information`The `build_features`task completes feature engineering using Pandasto one-hot encode categorical features and scikit-learnto scale numeric features.

The mlflowpackage is used to trackthe scaler run in MLflow.

The task is defined using the `@aql.dataframe`decorator from the Astro Python SDK.



Documentation Source:
docs.astronomer.io/learn/use-case-airflow-mlflow.md

Documentation Title:
Predict possum tail length using MLflow, Airflow, and linear regression | Astronomer Documentation

Documentation Content:
!#### Prediction DAG​

After retrieving the feature dataframe, the target column, and the `model_run_id`from XCom, the `run_prediction`task uses the ModelLoadAndPredictOperatorto run a prediction on the whole dataset using the latest version of the registered RidgeCV model.

`run_prediction =ModelLoadAndPredictOperator(mlflow_conn_id="mlflow_default",task_id="run_prediction",model_uri=f"s3://{MLFLOW_ARTIFACT_BUCKET}/"+"{{ ti.xcom_pull(task_ids='fetch_model_run_id')}}"+"/artifacts/model",data=fetched_feature_df,)`The predicted possum tail length values are converted to a dataframe and then plotted against the true tail lengths using matplotlib. The resulting graph offers a visual representation of how much variation of possum tail length can be explained by a linear regression model using the features in the dataset in this specific possum population of 104 animals.

Congratulations! You ran a ML pipeline tracking model parameters and versions in MLflow using the MLflow Airflow provider. You can now use this pipeline as a template for your own MLflow projects.

See also​
---------

* Documentation: MLflow.
* Tutorial: Use MLflow with Apache Airflow.
* Provider: MLflow Airflow provider.
Was this page helpful?
----------------------

YesNoSign up for Developer Updates
-----------------------------

Get a summary of new Astro features once a month.

SubmitYou can unsubscribe at any time. By proceeding you agree to our Privacy Policy, our Website Termsand to receive emails from Astronomer.

Edit this pagePreviousML orchestration with Airflow datasetsNextAirflow glossaryBefore you startClone the projectRun the project* Project contents
	Data sourceProject overviewProject code
See alsoLegal·Privacy·Security·Cookie Preferences!!© Astronomer 2023. Various trademarks held by their respective owners.



