import unittest

from tempconv.convert import celsius_to_fahrenheit


class CelsiusToFahrenheitTest(unittest.TestCase):
    def test_10_ac1_boiling_point(self):
        """#10 AC1: 100 °C is 212.0 °F."""
        self.assertEqual(celsius_to_fahrenheit(100), 212.0)

    def test_10_ac2_minus_forty(self):
        """#10 AC2: -40 °C is -40.0 °F."""
        self.assertEqual(celsius_to_fahrenheit(-40), -40.0)

    def test_10_ac3_rounds_to_two_decimal_places(self):
        """#10 AC3: 36.6 °C is 97.88 °F, not 97.88000000000001."""
        self.assertEqual(celsius_to_fahrenheit(36.6), 97.88)


if __name__ == "__main__":
    unittest.main()
