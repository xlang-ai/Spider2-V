#!/bin/bash

exec 2>/dev/null

export LOG_KEY='logmodelview'
export FILTER_KEY='flt_0_user=1'
export OD_LOGMODELVIEW='od_LogModelView=asc'
export OC_LOGMODELVIEW='oc_LogModelView=dttm'

echo "${LOG_KEY}, ${FILTER_KEY}, ${OD_LOGMODELVIEW},${OC_LOGMODELVIEW}"
