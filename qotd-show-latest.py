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

import db
import image
import params


HOST, PORT = ("0.0.0.0", 17)

TIME_FORMAT = '%Y-%m-%d %H:%M:%S.%f'


def create_quote(db, mode):
    imgd = db.get_latest_image()
    if imgd is None:
        return "Houston, we have a problem. There are no images available.\n"
    else:
        return '{summary}\n\nOriginal url: {url}\n\n{image}\n'.format(
            url = imgd['url'],
            summary = imgd['summary'].replace('\n', ' '),
            image = image.convert_buffer(imgd['data'], mode)
        )


if __name__ == '__main__':
    params.prepare_parser()
    options, arguments = params.retrieve_options()

    db.init('data/qotd-img.sqlite')
    print create_quote(db, options.mode)