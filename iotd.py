#!/usr/bin/env python

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

# This module requires feedparser to be installed.
#
# Feed parser can be found on http://code.google.com/p/feedparser/

import urllib
import os
import feedparser
from image import prepare_thumbnail

_NASA_IOTD = 'http://www.nasa.gov/rss/image_of_the_day.rss'


def _retrieve_feed():
    return feedparser.parse(_NASA_IOTD)


def _retrieve_image(image_uri):
    remote_image = urllib.urlretrieve(image_uri)
    thumb_name = remote_image[0] + '.png'
    image = prepare_thumbnail(remote_image[0])
    image.save(thumb_name)
    f = open(thumb_name)
    data = f.read()
    f.close()
    os.remove(remote_image[0])
    os.remove(thumb_name)
    return buffer(data)


def retrieve_and_store(db):
    img = get_current_image()
    return db.store_image(img)


def get_current_image():
    image_info = {}
    feed = _retrieve_feed()
    try:
        print feed
        image_info['title'] = feed['feed']['title']
        image_info['date'] = feed['updated_parsed']
        for entry in feed['entries']:
            image_info['summary'] = entry['summary_detail']['value']
            uri = filter(lambda x: 'rel' in x and x['rel'] == u'enclosure', entry['links'])
            image_info['image_uri'] = uri[0]['href']
            image_info['data'] = _retrieve_image(uri[0]['href'])
        return image_info
    except:
        return None

