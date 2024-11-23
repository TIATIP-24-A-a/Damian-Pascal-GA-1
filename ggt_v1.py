# gcd_calculator.py

from math import gcd
from functools import reduce


def calculate_gcd(numbers):
    """
    Calculate the GCD of a list of numbers.

    :param numbers: List of integers.
    :return: GCD of the list of numbers.
    """

    if len(numbers) == 0:
        raise ValueError('Numbers cannot be empty.')

    try:
        numbers = map(int, numbers)
    except ValueError:
        raise ValueError("Alle Eingaben muessen Ganzzahlen sein!.")

    if not numbers:
        raise ValueError("Es sind keine Nummern vorhanden")

    return reduce(gcd, numbers)


def parse_input(input_string):
    # Validierung der Benutzereigabe
    if not input_string:
        raise ValueError("Eingabe darf nicht leer sein.")
    try:
        numbers = list(map(int, input_string.split()))
        return numbers
    except ValueError:
        raise ValueError("Alle Eingaben muessen Ganzzahlen sein!.")

# Example usage
if __name__ == "__main__":
    try:
        # Eingabe von Benutzer und Bereinigung der führenden oder nachfolgenden Leerzeichen
        input_string = input("Fügen Sie Ganzzahlen getrennt durch Leerzeichen ein: ").strip()

        number = parse_input(input_string)

        #Berechnen und Ausgabe des groessten gemeinsamen Teilers
        result = calculate_gcd(numbers)
        print(f"Der groesste gemeinsame Teiler von {numbers} ist {result}")
    except ValueError as e:
        print(f"Fehler: {e}")
