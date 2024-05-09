function to_ready_state(){
    echo "source /home/user/anaconda3/etc/profile.d/conda.sh" >> ~/.bashrc
    echo "conda activate bigquery" >> ~/.bashrc
    pip install google-cloud-bigquery
    cd ~/Desktop
    python query.py
}
to_ready_state

gnome-terminal --working-directory=/home/user/Downloads
