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
        # Eingabe von Benutzer und Bereinigung der führenden oder nachfolgenden Leerzeichen
        input_string = input("Enter numbers separated by spaces: ").strip()

        # Validierung der Benutzereigabe
        if not input_string:
            raise ValueError("The list of numbers cannot be empty.")

        result = calculate_gcd(numbers)
        print(f"The GCD of {numbers} is {result}")
    except ValueError as e:
        print(e)
