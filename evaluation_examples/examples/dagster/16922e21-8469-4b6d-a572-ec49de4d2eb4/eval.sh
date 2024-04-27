#!/bin/bash

PROJECT_NAME=iris-analysis

cd ~/$PROJECT_NAME
source /home/user/anaconda3/etc/profile.d/conda.sh
conda activate dagster

RUN_ID=$(cat run_id.txt)
flag=$(dagster-cloud run status $RUN_ID | grep SUCCESS)
if [ -n "$flag" ] ; then
    echo "Check run succeeded"
else
    echo "Check run failed"
    exit 0
fi

flag=$(dagster-cloud deployment list-locations | grep iris)
if [ -n "$flag" ] ; then
    echo "Check code location succeeded"
else
    echo "Check code location failed"
    exit 0
fi

# pg.goto("https://happysix-test.dagster.cloud/prod/assets/iris_virginica")
# pg.locator("[target='_blank']").click()
# pg.locator("[target='_blank']").get_attribute("href")
# '/prod/runs/e56bc0da-d1b2-4fbe-adf5-1cd426a32a0b?focusedTime=1713712950062&selection=&logs='

# pg.goto("https://happysix-test.dagster.cloud/prod/environment")
# pg.locator("[aria-label='Download']").click()
# pg.locator("[role='menuitem']").click()