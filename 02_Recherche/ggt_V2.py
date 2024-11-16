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


# Example usage
if __name__ == "__main__":
    try:
        # Input from the user
        input_string = input("Enter numbers separated by spaces: ").strip()
        # Validate and convert input to a list of integers
        if not input_string:
            raise ValueError("The list of numbers cannot be empty.")
        try:
            numbers = list(map(int, input_string.split()))
        except ValueError:
            raise ValueError("All inputs must be valid integers.")

        # Calculate GCD
        result = calculate_gcd(numbers)
        print(f"The GCD of {numbers} is {result}")
    except ValueError as e:
        print(f"Error: {e}")
