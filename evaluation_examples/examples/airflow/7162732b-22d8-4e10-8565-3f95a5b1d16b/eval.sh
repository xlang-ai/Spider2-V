#!/bin/bash

source /home/user/anaconda3/etc/profile.d/conda.sh
#conda activate astro
cd /home/user/projects

http://localhost:8080/dags/example_astronauts/grid?tab=audit_log&limit=25&offset=1&sort.when=desc
export TAB_SET='tab=audit_log'
export OFFSET_KEY='offset=1'


echo "${TAB_SET}, ${OFFSET_KEY}"
