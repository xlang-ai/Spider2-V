#!/bin/bash

ping -c1 www.bing.com

if [ $? -eq 0 ]; then
    echo "succeed to connect to the internet"
    exit 0
fi

echo "password" | sudo -S systemctl restart NetworkManager
sleep 5

ping -c1 www.bing.com
if [ $? -eq 0 ]; then
    echo "succeed to connect to the internet after restarting network"
    exit 0
fi

echo "failed to connect to the internet even after restarting network"