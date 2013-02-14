#!/bin/usr/python

# -------------------------------------------------------------------------------------------------------------
# Copyright 2013 Oleksiy Voronin
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License. You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License
# is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and limitations under the License
# -------------------------------------------------------------------------------------------------------------

import datetime

import iotd
import db

TIME_FORMAT = '%Y-%m-%d %H:%M:%S.%f'

if __name__ == '__main__':
    db.init('data/qotd-img.sqlite')
    dt = datetime.datetime.now().strftime(TIME_FORMAT)
    print 'D: [{}] Grabbing NASA Image Of The Day'.format(dt)
    if iotd.retrieve_and_store(db):
        print 'D: [{}] Retrieved new NASA Image Of The Day'.format(dt)
    else:
        print 'D: [{}] Latest NASA Image Of The Day is already retrieved'.format(dt)