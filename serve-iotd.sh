#!/bin/bash

DIR=`dirname $0`
PORT=17
MODE=grayscale

# Make sure only root can run our script
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi

cd $DIR

python ./qotd-server.py -p $PORT -m $MODE >> /var/log/qotd-img.log &
echo $! > qotd-server.pid

