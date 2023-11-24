import math
import time

def is_prime(num):
    """
    Check if a number is prime.

    Parameters:
    - num (int): The number to check for primality.

    Returns:
    - bool: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, math.isqrt(num) + 1):
        if num % i == 0:
            return False
    return True

def factorize_number(number):
    """
    Factorize a given number into a product of two smaller numbers.

    Parameters:
    - number (int): The number to be factorized.

    Returns:
    - tuple: A tuple containing two factors of the given number.
    """
    for factor in range(2, math.isqrt(number) + 1):
        if number % factor == 0 and is_prime(factor):
            return factor, number // factor
    return number, 1

def main(filename):
    """
    Main function to read numbers from a file, factorize them, and print the results.

    Parameters:
    - filename (str): The name of the file containing natural numbers to factorize.
    """
    with open(filename, 'r') as file:
        for line in file:
            number = int(line)
            result = factorize_number(number)
            print(f"{number}={'*'.join(map(str, result))}")

if __name__ == "__main__":
    start_time = time.time()
    main("tests/test00")
    end_time = time.time()
    print(f"\nreal\t{end_time - start_time:.3f}s")
