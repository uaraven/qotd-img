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


def generate_palette(distribution):
    max = distribution[0][0]
    result = []
    for brightness, ignored in distribution:
        c = 255 * brightness / max
        result.append(c)
        result.append(c)
        result.append(c)
    return result


BlackAndWhiteMapping = {
    'palette': [0x00, 0x00, 0x00, 0xFF, 0xFF, 0xFF],
    'charmap': [' ', '@']
}

GrayscaleMapping = {
    'palette': generate_palette(CHAR_DISTRIBUTION),
    'charmap': map(lambda x: x[1], CHAR_DISTRIBUTION)
}


def image_to_text(image, mapping):
    palette = mapping['palette'] + [0] * (768 - len(mapping['palette']))
    prepared_image = prepare(image, palette)
    sz = prepared_image.size
    r = []
    for y in range(sz[1]):
        ln = ''
        for x in range(sz[0]):
            pxi = prepared_image.getpixel((x, y))
            ln += mapping['charmap'][pxi]
        r.append(ln)
    return '\n'.join(r)

