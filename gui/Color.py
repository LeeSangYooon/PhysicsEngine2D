from random import uniform
import colorsys

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


def random_color():
    return hsv_to_rgb(uniform(0, 1), 0.88, 1)


def hsv_to_rgb(h: float, s: float, v: float) -> tuple:
    r, g, b = colorsys.hsv_to_rgb(h, s, v)
    rgb = tuple(int(x * 255) for x in (r, g, b))
    return rgb
