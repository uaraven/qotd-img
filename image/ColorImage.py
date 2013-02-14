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

from common import prepare, CHAR_DISTRIBUTION


def _darker_color(color, percent):
    return [x * percent / 100 for x in color]


def _generate_multicolor(chars, base_color_map):
    pass

#    palette = []
#    max = chars[0][0]
#    for char, brightness in chars:
#        for i in range(len(base_color_map['palette'])):
#            new_color =


SimpleColorMappping = {
    'palette': [
        0x00, 0x00, 0x00, # black
        0x00, 0x00, 0xAA, # low blue
        0x00, 0xAA, 0x00, # low green
        0x00, 0xAA, 0xAA, # low cyan
        0xAA, 0x00, 0x00, # low red
        0xAA, 0x00, 0xAA, # low magenta
        0xAA, 0x55, 0x00, # brown
        0xAA, 0xAA, 0xAA, # light gray
        0x55, 0x55, 0x55, # dark gray
        0x55, 0x55, 0xFF, # high blue
        0x55, 0xFF, 0x55, # high green
        0x55, 0xFF, 0xFF, # high cyan
        0xFF, 0x55, 0x55, # high red
        0xFF, 0x55, 0xFF, # high magenta
        0xFF, 0xFF, 0x55, # yellow
        0xFF, 0xFF, 0xFF  # white
    ],
    'charmap': ['*'] * 16,
    'ansi': ['30', # black
             '34', # low blue
             '32', # low green
             '36', # low cyan
             '31', # low red
             '35', # low magenta
             '33', # brown
             '37', # light gray
             '30;1', # dark gray
             '34;1', # high blue
             '32;1', # high green
             '36;1', # high cyan
             '31;1', # high red
             '35;1', # high magenta
             '33;1', # yellow
             '37;1'         # white
    ]
}

MultiColorMap = _generate_multicolor(CHAR_DISTRIBUTION, SimpleColorMappping)

_escape = '\033[%sm'


def image_to_text(image, mapping):
    palette = mapping['palette'] + [0] * (768 - len(mapping['palette']))
    prepared_image = prepare(image, palette)
    sz = prepared_image.size
    r = []
    for y in range(sz[1]):
        ln = ''
        for x in range(sz[0]):
            pxi = prepared_image.getpixel((x, y))
            ln += _escape % mapping['ansi'][pxi] + mapping['charmap'][pxi] + _escape % '0'
        r.append(ln)
    return '\n'.join(r)


