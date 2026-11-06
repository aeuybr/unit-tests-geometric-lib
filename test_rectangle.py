import unittest
import rectangle


class RectangleTestCase(unittest.TestCase):
    def test_area_numbers(self):
        cases = [
            (3, 5, 15),
            (10, 0, 0),
            (4, 4, 16),
            (2.5, 4, 10),
            (1, 1, 1),
            (1, 1000, 1000),
            (1000, 1, 1000),
            (0, 5, 0),
            (5, 0, 0),
            (0, 1000000, 0),
            (7, 11, 77),
            (11, 7, 77),
            (100, 200, 20000),
            (999, 1001, 999999),
            (1000, 1000, 1000000),
            (1000000, 1000000, 1000000000000),
            (1000000000000, 1000000000000, 1000000000000000000000000),
            (12345, 67890, 838102050),
        ]
        for a, b, expected in cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(rectangle.area(a, b), expected)

    def test_perimeter_numbers(self):
        cases = [
            (3, 5, 16),
            (0, 0, 0),
            (4, 4, 16),
            (2.5, 4, 13),
            (1, 1, 4),
            (1, 1000, 2002),
            (1000, 1, 2002),
            (0, 5, 10),
            (5, 0, 10),
            (0, 1000000, 2000000),
            (7, 11, 36),
            (11, 7, 36),
            (100, 200, 600),
            (999, 1001, 4000),
            (1000, 1000, 4000),
            (1000000, 1000000, 4000000),
            (1000000000000, 1000000000000, 4000000000000),
            (12345, 67890, 160470),
        ]
        for a, b, expected in cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(rectangle.perimeter(a, b), expected)

    def test_area_string(self):
        cases = [
            ('3', 5),
            ('', 5),
            (5, ''),
            ('abc', 5),
            (5, 'abc'),
            ('3', '5'),
            (3, '5'),
        ]
        for a, b in cases:
            with self.subTest(a=a, b=b):
                with self.assertRaises(TypeError):
                    rectangle.area(a, b)

    def test_area_negative(self):
        cases = [
            (-3, 5),
            (-1, 5),
            (5, -1),
            (-2, -3),
            (-0.001, 5),
            (5, -0.001),
            (-1000000, 2),
            (2, -1000000),
        ]
        for a, b in cases:
            with self.subTest(a=a, b=b):
                with self.assertRaises(ValueError):
                    rectangle.area(a, b)

    def test_perimeter_string(self):
        cases = [
            ('3', 5),
            ('', 5),
            (5, ''),
            ('abc', 5),
            (5, 'abc'),
            ('3', '5'),
            (3, '5'),
        ]
        for a, b in cases:
            with self.subTest(a=a, b=b):
                with self.assertRaises(TypeError):
                    rectangle.perimeter(a, b)

    def test_perimeter_negative(self):
        cases = [
            (-3, 5),
            (-1, 5),
            (5, -1),
            (-2, -3),
            (-0.001, 5),
            (5, -0.001),
            (-1000000, 2),
            (2, -1000000),
        ]
        for a, b in cases:
            with self.subTest(a=a, b=b):
                with self.assertRaises(ValueError):
                    rectangle.perimeter(a, b)

    def test_area_decimal(self):
        cases = [
            (0.1, 0.2, 0.02, 2e-14),
            (0.001, 1000, 1.0, 1e-12),
            (1000, 0.001, 1.0, 1e-12),
            (0.25, 0.5, 0.125, 1.25e-13),
            (1.25, 2.75, 3.4375, 3.4375e-12),
            (999.5, 2, 1999.0, 1.999e-09),
        ]
        for a, b, expected, delta in cases:
            with self.subTest(a=a, b=b):
                self.assertAlmostEqual(rectangle.area(a, b), expected, delta=delta)

    def test_perimeter_decimal(self):
        cases = [
            (0.1, 0.2, 0.6, 6e-13),
            (0.001, 1000, 2000.002, 2.000002e-09),
            (1000, 0.001, 2000.002, 2.000002e-09),
            (0.25, 0.5, 1.5, 1.5e-12),
            (1.25, 2.75, 8.0, 8e-12),
            (999.5, 2, 2003.0, 2.003e-09),
        ]
        for a, b, expected, delta in cases:
            with self.subTest(a=a, b=b):
                self.assertAlmostEqual(rectangle.perimeter(a, b), expected, delta=delta)


if __name__ == "__main__":
    unittest.main()
