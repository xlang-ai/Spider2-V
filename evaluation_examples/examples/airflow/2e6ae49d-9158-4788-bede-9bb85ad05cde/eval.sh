#!/bin/bash

source /home/user/anaconda3/etc/profile.d/conda.sh
#conda activate astro
cd /home/user/projects

export FILTER_SET='_first_name=Linda'
export USER_STASTIC='userstatschartview'

echo "${FILTER_SET}, ${USER_STASTIC}"
