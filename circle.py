import math


def _check_radius(r):
    if not isinstance(r, (int, float)):
        raise TypeError("radius must be a number")
    if r < 0:
        raise ValueError("radius must be non-negative")


def area(r):
    _check_radius(r)
    return math.pi * r * r


def perimeter(r):
    _check_radius(r)
    return 2 * math.pi * r

