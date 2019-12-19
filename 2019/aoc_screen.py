from PIL import Image
from PIL import ImageOps
import numpy as np


def get_frame(coords):
    np_coords = np.array([(k[0], k[1]) for k in coords.keys()])
    max_x = max(np_coords[:, 0])
    max_y = max(np_coords[:, 1])
    offset_x = np.abs(min(np_coords[:, 0]))
    offset_y = np.abs(min(np_coords[:, 1]))

    return max_x, max_y, offset_x, offset_y


def get_complex_frame(coords):
    np_coords = np.array([(int(k.real), int(k.imag)) for k in coords.keys()])
    max_x = int(max(np_coords[:, 0]))
    max_y = int(max(np_coords[:, 1]))
    offset_x = int(np.abs(min(np_coords[:, 0])))
    offset_y = int(np.abs(min(np_coords[:, 1])))

    return max_x, max_y, offset_x, offset_y


def screen(coord_dictionary):
    max_x, max_y, offset_x, offset_y = get_frame(coord_dictionary)

    background = 0

    red = (255, 0, 0, 0)
    white = (255, 255, 255, 0)
    green = (0, 255, 0, 0)
    blue = (0, 0, 255, 0)

    im = Image.new('RGB', (max_x + offset_x + 1, max_y + offset_y + 1), color=background)

    for k, v in coord_dictionary.items():
        if v == 1:
            im.putpixel((k[0] + offset_x, k[1] + offset_y), red)
        if v == 2:
            im.putpixel((k[0] + offset_x, k[1] + offset_y), white)
        if v == 3:
            im.putpixel((k[0] + offset_x, k[1] + offset_y), green)
        if v == 4:
            im.putpixel((k[0] + offset_x, k[1] + offset_y), blue)

    h, w = im.size

    upsize = 20
    im = im.resize((h * upsize, w * upsize))

    # im.save('blah.png')
    im = ImageOps.flip(im)
    im.show()


def screen_complex(coord_dictionary):
    max_x, max_y, offset_x, offset_y = get_complex_frame(coord_dictionary)

    background = 0
    red = (255, 0, 0, 0)
    white = (255, 255, 255, 0)
    green = (0, 255, 0, 0)
    blue = (0, 0, 255, 0)

    im = Image.new('RGB', (max_x + offset_x + 1, max_y + offset_y + 1), color=background)

    for k, v in coord_dictionary.items():
        k = (int(k.real) + offset_x, int(k.imag) + offset_y)
        if v == 1:
            im.putpixel(k, red)
        elif v == 0:
            im.putpixel(k, white)
        elif v == "X":
            im.putpixel(k, green)
        else:
            im.putpixel(k, blue)

    h, w = im.size

    upsize = 10
    im = im.resize((h * upsize, w * upsize))
    # im = ImageOps.flip(im)
    im.show()