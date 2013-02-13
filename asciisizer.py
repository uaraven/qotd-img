# coding=utf-8
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


from PIL import Image
import StringIO

#_COLOR_MAP = [
#    (19, u'░'),
#    (22, u'♢'),
#    (25, u'♡'),
#    (30, u'☓'),
#    (33, u'☲'),
#    (35, u'☹'),
#    (38, u'▒'),
#    (40, u'☯'),
#    (42, u'☢'),
#    (46, u'⑦'),
#    (49, u'℗'),
#    (54, u'▞'),
#    (63, u'◙'),
#    (70, u'▓'),
#    (75, u'▟'),
#    (80, u'▊'),
#    (90, u'▉'),
#    (100, u'█'),
#]

_COLOR_MAP = [
    (0, ' '),
    (4, '`'),
    (5, '-'),
    (9, '+'),
    (10, ':'),
    (11, '!'),
    (12, '='),
    (13, '}'),
    (14, 'r'),
    (16, 'z'),
    (17, '*'),
    (19, 'H'),
    (22, 's'),
    (24, 'V'),
    (27, '$'),
    (28, '0'),
    (30, 'O'),
    (31, '9'),
    (36, '@'),
    (38, 'W'),
    (41, 'Q')
]

_MAX_COLOR = 45


def _prepare_image_for_processing(image_buffer):
    file = StringIO.StringIO(image_buffer)
    image = Image.open(file)
    return image


def _pixel_to_char(value):
    clapped_value = value * _MAX_COLOR / 255
    for index, c in enumerate(_COLOR_MAP):
        if c[0] >= clapped_value:
            return c[1]
    return _COLOR_MAP[-1][1]


def _convert_image_to_strings(image):
    sz = image.size
    strings = []
    for y in xrange(0, sz[1]):
        s = ''
        for x in xrange(0, sz[0]):
            pix_char = _pixel_to_char(image.getpixel((x, y)))
            s += pix_char
        strings.append(s)
    return strings


def image_to_ascii(image_buffer):
    img = _prepare_image_for_processing(image_buffer)
    st = _convert_image_to_strings(img)
    return '\n'.join(st)
