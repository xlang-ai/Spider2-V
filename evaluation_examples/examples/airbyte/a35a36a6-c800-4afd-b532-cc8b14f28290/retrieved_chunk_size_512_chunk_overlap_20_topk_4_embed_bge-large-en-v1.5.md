Documentation Source:
airbyte.com/tutorials/version-control-airbyte-configurations.md

Documentation Title:
Version control Airbyte configurations with Octavia CLI | Airbyte

Documentation Content:
You will need to pass a DEFINITION\_ID and RESOURCE\_NAME. Due to a current limitation, to create a source, you first need to get the definition id for the source. You can run the command **octavia list connectors sources** to get the connector id:

`octavia list connectors sources | grep postgres

Postgres airbyte/source-postgres 1.0.22 decd338e-5647-4c0b-adf4-da0e75f5a750`Then you can bootstrap a Postgres source with the **octavia generate source**command:

`octavia generate source decd338e-5647-4c0b-adf4-da0e75f5a750 postgres

🐙 - Octavia is targetting your Airbyte instance running at http://localhost:8000 on workspace 36ddb450-66e4-4988-91bf-67279eed5098.
✅ - Created the source template for postgres in sources/postgres/configuration.yaml.`The CLI creates a **postgres**folder under sources with a **configuration.yaml**file.

`tree .
.
├── api_http_headers.yaml
├── connections
├── destinations
└── sources
 └── postgres
 └── configuration.yaml

4 directories, 2 files`The YAML file contains all the fields with the default values you see on the UI, and the description for each field as a comment. Below you can see the beginning of the file.

`more sources/postgres/configuration.yaml



Documentation Source:
airbyte.com/tutorials/version-control-airbyte-configurations.md

Documentation Title:
Version control Airbyte configurations with Octavia CLI | Airbyte

Documentation Content:
`octavia apply

🐙 - Octavia is targetting your Airbyte instance running at http://localhost:8000 on workspace 36ddb450-66e4-4988-91bf-67279eed5098.
🐙 - bigquery does not exists on your Airbyte instance, let's create it!
🎉 - Successfully created bigquery on your Airbyte instance!
💾 - New state for bigquery saved at ./destinations/bigquery/state_36ddb450-66e4-4988-91bf-67279eed5098.yaml
🐙 - postgres exists on your Airbyte instance according to your state file, let's check if we need to update it!
😴 - Did not update because no change detected.`Then you can see that the changes were applied in the UI. Remember to test the connection.

!Create a connection with Octavia CLI
------------------------------------

Once you have source and destination configuration files, you can create a connection template with the **octavia generate connection**command.

`octavia generate connection --source sources/postgres/configuration.yaml --destination destinations/bigquery/configuration.yaml postgres-to-bigquery

🐙 - Octavia is targetting your Airbyte instance running at http://localhost:8000 on workspace 36ddb450-66e4-4988-91bf-67279eed5098.
✅ - Created the connection template for postgres-to-bigquery in connections/postgres_to_bigquery/configuration.yaml.`After editing the configuration, your configuration should look like this:

`cat connections/postgres_to_bigquery/configuration.yaml

definition_type: connection
resource_name: "postgres-to-bigquery"
source_configuration_path: sources/postgres/configuration.yaml
destination_configuration_path: destinations/bigquery/configuration.yaml

configuration:
 status: active
 namespace_definition: source
 namespace_format: "${SOURCE_NAMESPACE}"
 prefix: ""
 resource_requirements:
 cpu_limit: ""
 cpu_request: ""
 memory_limit: ""
 memory_request: ""
 schedule_type: manual
 sync_catalog: # OPTIONAL | object | 🚨 ONLY edit streams.config, streams.stream should not be edited as schema cannot be changed.



Documentation Source:
airbyte.com/tutorials/version-control-airbyte-configurations.md

Documentation Title:
Version control Airbyte configurations with Octavia CLI | Airbyte

Documentation Content:
If an error occurs, you will get a stack trace from the API response.

`octavia apply

🐙 - Octavia is targetting your Airbyte instance running at http://localhost:8000 on workspace 36ddb450-66e4-4988-91bf-67279eed5098.
🐙 - postgres does not exists on your Airbyte instance, let's create it!
🎉 - Successfully created postgres on your Airbyte instance!
💾 - New state for postgres saved at ./sources/postgres/state_36ddb450-66e4-4988-91bf-67279eed5098.yaml`Then you can check that the configuration is also available in the UI.

!After you apply some configuration changes with Octavia, no connection test will be run like when you save connector settings in the UI (see GitHub issue). You can still use the UI to test that the source setting allows Airbyte to connect.

‍

!After you apply some changes, Octavia creates a **state.yaml**file in the resource directory with the checksum of the latest configuration applied and the generation timestamp. The state files are instance and workspace specific so they are only useful when multiple users or Octavia CLI processes work on the same instance and workspace. If you apply the same configuration across multiple instances, then you don’t need to commit state files in your Git repository.

Each time you run the apply command, Octavia will also compute and display differences between the current resource state locally including changes since you last run the apply command, and the state in your Airbyte instance including changes you may have done on the UI.



Documentation Source:
airbyte.com/tutorials/version-control-airbyte-configurations.md

Documentation Title:
Version control Airbyte configurations with Octavia CLI | Airbyte

Documentation Content:
🎉 - Successfully updated postgres-to-bigquery on your Airbyte instance!
💾 - New state for postgres-to-bigquery stored at connections/postgres_to_bigquery/state_36ddb450-66e4-4988-91bf-67279eed5098.yaml.`Above, you will notice the two differences related to our configuration changes locally:  root['schedule\_data'] and root['schedule\_type']. The rest of the differences come from Airbyte adding some extra changes after applying the local config. To avoid this difference, you must import the Airbyte config locally and commit these fields.

Import an existing Airbyte YAML configuration
---------------------------------------------

If you have already configured an Airbyte instance and want to version control changes or manage configurations with Octavia, you can get the instance configuration with the **octavia import all**command. This command will retrieve all sources, destinations, and connection configurations. You can then commit this to a Git repository. Once you start to edit Airbyte resources with Octavia CLI then is better to avoid using the UI as well as you will continue to see some differences when importing changes.

Before retrieving the configurations, you have to bootstrap an Octavia project. For example, if you change to a new folder locally, create an octavia project with octavia init and run the import command, you will get this output.

`octavia init

🐙 - Octavia is targetting your Airbyte instance running at http://localhost:8000 on workspace 36ddb450-66e4-4988-91bf-67279eed5098.
🐙 - Project is not yet initialized.
🔨 - Initializing the project.
✅ - Created the following directories: sources, destinations, connections.
✅ - Created API HTTP headers file in api_http_headers.yaml``octavia import all

🐙 - Octavia is targetting your Airbyte instance running at http://localhost:8000 on workspace 36ddb450-66e4-4988-91bf-67279eed5098.
✅ - Imported source postgres in sources/postgres/configuration.yaml.



