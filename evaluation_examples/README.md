# Evaluation examples
In this file, we will briefly introduce the usage of each sub-folder:
1. document warehouse: `documents/`
2. task format of examples: `examples/`
3. real accounts: `settings/`

## Document Warehouse
To support retrieval augmented generation framework, we crawl and pre-process HTML from official documentation of various applications. For detailed information, see [Documents](../evaluation_examples/documents/README.md).

## Task Format
Here we introduce the format of task examples. Take the BigQuery task `bigquery/3363a913-d3e9-42c2-9d76-9cd9e9bafec7` as an example, the `.json` configuration file is:
```json
{
    "id": "3363a913-d3e9-42c2-9d76-9cd9e9bafec7",
    "snapshot": "bigquery",
    "instruction": "I want to know how many austin bike stations are active? Save the query results into '/home/user/Downloads/answer.csv'.",
    "source": [
        "https://cloud.google.com/bigquery/docs/quickstarts/query-public-dataset-console"
    ],
    "action_number": 9,
    "config": [
        {
            "type": "bigquery_init",
            "parameters": {
                "config_file": "evaluation_examples/settings/google/gcp_config.json",
                "project_name": "bigquery-project",
                "actions": [
                    {
                        "type": "empty"
                    }
                ]
            }
        },
        {
            "type": "google_chrome_browser",
            "parameters": {
                "debugging_port": 1337,
                "listening_port": 9222,
                "urls": [
                    "https://www.bing.com/"
                ]
            }
        },
        {
            "type": "bigquery_login",
            "parameters": {
                "settings_file": "evaluation_examples/settings/google/settings.json",
                "config_file": "evaluation_examples/settings/google/gcp_config.json",
                "project_name": "bigquery-project"
            }
        }
    ],
    "related_apps": [
        "bigquery",
        "chromium"
    ],
    "tags": [
        "cli+gui",
        "account",
        "data_warehousing",
        "abstract"
    ],
    "evaluator": {
        "func": "compare_csv",
        "result": {
            "type": "vm_file",
            "path": "/home/user/Downloads/answer.csv",
            "dest": "pred.csv"
        },
        "expected": {
            "type": "local_file",
            "path": "evaluation_examples/examples/bigquery/3363a913-d3e9-42c2-9d76-9cd9e9bafec7/answer.csv",
            "dest": "gold_output.csv"
        },
        "options": {}
    },
    "counterpart": "a954c45e-fb59-4231-a052-a7f74dc16bf1"
}
```
- `id`: the globally unique uuid of the current example
- `snapshot`: it indicates the focused professional application
- `instruction`: the task instruction, user intent, or task goal
- `source`: the list of URLs based on which we construct the current example
- `action_number`: under the folder of each task example, we also provide a special file `verbose_instruction.txt`, which indicates how to complete the current task step-by-step. This field is exactly the number of actions based on `verbose_instruction.txt`
- `related_apps`: the list of professional applications used in the current example. The complete set includes $21$ applications:
    - `{'airflow', 'dagster', 'snowflake', 'duckdb', 'bigquery', 'jupyter', 'dbt', 'mysql', 'servicenow', 'terminal', 'metabase', 'airbyte', 'docker', 'hasura_cloud', 'sqlite3', 'vscode', 'chromium', 'postgresql', 'superset', 'dbt_cloud', 'excel'}`
- `tags`: different categories to label the current example
    - `verbose`/`abstract`: whether the `instruction` field offers a detailed step-by-step solution
    - `cli`/`gui`/`cli+gui`: whether a command line interface (cli) or a graphical user interface (gui) is necessary to finish the current task
    - `account`: whether a real account is needed to finish the current task
    - data pipeline chosen from $7$ categories: `['data_ingestion_and_integration', 'data_warehousing', 'data_orchestration', 'data_analysis_and_visualization', 'traditional_data_processing', 'it_service_management', 'data_transformation']`
- `counterpart`: if the current example uses an abstract instruction, this filed indicates the uuid of its counterpart (that is, the same task with a verbose instruction or step-by-step tutorial), or vice versa
- `config`: a list of functions to initialize or reset the environment in the virtual machine. Each function is represented by a JSON dict, where the `type` field indicates the function name and the `parameters` field indicates the parameters of the function. For example, in this example, it sequentially invokes:
    1. [`bigquery_init_setup`](../desktop_env/configs/bigquery.py) function: clear the cloud workspace of GCP `bigquery-project`
    2. [`google_chrome_browser_setup`](../desktop_env/configs/general.py) function: launch the Google Chrome application
    3. [`bigquery_login_setup`](../desktop_env/configs/bigquery.py) function: utilize playwright to automatically sign in the provided Google account in `settings/google/settings.json`
- `evaluator`: this filed defines how to evaluate the final outcome. Concretely, 
    - `func` defines the metric function used to compare the predicted and golden results. In this example, function [`compare_csv`](../desktop_env/evaluators/metrics/table.py) is utilized
    - `result` defines how to get the predicted result from the final states of the VM. In this example, we invoke the function [`get_vm_file`](../desktop_env/evaluators/getters/file.py) to copy the file from virtual machine path `/home/user/Downloads/answer.csv` to localhost file `pred.csv`
    - `expected` defines how to get the golden result. In this example, we invoke the function [`get_local_file`](../desktop_env/evaluators/getters/file.py) to obtain the oracle file `gold_output.csv` from localhost path `evaluation_examples/examples/bigquery/3363a913-d3e9-42c2-9d76-9cd9e9bafec7/answer.csv`
    - `options` gives the keyword arguments for the metric function. In this case, there is no keyword arguments. In other words, we use the default keyword arguments for metric [`compare_csv`](../desktop_env/evaluators/metrics/table.py)


## Real Accounts
For task examples that require real accounts (*e.g.*, the `tags` field containing value `account`, or the `related_apps` field containing any value of `['snowflake', 'bigquery', 'servicenow', 'dbt_cloud', 'hasura_cloud']`), we need to sign up and obtain credentials before testing them. The account information and credentials need to be filled into corresponding JSON templates under folder `evaluation_examples/settings/`. Please refer to [Account Guideline](../ACCOUNT_GUIDELINE.md) for details on how to register and fill in necessary information.