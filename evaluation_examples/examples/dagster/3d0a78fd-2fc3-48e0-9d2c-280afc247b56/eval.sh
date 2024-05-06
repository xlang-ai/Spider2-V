#!/bin/bash

exec 2>/dev/null

PROJECT_NAME=math-proj

cd /home/user/$PROJECT_NAME
source /home/user/anaconda3/etc/profile.d/conda.sh
conda activate dagster

export DAGSTER_HOME=~/.dagster

# Extract run IDs from the file
run_ids=$(dagster run list | grep -oP 'Run: \K.*')

# Initialize a flag to indicate if validation passed
validation_passed=false

# Loop over each run ID
for run_id in $run_ids
do
    # Run the dagster debug export command for each run ID
    dagster debug export $run_id run_log.gz

    # Extract the run_log.gz file
    gunzip -qf run_log.gz

    # Check if run_log contains "Validation passed"
    if grep -q "Validation passed" run_log; then
        validation_passed=true
        break
    fi
done

# Output the result
if $validation_passed; then
    echo "Validation succeeded"
else
    echo "Validation failed"
fi