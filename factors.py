import sys
import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, math.isqrt(num) + 1):
        if num % i == 0:
            return False
    return True

def factorize_number(number):
    if number <= 1:
        print(f"{number}={number}")
        return

    print(f"{number}=", end='')

    while number > 1:
        factor_found = False

        # Check if the number itself is prime
        if is_prime(number):
            print(f"{number}")
            break

        # Find the smallest prime factor using Pollard's rho algorithm
        for factor in range(2, number + 1):
            if number % factor == 0 and is_prime(factor):
                print(f"{factor}", end='')
                number //= factor
                factor_found = True
                if number > 1:
                    print("*", end='')
                break

        # If no factor is found, it means the number is prime
        if not factor_found:
            print(f"{number}")
            break

def main(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                number = int(line)
                factorize_number(number)
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
