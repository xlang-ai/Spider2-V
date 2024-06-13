#!/bin/bash

source /home/user/anaconda3/etc/profile.d/conda.sh
#conda activate astro
cd /home/user/projects

export DAG_SEARCH_SET='search=Astro'
export SORTING_KEY='sorting_key=dag_id'
export SORTING_ORDER='sorting_direction=asc'


echo "${DAG_SEARCH_SET}, ${SORTING_KEY}, ${SORTING_ORDER}"
