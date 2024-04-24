#!/bin/bash

exec 1>/dev/null
exec 2>/dev/null

source /home/user/anaconda3/etc/profile.d/conda.sh
conda create -n jupyterlab python=3.11 -y
conda activate jupyterlab

pip install jupyter==1.0.0 jupyterlab==4.1.6 ipykernel==6.29.4 numpy==1.26.4 pandas==2.2.2 matplotlib==3.8.4 seaborn==0.13.2 scipy==1.13.0