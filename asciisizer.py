# QOTD-Image
# Copyright 2013 Oleksiy Voronin
#
# This product is licensed under Apache License 2.0
#

from PIL import Image, ImageEnhance
import StringIO

_THUMBNAIL_SIZE = (56, 56)

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
    (22, 'U'),
    (24, 'D'),
    (26, '$'),
    (28, '0'),
    (30, 'O'),
    (31, '9'),
    (36, '@'),
    (38, 'W'),
    (41, 'Q')
]

_MAX_COLOR = 45
_ASPECT_CORRECTION = 2
_BRIGHTNESS_CORRECTION = 0.5
_CONTRAST_CORRECTION = 1.1


def _prepare_image_for_processing(image_buffer):
    file = StringIO.StringIO(image_buffer)
    image = Image.open(file)
    image = image.convert('L')
    image.thumbnail(_THUMBNAIL_SIZE)
    new_size = (int(image.size[0] * _ASPECT_CORRECTION), image.size[1])
    image = image.resize(new_size)
    brightness = ImageEnhance.Brightness(image)
    image = brightness.enhance(_BRIGHTNESS_CORRECTION)
    contrast = ImageEnhance.Contrast(image)
    image = contrast.enhance(_CONTRAST_CORRECTION)
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
