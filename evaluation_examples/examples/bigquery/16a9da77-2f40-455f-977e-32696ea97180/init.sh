function to_ready_state(){
    echo "source /home/user/anaconda3/etc/profile.d/conda.sh" >> ~/.bashrc
    echo "conda activate bigquery" >> ~/.bashrc
    mkdir -p /home/user/projects/bigquery/project1
}
to_ready_state

gnome-terminal --working-directory=/home/user/projects/bigquery/project1
code /home/user/projects/bigquery/project1
