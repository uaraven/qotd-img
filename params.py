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

from optparse import OptionParser
from image import GRAYSCALE

parser = None


def prepare_parser(usage = ''):
    global parser
    parser = OptionParser(usage)
    parser.add_option("-m", "--mode", dest = "mode", help = "Select image processing mode bw|grayscale|color",
                      default = GRAYSCALE)


def retrieve_options():
    global parser
    return parser.parse_args()


def print_options():
    global parser
    parser.print_usage()


def print_usage():
    pass