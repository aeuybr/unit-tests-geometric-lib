def _check_sides(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("side lengths must be numbers")
    if a < 0 or b < 0:
        raise ValueError("side lengths must be non-negative")


def area(a, b):
    _check_sides(a, b)
    return a * b


def perimeter(a, b):
    _check_sides(a, b)
    return 2 * (a + b)
