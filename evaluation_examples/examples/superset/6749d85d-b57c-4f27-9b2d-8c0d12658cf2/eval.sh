#!/bin/bash

exec 2>/dev/null

export STANDALONE_KEY='standalone=2'
export FILTER_KEY='show_filters=0'


echo "${STANDALONE_KEY}, ${FILTER_KEY}"
