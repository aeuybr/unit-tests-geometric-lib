import unittest
import square


class SquareTestCase(unittest.TestCase):
    def test_area_numbers(self):
        cases = [
            (5, 25),
            (0, 0),
            (1, 1),
            (2.5, 6.25),
            (2, 4),
            (7, 49),
            (10, 100),
            (99, 9801),
            (100, 10000),
            (999, 998001),
            (1000, 1000000),
            (10000, 100000000),
            (1000000, 1000000000000),
            (1000000000000, 1000000000000000000000000),
        ]
        for a, expected in cases:
            with self.subTest(a=a):
                self.assertEqual(square.area(a), expected)

    def test_perimeter_numbers(self):
        cases = [
            (5, 20),
            (0, 0),
            (1, 4),
            (2.5, 10),
            (2, 8),
            (7, 28),
            (10, 40),
            (99, 396),
            (100, 400),
            (999, 3996),
            (1000, 4000),
            (10000, 40000),
            (1000000, 4000000),
            (1000000000000, 4000000000000),
        ]
        for a, expected in cases:
            with self.subTest(a=a):
                self.assertEqual(square.perimeter(a), expected)

    def test_area_string(self):
        cases = [
            '5',
            '',
            'abc',
            '0',
            '-5',
            '1.5',
        ]
        for a in cases:
            with self.subTest(a=a):
                with self.assertRaises(TypeError):
                    square.area(a)

    def test_area_negative(self):
        cases = [
            -5,
            -1,
            -0.001,
            -0.5,
            -1000,
            -1000000000000,
        ]
        for a in cases:
            with self.subTest(a=a):
                with self.assertRaises(ValueError):
                    square.area(a)

    def test_perimeter_string(self):
        cases = [
            '5',
            '',
            'abc',
            '0',
            '-5',
            '1.5',
        ]
        for a in cases:
            with self.subTest(a=a):
                with self.assertRaises(TypeError):
                    square.perimeter(a)

    def test_perimeter_negative(self):
        cases = [
            -5,
            -1,
            -0.001,
            -0.5,
            -1000,
            -1000000000000,
        ]
        for a in cases:
            with self.subTest(a=a):
                with self.assertRaises(ValueError):
                    square.perimeter(a)

    def test_area_decimal(self):
        cases = [
            (0.001, 1e-06, 1e-15),
            (0.01, 0.0001, 1e-15),
            (0.1, 0.01, 1e-14),
            (0.25, 0.0625, 6.25e-14),
            (1.25, 1.5625, 1.5625e-12),
            (12.75, 162.5625, 1.625625e-10),
            (999.5, 999000.25, 9.9900025e-07),
        ]
        for a, expected, delta in cases:
            with self.subTest(a=a):
                self.assertAlmostEqual(square.area(a), expected, delta=delta)

    def test_perimeter_decimal(self):
        cases = [
            (0.001, 0.004, 4e-15),
            (0.01, 0.04, 4e-14),
            (0.1, 0.4, 4e-13),
            (0.25, 1.0, 1e-12),
            (1.25, 5.0, 5e-12),
            (12.75, 51.0, 5.1e-11),
            (999.5, 3998.0, 3.998e-09),
        ]
        for a, expected, delta in cases:
            with self.subTest(a=a):
                self.assertAlmostEqual(square.perimeter(a), expected, delta=delta)


if __name__ == "__main__":
    unittest.main()
