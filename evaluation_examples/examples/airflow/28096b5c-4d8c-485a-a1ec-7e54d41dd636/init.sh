#!/bin/bash

####################################################################################################
# Please ensure that Chromium or Chrome, VSCode, docker and anaconda3 is installed on your system before running this script.
# The installed anaconda3 should be in the directory /home/user/anaconda3/.
# Docker engine is installed following official docs: https://docs.docker.com/engine/install/ubuntu/
# Astro CLI is installed following official docs and Postgresql is installed via sudo apt-get install -y postgresql postgresql-contrib.
# This script is tested on Ubuntu 22.04 LTS.
####################################################################################################

exec 1>/dev/null
exec 2>/dev/null

PASSWORD=password

# uninstall docker
echo $PASSWORD | sudo -S systemctl stop docker.service
echo $PASSWORD | sudo -S systemctl stop containerd.service
echo $PASSWORD | sudo -S systemctl disable docker.service
echo $PASSWORD | sudo -S systemctl disable containerd.service
echo $PASSWORD | sudo -S apt-get purge -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin docker-ce-rootless-extras
echo $PASSWORD | sudo -S rm -rf /var/lib/docker /etc/docker /var/lib/containerd
echo $PASSWORD | sudo -S gpasswd -d user docker
echo $PASSWORD | sudo -S groupdel docker

# uninstall astro-cli
echo $PASSWORD | sudo -S rm -rf /usr/local/bin/astro

# uninstall postgresql
echo $PASSWORD | sudo -S systemctl stop postgresql
echo $PASSWORD | sudo -S systemctl disable postgresql
echo $PASSWORD | sudo -S rm -rf /etc/postgresql /var/lib/postgresql /var/log/postgresql
echo $PASSWORD | sudo -S apt-get purge -y postgresql postgresql-*
echo $PASSWORD | sudo -S deluser postgres
echo $PASSWORD | sudo -S groupdel docker

echo $PASSWORD | sudo -S apt-get autoremove -y