#!/bin/bash

exec 2>/dev/null

FILE_PATH="/home/user/Desktop/connection_config.json"
connection_config=false

REQUIRED_FIELDS=("connectionId" "name" "namespaceDefinition" "prefix" "sourceId" "destinationId" "operationIds" "syncCatalog" "schedule" "scheduleType" "scheduleData" "status" "sourceCatalogId" "geography" "breakingChange" "notifySchemaChanges" "notifySchemaChangesByEmail" "nonBreakingChangesPreference" "created_at" "backfillPreference")


if [ -f "$FILE_PATH" ]; then
    echo "File exists: $FILE_PATH"
else
    continue
fi

all_fields_present=true
for field in "${REQUIRED_FIELDS[@]}"; do
    if ! jq -e "has(\"$field\")" "$FILE_PATH" > /dev/null; then
        echo "Missing field: $field"
        all_fields_present=false
    fi
done

if [ "${all_fields_present}" = true ]; then
    connection_config=true
fi

if [ ${connection_config} = true ] ; then
    echo "Airbyte connection config JSON file export, succeeded"
else
    echo "Airbyte connection config JSON file export, failed"
    exit 0
fi
