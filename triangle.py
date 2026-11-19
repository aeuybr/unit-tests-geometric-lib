import math


def _check_sides(a, b, c):
    if not all(isinstance(side, (int, float)) for side in (a, b, c)):
        raise TypeError("side lengths must be numbers")
    if min(a, b, c) <= 0:
        raise ValueError("side lengths must be positive")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("the sides must form a non-degenerate triangle")


def area(a, b, c):
    _check_sides(a, b, c)
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))


def perimeter(a, b, c):
    _check_sides(a, b, c)
    return a + b + c
