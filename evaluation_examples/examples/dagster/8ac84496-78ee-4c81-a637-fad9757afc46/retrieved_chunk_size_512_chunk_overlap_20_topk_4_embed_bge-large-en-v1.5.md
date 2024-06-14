Documentation Source:
release-1-7-2.dagster.dagster-docs.io/integrations/dagstermill/using-notebooks-with-dagster.md

Documentation Title:
Using Jupyter notebooks with Papermill and Dagster Tutorial

Documentation Content:
Step 5.3: Modify the notebook

We need to make a small change in our Jupyter notebook to allow Dagster to supply the `iris_dataset`asset as input. Behind the scenes, Dagster uses `papermill`to inject parameters into notebooks. `papermill`works by replacing a notebook cell with the `parameters`tag with a custom cell that can fetch the desired data.

To accomplish this, we need to tag the cell in the `iris-kmeans`notebook that fetches the Iris dataset. This allows us to replace the cell with the data-fetching logic that loads the `iris_dataset`asset and retain the ability to run the Jupyter notebook in a standalone context. We'll cover this in more detail later in the tutorial.

To add the `parameters`tag, you may need to turn on the display of cell tags in Jupyter:

1. In Jupyter, navigate to **View > Cell Toolbar > Tags**:

!
2. Click **Add Tag**to add a `parameters`tag:

!

Step 6: Materialize the assets#
-------------------------------

Next, we'll materialize our `iris_dataset`and notebook assets.

In the UI, open the **Asset Graph**page.

2. Click the **Reload definitions**button. This ensures that the UI picks up the changes you made in the previous steps.

At this point, the `iris_dataset`asset should display above the `iris_kmeans_jupyter`asset as an upstream dependency:

!
Click the **Materialize all**button near the top right corner of the page, which will launch a run to materialize the assets.


That's it! You now have working Jupyter and Dagster assets!

Extra credit: Fetch a Dagster asset in a Jupyter notebook#
----------------------------------------------------------

What if you want to do additional analysis of the Iris dataset and create a new notebook? How can you accomplish this without duplicating code or re-fetching data?

The answer is simple: use the `iris_dataset`Dagster asset!



Documentation Source:
release-1-7-2.dagster.dagster-docs.io/integrations/dagstermill/using-notebooks-with-dagster.md

Documentation Title:
Using Jupyter notebooks with Papermill and Dagster Tutorial

Documentation Content:
Step 5.2: Provide the iris\_dataset asset to the notebook asset

Next, we need to tell Dagster that the `iris_datset`asset is input data for the `iris-kmeans`notebook. To do this, add the `ins`parameter to the notebook asset:

`# tutorial_template/assets/__init__.pyfromdagstermill importdefine_dagstermill_asset
fromdagster importasset,file_relative_path,AssetIn
importpandas aspd



Documentation Source:
release-1-7-2.dagster.dagster-docs.io/integrations/dagstermill/using-notebooks-with-dagster.md

Documentation Title:
Using Jupyter notebooks with Papermill and Dagster Tutorial

Documentation Content:
The answer is simple: use the `iris_dataset`Dagster asset!

In the Jupyter notebook, import the Dagster `Definitions`object and use the `Definitions.load_asset_value`function to load the data for the `iris_dataset`asset we created in Step 5.1: Create the Iris dataset asset:

`fromtutorial_template importtemplate_tutorial

iris =template_tutorial.load_asset_value("iris_dataset")`Then, whenever you run the notebook using Jupyter, you'll be able to work with the `iris_dataset`asset:

`jupyter notebook /path/to/new/notebook.ipynb`Behind the scenes, when `load_asset_value`is called, Dagster fetches the value of `iris_dataset`that was most recently materialized and stored by an I/O manager.

To integrate the new notebook, follow the steps from Step 5.3to add the `parameters`tag to the cell that fetches the `iris_dataset`asset via `load_asset_value`.

Conclusion#
-----------

Now we have successfully created an asset from a Jupyter notebook and integrated it with our Dagster project! To learn about additional `dagstermill`features, refer to the Dagstermill integration reference.

On This Page- Using Jupyter notebooks with Papermill and Dagster
	Dagster conceptsPrerequisitesStep 1: Explore the Jupyter notebookStep 2: Create a Dagster asset from the Jupyter NotebookStep 3: Add a Dagster Definitions object and supply an I/O managerStep 4: Materialize the notebook asset7. Step 5: Add an upstream asset
		Step 5.1: Create the Iris dataset assetStep 5.2: Provide the iris\_dataset asset to the notebook assetStep 5.3: Modify the notebook
	Step 6: Materialize the assetsExtra credit: Fetch a Dagster asset in a Jupyter notebookConclusion
Edit Page on GitHubShare FeedbackStar



Documentation Source:
release-1-7-2.dagster.dagster-docs.io/integrations/dagstermill/using-notebooks-with-dagster.md

Documentation Title:
Using Jupyter notebooks with Papermill and Dagster Tutorial

Documentation Content:
When clicked, Dagster will render the notebook - referenced in the `notebook_path`parameter - that'll be executed when the `iris_kmeans_jupyter`asset is materialized:

!
Click the **Materialize**button. To view the execution as it happens, click the **View**button in the alert that displays.


After the run completes successfully, you can view the executed notebook in the UI. Click the asset again and locate the **View Notebook**button in the **Materialization in Last Run**section of the sidebar:

!Click the button to display the executed notebook - specifically, the notebook that was executed and written to a persistent location:

!Step 5: Add an upstream asset#
------------------------------

While our `iris-kmeans`notebook asset now materializes successfully, there are still some improvements we can make. The beginning of the notebook fetches the Iris dataset, which means that every time the notebook is materialized, the data is re-fetched.

To address this, we can factor the Iris dataset into its own asset. This will allow us to:

**Use the asset as input to additional notebooks.**This means all notebooks analyzing the Iris dataset will use the same source data, which we only have to fetch once.

**Materialize notebooks without fetching data for each materialization.**Instead of making potentially expensive API calls, Dagster can fetch the data from the previous materialization of the Iris dataset and provide that data as input to the notebook.


In this step, you'll:

Create the Iris dataset assetProvide the Iris dataset as input to the notebookModify the notebook



