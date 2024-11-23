# gcd_calculator.py
from ggt_v1 import parse_input
from ggt_v1 import calculate_gcd

# Example usage
if __name__ == "__main__":
    try:
        # Input from the user
        input_string = input("Enter numbers separated by spaces: ")
        numbers = parse_input(input_string)
        result = calculate_gcd(numbers)
        print(f"The GCD of {numbers} is {result}")
    except ValueError as e:
        print(e)

# Unit tests
import unittest


class TestGCDCalculator(unittest.TestCase):
    def test_calculate_gcd_single_number(self):
        self.assertEqual(calculate_gcd([7]), 7)

    def test_calculate_gcd_multiple_numbers(self):
        self.assertEqual(calculate_gcd([48, 72, 108]), 12)

    def test_calculate_gcd_prime_numbers(self):
        self.assertEqual(calculate_gcd([13, 17, 19]), 1)

    def test_calculate_gcd_empty_list(self):
        with self.assertRaises(ValueError):
            calculate_gcd([])

    def test_validate_input_invalid(self):
        with self.assertRaises(ValueError):
            calculate_gcd([48, "abc", 108])

    def test_validate_input_valid(self):
        self.assertEqual(parse_input("48 72 108"), [48, 72, 108])



    def test_validate_input_empty(self):
        with self.assertRaises(ValueError):
            parse_input("")


if __name__ == "__main__":
    unittest.main()

