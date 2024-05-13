#!/bin/bash

exec 1>/dev/null
exec 2>/dev/null

function to_ready_state(){
    echo "source /home/user/anaconda3/etc/profile.d/conda.sh" >> ~/.bashrc
    echo "conda activate bigquery" >> ~/.bashrc
    source /home/user/anaconda3/etc/profile.d/conda.sh
    conda activate bigquery
    cd ~/Desktop
    python query.py
}
to_ready_state

gnome-terminal --working-directory=/home/user/Downloads
