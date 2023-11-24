def factorize_number(number):
    """
    Factorize a given number into a list of two factors.

    Parameters:
    - number (int): The number to be factorized.

    Returns:
    - list: A list containing two factors of the given number.
    """
    factors = []

    # Check for divisibility by 2
    while number % 2 == 0:
        factors.extend([2, number // 2])
        return factors

    # Check odd numbers starting from 3
    for i in range(3, int(number**0.5) + 1, 2):
        while number % i == 0:
            factors.extend([i, number // i])
            return factors

    # If the number is prime
    if number > 1:
        factors.extend([number, 1])
    return factors

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
    import sys
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <filename>")
        sys.exit(1)
    main(sys.argv[1])
