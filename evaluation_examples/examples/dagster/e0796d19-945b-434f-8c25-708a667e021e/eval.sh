#!/bin/bash
exec 2>/dev/null

PROJECT_NAME=harry-potter-potions
cd /home/user/$PROJECT_NAME
source /home/user/anaconda3/etc/profile.d/conda.sh
conda activate dagster
pip install pytest > /dev/null

export DAGSTER_HOME=~/.dagster

pytest harry_potter_potions_tests