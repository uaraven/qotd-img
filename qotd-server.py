#!/bin/usr/python

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
        return "Houston, we have a problem. There is no images available.\n"
    else:
        return '{title}\n{summary}\n\n{image}\n'.format(
            title = imgd['title'],
            summary = imgd['summary'],
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