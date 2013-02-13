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


# This application requires PIL version 1.1.6 or higher to be installed
# You can get get PIL from your distro's repository or directly from
# http://www.pythonware.com/library/

import datetime
import sys
import SocketServer

import asciisizer
import db


HOST, PORT = ("0.0.0.0", 17)

TIME_FORMAT = '%Y-%m-%d %H:%M:%S.%f'


class TCPQuoteHandler(SocketServer.StreamRequestHandler):
    def handle(self):
        try:
            db.log_access(datetime.datetime.now(), self.client_address[0])
            self.wfile.write(create_quote(db))
        except Exception, e:
            dt = datetime.datetime.now().strftime(TIME_FORMAT)
            print 'E: [{}] Failed to create quote - {}'.format(dt, str(e))


def create_quote(db):
    imgd = db.get_latest_image()
    if imgd is None:
        return "Houston, we have a problem. There are no images available.\n"
    else:
        return '{summary}\n\nOrignal url: {url}\n\n{image}\n'.format(
            url = imgd['url'],
            summary = imgd['summary'].replaceall('\n', ' '),
            image = asciisizer.image_to_ascii(imgd['data'])
        )


def initialize_server():
    return SocketServer.TCPServer((HOST, PORT), TCPQuoteHandler)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        PORT = int(sys.argv[1])
    db.init('data/qotd-img.sqlite')
    dt = datetime.datetime.now().strftime(TIME_FORMAT)
    print 'D: [{}] Started serving on port {}'.format(dt, PORT)
    server = initialize_server()
    server.serve_forever()
