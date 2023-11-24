#include "rsa.h"

/**
 * gcd - Calculate the greatest common divisor (GCD) of two numbers.
 *
 * @a: The first number.
 * @b: The second number.
 * 
 * Return: The GCD of a and b.
 */
long long gcd(long long a, long long b)
{
    while (b != 0)
    {
        long long temp = b;
        b = a % b;
        a = temp;
    }

    return (a);
}

/**
 * pollards_rho - Apply Pollard's Rho algorithm to find a non-trivial factor of a number.
 *
 * @n: The number to factorize.
 * 
 * Return: A non-trivial factor of n.
 */
long long pollards_rho(long long n)
{
    long long x = rand() % (n - 2) + 2;
    long long y = x;
    long long d = 1;

    if (n % 2 == 0)
        return (2);

    long long f(long long x)
    {
        return ((x * x + 1) % n);
    }

    while (d == 1)
    {
        x = f(x);
        y = f(f(y));
        d = gcd(abs(x - y), n);
    }

    return (d);
}

/**
 * factorize_number - Factorize a given number into its prime factors.
 *
 * @number: The number to factorize.
 */
void factorize_number(long long number) {
    if (number <= 1) {
        printf("%lld=%lld\n", number, number);
        return;
    }

    printf("%lld=", number);

    while (number > 1)
    {
        long long factor = pollards_rho(number);

        printf("%lld", factor);
        number /= factor;
        if (number > 1)
            printf("*");
    }

    printf("\n");
}