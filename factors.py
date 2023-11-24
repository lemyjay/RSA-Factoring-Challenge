import sys
import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def pollards_rho(n):
    if n % 2 == 0:
        return 2

    x = 2
    y = 2
    d = 1

    f = lambda x: (x**2 + 1) % n

    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x - y), n)

    return d

def factorize_number(number):
    if number <= 1:
        return [number]

    factors = []
    while number > 1:
        factor = pollards_rho(number)
        factors.append(factor)
        number //= factor

    return factors

def main(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                number = int(line)
                factors = factorize_number(number)
                factors_str = '*'.join(map(str, factors))
                print(f"{number}={factors_str}")
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
