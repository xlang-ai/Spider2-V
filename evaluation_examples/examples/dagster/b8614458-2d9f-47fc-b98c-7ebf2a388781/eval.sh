#!/bin/bash

exec 2>/dev/null

PROJECT_NAME=hacker-news-ml-pipeline

cd /home/user/$PROJECT_NAME
source /home/user/anaconda3/etc/profile.d/conda.sh
conda activate dagster

export DAGSTER_HOME=~/.dagster

test_set_score_check=$(python -c "import numpy as np; result = np.load('/home/user/.dagster/storage/model_test_set_score', allow_pickle=True); print(type(result) == np.float64 and result < 1.)")

if [ "$test_set_score_check" == "True" ]; then
    echo "Check test set score succeeded"
else
    echo "Check test set score failed"
fi

predictions_check=$(python -c "import numpy as np; result = np.load('/home/user/.dagster/storage/latest_story_comment_predictions', allow_pickle=True); print(len(result) == 13 and result.dtype == float)")

if [ "$predictions_check" == "True" ]; then
    echo "Check predictions succeeded"
else
    echo "Check predictions failed"
fi
