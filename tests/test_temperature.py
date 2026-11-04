import unittest

from src.temperature import c_to_f, c_to_k, f_to_c


class TemperatureTest(unittest.TestCase):
    def test_freezing_point(self):
        self.assertEqual(c_to_f(0), 32)

    def test_boiling_point(self):
        self.assertEqual(c_to_f(100), 212)

    def test_kelvin(self):
        self.assertAlmostEqual(c_to_k(0), 273.15)

    def test_round_trip(self):
        self.assertAlmostEqual(f_to_c(c_to_f(37)), 37)


if __name__ == "__main__":
    unittest.main()
