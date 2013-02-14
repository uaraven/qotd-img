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

ASPECT_CORRECTION = 1.5
THUMBNAIL_SIZE = (112, 112)

CHAR_DISTRIBUTION = [
    (45, 'W'),
    (36, '@'),
    (30, 'O'),
    (27, '$'),
    (24, 'V'),
    (20, 'H'),
    (17, '*'),
    (14, '='),
    (10, ':'),
    (5, '-'),
    (3, '`'),
    (0, ' ')
]


def prepare(src_image, palette):
    image = src_image
    image.thumbnail(THUMBNAIL_SIZE)
    new_size = (image.size[0], int(image.size[1] / ASPECT_CORRECTION))
    image = image.resize(new_size)
    if palette is not None:
        palette_image = Image.new("P", (1, 1))
        palette_image.putpalette(palette)
        image = image.quantize(palette = palette_image)

    return image