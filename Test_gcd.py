# gcd_calculator.py

from math import gcd
from functools import reduce


def calculate_gcd(numbers):
    """
    Calculate the GCD of a list of numbers.

    :param numbers: List of integers.
    :return: GCD of the list of numbers.
    """
    if not numbers:
        raise ValueError("The list of numbers cannot be empty.")
    return reduce(gcd, numbers)


def validate_input(input_string):
    """
    Validate and parse user input into a list of integers.

    :param input_string: String of space-separated values.
    :return: List of integers.
    """
    try:
        numbers = list(map(int, input_string.split()))
        if not numbers:
            raise ValueError
        return numbers
    except ValueError:
        raise ValueError("Please enter a list of valid integers separated by spaces.")


# Example usage
if __name__ == "__main__":
    try:
        # Input from the user
        input_string = input("Enter numbers separated by spaces: ")
        numbers = validate_input(input_string)
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

    def test_validate_input_valid(self):
        self.assertEqual(validate_input("48 72 108"), [48, 72, 108])

    def test_validate_input_invalid(self):
        with self.assertRaises(ValueError):
            validate_input("48 abc 108")

    def test_validate_input_empty(self):
        with self.assertRaises(ValueError):
            validate_input("")


if __name__ == "__main__":
    unittest.main()

