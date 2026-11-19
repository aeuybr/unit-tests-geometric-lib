def _check_side(a):
    if not isinstance(a, (int, float)):
        raise TypeError("side must be a number")
    if a < 0:
        raise ValueError("side must be non-negative")


def area(a):
    _check_side(a)
    return a * a


def perimeter(a):
    _check_side(a)
    return 4 * a
