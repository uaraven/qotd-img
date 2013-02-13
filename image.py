import Image
import ImageEnhance

__author__ = 'raven'

_ASPECT_CORRECTION = 1.5
_BRIGHTNESS_CORRECTION = 1
_CONTRAST_CORRECTION = 1
_THUMBNAIL_SIZE = (112, 112)


def prepare_thumbnail(file_name):
    image = Image.open(file_name)
    image = image.convert('L')
    image.thumbnail(_THUMBNAIL_SIZE)
    new_size = (image.size[0], int(image.size[1] / _ASPECT_CORRECTION))
    image = image.resize(new_size)
    if _BRIGHTNESS_CORRECTION != 1:
        brightness = ImageEnhance.Brightness(image)
        image = brightness.enhance(_BRIGHTNESS_CORRECTION)
    if _CONTRAST_CORRECTION != 1:
        contrast = ImageEnhance.Contrast(image)
        image = contrast.enhance(_CONTRAST_CORRECTION)
    return image