__author__ = 'raven'

import sys
import asciisizer
from image import prepare_thumbnail


if __name__ == '__main__':
    try:
        file = sys.argv[1]
        img = prepare_thumbnail(file)
        print asciisizer.pil_image_to_ascii(img)
    except:
        print 'img2ascii.py image_file'