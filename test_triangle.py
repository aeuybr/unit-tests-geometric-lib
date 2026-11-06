import unittest
import triangle


class TriangleTestCase(unittest.TestCase):
    def test_area_numbers(self):
        cases = [
            (3, 4, 5, 6),
            (5, 12, 13, 30),
            (1.5, 2, 2.5, 1.5),
            (8, 15, 17, 60),
            (7, 24, 25, 84),
            (20, 21, 29, 210),
            (9, 40, 41, 180),
            (12, 35, 37, 210),
            (11, 60, 61, 330),
            (5, 5, 6, 12),
            (5, 5, 8, 12),
            (13, 13, 10, 60),
            (13, 14, 15, 84),
            (5, 12, 13, 30),
            (5, 13, 12, 30),
            (12, 5, 13, 30),
            (12, 13, 5, 30),
            (13, 5, 12, 30),
            (13, 12, 5, 30),
        ]
        for a, b, c, expected in cases:
            with self.subTest(a=a, b=b, c=c):
                self.assertEqual(triangle.area(a, b, c), expected)

    def test_area_decimal(self):
        cases = [
            (2, 2, 2, 1.7320508075688772, None),
            (0.003, 0.004, 0.005, 6e-06, 1e-15),
            (0.3, 0.4, 0.5, 0.06, 6e-14),
            (1.5, 2.0, 2.5, 1.5, 1.5e-12),
            (6, 8, 10, 24.0, 2.4e-11),
            (30, 40, 50, 600.0, 6e-10),
            (300, 400, 500, 60000.0, 6e-08),
            (3000, 4000, 5000, 6000000.0, 6e-06),
            (3000000, 4000000, 5000000, 6000000000000.0, 6.0),
            (3000000000000, 4000000000000, 5000000000000, 6e+24, 6000000000000.0),
        ]
        for a, b, c, expected, delta in cases:
            with self.subTest(a=a, b=b, c=c):
                self.assertAlmostEqual(triangle.area(a, b, c), expected, delta=delta)

    def test_perimeter_numbers(self):
        cases = [
            (3, 4, 5, 12),
            (5, 12, 13, 30),
            (2, 2, 2, 6),
            (1.5, 2, 2.5, 6),
            (8, 15, 17, 40),
            (7, 24, 25, 56),
            (20, 21, 29, 70),
            (9, 40, 41, 90),
            (12, 35, 37, 84),
            (11, 60, 61, 132),
            (5, 5, 6, 16),
            (5, 5, 8, 18),
            (13, 13, 10, 36),
            (13, 14, 15, 42),
            (5, 12, 13, 30),
            (5, 13, 12, 30),
            (12, 5, 13, 30),
            (12, 13, 5, 30),
            (13, 5, 12, 30),
            (13, 12, 5, 30),
        ]
        for a, b, c, expected in cases:
            with self.subTest(a=a, b=b, c=c):
                self.assertEqual(triangle.perimeter(a, b, c), expected)

    def test_area_string(self):
        cases = [
            ('3', 4, 5),
            ('abc', 4, 5),
            (3, 'abc', 5),
            (3, 4, 'abc'),
            ('', 4, 5),
            (3, '4', 5),
            (3, 4, '5'),
            ('3', '4', '5'),
        ]
        for a, b, c in cases:
            with self.subTest(a=a, b=b, c=c):
                with self.assertRaises(TypeError):
                    triangle.area(a, b, c)

    def test_area_negative(self):
        cases = [
            (-3, 4, 5),
            (-1, 4, 5),
            (3, -1, 5),
            (3, 4, -1),
            (-3, -4, -5),
            (-0.001, 4, 5),
            (3, -1000000, 5),
        ]
        for a, b, c in cases:
            with self.subTest(a=a, b=b, c=c):
                with self.assertRaises(ValueError):
                    triangle.area(a, b, c)

    def test_perimeter_string(self):
        cases = [
            ('3', 4, 5),
            ('abc', 4, 5),
            (3, 'abc', 5),
            (3, 4, 'abc'),
            ('', 4, 5),
            (3, '4', 5),
            (3, 4, '5'),
            ('3', '4', '5'),
        ]
        for a, b, c in cases:
            with self.subTest(a=a, b=b, c=c):
                with self.assertRaises(TypeError):
                    triangle.perimeter(a, b, c)

    def test_perimeter_negative(self):
        cases = [
            (-3, 4, 5),
            (-1, 4, 5),
            (3, -1, 5),
            (3, 4, -1),
            (-3, -4, -5),
            (-0.001, 4, 5),
            (3, -1000000, 5),
        ]
        for a, b, c in cases:
            with self.subTest(a=a, b=b, c=c):
                with self.assertRaises(ValueError):
                    triangle.perimeter(a, b, c)

    def test_area_degenerate(self):
        cases = [
            (1, 2, 3),
            (2, 3, 5),
            (5, 2, 3),
            (3, 5, 2),
            (0, 5, 5),
            (5, 0, 5),
            (5, 5, 0),
            (0, 0, 0),
            (1000, 2000, 3000),
            (0.5, 0.5, 1),
        ]
        for a, b, c in cases:
            with self.subTest(a=a, b=b, c=c):
                with self.assertRaises(ValueError):
                    triangle.area(a, b, c)

    def test_perimeter_degenerate(self):
        cases = [
            (1, 2, 3),
            (2, 3, 5),
            (5, 2, 3),
            (3, 5, 2),
            (0, 5, 5),
            (5, 0, 5),
            (5, 5, 0),
            (0, 0, 0),
            (1000, 2000, 3000),
            (0.5, 0.5, 1),
        ]
        for a, b, c in cases:
            with self.subTest(a=a, b=b, c=c):
                with self.assertRaises(ValueError):
                    triangle.perimeter(a, b, c)

    def test_perimeter_decimal(self):
        cases = [
            (0.003, 0.004, 0.005, 0.012, 1.2e-14),
            (0.3, 0.4, 0.5, 1.2, 1.2e-12),
            (1.5, 2.0, 2.5, 6.0, 6e-12),
            (6, 8, 10, 24.0, 2.4e-11),
            (30, 40, 50, 120.0, 1.2e-10),
            (300, 400, 500, 1200.0, 1.2e-09),
            (3000, 4000, 5000, 12000.0, 1.2e-08),
            (3000000, 4000000, 5000000, 12000000.0, 1.2e-05),
            (3000000000000, 4000000000000, 5000000000000, 12000000000000.0, 12.0),
        ]
        for a, b, c, expected, delta in cases:
            with self.subTest(a=a, b=b, c=c):
                self.assertAlmostEqual(triangle.perimeter(a, b, c), expected, delta=delta)

    def test_area_impossible(self):
        cases = [
            (1, 2, 4),
            (4, 1, 2),
            (1, 4, 2),
            (1, 1, 1000000),
        ]
        for a, b, c in cases:
            with self.subTest(a=a, b=b, c=c):
                with self.assertRaises(ValueError):
                    triangle.area(a, b, c)

    def test_perimeter_impossible(self):
        cases = [
            (1, 2, 4),
            (4, 1, 2),
            (1, 4, 2),
            (1, 1, 1000000),
        ]
        for a, b, c in cases:
            with self.subTest(a=a, b=b, c=c):
                with self.assertRaises(ValueError):
                    triangle.perimeter(a, b, c)


if __name__ == "__main__":
    unittest.main()
