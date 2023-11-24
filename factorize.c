#include "rsa.h"

/**
 * isPrime - Checks if a number is prime.
 * @num: The number to be checked.
 *
 * Return: 1 if prime, 0 otherwise.
 */
int isPrime(long long num)
{
    long long i;
    
    if (num < 2)
    {
        return 0;  /* Not prime */
    }

    for (i = 2; i * i <= num; ++i)
    {
        if (num % i == 0)
        {
            return 0;  /* Not prime */
        }
    }

    return 1;  /* Prime */
}


/**
 * factorizeNumber - Factorizes numbers from the file
 *                      This function reads numbers from the specified
 *                   file, performs factorization and prints the results.
 * 
 * @file: pointer to the file containing numbers to factorize 
 */
void factorizeNumber(FILE *file)
{
    long long number, factor;

    while (fscanf(file, "%lld", &number) == 1) {
        /* Handle even numbers */
        if (number % 2 == 0) {
            printf("%lld=2*%lld\n", number, number / 2);
            continue;
        }

        /* Find factors of the number */
        for (factor = 3; factor * factor <= number; factor += 2) {
            if (number % factor == 0 && isPrime(factor)) {
                printf("%lld=%lld*%lld\n", number, factor, number / factor);
                break;
            }
        }
    }
}