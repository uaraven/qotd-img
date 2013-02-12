#!/usr/bin/env python

from PIL import ImageFont
import sys

DEFAULT = '/usr/share/fonts/truetype/freefont/FreeMono.ttf'


def draw_char(c, font):
    img = font.getmask(c, mode = 'L')
    return img, img.size


def get_char_coverage(font_name):
    font = ImageFont.truetype(font_name, 16)
    #    res = {}
    map_list = []
    for c in range(32, 128):
        img, sz = draw_char(chr(c), font)
        hh = img.histogram()
        pxl = sz[0] * sz[1]
        whiteness = 100 - hh[0] * 100 / pxl
        map_list.append((chr(c), whiteness))
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