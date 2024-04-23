#!/bin/bash


exec 2>/dev/null

PASSWORD='password'

# 1. install JAVA, set JAVA_HOME
echo $PASSWORD | sudo -S apt-get update && apt-get install -y default-jre default-jdk
JAVA_RUNTIME=$(readlink -f $(which java))
JAVA_HOME=$(dirname $(dirname $JAVA_RUNTIME))
export JAVA_HOME=$JAVA_HOME
echo "export JAVA_HOME=$JAVA_HOME" >> ~/.bashrc
echo $PASSWORD | sudo -S bash -c "echo 'export JAVA_HOME=$JAVA_HOME' >> /etc/environment" # may need to restart the system

# 2. install Metabase from jar package
mkdir -p /home/user/projects/metabase && cd /home/user/projects/metabase
wget -c https://downloads.metabase.com/v0.49.6/metabase.jar

# 3. install postgres
function install_postgres() {
    echo $PASSWORD | sudo -S apt-get install postgresql postgresql-contrib -y >/dev/null 2>&1
    cd /home
    # allow connection from any IP (including docker container)
    config_file=$(echo $PASSWORD | sudo -S -u postgres psql -tc "SHOW config_file" | awk 'NR==1 {print $1}')
    echo $PASSWORD | sudo -S bash -c "echo \"listen_addresses = '*'\" >> ${config_file}"
    # change the default authentication method to scram-sha-256
    hba_file=$(echo $PASSWORD | sudo -S -u postgres psql -tc "SHOW hba_file" | awk 'NR==1 {print $1}')
    echo $PASSWORD | sudo -S cp ${hba_file} ${hba_file}.bak
    echo $PASSWORD | sudo -S bash -c "sudo sed -i 's/local[[:space:]]\+all[[:space:]]\+all[[:space:]]\+peer/local   all             all                                     scram-sha-256/' ${hba_file}"
    echo $PASSWORD | sudo -S bash -c "sudo sed -i 's/local[[:space:]]\+replication[[:space:]]\+all[[:space:]]\+peer/local   replication     all                                     scram-sha-256/' ${hba_file}"
    echo $PASSWORD | sudo -S bash -c "echo \"host    all             all             172.16.0.0/14           scram-sha-256\" >> ${hba_file}"
    sudo systemctl restart postgresql
}
install_postgres