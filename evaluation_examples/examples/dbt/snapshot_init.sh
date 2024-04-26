#!/bin/bash

exec 2>/dev/null

source /home/user/anaconda3/etc/profile.d/conda.sh
conda create -n dbt python=3.11 -y
conda activate dbt
pip install dbt-core==1.7.13 dbt-duckdb==1.7.4