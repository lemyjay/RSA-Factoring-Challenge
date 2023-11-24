import sys
import math

def is_prime(num):
    """
    Check if a given number is prime.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, math.isqrt(num) + 1):
        if num % i == 0:
            return False
    return True

def factorize_number(number):
    """
    Factorize a given number into two smaller numbers.

    Args:
        number (int): The number to factorize.

    Returns:
        tuple: A tuple containing two factors.
    """
    for factor in range(2, math.isqrt(number) + 1):
        if number % factor == 0 and is_prime(factor):
            return number // factor, factor
    return number, 1

def main(filename):
    """
    Main function to read numbers from a file and factorize them.

    Args:
        filename (str): The name of the file containing numbers to factorize.
    """
    try:
        with open(filename, 'r') as file:
            for line in file:
                number = int(line)
                result = factorize_number(number)
                print(f"{number}={'*'.join(map(str, result))}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    main(filename)
