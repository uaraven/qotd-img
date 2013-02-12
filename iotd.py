#!/usr/bin/env python

# This module requires feedparser to be installed.
#
# Feed parser can be found on http://code.google.com/p/feedparser/

import urllib
import os

import feedparser


_NASA_IOTD = 'http://www.nasa.gov/rss/image_of_the_day.rss'


def _retrieve_feed():
    return feedparser.parse(_NASA_IOTD)


def _retrieve_image(image_uri):
    remote_image = urllib.urlretrieve(image_uri)
    f = open(remote_image[0])
    data = f.read()
    f.close()
    os.remove(remote_image[0])
    return buffer(data)


def retrieve_and_store(db):
    img = get_current_image()
    return db.store_image(img)


def get_current_image():
    image_info = {}
    feed = _retrieve_feed()
    try:
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

