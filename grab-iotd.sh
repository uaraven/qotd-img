#!/bin/bash

DIR=`dirname $0`
cd $DIR

# If we are not root, we cannot write to /var/log
if [[ $EUID -ne 0 ]]; then
    python ./qotd-grabber.py
   exit 1
fi

python ./qotd-grabber.py
