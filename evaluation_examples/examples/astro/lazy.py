import os
import json
import pandas as pd

# Specify the directory where you want to create the new folders
base_dir = '/Users/fujipqiu/Github/DesktopEnv/evaluation_examples/examples/astro'

# Read the form
df = pd.read_excel('/Users/fujipqiu/Github/DesktopEnv/evaluation_examples/examples/astro/excel.xlsx')

# Specify the range of rows you want to process
start_row = 11  # 0-indexed, so 4 is the 5th row
end_row = 12

# Iterate over the specified range of rows in the form
for index, row in df.iloc[start_row:end_row].iterrows():
    # Extract the UUID, instruction, and source link
    uuid = row['UUID']
    instruction = row['Instruction']
    source_link = row['Source Link']

    # Create a directory named after the UUID in the specified directory
    os.makedirs(os.path.join(base_dir, uuid), exist_ok=True)

    # Create empty eval.sh and init.sh files
    open(os.path.join(base_dir, uuid, 'eval.sh'), 'a').close()
    open(os.path.join(base_dir, uuid, 'init.sh'), 'a').close()

    # Create a JSON file named UUID.json
    with open(os.path.join(base_dir, uuid, f'{uuid}.json'), 'w') as f:
        # Write the required content to the JSON file
        json.dump({
            "id": uuid,
            "snapshot": "airflow",
            "instruction": instruction,
            "source": [source_link],
            "config": [],
            "trajectory": "",
            "related_apps": [],
            "tags": [],
            "evaluator": {
                "func": "",
                "result": {
                    "type": "",
                    "src": "",
                    "dest": ""
                },
                "expected": {
                    "type": "",
                    "rules": {
                        "include": [],
                        "exclude": []
                    }
                }
            }
        }, f, indent=4)