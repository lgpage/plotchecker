from __future__ import division

import matplotlib
import matplotlib.colors
import matplotlib.markers
import numpy as np
import six


class InvalidPlotError(Exception):
    pass


class PlotChecker(object):

    _named_colors = matplotlib.colors.ColorConverter.colors.copy()
    for colorname, hexcode in matplotlib.colors.cnames.items():
        _named_colors[colorname] = matplotlib.colors.hex2color(hexcode)

    def __init__(self, axis):
        self.axis = axis

    @classmethod
    def _color2rgb(cls, color):
        if isinstance(color, six.string_types):
            if color in cls._named_colors:
                return np.array(cls._named_colors[color], dtype=float)
            else:
                return np.array(matplotlib.colors.hex2color(color), dtype=float)
        elif len(color) == 3:
            return np.array(color, dtype=float)
        elif len(color) == 4:
            return np.array(color, dtype=float)[:3]
        else:
            raise ValueError("Invalid color: {}".format(color))

    @classmethod
    def _color2alpha(cls, color):
        if isinstance(color, six.string_types):
            return 1.0
        elif len(color) == 3:
            return 1.0
        elif len(color) == 4:
            return float(color[3])
        else:
            raise ValueError("Invalid color: {}".format(color))

    @classmethod
    def _tile_or_trim(cls, x, y):
        xn = x.shape[0]
        yn = y.shape[0]
        if xn > yn:
            numrep = np.ceil(xn / yn)
            y = np.tile(y, (numrep,) + (1,) * (y.ndim - 1))
        if xn < yn:
            y = y[:xn]
        return y


# def get_label_text(ax):
#     text = [x for x in ax.get_children()
#             if isinstance(x, matplotlib.text.Text)]
#     text = [x for x in text if x.get_text() != ax.get_title()]
#     text = [x for x in text if x.get_text().strip() != '']
#     return [x.get_text().strip() for x in text]


# def get_label_pos(ax):
#     text = [x for x in ax.get_children()
#             if isinstance(x, matplotlib.text.Text)]
#     text = [x for x in text if x.get_text() != ax.get_title()]
#     text = [x for x in text if x.get_text().strip() != '']
#     return np.vstack([x.get_position() for x in text])


# def get_imshow_data(ax):
#     image, = ax.get_images()
#     return image._A