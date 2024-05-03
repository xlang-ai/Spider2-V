#!/bin/bash

source /home/user/anaconda3/etc/profile.d/conda.sh
#conda activate astro
cd /home/user/projects

export OWNER_KEY='_flt_0_owner=admin'
export EVENT_KEY='_flt_0_event=delete'
export VIEW_SET='_oc_LogModelView=execution_date'
export ASC_SET='_od_LogModelView=asc'


echo "${OWNER_KEY}, ${EVENT_KEY},${VIEW_SET},${ASC_SET}"
