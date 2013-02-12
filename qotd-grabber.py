#!/bin/usr/python

# This application requires PIL version 1.1.6 or higher to be installed
# You can get get PIL from your distro's repository or directly from
# http://www.pythonware.com/library/

import datetime

import iotd
import db


TIME_FORMAT = '%Y-%m-%d %H:%M:%S.%f'

if __name__ == '__main__':
    db.init('data/qotd-img.sqlite')
    dt = datetime.datetime.now().strftime(TIME_FORMAT)
    try:
        print 'D: [{}] Grabbing NASA Image Of The Day'.format(dt)
        if iotd.retrieve_and_store(db):
            print 'D: [{}] Retrieved new NASA Image Of The Day'.format(dt)
        else:
            print 'D: [{}] Latest NASA Image Of The Day is already retrieved'.format(dt)
    except Exception, e:
        print 'E: [{}] Failed to retrieve IOTD - [{}]'.format(dt, str(e))

