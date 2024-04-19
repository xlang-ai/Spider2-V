#!/bin/bash

# sometimes when reverting to snapshot the network is disconnected
# we need to check the network service, if connceted, just skip
# o.w., we need to restart the network server

TARGET="www.google.com"

PING_COUNT=3


function check_network() {
    for (( i=1; i<=$PING_COUNT; i++ )); do
        if ping -c 1 $TARGET > /dev/null 2>&1; then
            echo "Network connection succeeds, just skip."
            exit 0
        fi
    done
    echo "Network connection failed, try to re-connect ..."
}

msg=$(check_network | grep "succeed")
if [ $? -eq 0 ] ; then
    echo $msg
    exit 0
fi

echo "password" | sudo -S systemctl restart NetworkManager.service

sleep 5

msg=$(check_network | grep "succeed")
if [ $? -eq 0 ] ; then
    echo $msg
    exit 0
else
    echo "failed"
    exit 1
fi