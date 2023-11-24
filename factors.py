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

    print(f"{number}=", end="")

    while number > 1:
        factor = pollards_rho(number)
        print(factor, end="")
        number //= factor
        if number > 1:
            print("*", end="")

    print()

def pollards_rho(n):
    if n % 2 == 0:
        return 2

    x = randrange(2, n - 1)
    y = x
    d = 1

    def f(x):
        return (x * x + 1) % n

    while d == 1:
        x = f(x)
        y = f(f(y))
        d = math.gcd(abs(x - y), n)

    return d

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    try:
        with open(filename, 'r') as file:
            for line in file:
                number = int(line)
                factorize_number(number)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Error: {e}")
