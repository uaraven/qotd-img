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
import SocketServer
import traceback
import sys

import image
import params
import db


HOST, PORT = ("0.0.0.0", 17)
MODE = image.GRAYSCALE
TIME_FORMAT = '%Y-%m-%d %H:%M:%S.%f'


class TCPQuoteHandler(SocketServer.StreamRequestHandler):
    def handle(self):
        try:
            print 'D: [{}] Access from {}'.format(datetime.datetime.now().strftime(TIME_FORMAT), self.client_address[0])
            db.log_access(datetime.datetime.now(), self.client_address[0])
            self.wfile.write(create_quote(db, MODE))
        except Exception, e:
            self.wfile.close()
            self.rfile.close()
            dt = datetime.datetime.now().strftime(TIME_FORMAT)
            print 'E: [{}] Failed to create quote - {}'.format(dt, str(e))
            traceback.print_tb(sys.exc_info()[2])

    sys.stdout.flush()


def create_quote(db, mode):
    imgd = db.get_latest_image()
    if imgd is None:
        return "Houston, we have a problem. There are no images available.\n"
    else:
        return '{summary}\n\nOrignal url: {url}\n\n{image}\n'.format(
            url = imgd['url'],
            summary = imgd['summary'].replace('\n', ' '),
            image = image.convert_buffer(imgd['data'], mode)
        )


def initialize_server(port):
    return SocketServer.TCPServer((HOST, port), TCPQuoteHandler)


if __name__ == '__main__':
    params.prepare_parser()
    params.parser.add_option("-p", "--port", dest = "port", help = "Port to listen on (default is 17)",
                             default = PORT)

    options, arguments = params.retrieve_options()

    MODE = options.mode

    db.init('data/qotd-img.sqlite')
    dt = datetime.datetime.now().strftime(TIME_FORMAT)
    print 'D: [{}] Started serving on port {}'.format(dt, options.port)
    server = initialize_server(int(options.port))
    sys.stdout.flush()

    server.serve_forever()
