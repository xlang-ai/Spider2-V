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



Documentation Source:
docs.astronomer.io/learn/use-case-airflow-mlflow.md

Documentation Title:
Predict possum tail length using MLflow, Airflow, and linear regression | Astronomer Documentation

Documentation Content:
Skip to main content!!**Docs**DocsFind what you're looking forLearn About AstronomerGet Started FreeHomeAstroAstro CLISoftwareLearnTry AstroOverviewGet startedAirflow conceptsAirflow tutorialsIntegrations & connections* Use cases
	Data quality checks with setup/ teardown tasksELT with Airflow + DatabricksELT with Airflow + dbtFinancial ELT and ML pipelineLLMOps RAG with Airflow + WeaviateLLMOps with Cohere + OpenSearchML orchestration with Airflow datasetsRegression with Airflow + MLflow
Airflow glossarySupport Knowledge BaseOffice HoursWebinarsAstro StatusUse casesRegression with Airflow + MLflow
On this pagePredict possum tail length using MLflow, Airflow, and linear regression
=======================================================================

MLflowis a popular tool for tracking and managing machine learning models. When combined, Airflow and MLflow make a powerful platform for ML orchestration (MLOx).

This use case shows how to use MLflow with Airflow to engineer machine learning features, train a scikit-learn Ridge linear regression model, and create predictions based on the trained model.

infoFor more detailed instructions on using MLflow with Airflow, see the MLflow tutorial.

!Before you start​
-----------------

Before trying this example, make sure you have:

* The Astro CLI.
* Docker Desktop.

Clone the project​
------------------

Clone the example project from the Astronomer GitHub. To keep your credentials secure when you deploy this project to your own git repository, make sure to create a file called `.env`with the contents of the `.env_example`file in the project root directory.

The repository is configured to spin up and use local MLflow and MinIO instances without you needing to define connections or access external tools.

Run the project​
----------------

To run the example project, first make sure Docker Desktop is running. Then, open your project directory and run:

astro dev startThis command builds your project and spins up 6 Docker containers on your machine to run it:

* The Airflow webserver, which runs the Airflow UI and can be accessed at `https://localhost:8080/`.
* The Airflow scheduler, which is responsible for monitoring and triggering tasks.



