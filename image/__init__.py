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


import cStringIO
from PIL import Image

import BwImage
import ColorImage
import common


BW = 'bw'
GRAYSCALE = 'grayscale'
COLOR_SIMPLE = 'color'

_MAPPINGS = {BW: (BwImage.BlackAndWhiteMapping, BwImage),
             GRAYSCALE: (BwImage.GrayscaleMapping, BwImage),
             COLOR_SIMPLE: (ColorImage.SimpleColorMappping, ColorImage)
}


def convert_image(file_name, mode):
    image = Image.open(file_name)
    mapping = _MAPPINGS[mode]
    return mapping[1].image_to_text(image, mapping[0])


def convert_buffer(buffer, mode):
    file = cStringIO.StringIO(buffer)
    image = Image.open(file)
    mapping = _MAPPINGS[mode]
    return mapping[1].image_to_text(image, mapping[0])


def prepare_image(file_name):
    image = Image.open(file_name)
    return common.prepare(image, None)