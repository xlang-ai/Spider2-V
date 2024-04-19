#!/bin/bash

# sometimes when reverting to snapshot the network is disconnected
# we need to check the network service, if connceted, just skip
# o.w., we need to restart the network server

TARGET="www.google.com"

PING_COUNT=3

function check_network() {
    for (( i=1; i<=$PING_COUNT; i++ )); do
        if ping -c 1 $TARGET >/dev/null 2>&1 ; then
            echo "Network connection succeeds, just skip."
            exit 0
        fi
        sleep 0.2
    done
    echo "Network connection failed, try to re-connect ..."
}

# 1. check the network status through ping Google
msg=$(check_network | grep "succeed")
if [ $? -eq 0 ] ; then
    echo $msg
    exit 0
fi

# 2. try to restart the network service via systemctl
function restart_network_manager() {
    echo "password" | sudo -S systemctl restart NetworkManager.service
    sleep 2
}
restart_network_manager
msg=$(check_network | grep "succeed")
if [ $? -eq 0 ] ; then
    echo $msg
    exit 0
fi

# 3. another method: try to restart the network service via nmcli
function restart_network_nmcli() {
    uuid=$(nmcli -f UUID,TYPE con show | grep -i 'ethernet' | awk '{print $1}')
    echo "password" | sudo -S bash -c "nmcli con down ${uuid} && nmcli con up ${uuid}"
    sleep 2
}
restart_network_nmcli
msg=$(check_network | grep "succeed")
if [ $? -eq 0 ] ; then
    echo $msg
    exit 0
fi

echo "failed"
exit 1