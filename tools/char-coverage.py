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


from PIL import ImageFont
import sys

DEFAULT = '/usr/share/fonts/truetype/freefont/FreeMono.ttf'
#DEFAULT = '/usr/share/fonts/truetype/droid/DroidSansMono.ttf'


def draw_char(c, font):
    img = font.getmask(c, mode = '1')
    return img, img.size


def get_char_coverage(font_name):
    font = ImageFont.truetype(font_name, 16)
    #    res = {}
    map_list = []
    for c in range(32, 0x7F):
        img, sz = draw_char(unichr(c), font)
        hh = img.histogram()
        pxl = sz[0] * sz[1]
        if pxl != 0:
            whiteness = 100 - hh[0] * 100 / pxl
            map_list.append((unichr(c), whiteness))
            #        if whiteness not in res:
            #            res[whiteness] = chr(c)
        #    for w in res:
    #        map_list.append((res[w], w))

    return sorted(map_list, key = lambda x: x[1])


def print_char_coverage(cc):
    global c
    print '_COLOR_MAP = ['
    for c in cc:
        print '(' + str(c[1]) + ', \'' + c[0] + '\'),'
    print ']'


if __name__ == '__main__':
    if len(sys.argv) > 1:
        font = sys.argv[1]
    else:
        font = DEFAULT
    cc = get_char_coverage(font)
    print_char_coverage(cc)